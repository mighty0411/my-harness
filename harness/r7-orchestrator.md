# R7. 오케스트레이터

## CLAUDE.md 구성 (R8 후 초안 승인)
- 위치: Design-harness/CLAUDE.md, 80줄 이하
- 내용: 기준 문서 우선순위 (r0), 단계표 (r2), 트리거 6개 (r6)
- 상세는 harness/r*.md와 rules.json을 참조로 연결. 수치를 CLAUDE.md에 복사하지 않음

## 오케스트레이터가 어기면 안 되는 것 (5개)
1. output/run/state.json 없이 단계를 실행하지 않는다
2. judge가 통과시키지 않은 단계에서 다음 단계로 가지 않는다
3. G5 승인 없이 S6에 들어가지 않는다
4. output/run/ 밖의 산출물을 직접 편집하지 않는다
5. 같은 단계에서 3회 연속 실패하면 멈추고 위반 목록을 보고한다

## 세션 시작
- 새 세션에서 state.json이 있으면 상태 요약만 보여 주고 "이어서" 입력을 기다린다. 자동 실행 없음

## 에이전트 간 전달
- 파일로만 전달 (산출물 md, Figma ID). 대화 요약은 전달 수단으로 쓰지 않는다
- 단계마다 서브에이전트를 한 번 호출한다

## Figma 덤프 (R4·R6 어긋남 정리)
- judge에게 Figma 읽기 도구(get_metadata, get_design_context, get_variable_defs)만 추가 허용. use_figma는 주지 않는다. designer는 덤프를 만들지 않는다
- 읽은 결과는 harness/scripts/figma_to_dump.py로 변환하고 save_dump.py를 거쳐 output/verdict/dump/에 저장
- 스크립트는 dump JSON만 읽어 rules.json과 대조
- variant 세트(컴포넌트 세트) 프레임은 get_design_context 코드가 삼항식이라 변환기가 읽지 못한다. META는 세트 프레임에서, CODE는 variant 자식 노드를 개별로 읽어 이어 붙여 한 ### FRAME 에 넣는다
- variant 세트의 get_metadata는 variant 자식(option/* 등)을 보여 주지 않는다. variant 노드마다 get_metadata를 한 번 더 읽어 같은 ### FRAME 아래 ### META 블록으로 이어 붙이면 변환기가 세트 안의 같은 ID를 대신한다
- 화면에 쓴 컴포넌트 인스턴스의 안쪽 노드는 get_metadata에 나오지 않고 코드에만 I26:234;23:55 같은 ID로 나온다. 변환기가 코드의 I 노드를 덤프에 넣으므로 화면 프레임은 META·CODE를 그대로 넣으면 된다
- 컴포넌트 루트의 배경·반경도 검사하려면 ### FRAME <ID> +root 로 적는다 (컴포넌트 프레임에만. 화면 프레임에는 쓰지 않는다)
- 값이 변수에 묶이면 코드에 var(--이름,기본값)으로 나온다. 변환기는 기본값을 읽는다. get_variable_defs는 노드가 쓰는 변수만 돌려주므로, 컬렉션 전체 검사가 필요하면 컴포넌트별 결과를 합쳐 ### VARS 한 개로 넣는다
- 변경분만 읽기: 이미 전체 덤프(s4·s6·s7.json)가 있고 바뀐 컴포넌트·프레임이 분명하면, 그 노드만 위 절차로 읽어 `save_dump.py <name> --merge` 로 저장한다. 같은 frame id는 교체, 없던 id는 추가, 나머지는 유지한다. variables는 기존 값에 합친다. 이어서 같은 게이트를 다시 실행한다
  - 컴포넌트를 바꾸면 그 컴포넌트(S6)와, 그 인스턴스가 있는 화면 프레임(S7)을 함께 읽는다. 인스턴스 안쪽 노드는 원본 컴포넌트를 따라가므로 화면 프레임을 건너뛰면 G8이 낡은 값을 본다
  - 전체를 다시 읽어야 하는 경우: 덤프가 없을 때, 바뀐 곳을 특정할 수 없을 때, 변수(토큰) 값 자체를 바꿨을 때, 프레임을 지우거나 다시 만들었을 때(--merge는 삭제를 반영하지 못한다), 최종 확인(S8) 직전
- 약점: 읽은 결과가 Bash(heredoc)를 거쳐 스크립트에 전달됨. 필요한 속성이 모두 읽히는지는 R8에서 검증했다 (r8-verification.md 검증 결과)
