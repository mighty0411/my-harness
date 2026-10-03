# R4. 산출물

## 단계별 파일 (output/)
| 단계 | 파일 | 필수 내용 |
|---|---|---|
| S1 | research/s1-references.md | 경쟁사 목록, 화면별 레퍼런스 항목(uibowl URL) |
| S2 | research/s2-analysis.md | 반영 포인트 목록, 항목별 근거 레퍼런스 |
| S3 | spec/s3-screen-spec.md | 화면 3개 설계 (구성 요소, 상태, 상호작용) |
| S4 | design/s4-keyscreens.md | Figma 파일 URL, 프레임 ID (`- frame: <ID> \| <이름>` 한 줄씩). 안 방식이면 화면마다 2~3안 |
| S5 | run/s5-approval.md | 확정 기록 (확정 일시, 확정한 프레임 ID) |
| S6 | design/s6-tokens-components.md | Figma 변수·컴포넌트 ID 목록 (컴포넌트 7개 포함) |
| S7 | design/s7-screens.md | 완성본 프레임 ID 3개 |
| S8 | verdict/s8-report.json | 규칙 ID별 통과·위반 개수, 위반 노드 ID |
- Figma 안의 산출물은 파일에 URL과 프레임·노드 ID만 기록한다

## 규칙 SSOT
- `harness/rules.json` 1개가 유일한 원본 (D01~D12, 상태 배지 7종, V1·V2)
- r3-rules.md는 규칙 ID와 의미만 유지 (수치는 rules.json 참조)

## 재개
- `output/run/state.json`: 실행 입력값(대상 화면, 경쟁사, Figma 파일 URL), 단계별 상태(pending / passed / failed), 마지막 passed 단계
- 재개 = 마지막 passed 다음 단계부터
- 실패 시 복귀 지점: R5

## Figma 검사 방식
- 판정자가 Figma 읽기 도구(get_metadata, get_design_context, get_variable_defs)로 읽은 결과를 harness/scripts/figma_to_dump.py로 덤프 JSON으로 변환하고, harness/scripts/save_dump.py를 거쳐 `output/verdict/dump/*.json`으로 저장
- 변환은 규칙 기반 스크립트가 한다 (사람·LLM이 손으로 옮기지 않는다). 입력 형식은 figma_to_dump.py 상단 설명 참조
- 스크립트는 dump JSON만 읽어 rules.json과 대조 (Figma 직접 접근 없음)
- 노드 이름 규칙: rules.json의 `node_names`를 따른다 (V1·V2 검사에 필요)

## Figma 구조 (원본: rules.json `figma`)
- 파일: 실행당 1개, 이름 `Design-harness` (rules.json figma.file_name). 위치는 실행 시작 입력값 (프로젝트 URL → 그 프로젝트, 기존 파일 URL → 그 파일 안에 페이지 생성, 없음 → Drafts)
- URL은 문서에 적지 않고 output/run/state.json에만 기록한다
- 판정 대상 페이지 3개: `S4 Keyscreens`, `S6 Components`, `S7 Screens`. 토큰은 파일 변수·스타일이고 페이지에 있지 않다. 사람이 값을 보는 `토큰 가이드 (Token Guide)` 페이지는 별도로 두며 판정 범위 밖이다 (아래 '토큰 가이드 규칙')
- 화면 프레임 이름: `screen/home`, `screen/skills`, `screen/my-assets/register`, `screen/my-assets/sale-request`
- 상태 접미사: V1용 `@seller`, `@non-seller` / V2용 `@unchecked`, `@checked`
  - 예: `screen/my-assets/sale-request@unchecked`
