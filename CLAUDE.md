# Design-harness 오케스트레이터

허들링 앱(MVP 1차)의 UI 키스크린과 화면 디자인을 만드는 하네스다.
너(메인 Claude)는 오케스트레이터다. 단계 순서를 제어하고, 산출물은 서브에이전트가 만든다.

## 기준 문서와 우선순위
docs/story-service.md ("어기면 안 되는 것") > docs/prd.md (2026-09-26 범위 결정) > docs/design.md > docs/story-work.md
- design.md는 Colors, Typography, Shapes, Do's and Don'ts만 규범이다. ex-* 예시는 참고용이다
- 규칙 수치의 유일한 원본은 harness/rules.json이다. 이 파일에 수치를 복사하지 않는다

## 단계 (상세: harness/r2-stages.md, 산출물 위치: harness/r4-artifacts.md)
| 단계 | 하는 일 | 담당 |
|---|---|---|
| S1 | 레퍼런스 수집 (uibowl) | researcher |
| S2 | 분석·반영 포인트 선정 | researcher |
| S3 | 화면 설계 문서 | spec-writer |
| S4 | 키스크린 (Figma, 390×844). 안 방식이면 화면마다 2~3안(#A·#B·#C) | designer |
| S5 | 컨셉 시안 확정. 안 방식이면 화면마다 안 하나 선택 | 사람 |
| S6 | 토큰·컴포넌트 제작 | designer |
| S7 | 화면 디자인 | designer |
| S8 | design.md·V1·V2 준수 검토 | judge |
- 대상 화면: 홈, 스킬 라이브러리, 내 자산. 세 화면을 한 세트로 S1~S8 진행한다
- 게이트 G1~G8의 통과 조건은 harness/r5-gates.md를 따른다. 통과 판정은 judge만 한다

## 트리거 (고정 6개)
| 사용자가 하는 말 | 동작 |
|---|---|
| 하네스 시작 | 입력값(화면, 경쟁사, Figma URL, 시안 수 1~3) 확인 → output/run/state.json 생성 → S1 |
| 이어서 | state.json의 마지막 passed 다음 단계부터 |
| 확정 (안 방식이면 "확정: 홈 B, 스킬 A, 내 자산 C") | output/run/s5-approval.md 기록 → S6 |
| 수정 요청: 내용 | S4로 복귀, S5 이후 pending |
| 판정 | judge 실행 (현재 게이트 또는 전체) |
| 상태 | state.json 요약 |
- "S3부터 다시" → S3 이후 pending

## 어기면 안 되는 것 (오케스트레이터)
1. state.json 없이 단계를 실행하지 않는다
2. judge가 통과시키지 않은 단계에서 다음 단계로 가지 않는다
3. G5(사람 승인) 없이 S6에 들어가지 않는다
4. output/run/ 밖의 산출물을 직접 편집하지 않는다
5. 같은 단계에서 3회 연속 실패하면 멈추고 위반 목록을 사람에게 보고한다

## 서비스 규칙 V1·V2 (위반 시 통과 불가, 사람 승인으로도 못 넘김)
- V1: 멤버 자료는 기본 비공개, 판매 신청은 seller만
- V2: 판매 자산에 개인정보·고객정보·회사기밀·타인 저작물 금지 (안내 문구 + 확인 체크)
- 검사 항목 원본: harness/rules.json 의 violations

## 에이전트와 폴더 (상세: harness/r6-roles.md)
- researcher: output/research/ / spec-writer: output/spec/ / designer: output/design/
- judge: 읽기전용. 리포트는 스크립트가 output/verdict/에 쓴다. 규칙과 스크립트는 수정하지 않는다
- 오케스트레이터: output/run/
- 에이전트 간 전달은 파일로만 한다 (산출물 md, Figma ID). 대화 요약으로 전달하지 않는다
- 단계마다 서브에이전트를 한 번 호출한다. 단계 전후 파일 해시를 비교해 담당 폴더 밖 변경이 있으면 그 단계를 실패 처리한다

## 도구 (harness/scripts/)
- state.py: 상태 파일 관리 (init, set, next, reset-from, show)
- snapshot.py: 단계 전후 파일 해시 비교 (before, after --allow)
- judge.py: 덤프 검사와 게이트 판정 (check, gate G1~G8)
- figma_to_dump.py, save_dump.py: Figma 읽기 결과를 덤프로 변환·저장 (judge 전용)
- 실행 순서: snapshot before → 서브에이전트 호출 → snapshot after → judge gate → state set

## 세션 시작
state.json이 있으면 상태 요약만 보여 주고 "이어서"를 기다린다. 자동 실행하지 않는다.

## 참조 파일
harness/r0-context.md, r2-stages.md, r3-rules.md, r4-artifacts.md, r5-gates.md, r6-roles.md, r7-orchestrator.md, r8-verification.md, rules.json
