# S4 키스크린

Figma 파일: https://www.figma.com/design/CNelXB5JxSwpeJNurQRm3L/Design-harness
페이지: S4 Keyscreens (page id 19:2)

대상 화면: 홈, 스킬 라이브러리, 내 자산 (V1 등록 화면). 모두 390×844. 기준: output/spec/s3-screen-spec.md 최신본(공통 UI 2차: status-bar 47, header Hug 52, content-area 상 16·하 32·간격 24, footer).

- frame: 82:75 | screen/home
- frame: 82:164 | screen/skills
- frame: 19:3 | screen/my-assets/register@seller

## 영역 ID
- 19:3 register@seller: status-bar 82:6, header 82:20, content-area 82:30, footer 71:2 (action-area 82:70 + home-indicator 71:3 컴포넌트)
- 82:75 home: status-bar 82:76, header 82:90, content-area 82:98, footer 82:140 (tab-bar 홈 [selected] + home-indicator 인스턴스)
- 82:164 skills: status-bar 82:165, header 82:179, content-area 82:187, footer 82:224 (tab-bar 스킬 [selected] + home-indicator 인스턴스)

## 노드 메모
- 이전 실행의 프레임 19:50(register@non-seller), 19:92(sale-request@unchecked), 31:2(구 home), 31:55(구 skills)는 G4 프레임 상한(3개)과 최신 S3 반영을 위해 삭제했다. 19:3은 재사용해 최신 S3 기준으로 다시 구성했다. non-seller·sale-request 상태 프레임은 S7에서 만든다.
- home: 인사말, section/progress(list-row 3, status-badge 작성 중·제출 완료·작성 중), section/recommended-skills(recommended-strip, skill-card 3장 가로 스크롤, 세 번째 카드 일부 노출), 내 자산 요약 list-row(우측 화살표). skill-card에 status-badge 없음. 하단 tab-bar 5탭, tab/홈[selected]만 채움 글리프+SemiBold 라벨
- skills: text-input(rest, 안내 문구 스킬 검색), category-chips(chip/전체[selected] 외 6개, 가로 clip), skill-list(skill-card 4장, 검증된 스킬 2장, status-badge 없음). tab/스킬[selected]
- register@seller: text-input[focus](제목, 1px #141414 링), 설명 text-input, file-attach-row, visibility-selector 안 option/private[selected], option/member-only, option/sale-request. footer action-area: save-draft-button(좌) · register-button(우) 각 175×48 간격 8
- 색·반경·간격은 rules.json 값만 사용. accent(#0066ff) 사용 0, 그림자·그라디언트 없음, 폰트 Pretendard(Regular/SemiBold/Bold)만. notch 아래 모서리 반경 16
- 금지 항목 4종 안내와 confirm-checkbox(V2)는 sale-request 프레임에 있으며 G4 상한 때문에 S4에 두지 않았다. S7에서 sale-request@unchecked, @checked로 만든다
- 2회차 수정(G4 D12 등): skills 82:189·register@seller 82:38 placeholder 글자색 #adadad → #262626(#f0f0f0 위 금지 조합 해소). home 82:114 제출 완료 status-badge 채움 제거(fill 없음, stroke #e0e0e0 solid, text #141414). 82:108·82:120과 프레임 구성은 변경 없음
- MVP 제외 표현(허들링 픽, 구매, 피드백, 판매 중, 판매 중지) 사용 없음

## 수정(사용자 요청, radio-wrap 통일)
대상: 19:3의 radio-wrap 82:53·82:59·82:65, 옵션 행 82:52·82:58·82:64. S5 확정본 88:175의 radio-wrap 88:231·88:237·88:243, 행 88:230·88:236·88:242도 같은 값으로 맞춤(원본=확정본). 노드 ID·이름·[selected]·문구·V1 유지, 행 높이 71/67 그대로. B·C(94:4, 94:93) 미수정.
- 변경 전: radio(ellipse 20×20) 채움 #ffffff 고정값. 선택(82:54) = ink 외곽선 6px(두꺼운 링), 비선택(82:60, 82:66) = #262626 외곽선 2px. 선택 행 82:52 stroke ink 2px, 비선택 행 stroke 없음. 변수 바인딩 없음
- 변경 후: radio-wrap(투명 20×20) > radio(ellipse 20×20, 채움 canvas 22:5, 외곽선 1px INSIDE). 선택 = 외곽선 ink 22:4 + radio-dot(ellipse 10×10, ink 22:4, 도형, x5 y5) 신규 1개. 비선택 = 외곽선 hairline #e0e0e0(22:8), 점 없음. 선택 행 stroke 2px → 1px(ink 유지), 비선택 행 stroke 없음 그대로. 새 색·반경 없음
- 신규 노드: 선택 상태에만 radio-dot 82:53 안(19:3), 88:231 안(88:175)에 1개씩 추가
- 컴포넌트 인스턴스로 바꾸지 않음. S4 선택 행 배경은 흰색이라 canvas/ink 구성이 보임(S4 스크린샷은 생성만 했고 직접 열어 보지 못함, 노드 수치로 확인)

## 수정(사용자 요청, 포커스 링 1px)
대상: text-input[focus] 82:33(19:3 안 field/제목 82:31)과 S5 확정본 88:175 안 88:211(field/제목 88:209). 규칙 원본 rules.json input.focus_ring '1px #141414'에 맞춤.
- 변경 전: strokeWeight 2px(상하좌우), INSIDE, 색 ink #141414, 358×48 FIXED
- 변경 후: strokeWeight 1px(상하좌우), INSIDE 유지, 색 #141414 그대로, 358×48 FIXED 그대로(높이 변화 없음, 터치 타깃 44 이상)
- 기본 상태 입력창(82:37, 82:188, 88:115, 88:215)은 테두리 없음 그대로 미수정. B·C 제안 프레임(94:4, 94:93) 안 94:40, 94:129는 지시대로 미수정(여전히 2px)
- S4 노드는 stroke 색 변수 바인딩이 원래 없음(값 #141414 그대로, 이번에 바인딩은 건드리지 않음)

## 수정(사용자 요청, 입력창 반경 8)
규칙 원본 rules.json radius.input 8에 맞춤. 새 변수 `radius/field`(8) VariableID:106:406(tokens 컬렉션, S6 기록 참고)을 입력창에만 바인딩. 높이·포커스 링 1px·테두리·채움 그대로.
- 변경 전: 네 모서리 반경 16, 변수 바인딩 없음. 변경 후: 반경 8, radius/field(106:406) 바인딩
- 19:3(register@seller) 안: 82:33(text-input[focus], 48), 82:37(text-input, 80)
- 82:164(screen/skills) 안: 82:188(text-input, 검색, 48)
- S5 확정본 88:175 안: 88:211(text-input[focus], 48), 88:215(text-input, 80). 88:91(confirmed/screen/skills) 안: 88:115(text-input, 48)
- 미수정(지시): B·C 제안 프레임 94:4·94:93 안 입력창 94:40, 94:44, 94:129, 94:133은 반경 16 그대로. 입력창이 아닌 요소(list-row, option 행, 카드, file-attach-row, confirm-checkbox)는 건드리지 않음
- 판단이 애매해 바꾸지 않은 노드 없음. text-input 이름이 아닌 입력창 모양 노드는 따로 찾지 않았음(이름 검색 기준)

## 수정(사용자 요청, 버튼 반경 8)
규칙 원본 rules.json radius.button 8에 맞춤. 새 변수 `radius/button-rect`(8) VariableID:120:408(tokens, S6 기록 참고)을 버튼에만 바인딩. 높이 48·채움·외곽선·글자·이름·ID 그대로.
- 변경 전: 네 모서리 9999, 변수 바인딩 없음. 변경 후: 8, 120:408 바인딩
- 19:3(register@seller) 안 action-area 82:70의 save-draft-button 82:71, register-button 82:73
- S5 확정본 88:175 안 action-area 88:177의 save-draft-button 88:178, register-button 88:180
- 안 바꿈(사람 판단 필요): file-attach-row 안 44×44 원형 아이콘 버튼 add-action 82:47·delete-action 82:45(19:3 안), 88:225·88:223(88:175 안)은 9999 그대로
- 미수정(지시): B·C 제안 프레임 94:4·94:93 안 버튼, 탭바 제안 101:4·105:29. 칩(chip/*)·tab-bar·tab은 알약 그대로
- 홈 82:75·스킬 82:164, 확정 홈·스킬 88:2·88:91에는 버튼 모양 노드 없음

## 공개 범위 시안 제안
19:3(register@seller)의 공개 범위 필드만 바꾼 비교용 제안 프레임이다. 확정 프레임 목록과 무관하다. #A는 기존 19:3(라디오 + 제목·설명 가로 행 3줄, 선택 행 1px ink 외곽선). 나머지 영역은 19:3과 동일. 색·반경·간격은 tokens 변수에 바인딩했고, 선택 상태는 option/private[selected] 하나만, option/sale-request는 이 seller 프레임에만 있다.
배치 메모: 19:3 바로 오른쪽(x 430)은 기존 home(470)·skills(940)과 겹쳐 기존 프레임을 옮기지 않으려고 skills 오른쪽 끝(1330)에서 간격 40 두고 B(x 1370), C(x 1800)를 놓았다. 라벨은 각 프레임 위(y -60)에 있다(94:90, 94:174).

- B안 screen/my-assets/register#B@seller, ID 94:4 (라벨 94:90)
  - 설명: 라디오 없이 옵션마다 제목+한 줄 설명이 든 세로 선택 카드 3장(높이 67, 간격 8, 반경 card 24). 선택 카드는 ink 채움 + 흰 글자 + 우측 '선택됨' 표시, 나머지는 canvas-soft 채움
  - 장점: 설명이 항상 3개 다 보여 판매 신청의 의미를 비교하기 쉽다. 카드가 커서 터치가 쉽고 #A와 선택 표현이 확연히 다르다
  - 단점: 세로를 많이 쓴다(필드 하단 617, content-area 하단 여백 32 이내로 간신히 들어감). ink 채움이 다른 CTA·강조보다 무겁게 보일 수 있다

- C안 screen/my-assets/register#C@seller, ID 94:93 (라벨 94:174)
  - 설명: 3분할 세그먼트 컨트롤(전체 높이 52, 각 세그먼트 44, 반경 tab) + 선택한 옵션 설명을 아래 한 줄로 표시. 선택 세그먼트는 canvas 채움 + SemiBold, 그림자 없음
  - 장점: 세로 공간을 가장 적게 쓰고(필드 하단 480) 3옵션을 한눈에 비교한다. 선택 변경이 단순하다
  - 단점: 옵션 설명이 선택한 것 하나만 보인다. 라벨이 긴 문구(예: 판매 신청)가 늘면 폭이 빠듯하다. 세그먼트 기본 모양이라 판매 신청 옵션의 seller 한정 맥락이 덜 드러난다

## 탭바 그림자 시안 제안
사용자 요청 참고용 시안이다. 확정 프레임·판정 대상 아님(이름 proposal/..., screen/ 접두 없음).
- 프레임 ID 101:4 (proposal/tab-bar-shadow, 390×150, x 2230 y 0, 기존 마지막 프레임 오른쪽 끝 2190에서 간격 40, 배경 canvas 변수 #ffffff). 라벨 텍스트 101:32 (프레임 위 y -60)
- 내부: tab-bar(set 23:53)의 active=홈 인스턴스 101:5 (x16 y24, 358×64), home-indicator 사각형(134×5, ink). 위아래 여백 24. 원본 컴포넌트는 수정하지 않고 인스턴스 오버라이드만 적용
- 인스턴스 오버라이드: 채움 canvas 변수(#ffffff, 원본은 canvas-soft #f3f3f3), 스트로크 없음, 반경 9999 유지. 탭 아이콘·라벨·색은 원본 그대로(글자 #141414 on #ffffff, D12 충족)
- 사용한 그림자: drop shadow 색 #141414 불투명도 9%, x 0, y -2, blur 14, spread 0. 스크린샷으로 흰 배경과 구분되는 은은한 번짐 확인
- y 0 시안: 프레임 ID 105:29 (proposal/tab-bar-shadow-y0, 390×150, x 2660 y 0, 101:4 오른쪽 간격 40). 라벨 텍스트 105:57 (y -60). 101:4 복제, 구성 동일(tab-bar 인스턴스 105 내부, 흰 채움 오버라이드, 스트로크 없음, home-indicator). 그림자는 인스턴스에 직접 지정: drop shadow #141414 불투명도 10%, x 0, y 0, blur 16, spread 0 (위아래 골고루). 효과 스타일 shadow/nav는 적용·수정하지 않음. z-순서: tab-bar가 맨 위(home-indicator 위). 스크린샷은 생성했으나 직접 열어 보지 못했고 노드 수치로 확인
- 규칙 충돌: docs/design.md와 harness/rules.json은 그림자를 금지한다. 이 시안은 채택 시 규칙 변경이 필요한 제안이며, 현재 규칙 기준으로는 위반이다. 판정에서 읽히지 않도록 proposal/ 이름을 썼다

## 홈 진행 현황 비교 시안 (참고용)
비교용 프레임이다. 확정 프레임 목록과 무관, G4·S4 덤프 대상 아님. 82:75가 #A, S7 홈 36:49 복제본에서 section/progress만 바꾼 `screen/home#B`(153:166, 단계 진행 바 카드)·`screen/home#C`(153:252, 상태 요약 칩 + 컴팩트 행)를 S4 페이지 오른쪽 끝(x 3090, 3520)에 놓고 라벨 153:331·153:334를 y -60에 두었다. 상세는 output/design/ref-progress-variants.md.

## 수정(사용자 요청, status-badge 4종 아이콘)
- screen/home(82:75) 안 일반 프레임 status-badge에 16×16 (이후 12×12로 변경) 아이콘 프레임(icon/edit·icon/send, 안 벡터 `shape`, 선 1.5px 둥근 끝, 채움 없음, 선 색은 배지 글자색과 같은 값(변수 없는 기존 방식 그대로)) 추가, 배지 itemSpacing 0 → 4. 높이 28 그대로
  - 82:108 '작성 중' → icon/edit 123:419(shape 123:420), 폭 60 → 80
  - 82:114 '제출 완료' → icon/send 123:421(shape 123:422), 71 → 91
  - 82:120 '작성 중' → icon/edit 123:423(shape 123:424), 60 → 80
- S5 Approval 확정본 confirmed/screen/home(88:2) 안 같은 배지 처리(S5 페이지 87:2): 88:35 '작성 중' → icon/edit 123:425(shape 123:426), 60 → 80. 88:41 '제출 완료' → icon/send 123:427(shape 123:428), 71 → 91. 88:47 '작성 중' → icon/edit 123:429(shape 123:430), 60 → 80. 높이 28

## 수정(사용자 결정, 배지 아이콘 12×12로 변경)
직전 16px 통일 지시는 무효. 위 '수정(사용자 요청, status-badge 4종 아이콘)'의 아이콘 프레임을 ID·이름 유지한 채 16×16 → 12×12로 리사이즈. 안 벡터 `shape`는 0.75배 비율 유지·가운데·선 1.5px 유지(edit 11×11 → 8.25×8.25, send 12×12 → 9×9). 간격 4·세로 가운데·선 색 그대로, 배지 높이 28·외곽선·채움·반경·라벨 불변.
- screen/home(82:75): icon/edit 123:419(배지 80 → 76), icon/send 123:421(91 → 87), icon/edit 123:423(80 → 76)
- S5 확정본 confirmed/screen/home(88:2): icon/edit 123:425(80 → 76), icon/send 123:427(91 → 87), icon/edit 123:429(80 → 76)
- 판정 스크립트는 돌리지 않음

## 수정(사용자 반영, 제출 완료 배지 stroke #141414)
사용자가 S6 status-badge variant 제출 완료(23:6)의 stroke를 #141414(color/ink)로 바꾸고 rules.json status_badges도 갱신해, 일반 프레임 배지를 맞춤. 두께 1·INSIDE·solid·채움 없음·icon/send 12×12·라벨·폭·높이는 그대로.
- 82:114 (S4 screen/home 안 status-badge '제출 완료'): stroke #e0e0e0 → #141414, color/ink(VariableID:22:4) 바인딩
- 88:41 (S5 confirmed/screen/home 88:2 안 status-badge '제출 완료'): stroke #e0e0e0 → #141414, color/ink(VariableID:22:4) 바인딩
- 안 바꿈: S6 컴포넌트, S7, 다른 배지(작성 중, 임시저장, 검수 대기 등). 판정 스크립트는 돌리지 않음

## 수정(사용자 요청, text-input·submit-button·action-area 높이 48→56)
docs/design.md 높이 56에 맞춤. 높이만 변경(패딩·반경·채움·외곽선·글자·변수 바인딩·간격 24/8 그대로, 새 값 없음). B·C 제안 프레임(94:*) 미수정. 판정 스크립트는 돌리지 않음.
- 입력창 한 줄 높이 48 → 56: 82:33(text-input[focus], 19:3 안), 82:188(text-input, 82:164 skills 검색), 88:211(text-input[focus], 88:175 안), 88:115(text-input, 88:91 skills 안). 80 그대로(미수정): 82:37, 88:215
- 버튼 175×48 → 175×56: save-draft-button 82:71·register-button 82:73(action-area 82:70 48 → 56), 88:178·88:180(action-area 88:177 48 → 56)
- footer action 71:2(19:3 안), 88:176(88:175 안): HUG 82 → 90, y762 → 754(끝 844). nav footer 82:224·88:151은 변경 없음
- content-area 82:30, 88:208(FIXED): 663 → 655. 재배치(content-area 기준 y 전 → 후): field/제목 h79 → 87, field/설명 y119 → 127, field/파일 첨부 y254 → 262, field/공개 범위 y369 → 377(h250), 끝 619 → 627. 기준선(655 - 32) 623 대비 넘침 4px(88:208도 동일), footer와 겹침 0(화면 y 726 < 754). 값은 바꾸지 않음, 사람 결정 필요
- skills 82:164, 88:91: category-chips y88 → 96, skill-list y156 → 164(끝 748 → 756), content-area 82:187·88:114는 FIXED 647 그대로(기존에 이미 넘친 상태, 끝 756 → 647 대비 109 초과, 기존 748에서 +8). 잘림·footer(y746) 겹침은 기존 문제의 연장이라 값을 바꾸지 않고 보고
