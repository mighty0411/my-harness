# R8. 검증과 리뷰

## 1. 대비 충돌 수정 (rules.json, r3-rules.md 반영)
- 작성 중, 임시저장 배지: 흰 배경(#ffffff) + #e0e0e0 점선 외곽선 + #707070 글자 (대비 4.95:1)
- rules.json: 두 배지에 stroke_style "dashed" 추가, 기존 fill #f3f3f3 제거
- D12: 대비를 계산으로 검사. 금지 조합 명시 = #707070 on #f3f3f3 (4.46), #707070 on #f0f0f0 (4.35), #adadad on #ffffff/#f3f3f3/#f0f0f0 (본문)
- 허용 확인값: #707070 on #ffffff 4.95, #adadad on #141414 8.21

## 2. 판정 스크립트 검증 (harness/tests/)
- pass.json 1개 + 규칙별 위반 덤프 15개 (fail-D01 ~ fail-D12, fail-V1, fail-V2, fail-badge)
- 통과 기준: pass.json은 위반 0, fail-X.json은 정확히 규칙 X만 실패. 일치율 100%

## 3. Figma 덤프 검증
- 테스트용 Figma 파일에 샘플 노드 세트를 만들고 조회 도구 결과 확인
- 필수 속성 10종: 채움, 선, 반경, 폰트 패밀리, 폰트 굵기, 폰트 크기, 자간, padding·gap, 효과(그림자), 크기
- 하나라도 누락되면 그 속성에 의존하는 규칙은 "판정 불가"로 표시하고 r3 판정 제외로 이동
- 선행 조건: Figma MCP 인증

## 4. 시범 실행과 문서 일관성
- 시범 실행: 내 자산 화면 1개로 S1~S8 전 단계 실행
- 위반 주입 2건: V1 (기본 선택을 비공개가 아니게), V2 (확인 체크박스 삭제). 둘 다 G8에서 실패해야 통과
- harness/scripts/check_docs.py: r*.md 안의 참조 (D01~D12, G1~G8, S1~S8, V1·V2, 파일 경로)가 실제 정의와 맞는지 검사. 깨진 참조 0이면 통과

## 구현 순서 (CLAUDE.md 승인 후)
1. harness/scripts/ (판정 스크립트, save_dump.py, check_docs.py)
2. harness/tests/ 픽스처 16개, 스크립트 검증
3. .claude/agents/ 4개 정의 파일
4. Figma 덤프 검증 (인증 후)
5. 시범 실행과 위반 주입

## 검증 결과 (2026-09-30)

### 3. Figma 덤프 검증 (완료)
- 테스트 자료: 파일 `Design-harness`의 `Dump Test` 페이지 (프레임 1개, 노드 14개). 검증용이며 삭제 여부는 사용자가 정한다
- 읽기 도구 3종(get_metadata, get_design_context, get_variable_defs)으로 필수 속성 10종을 모두 읽을 수 있음
- 값은 JSON이 아니라 Tailwind 클래스로 나옴 → 규칙 기반 변환 스크립트 figma_to_dump.py로 덤프를 만든다
- 알게 된 것
  - Pretendard는 굵기 클래스(font-semibold 등) 없이 `font-['Pretendard:SemiBold']`로만 나옴 → 굵기는 스타일 이름에서 rules.json font.weight_styles로 계산
  - 자간·반경·패딩은 0이면 클래스가 생략됨 → 생략은 0으로 해석
  - 선택됨·비활성·아이콘 같은 상태는 속성으로 나오지 않음 → 노드 이름 표기 규칙 추가 (r4-artifacts.md 상태 표기 규칙)
  - `get_variable_defs`는 변수가 없으면 빈 객체. G6 변수 검사는 실제 변수를 만든 뒤 다시 확인 필요
- Pretendard: Figma 데스크톱 앱 재시작 후 use_figma에서 9개 굵기가 목록에 나오고 Regular·Bold·SemiBold 로드 확인. Figma 굵기 이름은 공백 없는 `SemiBold`
- 파일 제목은 플러그인 API로 바꿀 수 없다 (figma.root.name은 문서 노드 이름). Figma에서 직접 바꿈

### 2. 판정 스크립트 검증
- harness/tests/run_tests.py: 51/51 일치 (규칙 픽스처 16, 게이트 18, 변환 17)
- 변환 검증은 실제 Dump Test 읽기 결과를 그대로 저장한 픽스처(tests/fixtures/figma/)로 하며, 기대한 위반(D05·D06·D07·D08)만 나옴

### 4. 문서 일관성
- harness/scripts/check_docs.py: 깨진 참조 0

### 변환기 보강 (2026-09-30, 시범 실행 S6의 G6 실패에서 발견)
- 발견: 변수에 묶인 값(rounded-[var(--radius\/badge,9999px)] 등)을 변환기가 읽지 못해 반경이 0, 색이 빈 값으로 저장됨 → D04 오탐 2건, D02 사실상 미검사. 컴포넌트 인스턴스(<StatusBadge className=.../>)는 data-node-id가 없어 스타일 누락. variant 세트 프레임 코드는 삼항식이라 태그 파싱 실패
- 수정: figma_to_dump.py가 var(--이름,기본값) 기본값을 읽고, 인스턴스는 이름(status-badge)과 태그 이름(StatusBadge)으로 짝지음. variant는 자식 노드를 개별로 읽어 CODE에 이어 붙이는 절차로 해결 (r7)
- 2차 발견 (같은 G6 재판정에서 judge가 보고한 커버리지 한계): variant 세트의 get_metadata는 variant 자식을 안 보여 주고, 컴포넌트 루트는 노드로 담기지 않아 option 카드·skill-card 루트의 배경·반경이 검사되지 않았다. 게이트 스크립트는 이를 판정 불가로 기록하지 않았다
- 2차 수정: ### META 여러 개(variant 별 메타가 세트의 같은 ID를 대신), ### FRAME <ID> +root(루트 노드 검사) 추가. 절차는 r7
- 3차 발견: 글자 색·폰트가 부모 div에만 붙어(CSS 상속) 글자 노드 값이 비었다(G4의 D07 판정 불가와 같은 원인). variant 코드의 작은따옴표 className, font-["…"] 큰따옴표 표기, style={{ }} 중첩 중괄호도 못 읽었다
- 3차 수정: 글자 색·폰트·굵기·크기를 가장 가까운 조상에서 상속, 따옴표·중첩 중괄호 처리. S6 덤프에서 글자 노드 61개 모두 색·폰트 채워짐 확인
- 4차 발견 (S7의 G7 재판정): 화면에 쓴 인스턴스의 안쪽 노드(option/*, checkbox-box, 안쪽 status-badge와 글자)는 메타에 없고 코드에만 I 노드로 나오는데 변환기가 조용히 버렸다 → V1 오탐 2건("기본 선택 []"), V2·배지 검사 공백. G7 스크립트는 V1을 보지 않아 통과로 나왔음
- 4차 수정: 코드의 I 노드를 이름(data-name)·태그 중첩 부모·상속·배경과 함께 덤프에 넣고, 안쪽 status-badge는 글자·아이콘을 접어 넣음. 배지 라벨은 아이콘 글리프를 제외한 첫 글자
- 남은 한계: variant 심볼 루트의 배경·반경은 노드로 담기지 않음. 컴포넌트 세트 안의 variant·state 필드는 이름이 variant=... 형식이라 비어 있음(화면 프레임에서 [disabled] 등을 붙이면 채워짐)
- 테스트: run_tests.py 70/70 (변환 픽스처 s6-list-row, s6-checkbox-checked, s6-vis-set·variant 추가, 상속·따옴표·중첩 중괄호 케이스)

### 5. 시범 실행 (2026-09-30, 내 자산 화면 1개, S1~S8)
- 결과: S1~S8 전 단계 passed. 게이트 G1~G8 통과 (G2 1회, G4 1회, G6 1회 실패 후 재작업·보강으로 통과)
- 실패에서 나온 것
  - G2: 대상 화면 밖(홈·스킬 라이브러리) 포인트 → researcher 재작성
  - G4: D04 delete-button 반경 0 → designer 수정
  - G6: 변환기 한계 4건 (변수 var() 값, variant 세트 코드·메타, 글자 상속, 따옴표·중첩 중괄호) → 위 "변환기 보강" 1~3차
  - G7: 인스턴스 안쪽 노드 누락(V1·V2·배지 검사 공백) → 4차 보강
- 위반 주입: 실제 S7 덤프 복사본(임시 폴더)에 심고 gate G8 실행. 대조군 통과, 주입 4건 모두 실패
  - V1 기본 선택이 비공개가 아님 → "기본 선택 ['option/member-only'], 기대 [option/private]"
  - V1 non-seller 프레임에 option/sale-request 노출 → 실패
  - V2 확인 체크박스 삭제 → 두 프레임 모두 "confirm-checkbox 없음"
  - V2 체크 전 submit-button 활성 → "disabled가 아님"
- 주의: 주입은 Figma 안이 아니라 덤프 JSON 단계에서 했다. Figma에서 노드를 바꿔 다시 읽는 경로(읽기→변환→판정 전체)의 위반 검출은 이번에 확인하지 않았다
- 시각 확인 미실시: designer가 S4·S6·S7에서 스크린샷을 열어 보지 못했다. 구조 검사(규칙 값)로만 검증했다

### 세 화면 확장에서 확인된 판정 한계 (2026-09-30)
- 게이트가 역할을 노드 이름의 부분 문자열로 정한다(judge.py ROLE_HINTS). 역할 단어가 없는 이름(variant `layout=…`·`status=…`·`active=…`, `chip/*`, `tab/*`, `option/*`, `list-row` 등)은 D04(반경)·D10(높이) 검사에서 빠진다. 반대로 컨테이너 이름에 역할 단어가 들어가면(예: skill-card-strip) 오탐이 난다. S4에서 컨테이너 이름을 바꿔 피했다
- 그 결과 status-badge variant 3개(제출 완료·검수 대기·수정 요청)에 흰 채움이 남은 것을 G6가 잡지 못했고, 홈 화면의 배지 인스턴스에서 G7·G8이 처음 잡았다 → 컴포넌트 검사는 variant를 규격표(rules.json status_badges)와 직접 대조하는 항목을 판정 절차에 넣는 게 안전하다
- 화면 코드에서 컴포넌트 인스턴스가 `<ListRow className=… />` 함수 호출로 나오면, 안쪽 글자는 컴포넌트 정의의 기본값이고 인스턴스에서 바꾼 글자(override)는 코드에 반영되지 않는다. 안쪽 노드 ID도 컴포넌트 쪽 ID라 화면 메타와 짝지을 수 없다. 이런 인스턴스 안쪽 글자의 색·폰트·대비(D07, D12)와 override 문구는 게이트로 확인되지 않는다. 컴포넌트 자체는 S6 variant별로 검사되므로, 남는 위험은 화면에서 인스턴스를 덮어쓴 값이다. 눈으로 확인하거나 use_figma 계열로 인스턴스 안쪽을 직접 읽는 별도 경로가 필요하다
- 판정 입력(번들)은 모델이 도구 결과를 손으로 옮겨 적어 만든다. 옛 번들 재사용, 클래스 순서 변경, VARS 오기 같은 실수가 이번에 각각 한 번씩 나왔다. 글자 노드 수 대조는 이를 걸러 내는 데 쓸 수 있으나 미세한 변경은 못 잡는다

### 공통 UI 재구성에서 확인된 판정 기준 변경 (2026-10-01)
- 화면 골격을 status-bar·header·content-area·action-area(또는 tab-bar)·home-indicator로 분리하면서, 좌우 여백 16이 프레임 루트가 아니라 content-area 에만 있게 되어 D09 "화면 좌우 패딩 0/0"이 4건 걸렸다(디자인은 규칙 의도대로였음)
- 변환기 수정: 루트에 좌우 패딩이 없고 content-area 가 있으면 그 좌우 패딩을 frame.padding 으로 쓴다. 판정 스크립트·규칙은 그대로다. 즉 D09 화면 패딩 검사는 이 구조에서 content-area 의 좌우 여백을 검사한다. 루트에 패딩이 있으면 루트 값을 그대로 쓴다
- 알려진 한계: notch 하단 개별 모서리 반경(rounded-bl/br), tab·chip 의 selected 상태, 영역 y 위치·겹침은 덤프에 없어 검사되지 않는다

### 함수 컴포넌트 인스턴스 안쪽 노드 (2026-10-01, 공통 UI 적용 후 G8 V2 실패에서 발견)
- 발견: 화면 코드에서 인스턴스가 `<ActionArea className=.../>` 같은 함수 호출로 나오면 안쪽 노드가 I 노드가 아니라 컴포넌트 정의 ID(64:181)로만 나온다. 그래서 sale-request@unchecked의 제출 버튼이 덤프에 없어 G8이 V2 "submit-button 없음"으로 실패했다(디자인은 정상). 같은 이유로 홈·스킬의 인스턴스 안쪽 글자(list-row, skill-card)와 status-bar·home-indicator 안쪽도 그동안 덤프에 없었다
- 수정: 변환기가 코드의 함수 정의 안 노드를, 메타의 같은 이름 인스턴스 아래에 I<인스턴스ID>;<정의ID> 로 넣는다. 정의 안에 변형 분기(=== · && · id={… ? …})가 있는 함수(한 프레임에 여러 변형을 섞어 쓴 경우, 예: 홈의 list-row progress+summary)는 넣지 않는다
- 남은 한계: 변형을 섞어 쓴 함수 컴포넌트의 안쪽은 여전히 덤프에 없다. 화면에서 인스턴스의 글자를 덮어쓴 값(override)도 코드에 반영되지 않는다
- 테스트: run_tests.py 75/75

### 아직 검증하지 못한 것
- 아이콘 노드(icon/check 등)가 get_design_context에서 어떻게 읽히는지. 인스턴스·variant는 위 "변환기 보강"에서 확인
- Figma 안에서 위반을 주입해 읽기부터 판정까지 전체 경로로 검출하는지
- 홈·스킬 라이브러리 화면 (이번 시범은 내 자산만)
- 컴포넌트 variant 심볼 루트의 배경·반경, 변수 컬렉션 전체 값 검사(get_variable_defs는 노드가 쓰는 변수만 반환)
- get_variable_defs에 실제 변수가 있을 때의 분류 (테스트는 가짜 입력)
