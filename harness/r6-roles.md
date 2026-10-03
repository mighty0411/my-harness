# R6. 역할

## 에이전트와 편집 폴더 (에이전트당 1개)
| 에이전트 | 맡은 단계 | 편집 폴더 | 정의 파일 |
|---|---|---|---|
| researcher | S1, S2 | output/research/ | .claude/agents/researcher.md |
| spec-writer | S3 | output/spec/ | .claude/agents/spec-writer.md |
| designer | S4, S6, S7 (Figma 포함) | output/design/ | .claude/agents/designer.md |
| judge | 모든 게이트, S8 | 없음 (읽기전용) | .claude/agents/judge.md |
| 오케스트레이터 (메인 Claude) | 순서 제어, S5 기록 | output/run/ | CLAUDE.md |

## 읽기전용 판정자
- judge 도구: Read, Grep, Bash (판정 스크립트 실행용), Figma 읽기 도구(get_metadata, get_design_context, get_variable_defs, get_screenshot). Edit·Write, use_figma 없음
- 리포트와 덤프는 스크립트가 output/verdict/에 씀 (덤프 변환·저장: harness/scripts/figma_to_dump.py, save_dump.py)
- 판정 스크립트 원본: harness/scripts/ (에이전트 수정 금지, 사람만 수정)
- 판정 규칙 원본: harness/rules.json (에이전트 수정 금지)

## 폴더 제한 확인 (사후 검사)
- 규칙은 각 에이전트 정의 파일의 프롬프트에 적는다
- 단계 실행 전후에 파일 목록과 해시를 비교. 담당 폴더 밖의 변경이 있으면 그 단계를 실패 처리
- 한계: 사전 차단이 아니라 사후 검출. Bash로 다른 경로에 쓸 수 있음

## 자연어 트리거 (고정 6개)
| 사용자가 하는 말 | 동작 |
|---|---|
| 하네스 시작 | 입력값(화면, 경쟁사) 확인, state.json 생성, S1 시작 |
| 이어서 | state.json을 읽고 마지막 통과 다음 단계부터 진행 |
| 확정 | S5 승인 기록, S6 진행 |
| 수정 요청: 내용 | S4로 복귀 |
| 판정 | judge 실행 (현재 게이트 또는 전체) |
| 상태 | state.json 요약 |
- 특정 단계부터 재실행: "S3부터 다시" → S3 이후 pending
