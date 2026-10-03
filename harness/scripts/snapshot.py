#!/usr/bin/env python3
"""단계 전후 파일 해시 비교로 '담당 폴더 밖 변경'을 검출한다 (사후 검사).

  snapshot.py before <label>
  snapshot.py after  <label> --allow output/research [--allow ...]
종료 코드: 0 = 허용 폴더 안의 변경만 있음, 1 = 허용 밖 변경 있음 (그 단계를 실패 처리)
스냅샷은 output/run/snapshots/<label>.json 에 저장된다 (비교 대상에서 제외).
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WATCH = ["output", "harness", "docs", ".claude", "CLAUDE.md"]
SNAP_DIR = ROOT / "output" / "run" / "snapshots"
SKIP_PARTS = {"__pycache__", ".DS_Store"}


def collect():
    files = {}
    for w in WATCH:
        base = ROOT / w
        paths = [base] if base.is_file() else (sorted(base.rglob("*")) if base.exists() else [])
        for p in paths:
            if not p.is_file() or SKIP_PARTS & set(p.parts):
                continue
            rel = p.relative_to(ROOT).as_posix()
            if rel.startswith("output/run/snapshots/"):
                continue
            files[rel] = hashlib.sha256(p.read_bytes()).hexdigest()
    return files


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=["before", "after"])
    ap.add_argument("label")
    ap.add_argument("--allow", action="append", default=[])
    a = ap.parse_args()
    f = SNAP_DIR / f"{a.label}.json"
    if a.mode == "before":
        SNAP_DIR.mkdir(parents=True, exist_ok=True)
        f.write_text(json.dumps(collect(), ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"스냅샷 저장: {a.label}")
        return
    if not f.exists():
        sys.exit(f"before 스냅샷 없음: {a.label}")
    old, new = json.loads(f.read_text(encoding="utf-8")), collect()
    changed = sorted({k for k in set(old) | set(new) if old.get(k) != new.get(k)})
    allow = [x.rstrip("/") + "/" for x in a.allow]
    bad = [c for c in changed if not any(c.startswith(x) for x in allow)]
    print(json.dumps({"changed": changed, "outside_allowed": bad}, ensure_ascii=False, indent=2))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
