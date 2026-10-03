#!/usr/bin/env python3
"""문서 일관성 검사: r*.md와 CLAUDE.md 안의 참조가 실제 정의와 맞는지 확인한다.
검사: 규칙 ID(D01~D12, G1~G8, S1~S8, V1·V2), 파일 경로, rules.json 키, output/ 하위 폴더.
종료 코드: 0 = 깨진 참조 0, 1 = 깨진 참조 있음
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
H = ROOT / "harness"
OUT_DIRS = {"research", "spec", "design", "run", "verdict"}


def defined(path, pattern):
    return set(re.findall(pattern, (H / path).read_text(encoding="utf-8"), flags=re.M))


def main():
    rules = json.loads((H / "rules.json").read_text(encoding="utf-8"))
    ids = (defined("r3-rules.md", r"^\|\s*(D\d\d)\s*\|") | defined("r5-gates.md", r"^\|\s*(G\d)\s*\|")
           | defined("r2-stages.md", r"^\|\s*(S\d)\s*\|") | set(rules["violations"]))
    files = sorted(H.glob("r*.md")) + [ROOT / "CLAUDE.md"]
    broken = []
    for f in files:
        text = f.read_text(encoding="utf-8")
        rel = f.relative_to(ROOT).as_posix()
        for tok in sorted(set(re.findall(r"(?<![A-Za-z0-9#])([DGSV]\d{1,2})(?![A-Za-z0-9])", text))):
            if tok not in ids:
                broken.append(f"{rel}: 정의 없는 ID {tok}")
        for p in sorted(set(re.findall(r"(?<![A-Za-z0-9_-])((?:harness|docs)/[A-Za-z0-9_./-]+|\.claude/agents/[A-Za-z0-9_.-]+)(?![A-Za-z0-9_./*-])", text))):
            p = p.rstrip(".,)")
            if "*" in p or "<" in p:
                continue
            if not (ROOT / p).exists():
                broken.append(f"{rel}: 없는 경로 {p}")
        for d in sorted(set(re.findall(r"output/(\w+)/", text))):
            if d not in OUT_DIRS:
                broken.append(f"{rel}: 정의 없는 output 하위 폴더 {d}")
        keys = re.findall(r"rules\.json[^`\n]{0,6}`([A-Za-z_.]+)`", text) + re.findall(r"rules\.json\s*의\s*([a-z_]+)", text)
        for k in sorted(set(keys)):
            cur = rules
            for part in k.split("."):
                if isinstance(cur, dict) and part in cur:
                    cur = cur[part]
                else:
                    broken.append(f"{rel}: rules.json에 없는 키 {k}")
                    break
        if re.search(r"(?<![\w/])rules\.json", text) and not (H / "rules.json").exists():
            broken.append(f"{rel}: rules.json 없음")
    print(json.dumps({"checked": [f.relative_to(ROOT).as_posix() for f in files], "broken": broken},
                     ensure_ascii=False, indent=2))
    sys.exit(1 if broken else 0)


if __name__ == "__main__":
    main()
