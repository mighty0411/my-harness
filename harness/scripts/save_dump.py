#!/usr/bin/env python3
"""Figma 조회 결과(JSON)를 stdin으로 받아 output/verdict/dump/<name>.json 으로 저장한다.

  cat 조회결과.json | save_dump.py s7
name은 s4, s6, s7 또는 소문자·숫자·-·_ 만 허용. 저장 경로는 output/verdict/dump/ 로 고정된다.

변경분만 읽었을 때는 --merge 를 붙인다. 기존 덤프에서 같은 frame id 는 새 것으로 교체하고,
없던 id 는 추가하며, 나머지 프레임은 그대로 둔다. variables 는 기존 값에 새 값을 합친다
(새로 읽은 컴포넌트가 쓰는 변수가 빠지지 않게. 기존 값이 남아 보수적으로 판정될 수 있다).
  cat 변경분.json | save_dump.py s6 --merge
기존 덤프가 없으면 --merge 는 오류다(전체를 먼저 읽어 저장해야 한다).
필수 구조: {"frames": [{"name", "page", "width", "height", "nodes": [...]}]}
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DUMP_DIR = ROOT / "output" / "verdict" / "dump"


def merge(old, new):
    ids = {f.get("id") for f in new["frames"]}
    if None in ids or "" in ids:
        sys.exit("--merge 는 모든 프레임에 id 가 있어야 합니다")
    by_id = {f["id"]: f for f in new["frames"] if f.get("id")}
    frames, used = [], set()
    for f in old["frames"]:
        fid = f.get("id")
        if fid in by_id:
            frames.append(by_id[fid])
            used.add(fid)
        else:
            frames.append(f)
    frames += [f for fid, f in by_id.items() if fid not in used]
    out = dict(old)
    out["frames"] = frames
    nv = new.get("variables")
    if isinstance(nv, dict):
        ov = dict(out.get("variables") or {})
        for k, vals in nv.items():
            cur = list(ov.get(k) or [])
            cur += [v for v in vals if v not in cur]
            ov[k] = cur
        out["variables"] = ov
    return out, len(used), len(by_id) - len(used)


def main():
    args = [a for a in sys.argv[1:] if a != "--merge"]
    do_merge = len(args) != len(sys.argv) - 1
    if len(args) != 1 or not re.fullmatch(r"[a-z0-9_-]+", args[0]):
        sys.exit("사용법: save_dump.py <name> [--merge]  (name: 소문자·숫자·-·_)")
    sys.argv = [sys.argv[0], args[0]]
    try:
        d = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        sys.exit(f"JSON 형식 오류: {e}")
    if not isinstance(d, dict) or not isinstance(d.get("frames"), list) or not d["frames"]:
        sys.exit("frames 배열이 필요합니다")
    for i, f in enumerate(d["frames"]):
        missing = [k for k in ("name", "page", "width", "height", "nodes") if k not in f]
        if missing:
            sys.exit(f"frames[{i}]에 필수 필드 없음: {missing}")
    DUMP_DIR.mkdir(parents=True, exist_ok=True)
    out = DUMP_DIR / f"{sys.argv[1]}.json"
    if do_merge:
        if not out.exists():
            sys.exit(f"--merge: 기존 덤프 없음 ({out.relative_to(ROOT)}). 전체를 먼저 저장하세요")
        d, replaced, added = merge(json.loads(out.read_text(encoding="utf-8")), d)
        out.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"병합 저장: {out.relative_to(ROOT)} (교체 {replaced}개, 추가 {added}개, 전체 프레임 {len(d['frames'])}개)")
        return
    out.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"저장: {out.relative_to(ROOT)} (프레임 {len(d['frames'])}개)")


if __name__ == "__main__":
    main()