- 컴포넌트·옵션 노드 이름: rules.json `node_names`
- 화면 프레임은 모두 390×844
- 판정 범위: rules.json `figma`에 적힌 페이지와 프레임 이름만 본다 (기존 파일의 다른 페이지·프레임은 무시)
- 안 표시: 안 방식에서는 프레임 이름에 `#A`, `#B`, `#C`를 붙인다. 상태 접미사 앞에 둔다 (`screen/home#A`, `screen/my-assets/register#A@seller`). 판정은 안 표시를 떼고 화면과 상태를 본다. S7 완성본 이름에는 안 표시를 쓰지 않는다
- 페이지 이름: 번호와 영문 이름 뒤에 괄호로 한글 설명을 붙인다 (`S7 Screens (화면 디자인)`). 판정은 괄호 앞부분으로 비교한다 (judge.py page_key). 페이지 순서는 S4 → S5 Approval → S6 → S7 → 토큰 가이드
- 토큰 가이드 규칙 (designer 지시에 그대로 쓰는 문서 규칙이며 판정 스크립트는 검사하지 않는다)
  - 목적: 파일의 실제 토큰 구조를 표로 보여 주는 참고용 페이지 `토큰 가이드 (Token Guide)`. 값의 원본은 Figma 변수·스타일과 rules.json이며 가이드는 복사본이다
  - 프레임 2개를 같은 페이지에 왼쪽부터 가로로 놓는다: 왼쪽 `token-guide/variables`(변수 컬렉션 tokens), 오른쪽 `token-guide/styles`(텍스트·효과 스타일). 폭 720, y 같게 시작, 프레임 간격 80, 세로 auto layout HUG. 변수와 스타일은 Figma에서 다른 종류라 한 프레임에 섞지 않는다
  - 구조는 실제 Figma를 그대로 따른다 (추측 금지, 만들기 전에 조회). variables 안은 컬렉션 안 그룹(color, radius, spacing 등 실제 그룹명)별 표, styles 안은 `Text styles`(type/*)와 `Effect styles` 표. 그룹 헤더에 변수 타입·개수를 작게 적는다
  - 표 형식: 열 순서 `예시 | 이름 | 값`, 용도 글이 있는 항목만 마지막에 `용도` 열. 이름은 Figma 패널과 같게 전체 경로(`color/ink`)로 쓴다. 그룹 헤더 행(color/canvas-soft), 열 헤더 행(color/canvas-faint), 항목 행은 첫 열을 한 단계 들여쓴다. 행은 가로 auto layout, 셀 폭은 같은 표 안에서 FIXED로 통일, 행 사이는 1px color/hairline-soft
  - 예시 열은 반드시 변수·스타일에 바인딩한다 (색 chip은 변수, 반경·간격은 변수 바인딩 도형, 타이포는 텍스트 스타일 적용, 그림자는 효과 스타일 적용). 값 하드코딩 금지, 새 변수·스타일·hex를 가이드를 위해 만들지 않는다
  - 완전성: 실제 변수·스타일 이름이 가이드에 하나도 빠지지 않아야 한다. 만든 뒤 Figma 실제 목록과 이름을 비교해 확인하고 기록한다 (개수는 문서에 적지 않고 Figma 실제 값을 기준으로 한다)
  - 동기화: S6에서 변수·스타일을 추가·수정·삭제하면 같은 작업에서 가이드도 고친다
  - accent 견본은 가이드 안에 두며, 가이드는 화면(S7)이 아니라서 프레임당 accent 상한 개수에 넣지 않는다
  - 기록: 프레임 ID·행 수·옮긴 항목은 output/design/s6-tokens-components.md, 페이지 요약은 output/design/figma-pages.md
- 프레임 배치 규칙 (designer 지시에 그대로 쓰는 문서 규칙이며 판정 스크립트는 검사하지 않는다)
  - 캔버스: 화면 프레임은 작업 순서대로 왼쪽에서 오른쪽으로 한 줄(y 0)에 놓는다. 기본 순서는 `screen/home`, `screen/skills`, `screen/my-assets/register`(@seller, @non-seller), `screen/my-assets/sale-request`(@unchecked, @checked). 안 방식이면 같은 화면의 안(#A, #B, #C)을 이어서 놓는다
  - 간격: 화면 프레임 사이 80 (390 폭이면 x 시작점 간격 470). 제안(proposal/…) 프레임 사이 40. 제안 프레임은 화면 프레임 오른쪽 끝에서 이어 놓는다
  - 라벨: 프레임 위 y -60 (S5 확정본은 y 12)에 안 이름·ID 라벨을 두고 레이어 패널에서 프레임 바로 옆에 붙여 둔다
  - 레이어 패널: 위에서 아래로 읽는 순서가 캔버스 읽기 순서와 같게 한다 (Figma는 자식 인덱스가 클수록 패널 위쪽이므로 첫 번째 항목이 가장 큰 인덱스). 새 프레임을 만들 때마다 확인한다
  - S6 컴포넌트 페이지는 세로 한 열(x 0)에 작업 순서대로 위에서 아래로: status-badge, skill-card, list-row, tab-bar, visibility-selector, file-attach-row, confirm-checkbox, submit-button, text-input, 공통 UI(status-bar, header, action-area, home-indicator, footer). variant 세트는 폭이 넓어서 가로로 나열하지 않는다
  - S5 Approval: 확정본을 S4 순서대로 왼쪽에서 오른쪽에 놓고 안내 프레임은 그 아래(패널 맨 아래)에 둔다
  - 이름·ID·크기·내용은 배치 때문에 바꾸지 않는다 (위치와 순서만)
- S4 키스크린은 2~3개라 일부 화면만 포함. 내 자산이 포함되면 register, sale-request의 상태 프레임 필요

## 상태 표기 규칙 (원본: rules.json figma.state_tags, figma.icon_nodes)
- Figma 코드에는 선택됨·비활성 같은 상태가 속성으로 나오지 않으므로 노드 이름 끝에 대괄호로 적는다
- `[selected]`: option/* 노드 (예: `option/private[selected]`). 없으면 selected=false
- `[disabled]`: submit-button, button/* 노드 (예: `submit-button[disabled]`). 없으면 enabled
- `[focus]`: text-input 노드 (예: `text-input[focus]`). 없으면 rest
- 배지 아이콘: status-badge 안에 자식 노드를 배지 글자 앞에 둔다. 작성 중 `icon/edit`(✎, 연필), 임시저장 `icon/save`(▣, 저장), 제출 완료 `icon/send`(➤, 종이비행기), 검수 대기 `icon/clock`(◷, 시계), 수정 요청 `icon/alert`(!), 승인됨 `icon/check`(✓), 반려 `icon/close`(✕). 값은 rules.json status_badges의 icon, 이름→기호는 figma.icon_nodes. 기호는 판정용 식별자이고 Figma 아이콘은 벡터로 그린다
- 덤프 변환 때 대괄호 표기는 이름에서 떼어 내고 selected·variant·state·icon 필드로 옮긴다
