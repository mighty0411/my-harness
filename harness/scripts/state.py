#!/usr/bin/env python3
"""상태 파일 관리 (오케스트레이터 전용, output/run/state.json).

  state.py init [--competitors A B C] [--screens ...] [--variants N] [--figma-url URL] [--force]
  state.py set S1..S8 passed|failed|pending
  state.py next
  state.py reset-from S3
  state.py show
종료 코드: 0 정상, 1 규칙 위반(선행 단계 미통과 등), 2 연속 실패 한도 도달 (멈추고 보고)
"""
import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "output" / "run" / "state.json"
STAGES = [f"S{i}" for i in range(1, 9)]


def rules():
    return json.loads((ROOT / "harness" / "rules.json").read_text(encoding="utf-8"))


def load():
    if not STATE.exists():
        sys.exit("state.json 없음. 먼저 '하네스 시작'(state.py init)이 필요합니다.")
    return json.loads(STATE.read_text(encoding="utf-8"))


def save(s):
    STATE.parent.mkdir(parents=True, exist_ok=True)
    s["updated_at"] = datetime.now().isoformat(timespec="seconds")
    STATE.write_text(json.dumps(s, ensure_ascii=False, indent=2), encoding="utf-8")


def last_passed(s):
    lp = None
    for st in STAGES:
        if s["stages"][st] == "passed":
            lp = st
        else:
            break
    return lp


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    i = sub.add_parser("init")
    i.add_argument("--competitors", nargs="*", default=[])
    i.add_argument("--screens", nargs="*", default=None, help="대상 화면 (기본: rules.json gates.screens 전체)")
    i.add_argument("--variants", type=int, default=1, help="S4에서 화면마다 만들 시안 수 (1이면 안 구분 없음, 2~3이면 S5에서 화면마다 하나 선택)")
    i.add_argument("--figma-url", default=None)
    i.add_argument("--force", action="store_true")
    st = sub.add_parser("set")
    st.add_argument("stage", choices=STAGES)
    st.add_argument("status", choices=["passed", "failed", "pending"])
    sub.add_parser("next")
    r = sub.add_parser("reset-from")
    r.add_argument("stage", choices=STAGES)
    sub.add_parser("show")
    a = ap.parse_args()

    if a.cmd == "init":
        if STATE.exists() and not a.force:
            sys.exit("state.json이 이미 있습니다. 이어서 하려면 '이어서', 새로 시작하려면 --force")
        allowed = rules()["gates"]["screens"]
        chosen = a.screens or allowed
        bad = [x for x in chosen if x not in allowed]
        if bad:
            sys.exit(f"알 수 없는 화면 {bad}. 허용: {allowed}")
        vmax = rules()["gates"]["G4"]["variants_max"]
        if not 1 <= a.variants <= vmax:
            sys.exit(f"--variants 는 1~{vmax}")
        s = {"input": {"screens": chosen, "competitors": a.competitors, "variants": a.variants,
                       "figma_url": a.figma_url},
             "stages": {x: "pending" for x in STAGES}, "failures": {x: 0 for x in STAGES},
             "last_passed": None}
        save(s)
        print("초기화 완료")
        return
    s = load()
    limit = rules()["gates"]["max_consecutive_failures"]
    if a.cmd == "set":
        idx = STAGES.index(a.stage)
        if a.status == "passed" and idx > 0 and s["stages"][STAGES[idx - 1]] != "passed":
            print(f"거부: {STAGES[idx - 1]}가 통과되지 않았습니다 (선행 단계 미통과)")
            sys.exit(1)
        s["stages"][a.stage] = a.status
        if a.status == "passed":
            s["failures"][a.stage] = 0
        elif a.status == "failed":
            s["failures"][a.stage] += 1
        s["last_passed"] = last_passed(s)
        save(s)
        if s["failures"][a.stage] >= limit:
            print(f"STOP: {a.stage} {limit}회 연속 실패. 멈추고 위반 목록을 사람에게 보고하세요.")
            sys.exit(2)
        print(f"{a.stage} = {a.status}")
    elif a.cmd == "next":
        nxt = next((x for x in STAGES if s["stages"][x] != "passed"), None)
        print(nxt or "DONE")
    elif a.cmd == "reset-from":
        for x in STAGES[STAGES.index(a.stage):]:
            s["stages"][x] = "pending"
            s["failures"][x] = 0
        s["last_passed"] = last_passed(s)
        save(s)
        print(f"{a.stage} 이후 pending")
    elif a.cmd == "show":
        print(json.dumps(s, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
