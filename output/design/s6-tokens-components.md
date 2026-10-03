# S6 토큰·컴포넌트

Figma: https://www.figma.com/design/CNelXB5JxSwpeJNurQRm3L/Design-harness
페이지: `S6 Components` (id 23:2 근처에서 생성, 컴포넌트는 아래 ID)

## 변수 (컬렉션 `tokens`)
- color: ink 22:4 | canvas 22:5 | canvas-soft 22:6 | field 22:7 | hairline 22:8 | ink-soft 22:9 | text-muted 22:10 | text-faint 22:11 | accent 22:12 | badge-overlay 22:13 | hairline-soft 161:2 (#f0f0f0, 신규)
- radius: button 22:14 | badge 22:15 | toggle 22:16 | tab 22:17 | input 22:18 (16, list-row·option 행·confirm-checkbox·file-attach-row용) | card 22:19 | none 22:20 | field 106:406 (8, text-input 전용, 신규) | button-rect 120:408 (8, 버튼 전용, 신규. 22:14 button 9999는 알약 전용으로 유지)
- spacing: 0 22:21 | 4 22:22 | 8 22:23 | 12 22:24 | 16 22:25 | 24 22:26 | 32 22:27 | 48 22:28 | 64 22:29

## 컴포넌트 (필수 7개)
- component: 35:82 | skill-card (COMPONENT_SET. variant layout=compact/full, verified=false/true. 3종: `layout=compact, verified=false` 35:69 (홈 추천, 폭 200, 제목·설명), `layout=full, verified=false` 35:70 (스킬 라이브러리 목록, 폭 358, 제목·설명·meta 행의 카테고리·유형), `layout=full, verified=true` 23:20 (기존 ID, meta 행 우측에 '검증된 스킬'))
- component: 35:90 | list-row (COMPONENT_SET. variant kind=progress 23:26 (기존 ID, 폭 326: title, 최근 수정일, 우측 status-badge 인스턴스), kind=summary 35:83 (폭 358, canvas-soft: title, 개수 요약, 우측 화살표))
- component: 23:19 | status-badge (variant 7종: 작성 중, 임시저장, 제출 완료, 검수 대기, 수정 요청, 승인됨, 반려. 아이콘 자식 icon/alert, icon/check, icon/close)
  - 사용자가 직접 수정: 제출 완료 variant(23:6) stroke #e0e0e0 → #141414(color/ink 바인딩), 검수 대기는 #e0e0e0 그대로
- component: 23:53 | tab-bar (variant active=홈 23:32 / 자료 35:3 / 스킬 23:39 / 내 학습 35:10 / 내 자산 23:46. 각 variant는 358×64 가로 auto layout(패딩 4, canvas-soft, radius/tab), 탭 5개 tab/홈·tab/자료·tab/스킬·tab/내 학습·tab/내 자산 (각 70×56 세로, 채움 없음, 현재 탭만 [selected]). 탭 자식 = icon-holder(48×32, 9999, 모든 탭 채움 없음) > icon/<탭명>(24×24) > shape 벡터(활성 탭 fill+stroke ink 2px, 비활성 채움 없음 선 #262626 2px), 그 아래 라벨(Pretendard 12, 활성 SemiBold ink, 비활성 Regular #262626). 탭 ID: 홈 23:32 = 44:2/44:7/44:12/44:17/44:22, 스킬 23:39 = 44:27/44:32/44:37/44:42/44:47, 내 자산 23:46 = 44:52/44:57/44:62/44:67/44:72, 자료 35:3 = 44:77/44:82/44:87/44:92/44:97, 내 학습 35:10 = 44:102/44:107/44:112/44:117/44:122)
- component: 23:98 | visibility-selector (variant: role=seller 3종 selected=private/member-only/sale-request, role=non-seller 2종 selected=private/member-only. non-seller에는 option/sale-request 없음, 기본 = option/private[selected])
- component: 23:99 | file-attach-row
- component: 23:112 | confirm-checkbox (variant checked=false/true)

## 추가 컴포넌트 (S7 화면용)
- component: 23:117 | submit-button (variant=enabled / variant=disabled)
- component: 23:122 | text-input (state=rest / state=focus)

## 추가 컴포넌트(공통 UI)
- component: 64:184 | status-bar (COMPONENT, 390×47, #ffffff. 자식: 시간 64:144 (Pretendard SemiBold 15, x16), icon/신호 64:145, icon/와이파이 64:150, icon/배터리 64:154 (우측 끝 374), notch 64:158 (209×30, x90.5 y0, #141414, 아래 두 모서리 반경 20))
- component: 64:187 | header (COMPONENT_SET, variant type=root / type=sub. 각 390×52 Hug, 가로 auto layout 상하 패딩 4·좌우 16, 세로 가운데, #ffffff)
  - `type=root` 64:185: 자식 순서 header-left 64:161 (x16 y4, 44×44, 채움 없음 투명) > icon/메뉴 64:162 (24×24) > 벡터 64:163 / title 64:160 (기본 '타이틀', SemiBold 17, x60 폭 270 가로 중앙) / header-right 64:164 (x330, 44×44, 채움 없음) > icon/알림 64:165 > 벡터 64:166
  - `type=sub` 64:186: header-left 64:169 > icon/뒤로 64:170 > 벡터 64:171, title 64:168, header-right 64:172 > icon/더보기 64:173 > 벡터 64:174
- component: 64:190 | action-area (COMPONENT_SET, variant count=2 / count=1. 각 390×48, #ffffff, 가로 auto layout 좌우 16·상하 0·간격 8. 이전 높이 128/72 폐기)
  - `count=2` 64:188: 좌 save-draft-button 64:178 (x16, 175×48, 흰 채움 + hairline 1px, 9999, 텍스트 64:179 '임시저장'), 우 register-button 64:176 (x199, 175×48, ink 채움, 9999, 텍스트 64:177 '등록')
  - `count=1` 64:189: submit-button[disabled] 64:181 (x16, 358×48, 흰 채움 + hairline 1px 점선, 9999, 텍스트 64:182 '판매 신청 제출' #707070). 기존 submit-button(23:117)은 폭 342·disabled 채움이 달라 인스턴스로 쓰지 않고 확정 시안 61:34 그대로 프레임으로 복제
- component: 64:191 | home-indicator (COMPONENT, 390×34, 채움 canvas #ffffff, 반경 없음. 자식 bar 72:4: 134×5, ink #141414, radius/button 9999, x128 y21 = 영역 하단에서 8 위)
- component: 72:333 | footer (COMPONENT_SET, variant type=nav / type=action. 390폭 세로 auto layout 간격 0, 가로 가운데, canvas 채움)
  - `type=nav` 72:296 (390×98): tab-bar 인스턴스 72:297 (tab-bar active=홈 23:32 기반, 358×64 x16 y0) / home-indicator 인스턴스 72:323 (390×34 y64, 안 bar 134×5 x128 y21)
  - `type=action` 72:325 (390×82): action-area 인스턴스 72:326 (count=2 64:188 기반, 390×48 y0) / home-indicator 인스턴스 72:331 (390×34 y48, 안 bar x128 y21)

## 메모
- 수정(공통 UI 2차, 확정 61:4·61:12·71:3·71:11 기준): header는 Hug 52(버튼 채움 제거), action-area는 390×48 가로 배치, home-indicator는 390×34 영역 + bar, footer 세트 추가. 모든 채움·반경은 tokens 변수(canvas 22:5, ink 22:4, radius/button 22:14) 바인딩, 새 변수·색·반경 없음. 세트 프레임은 variant를 감싸도록 810폭으로 맞춤. 스크린샷은 열 수 없어(이미지 뷰어·셸 없음) 노드 재조회 수치로만 확인
- S7 인스턴스 주의(공통 UI 2차): footer는 프레임 y 기준 type=nav y746(높이 98), type=action y762(높이 82), x0. header는 y47, content-area y99. header 타이틀 텍스트는 인스턴스에서 덮어쓰기(폭 270 가로 중앙 유지, SemiBold 17). action-area/footer action의 count=1 variant 제출 버튼은 disabled 모양이므로, @checked 프레임에서는 인스턴스 안 submit-button[disabled]를 활성(ink 채움, 실선 없음, 글자 canvas)으로 덮어쓰고 이름을 submit-button으로 바꾼다. footer type=action은 count=2가 기본이라 판매 신청 화면은 안 action-area 인스턴스를 count=1로 교체해야 한다
- 수정(공통 UI 컴포넌트, S5 확정 31:2·31:55·19:3·19:50 기준): status-bar·header·action-area·home-indicator를 확정 시안 57:2·61:37/61:4·61:12/61:34·57:19에서 복제해 컴포넌트화. 색은 tokens 변수(ink 22:4, canvas 22:5, canvas-soft 22:6, hairline 22:8, ink-soft 22:9, text-muted 22:10), 반경 radius/button 22:14, 간격 spacing 22:23·22:24·22:25 바인딩. 새 변수·새 색·새 반경 없음. 시간·타이틀·버튼 텍스트는 Pretendard SemiBold 15·17을 노드에 직접 지정
- S7 인스턴스 주의: header 타이틀은 인스턴스에서 텍스트만 덮어쓰기(가로 중앙 정렬 폭 200), status-bar 시간은 '9:41' 그대로, action-area는 count에 따라 y 배치(등록 692, 판매 신청 748, 프레임 y 기준 x0), 상태 표기 이름 접미사 [disabled]는 인스턴스에서 노드 이름으로 다시 적는다
- 색·반경·간격은 변수에 바인딩. 텍스트는 노드마다 Pretendard 굵기·크기 직접 지정 (SemiBold/Regular, 12·13·15·17)
- S7 화면에서 인스턴스를 쓸 때 상태 표기는 노드 이름 끝 대괄호로 다시 붙인다 (예: submit-button[disabled], text-input[focus])
- 그림자·그라디언트 없음, accent 미사용
- 수정(S5 확정 키스크린 31:2·31:55 반영, 보강): 새 컴포넌트·변수 없음. tab-bar를 5탭 5variant로, skill-card와 list-row를 COMPONENT_SET으로 바꿔 variant 추가 (기존 컴포넌트 ID 23:20, 23:26은 variant로 유지, 세트 ID는 위 목록). skill-card는 흰 canvas 채움 + field 1px 외곽선 + radius/card, list-row는 radius/input(16). 모든 색·반경·간격은 tokens 변수 바인딩, 텍스트는 Pretendard SemiBold/Regular 직접 지정(12·13·15·17)
- 칩은 컴포넌트 아님: 스킬 라이브러리 chip/* 은 S7에서 컴포넌트 밖 pill 프레임(radius/tab, 높이 44, 좌우 패딩 16, 선택 = ink 채움 + canvas 글자 [selected], 비선택 = canvas-soft + ink 글자, 텍스트 13 SemiBold)으로 조립
- 수정(G8 반영): status-badge(23:19) variant 제출 완료 23:6·검수 대기 23:8·수정 요청 23:10의 루트 fill을 #ffffff에서 제거(채움 없음), 외곽선·반경·패딩·폰트·글자색·아이콘은 그대로, 나머지 4개 variant는 rules.json status_badges와 일치 확인
- 수정(사람 요청, 진행 행 높이 50): list-row kind=progress(23:26) 높이 57 → 50. 원인은 줄 높이(title 23:28 150%, 최근 수정일 23:29 140%, 배지 label 140%)이며 확정 시안 31:9와 같이 줄 높이 AUTO로 변경 (title 18, 수정일 16, row-info 34, 배지 인스턴스 23:30 높이 24 y13). 글자 크기·굵기·색·반경·패딩·변수 바인딩·문구 그대로. kind=summary(35:83)는 57 그대로(미수정, 사람 확인 대기)
- 수정(사람 결정, list-row 높이 Hug): list-row 두 variant 루트 세로 크기 조절 HUG 확인(가로 FIXED 유지, 326/358). kind=summary(35:83)의 title 35:85·개수 요약 35:86 줄 높이 150%/140% → AUTO (title 18, 개수 요약 16, row-info 34). 결과 23:26과 35:83 모두 높이 50. 글자 크기·굵기·색·반경·패딩·변수 바인딩·문구 그대로
- 수정(사용자 요청, list-row 상하 여백 16): list-row 세트 35:90의 kind=progress 23:26·kind=summary 35:83 상·하 패딩 8 → 16, 두 값 모두 spacing 16 변수(22:25)에 바인딩(기존 22:23 바인딩 교체). 좌우 패딩 16·간격 12·반경·채움·글자·문구 그대로, 세로 HUG 유지. 결과 높이: 두 variant 모두 50 → 66 (row-info 34 + 16×2), 세트 프레임 35:90 높이 57 → 66(폭 708). 내부 y: row-info 16, 배지 23:30 y21(h24), 화살표 35:89 y23(h20). 이전 이력 높이 50 Hug. S7에서 홈·내 자산 레이아웃의 list-row 아래 요소 y 좌표를 16씩 아래로 밀어야 하며 tab-bar/footer(nav y746)와 겹치지 않는지 확인 필요
- 수정(S5 확정 하단 내비 반영, 31:44·31:97 기준): tab-bar(23:53) 5 variant를 아이콘(위)+라벨(아래) 구조로 재구성. variant ID·이름 유지, 탭 노드는 새 ID(위 목록). 선택 탭 = icon-holder ink 채움(변수 22:4) + 흰 아이콘(#ffffff) + 라벨 SemiBold 12 ink, 비선택 = 채움 없음 + 아이콘·라벨 #262626 Regular 12. 아이콘 벡터는 확정 시안에서 복제(2px 선, 둥근 끝, 채움 없음). 탭 패딩 위·아래 4(spacing 22:22)·좌우 0·간격 0, 반경 radius/tab(22:17)은 변수 바인딩. #262626은 확정 시안 값 그대로(변수 없음). 세트 크기 1886×64. 새 컴포넌트·변수 없음
- 수정(S5 확정 폴더 아이콘 반영, 43:11 기준): tab-bar(23:53) 5 variant의 icon/자료 shape 벡터 경로를 확정 시안 폴더 경로(18×15, 프레임 안 x3 y5)로 교체. shape ID: 홈 23:32 = 44:10, 스킬 23:39 = 44:35, 내 자산 23:46 = 44:60, 자료 35:3 = 44:85, 내 학습 35:10 = 44:110. 선 2px·ROUND/ROUND·채움 없음 재지정, 선 색은 자료 variant #ffffff, 나머지 4개 #262626 유지. 다른 탭·구조·변수 그대로, 새 컴포넌트·변수 없음
- 수정(사용자 수동, confirm-checkbox 23:112): 사용자가 Figma에서 직접 수정. 이전 기록에 세부 수치가 없어 변경 전후 diff는 확정 불가, 아래는 조회 시점(읽기 전용) 현재 상태. 세트 716×64(variant 2개 342×64, x0/x374). 두 variant 공통: 가로 auto layout, 패딩 12/16/12/16(spacing 22:24·22:25), 간격 12(22:24), 채움 canvas-soft #f3f3f3(22:6), 반경 radius/input 16(22:18), 가로 FIXED·세로 HUG. checkbox-box 24×24 원형(radius/toggle 22:16, 9999), 패딩 0(22:21). checked=false: box 채움 canvas(22:5) + 1px hairline #e0e0e0(22:8), 안 icon/check(텍스트 ✓, Pretendard SemiBold 12) 색 #e0e0e0(22:8)로 보임 상태. checked=true: box 채움 ink(22:4), 선 없음, icon/check 색 canvas #ffffff(22:5). label 폭 274 Pretendard Regular 13 줄 높이 150% ink(22:4), 2줄(h40), 문구 '금지 항목(개인정보, 고객정보, 회사기밀, 타인 저작물)이 포함되지 않았음을 확인합니다.'. 모든 채움·선·반경·간격은 tokens 변수 바인딩 확인, rules.json 집합 밖 색·반경·간격·폰트 없음, 그림자·그라디언트 없음. 점검 사항: (1) 컴포넌트 label 문구가 S7 인스턴스 오버라이드 문구('위 금지 항목이 포함되어 있지 않음을 확인했어요')와 다름(S7은 텍스트 덮어쓰기라 영향 없음), (2) checked=false의 icon/check #e0e0e0가 흰 box 위에 연하게 보임(대비 약 1.3:1, 장식 아이콘이라 텍스트 대비 금지 조합 아님), (3) checkbox-box 24×24는 단독 터치 타깃 44 미만이나 행 전체(컴포넌트 h64, S7 인스턴스 h48)가 44 이상, (4) 세트 프레임 자체 dashed 외곽선(Figma 기본 세트 표시)은 변경 아님. S7 영향: 26:203의 26:269, 26:274의 26:284 모두 x16 y298 358×48(content-area 안, 바로 위 prohibited-guide 하단 274와 간격 24, 겹침 없음, main 23:105/23:108 유지, 인스턴스 크기·label 덮어쓰기 유지). Figma는 수정하지 않음
- 수정(D12 대비 위반 해소, confirm-checkbox 23:112): checked=false variant(23:105)의 icon/check(90:394) 글자색만 #e0e0e0(hairline 22:8) → #707070으로 변경, 변수 color/text-muted(22:10)에 바인딩(흰 box 대비 4.95:1). 박스 스트로크·채움·checked=true·나머지 속성 그대로. S7 인스턴스 26:269의 icon/check(I26:269;90:394)가 #707070(22:10)으로 따라옴 확인
- 수정(S5 확정 반영): visibility-selector(23:98) option/member-only 설명 텍스트 23:60·23:70·23:80·23:90·23:97을 '멤버에게 공개돼요'로 변경 (텍스트만, ID 유지)
- 수정(사용자 요청, radio-wrap 통일): S4 radio-wrap 구조 기준으로 visibility-selector(23:98)의 라디오를 맞춤. 변경 전: 행 안 `radio` FRAME 20×20 자체가 채움 canvas·반경 radius/toggle·외곽선 1px을 가짐(ID 95:94 sel, 95:96, 95:97, 95:98, 95:99 sel, 95:101, 95:102, 95:103, 95:104 sel, 95:106 sel, 95:108, 95:109, 95:110 sel), 선택은 안에 radio-dot 10×10. 변경 후: 이 프레임을 그대로 두고(ID·ABSOLUTE 위치 유지) 이름을 `radio-wrap`으로 바꾸고 채움·외곽선·반경을 제거(투명 20×20), 안에 ellipse `radio` 20×20 추가(채움 canvas 22:5, 외곽선 1px INSIDE, 선택 = ink 22:4, 비선택 = hairline 22:8) 13개 신규. 선택 radio-dot(10×10 ellipse, ink 22:4)은 radio-wrap 안에 유지, 위치 x5 y5. 선택 행 stroke는 이미 ink 1px, 비선택 행 stroke 없음 그대로. 행 높이 71·세트 크기 변화 없음. S7 인스턴스 26:234(26:114)·26:254(26:161)에 radio-wrap > radio(+radio-dot)가 따라옴 조회 확인, 높이 229/150 그대로, S7 수정 없음. 스크린샷 23:54 확인: ink 행 위에서 흰 라디오와 ink 점이 보임
- 수정(사용자 요청, 포커스 링 1px): text-input 세트 23:122의 state=focus variant 23:120. 변경 전: stroke 2px INSIDE ink 22:4 바인딩, 세로 HUG, 342×51(strokesIncludedInLayout라 패딩 12+12+텍스트+선 4). 변경 후: stroke 1px INSIDE 유지, 색 22:4 바인딩 유지, 선 두께만 줄면 HUG 높이가 49로 줄어들어 세로를 FIXED 51로 고정해 높이 51 유지(패딩 12·반경·간격 그대로, 새 값 없음). 세트 716×51 그대로. state=rest 23:118은 테두리 없음 그대로 미수정. S7 인스턴스 26:224(26:116 안)·26:244(26:163 안)는 컴포넌트를 따라 stroke 1px, 색 22:4 바인딩 유지, 인스턴스에 2px 덮어쓰기 없음(overrides는 height·name·width와 텍스트뿐). 선을 줄인 뒤 인스턴스 높이가 49로 바뀌어 같은 높이 51(FIXED)로 고정함, y24 위치·부모 field-title 높이 75 그대로. 수치는 읽기 조회로 확인
- 수정(사용자 요청, visibility-selector를 S4 확정안에 맞춤): 기준 S4 19:3 안 visibility-selector 82:51(option 행 82:52 선택, 82:58, 82:64). 대상 23:98 variant 5개(23:54, 23:64, 23:74, 23:84, 23:91)의 option 행 13개. 변경 전: 행 세로 auto layout(패딩 12/16/12/48, 간격 4), 라디오 radio-wrap은 ABSOLUTE(x16 세로 중앙), 선택 행 채움 ink 22:4 + 글자(label·description) canvas 흰색, 라디오 radio가 radio-dot 위에 있어 점이 가려짐, 행 높이 71, variant 높이 229(non-seller 150), 설명 문구 member-only '멤버에게 공개돼요'·sale-request '검수를 거쳐 판매를 신청해요'. 변경 후(S4와 동일): 행 가로 auto layout, 패딩 12/16/12/16(22:24·22:25), 간격 12(22:24), 세로 가운데, 가로 FILL·세로 HUG, 최소 높이 44, strokesIncludedInLayout true. 자식 = radio-wrap(AUTO 배치, 20×20, 맨 앞) + option-text(세로, 간격 0(22:21), FILL/HUG, 신규 노드 99:29 등)가 label(15 SemiBold)·description(13 Regular, 150%) 포함. 선택 행 = 채움 canvas 22:5 + ink 22:4 1px INSIDE 외곽선, label ink 22:4, description ink-soft 22:9(#262626, 흰 바탕 대비 충분), radio = 채움 canvas + ink 1px + radio-dot ink(점이 위로 오게 순서 변경). 비선택 행 = 채움 canvas-soft 22:6(#f3f3f3), 외곽선 없음, label ink, description ink-soft, radio = 채움 canvas + hairline 22:8 1px. 반경 radius/input 16(22:18) 그대로. 설명 문구를 S4 문구로 교체: private '나만 볼 수 있어요', member-only '멤버가 볼 수 있어요', sale-request '승인 후 판매 자산으로 신청해요'(S7 인스턴스 오버라이드가 있는 텍스트는 오버라이드 유지). 결과 행 높이 선택 69·비선택 67(S4와 동일), 폭 342, variant 높이 seller 219·non-seller 144, label·description 글자색에 흰색 없음. 모든 채움·선은 tokens 변수 바인딩(실제 색값으로 재지정), 새 변수·색·반경·간격 없음. 스크린샷 23:74·26:114로 확인. S7 조회(수정 안 함): 26:234(26:114 안) main 23:54, 26:254(26:161 안) main 23:84가 컴포넌트를 따라 선택 행 흰 채움+ink 1px, 비선택 #f3f3f3으로 바뀜. 인스턴스 오버라이드는 크기(width/height)와 텍스트(26:234의 23:60·23:63, 26:254의 23:90 characters)뿐이고 채움·선 덮어쓰기 없음. 단 23:63(판매 신청 설명)은 오버라이드로 '판매 승인 회원만 선택할 수 있어요'라 S4 문구 '승인 후 판매 자산으로 신청해요'와 다름(미수정, 보고). 인스턴스 높이는 229 → 219(26:254는 150 → 144)로 줄어 아래 레이아웃 밀림 확인 필요
- 수정(사용자 요청, 파일 선택 버튼 + 아이콘): 대상 file-attach-row 23:99 안 button/attach 23:103. 변경 전: 88×44(가로 HUG·세로 FIXED 44), 패딩 좌우 16(22:25)·상하 0, 간격 0, 자식은 label 23:104 '파일 선택'(56×23)뿐, 채움 ink 22:4, texts 23:100 폭 218(FILL). 변경 후: 맨 앞에 `icon/plus` FRAME 108:402(16×16, 채움 없음, 기존 icon/<이름> 프레임 > `shape` 벡터 규칙을 따름) 추가. 안 벡터 `shape` 108:403은 두 선 교차(M8 3 L8 13, M3 8 L13 8), 선 2px·ROUND/ROUND(기존 24px 아이콘의 stroke 2px과 동일), 채움 없음, 선 색 color/canvas(22:5) 변수 바인딩(#ffffff). 버튼 itemSpacing을 spacing/4(22:22) 변수에 바인딩(기존 0 → 4), 세로 가운데 정렬(counterAxis CENTER), 패딩 좌우 16·상하 0 유지, 가로 HUG·세로 FIXED 44 유지(터치 영역 44 그대로). 결과 버튼 108×44(16+16+4+56+16), texts는 FILL이라 폭 218 → 198로 자동 축소(수정 불필요, texts FILL 이미 적용), 컴포넌트 23:99는 342×60 그대로(높이 변화 없음), label '첨부 파일' 198×23·hint '선택한 파일이 없어요' 198×17 한 줄 유지(줄바꿈·잘림 없음), 문구 변경 없음. 새 변수·hex·반경·간격 없음. 스크린샷 23:99는 요청했으나 이미지를 열 수 없어(셸·이미지 뷰어 없음) 눈으로 확인 못 함, 노드 재조회 수치로만 확인. S7 영향(수정 안 함): 이름이 file-attach-row인 인스턴스는 26:228(부모 field-file 26:124)·26:248(부모 field-file 26:171) 2개, main 23:99. 둘 다 크기 358×60 유지(높이 변화 없음)이고 button/attach가 78×44로 오버라이드된 상태이며, 안에 I26:228;108:402·I26:248;108:402 icon/plus가 따라와 나타남. 단 두 인스턴스의 label은 텍스트가 '삭제'(파일 선택된 상태, texts는 prompt-pack.zip/2.4MB)로 덮어쓰여 있어 '삭제' 앞에도 + 아이콘이 보임(의도와 다를 수 있음, 처리 필요하면 S7 인스턴스에서 icon/plus 숨김 또는 별도 결정)
- 수정(사용자 요청, 파일 선택 버튼 + 아이콘 표시 속성): file-attach-row 23:99에 불리언 컴포넌트 속성 `plus-icon`(키 plus-icon#109:2, 기본값 true)을 만들어 icon/plus 108:402의 visible에 연결. S7 인스턴스 26:228·26:248은 이 속성만 false로 설정('삭제' 앞 아이콘 숨김, 다른 오버라이드·텍스트·크기 그대로). 23:99 기본은 아이콘 보임(버튼 108×44). 두 인스턴스 button/attach는 아이콘 숨김 후 Hug로 78 → 58 폭(패딩 16+16+라벨 26), 높이 44·인스턴스 358×60 그대로, texts 폭은 FILL이라 244 → 264. 문구·색·반경 변경 없음
- 수정(사용자 요청, tab-bar 흰 배경+그림자, shadow/nav 스타일): (1) 효과 스타일 `shadow/nav` 신규, 스타일 ID `S:b6778c219288c41c596c8b89896060454b0dc099,`. 값 DROP_SHADOW #141414 불투명도 9%, x0 y-2 blur14 spread0(S4 시안 101:4 안 tab-bar 101:5 값과 동일). 색 변수 바인딩은 시도했으나 color/ink(22:4)가 불투명(a=1)이라 바인딩하면 그림자가 100%로 바뀌어(불투명도는 변수로 못 둠) 바인딩 해제, 값 고정. 설명란에 '하단 탭바 한정, 다른 곳 사용 금지'. (2) tab-bar 세트 23:53의 variant 5개(23:32, 35:3, 23:39, 35:10, 23:46) 변경 전: 채움 canvas-soft #f3f3f3(22:6 바인딩), 스트로크 없음, 효과 없음. 변경 후: 채움 canvas #ffffff(color/canvas 22:5 바인딩), 스트로크 없음 확인, 효과 스타일 shadow/nav 적용. 반경 radius/tab·패딩·탭 구성·아이콘·라벨·세트/variant ID 그대로. D12: 흰 배경에서 비선택 라벨 #262626, 선택 라벨 #141414라 통과(대비 높음, #707070 사용 없음). (3) S7 인스턴스 I73:543;72:297(home 36:49 footer 73:543 안, main 23:32), I73:572;72:297(skills 36:102 footer 73:572 안, main 23:39)에 흰 채움(22:5)+shadow/nav가 따라옴, 인스턴스 덮어쓰기 채움·효과 없음. S7 안 효과 있는 노드는 이 두 tab-bar 인스턴스뿐. footer 채움은 이미 canvas 흰색. (4) 토큰 가이드(87:3 페이지) 87:14에 'Shadow' 섹션 추가(제목 103:382, 설명 103:383, 견본 103:384 안 흰 박스 103:385 shadow/nav 적용, 값·용도 텍스트 103:387, 기존 내용 변경 없음, 프레임 높이 1974 → 2310). 견본 박스는 가이드 안 shadow/nav 두 번째 사용이나 토큰 견본 목적. 스크린샷은 파일로 내려받을 수 없어 눈으로 확인 못 함, 노드 재조회 수치로만 확인
- 수정(사용자 요청, 그림자 y+4, tab-bar Hug): 요청 'tab bar 하단에 그림자 효과가 안 나타난다. 높이는 허그로 해줘.' (1) 그림자: 효과 스타일 shadow/nav(S:b6778c219288c41c596c8b89896060454b0dc099,) 값 변경 전 DROP_SHADOW #141414 불투명도 9%, x0 y-2 blur14 spread0 → 변경 후 #141414 불투명도 10%, x0 y+4 blur16 spread0. 스타일 수정이 따라옴 확인: variant 5개(23:32, 35:3, 23:39, 35:10, 23:46), S7 인스턴스 I73:543;72:297·I73:572;72:297, 가이드 견본 103:385 모두 y4·blur16·불투명도 10%로 조회(직접 맞춘 노드 없음). 토큰 가이드 값 텍스트 103:387을 '불투명도 10%, x 0, y +4, blur 16'으로 갱신(나머지 문장 그대로, 견본 103:385는 스타일을 따라감). S4 proposal/tab-bar-shadow(101:4)는 건드리지 않음. (2) Hug: tab-bar variant 5개 세로 HUG·가로 FIXED 358은 이미 그 상태였음(변경 없음), 높이 64 그대로(탭 56 + 패딩 4×2). S7 인스턴스 I73:543;72:297·I73:572;72:297도 세로 HUG·높이 64, FIXED 덮어쓰기 없음(해제할 것 없음). (3) 가려짐 해결: footer 73:543·73:572(y746, 390×98, clipsContent=false)의 tab-bar는 y0~64, 그 아래 home-indicator(y64~98, 390×34, 흰 채움 22:5)가 자식 순서상 tab-bar 뒤에 그려져 그림자를 덮고 있었음(그림자 번짐 약 20, 아래 여유는 화면 하단 844까지 34라 공간은 충분). 최소 변경: footer 컴포넌트 세트(72:296의 부모)의 variant에 itemReverseZIndex=true(앞 자식이 위에 그려짐)를 켜 tab-bar가 home-indicator 위로 오게 함. 자식 순서·위치·크기·채움·레이아웃 변화 없음, 인스턴스 73:543·73:572에 따라옴 확인. 화면 36:49·36:102는 clips=true이나 그림자가 844 안에서 끝나 잘리지 않음. 스크린샷 36:49 확인: tab-bar 아래 그림자가 보임
- 수정(사용자 요청, visibility-selector 라디오·카드 stroke): 대상 23:98 전 variant 5개(23:54, 23:64, 23:74, 23:84, 23:91)의 option 행 13개. 변경 전: 라디오 노드 없음(행은 label+description 세로 배치만), 행 stroke 없음(선택 행은 ink 채움, 나머지 canvas-soft 채움), paddingLeft 16(22:25). 변경 후: (1) 각 option 행에 자식 `radio` 추가(20×20 frame, 도형만 사용, 글자 아님, layoutPositioning ABSOLUTE, x16 세로 중앙 y25.5, 채움 canvas 22:5, 반경 radius/toggle 22:16, 외곽선 1px INSIDE). 선택 안 된 행: 외곽선 hairline #e0e0e0(22:8), 점 없음. 선택된 행([selected]): 외곽선 ink #141414(22:4) + 자식 `radio-dot` 10×10 ellipse 채움 ink(22:4). 선택 행은 ink 채움이라 라디오 바탕을 canvas로 둬서 ink 외곽선·점이 보이게 함(ink 단색 원은 ink 행 위에서 안 보임). (2) 선택 행 stroke 신규 추가: ink(22:4) 1px INSIDE, strokesIncludedInLayout=false(행 높이 71 유지, 선택 안 된 행은 stroke 없음 그대로). (3) 라디오 자리 확보로 option 행 paddingLeft 16 → 48(spacing/48 22:28 바인딩), label/description 폭 310 → 278. 그 외 패딩·간격·반경·높이 71(터치 타깃 44 이상)·세트 크기(seller 342×229, non-seller 342×150) 변화 없음. option 이름·[selected] 표기·문구·V1(기본 option/private[selected] 하나, non-seller에 sale-request 없음) 유지. 확인: get_variable_defs(23:54)에 canvas·ink·hairline·radius/toggle·spacing/48 바인딩 조회, 새 hex 없음. S7 영향: 26:114의 인스턴스 26:234와 26:161의 인스턴스 26:254에 radio가 따라옴(행 71 유지, 크기 358×229 / 358×150 그대로, 덮어쓴 값은 기존 텍스트·크기뿐), S7 수정 없음
- 수정(사용자 요청, 텍스트 스타일 12개·폰트 가이드 보강): docs/design.md Typography 표 값 그대로, 요청 값과 차이 없음. 로컬 텍스트 스타일 12개 신규(Pretendard, 줄 높이 퍼센트, 자간 0px): type/display S:475dcc687ae2611f843c428d592d142ab6e598b5, (32 Bold 130%) / type/heading-1 S:e36cc4bdb5ea76cc97ba5f79c3af0eb4e9daa22b, (28 Bold 130%) / type/heading-2 S:117f0760a0f16bc5e3decf73a45aec74f81f0cae, (24 Bold 135%) / type/heading-3 S:78b19d8539bc690573ffc3792de7a5c4ccb356f1, (20 Bold 135%) / type/heading-4 S:e2fc4f3076569dc8eaf94a127eb1afa4572851f0, (18 Bold 135%) / type/title S:f90c26ee42e67b9c780ba0942b4505dc1ec80f73, (17 SemiBold 140%) / type/body-lg S:19b9623f701e645a8918ef20a05e494692207fe0, (17 Light 150%) / type/body S:a5342139ca5ac0420e430d04a27aa03fe25b15bc, (15 Regular 150%) / type/body-sm S:3f20720338e2be0c6414a2dbc465b018315e1a2e, (13 Regular 150%) / type/link S:a30a7aeef2a5eb6f299db669b0769b89be5b7bed, (15 SemiBold 150%) / type/label S:3c6ff230c87b12027d92ab30049cc92c8c27c4a2, (12 SemiBold 140%) / type/caption S:1a1180eda6dc08acad12e63d2d703e587742f4e4, (12 Regular 140%). 가이드 87:14 type-scale 87:113의 견본 텍스트 12개(87:115 등 각 type/* 프레임 첫 자식)에 해당 스타일 적용, 12px 라벨을 '이름 · 크기 · 굵기 · 줄 높이 · 자간' 형식으로 갱신(예: 'display · 32px · 700 (Bold) · 130% · 0'), 라벨 복제로 용도 한 줄 `use/<이름>` 추가(ID 115:3, 115:5, 115:7, 115:9, 115:11, 115:13, 115:15, 115:17, 115:19, 115:21, 115:23, 115:25, design.md Use 열의 한글 요약, 라벨과 같은 12 Regular·변수 22:10 색). type-scale 높이 613 → 875, 가이드 87:14는 자동 레이아웃이라 높이 2310 → 2572, Shadow 섹션(103:382 이하) y 1974 → 2236(+262), 섹션 간격 그대로. 기존 S6 컴포넌트·S4·S5·S7 텍스트에는 스타일을 적용하지 않음(노드 직접 지정 유지). 색 견본·반경·간격·Shadow 내용 변경 없음, 새 hex 없음. 스크린샷은 내려받을 수 없어 눈으로 확인 못 함, 노드 재조회 수치로만 확인
- 수정(사용자 요청, 텍스트 스타일 적용): S6 컴포넌트·variant 안 TEXT 92개(다른 컴포넌트 인스턴스 안쪽 글자 8개 제외)에 type/* 스타일 적용, 크기·굵기 불일치 0개(미적용 없음). 매핑 15 SemiBold→link, 17 SemiBold→title, 15 Regular→body, 13 Regular→body-sm, 12 SemiBold→label, 12 Regular→caption. 글자 색 바인딩·크기·굵기·문구·이름·ID 변경 없음, 변한 것은 줄 높이(AUTO→스타일 %)와 자간(0)뿐.
  - 적용 수: footer 0(안쪽 인스턴스뿐) / home-indicator 0 / action-area 3 / header 2 / status-bar 1 / text-input 2 / submit-button 2 / confirm-checkbox 4 / file-attach-row 3 / visibility-selector 26 / tab-bar 25 / list-row 5 / skill-card 9 / status-badge 10
  - 높이 변화(전→후): action-area·header·status-bar·footer·text-input·submit-button·confirm-checkbox·file-attach-row·visibility-selector·status-badge·tab-bar variant 높이 변화 없음(안쪽 글자 줄 높이만 커지고 위치 재배치, tab-bar 라벨 14→17). list-row 두 variant 66 → 75 (title 18→23, 수정일/개수 요약 16→20). skill-card layout=full 92 → 103 (verified true/false 모두), layout=compact 88 → 101. 세트 프레임(35:90, 35:82)의 표시 높이는 그대로 66·92(variant가 세트 밖으로 자람, 세트 크기는 수정 안 함)
  - 되돌린 노드(S6): 없음. 컴포넌트 높이 FIXED 고정 없음. 터치 타깃 44 미만 발생 없음. 주의: list-row 75는 S7 홈에서 content-area(647)를 넘겨 홈 화면 쪽에서 되돌림(s7-screens.md 참고)
- 수정(사용자 결정 A안, list-row·skill-card 스타일 되돌림, type/label-md 추가): (1) 새 텍스트 스타일 `type/label-md` ID `S:8889feaeffe6a49afb3d4e0abfd0b1849d825fb7,` (Pretendard SemiBold 13px, 줄 높이 140%, 자간 0px, design.md에 없는 추가 스타일). 토큰 가이드 87:14 type-scale 87:113에 견본 프레임 119:3 `type/label-md`(견본 119:4 스타일 적용, 라벨 119:5 'label-md · 13px · 600 (SemiBold) · 140% · 0', 용도 119:6 '필드 제목, 칩 라벨(design.md에 없는 추가 스타일)')를 type/link 뒤·type/label 앞에 추가. type-scale 875 → 941, 가이드 2572 → 2638, Shadow 섹션 y 2236 → 2302(+66). S6 컴포넌트 안 13px SemiBold 글자는 없음(조회 확인)이라 S6 적용 0개. (2) A안: list-row 세트 35:90 variant 2개(23:26, 35:83)와 skill-card 세트 35:82 variant 3개(23:20, 35:69, 35:70)의 모든 TEXT 노드(list-row 6, skill-card 9, 중첩 status-badge 인스턴스 글자 I23:30;23:3 포함)에서 텍스트 스타일 해제, 줄 높이 AUTO·자간 0 복원. 크기·굵기·색·문구 유지(색 채움 동일 확인). 복원 후 높이: list-row progress 66, summary 66 / skill-card full(verified=true) 92, compact 88, full(verified=false) 92. 컴포넌트 높이는 HUG 그대로, FIXED 고정 없음. 높이가 안 돌아온 곳 없음. status-badge 컴포넌트 자체(23:19)와 tab-bar 등 나머지는 변경 없음.
- 수정(사용자 요청, 입력창 반경 8): rules.json radius.input 16 → 8에 맞춤. 공용 변수 radius/input(22:18, 값 16)은 list-row·option 행·confirm-checkbox·file-attach-row도 쓰므로 값 그대로 두고, tokens 컬렉션에 새 변수 `radius/field`(FLOAT, 8, scope CORNER_RADIUS) ID VariableID:106:406 신규. text-input에만 바인딩. 변경 전 → 후: text-input 세트 23:122의 variant state=rest 23:118, state=focus 23:120의 네 모서리 반경 16(22:18 바인딩) → 8(106:406 바인딩). 높이(rest 47, focus FIXED 51)·focus 링 1px·패딩·채움 그대로. S7 인스턴스 26:224(focus), 26:226(rest), 26:244(focus), 26:246(rest), 36:104(rest) 모두 조회 결과 반경 8, 변수 106:406 바인딩, 높이 51/47/51/47/47 그대로 → 컴포넌트를 따라옴(반경 덮어쓰기 없음, 풀 것 없음, S7 노드 수정 없음). 토큰 가이드 87:14 Radius 섹션 radius-swatches(87:57)에 radius-item 복제본 106:407(shape 106:408 반경 106:406 바인딩, 이름 106:409 'radius/field', 값 106:410 '8')을 radius/input 항목 뒤에 추가, 기존 항목·내용 유지. S6 컴포넌트 설명 중 list-row·confirm-checkbox·visibility-selector 등의 'radius/input 16' 기록은 그대로 유효. 판정 스크립트는 돌리지 않음
- 수정(사용자 요청, text-input 상태별 높이 통일): text-input 세트 23:122의 state=rest 23:118 높이 47(세로 HUG) → 48, state=focus 23:120 높이 51(세로 FIXED) → 48. 두 variant 모두 세로 FIXED 48, 세로 가운데 정렬 유지(counterAxis CENTER), 패딩 12/16/12/16(spacing 변수 바인딩 유지), 포커스 링 1px INSIDE(ink 22:4), 반경 8(radius/field 106:406), 채움 #f0f0f0(field 22:7), 글자·문구·색·이름·ID 그대로. placeholder 글자 높이 23 + 상하 패딩 24 = 47이 48 안에 들어가 잘림 없음, 터치 타깃 48(44 이상). 세트 프레임 23:122는 716×51 그대로(variant가 48이라 아래 3px 빈 여백, 세트 크기 미수정). 판정 스크립트는 돌리지 않음
- 수정(사용자 요청, 버튼 반경 8): rules.json radius.button 8에 맞춤. 공용 변수 radius/button(22:14, 9999)은 home-indicator 막대·header 터치 영역·배지류도 쓰므로 값 그대로 두고, tokens 컬렉션에 새 변수 `radius/button-rect`(FLOAT, 8, scope CORNER_RADIUS) ID VariableID:120:408 신규. 버튼에만 네 모서리 바인딩. 높이·채움·외곽선·글자·아이콘·이름·ID 그대로.
  - 변경 전 → 후(9999 radius/button 22:14 → 8 radius/button-rect 120:408): submit-button 세트 23:117의 variant 23:113(enabled)·23:115(disabled) / action-area 세트 64:190의 count=2 안 64:178(save-draft-button)·64:176(register-button), count=1 안 64:181(submit-button[disabled]) / file-attach-row 23:99 안 23:103(button/attach, 108×44)
  - 인스턴스 따라옴 조회: S6 footer type=action 안 I72:326;64:178·I72:326;64:176, 그리고 S7 인스턴스(s7-screens.md 참고) 모두 반경 8·변수 120:408로 따라옴, 덮어쓴 반경 없음
  - 안 바꾼 것(보고): header-left/right 64:161·64:164·64:169·64:172(투명 44×44 아이콘 터치 영역), 컴포넌트 세트 wrapper 프레임(23:117 반경 5, 64:190 반경 5), checkbox-box(23:106 등, radius/toggle), tab-bar·tab·icon-holder·status-badge·bar(72:4)·칩은 알약 그대로
  - 토큰 가이드 87:14 Radius 섹션: radius-item 120:409(shape 120:410 반경 120:408 바인딩, 이름 120:411 'radius/button-rect', 값 120:412 '8 · 버튼(사각 라운드)')을 radius/field 항목 뒤에 추가. 기존 radius/button 값 텍스트 87:61을 '9999 · 알약 전용(배지·탭·토글·막대)'로 수정, 하단 주석 87:74도 알약 전용·button-rect 안내로 수정. 한 줄에 6개가 안 들어가(656폭) radius-swatches 87:57을 wrap(폭 656, 행 간격 16)으로 바꿔 radius/none이 둘째 줄로 내려감(높이 104 → 256). 가이드 87:14 높이 2638 → 2790(자동 레이아웃, 아래 섹션 y 자동 +152, 겹침 없음)
- 수정(사용자 요청, status-badge 4종 아이콘, 크기 16×16 통일 (이후 12×12로 변경)): status-badge 세트 23:19의 variant 7개 모두 라벨 앞 16×16 (이후 12×12로 변경) 아이콘 프레임(채움 없음, clip 꺼짐). 배지 itemSpacing 4를 spacing/4(VariableID:22:22)에 바인딩, 세로 가운데 정렬, 가로 Hug, 높이 불변(27/25), 외곽선·채움·반경·라벨(12px SemiBold) 그대로.
  - 신규 벡터 아이콘(프레임 icon/<이름> 안 벡터 `shape`, 선 1.5px, 둥근 끝·꼭짓점, 채움 없음, 선 색 변수 바인딩): 작성 중 23:2 → icon/edit 123:408(shape 123:409, color/text-muted 22:10), 폭 60 → 80. 임시저장 23:4 → icon/save 123:410(shape 123:411, text-muted), 68 → 88. 제출 완료 23:6 → icon/send 123:412(shape 123:413, color/ink 22:4), 71 → 91. 검수 대기 23:8 → icon/clock 123:414(shape 123:415, ink), 71 → 91
  - 기존 3종(글자 노드 11×17 '!' '✓' '✕')은 글자 노드를 유지하고 16×16 아이콘 프레임(자동 레이아웃, 가운데 정렬)으로 감쌈 (16×16, 이후 12×12로 변경). 프레임 이름이 기존 노드명을 이어받고 안 글자 노드 이름은 `shape`로 바꿈(글자 크기·색·문구 불변): 수정 요청 23:10 → icon/alert 123:416(글자 23:11), 폭 79 → 91. 승인됨 23:13 → icon/check 123:417(글자 23:14), 71 → 76. 반려 23:16 → icon/close 123:418(글자 23:17), 60 → 65
  - 세트 23:19: variant가 절대 배치라 겹침 방지로 x 재배치(간격 32 유지: 0, 112, 232, 355, 478, 601, 709), 세트 폭 673 → 774, 높이 27. 스크린샷으로 7개 확인
  - 판정 스크립트는 돌리지 않음
- 수정(사용자 결정, 배지 아이콘 12×12로 변경): 직전 16px 통일 지시는 무효. status-badge 세트 23:19 variant 7개의 아이콘 프레임을 ID·이름 유지한 채 16×16 → 12×12로 리사이즈(123:408 edit, 123:410 save, 123:412 send, 123:414 clock, 123:416 alert, 123:417 check, 123:418 close). 간격 spacing/4·세로 가운데·선 색 변수 바인딩·clip 꺼짐 그대로.
  - 신규 4종 벡터 `shape`: 비율 유지 0.75배, 프레임 안 가운데, 선 1.5px 유지(확인). edit 11×11 → 8.25×8.25 (x1.875 y1.875), save 10.5×11 → 7.875×8.25 (x2.0625 y1.875), send 12×12 → 9×9 (x1.5), clock 12×12 → 9×9 (x1.5)
  - 기존 3종 글자 `shape`(12px SemiBold 유지): alert 4×17, check 11×17, close 11×17. 글자 높이 17이 12를 넘지만 프레임 clip 꺼짐 상태에서 가운데 정렬만(x=(12-폭)/2: alert 4, check·close 0.5, y -2.5). 글자 박스만 넘치고 글리프 자체는 12×12 안(잘림 없음)
  - 배지 폭 전 → 후(높이 27/25 불변): 작성 중 80 → 76, 임시저장 88 → 84, 제출 완료 91 → 87, 검수 대기 91 → 87, 수정 요청 91 → 87, 승인됨 76 → 72, 반려 65 → 61
  - 세트 23:19: variant x 재배치(간격 32 유지: 0, 108, 224, 343, 462, 581, 685), 세트 폭 774 → 746, 높이 27
  - 판정 스크립트는 돌리지 않음
- 수정(사용자 요청, list-row 앞 20px 아이콘): list-row 세트 35:90 두 variant의 row-info 앞(맨 왼쪽)에 20×20 아이콘 추가. kind=progress(23:26)에 `icon/file` 127:5(안 벡터 `shape` 127:6, 12×16 접힌 모서리 문서), kind=summary(35:83)에 `icon/folder` 127:7(안 벡터 `shape` 127:8, 16×14 폴더). 프레임 채움 없음, 벡터 채움 없음·선 1.5px·ROUND/ROUND·선 색 color/ink-soft(VariableID:22:9) 바인딩. 아이콘과 row-info 간격은 기존 itemSpacing 12(spacing/12, VariableID:22:24 바인딩 유지), 세로 가운데 정렬(counterAxis CENTER, 아이콘 y23). row-info는 FILL(layoutGrow 1) 유지.
  - row-info 폭 전 → 후: progress 206 → 174, summary 298 → 266 (각 -32 = 아이콘 20 + 간격 12). 제목·보조 글 모두 한 줄(높이 18·16, 줄 높이 AUTO, 말줄임 없음), 행 높이 66(HUG, 상하 패딩 16) 그대로. 글자 스타일·색·반경·변수 바인딩 변경 없음, 텍스트 스타일 새로 적용 안 함.
  - S7 영향: 이름이 list-row인 인스턴스 6개(홈 36:56·36:62·36:68·36:86, sale-request 26:261·26:276) 모두 아이콘이 따라옴(덮어쓴 값 없음), 줄바꿈·겹침 없음, 높이 66. 자세한 내용은 s7-screens.md
  - 판정 스크립트는 돌리지 않음

## 수정(사용자 요청, skill-card 카테고리 12px·연하게·타이틀 위)
- 전: 카테고리·유형 글자(12px Regular, #707070, 줄 높이 AUTO)가 meta 행(35:73, 35:80) 안, 제목·설명 아래. 후: 크기·굵기·색 불변(이미 12px Regular #707070 = 허용 팔레트에서 가장 연한 본문 색, #adadad 금지라 더 연하게 못 함). 위치만 이동.
- full verified=true 23:20: 카테고리 35:74를 카드 맨 위(제목 35:71 바로 위)로 이동, 폭 FILL. meta 35:73엔 '검증된 스킬'만 남음. 높이 92 → 110 (HUG, 간격 4 유지)
- full verified=false 35:70: 카테고리 35:81을 맨 위로 이동. meta 35:80이 비어 숨김(visible=false). 높이 92 → 92(불변)
- compact 35:69: 카테고리 노드가 원래 없음(제목·설명만). 변경 없음, 높이 88 유지
- 새 hex·텍스트 스타일 적용 없음. 판정 스크립트는 돌리지 않음
- 수정(사용자 요청, 삭제 버튼 X 아이콘): file-attach-row 23:99(342×60 불변) 안에 button/delete 131:436 추가 (44×44, 반경 radius/button-rect VariableID:120:408 네 모서리 바인딩, 채움 color/ink 22:4 바인딩, 외곽선 없음, 자동 레이아웃 가운데). 안 icon/x 131:437(16×16, 채움 없음) 안 벡터 `삭제` 131:438(X 두 선 교차 10×10, 선 2px 둥근 끝·꼭짓점, 선 색 22:5 바인딩). 화면에 글자 없음, '삭제'는 벡터 레이어 이름에만 남김.
  - 방식: variant 대신 불리언 속성 추가(안전, 기존 인스턴스·ID 유지). show-attach#131:0(기본 true, button/attach 23:103 visible 연결), show-delete#131:1(기본 false, button/delete visible 연결). 기존 plus-icon#109:2 유지. 기본 상태(empty) 외형은 변경 전과 동일.
  - 이름 icon/x는 status-badge의 icon/close와 구분. 시안 기준(S4 delete-action 82:45)은 투명 원형 + 글자 '삭제'(X 아이콘 없음)라 형태 기준이 없어, 스타일은 button/attach(검정 채움, 흰 선)를 따름. 반경은 원형 9999가 아닌 8(D04). S4·S5는 수정하지 않음

## 수정(사용자 요청, 삭제 버튼 배경 제거·X 검정)
- button/delete 131:436: 채움 color/ink 22:4 → 없음(투명). 외곽선 없음, 44×44, 반경 8(radius/button-rect 120:408 바인딩 유지), 이름·show-delete 연결 유지.
- 벡터 `삭제` 131:438(icon/x 131:437 안, 16×16, 선 2px 둥근 끝): 선 색 color/canvas 22:5(흰색) → color/ink 22:4(#141414) 바인딩. 새 hex 없음.
- S4·S5 delete-action(82:45, 88:223 등)은 수정하지 않음.

## 수정(사용자 요청, skill-card 검증됨 배지·텍스트 간격 8)
- 배지: full verified=true 23:20의 meta 35:73 안 '검증된 스킬' 글자 35:75를 새 프레임 `badge/verified` 134:2 안으로 옮김(status-badge 이름 아님). 규격: 가로 auto layout 가로·세로 HUG(FIXED 아님), 세로 가운데 정렬, 반경 radius/badge(22:15, 9999) 네 모서리 바인딩, 채움 color/canvas-soft(22:6) 바인딩, 외곽선 없음, 패딩 상하 spacing/4(22:22)·좌우 spacing/8(22:23) 바인딩, 글자 12px SemiBold·색 color/ink(22:4) 바인딩, 줄 높이 AUTO(텍스트 스타일 미적용). 크기 71×22. 위치는 meta 행(설명 아래) 그대로. verified=false 35:70의 meta 35:80은 숨김 그대로.
- 간격: itemSpacing 4 → 8(spacing/8 22:23 바인딩) 세 variant 모두. 23:20(카테고리↔제목↔설명↔meta 배지 3곳), 35:70(카테고리↔제목↔설명 2곳, meta 숨김 상태), 35:69(제목↔설명 1곳). 카드 패딩 16·meta 가로 간격 0은 그대로.
- 카드 높이 전 → 후(HUG 유지): full verified=true 23:20 110 → 130(간격 +4×3 =12, 배지 22 vs 글자 14 = +8 → +20), full verified=false 35:70 92 → 100(+8), compact 35:69 88 → 92(+4)
- 새 hex·텍스트 스타일 없음. 판정 스크립트는 돌리지 않음

## 수정(사용자 요청, badge/verified를 카테고리 줄 우측으로)
- 대상: skill-card 세트 35:82의 variant `layout=full, verified=true` 23:20만. 35:69, 35:70 및 다른 컴포넌트는 수정 안 함.
- 새 행 프레임 `category-row` 139:36 (카드 맨 위 자식, 제목 35:71 위): 가로 auto layout, 가로 FILL(324, layoutAlign STRETCH)·세로 HUG(22), 세로 가운데 정렬, 간격 0, 패딩 0, 채움 없음. 자식 = 카테고리 35:74(왼쪽, 가로 FILL layoutGrow 1, 글자 높이 HEIGHT 자동 14) + `badge/verified` 134:2(오른쪽 끝 x253, 71×22 불변, 바인딩 불변).
- meta 35:73은 비어서 visible=false. 카드는 HUG 유지(세로 AUTO), FIXED 고정 없음. 카드 패딩 16·간격 8(spacing 변수 바인딩) 그대로. 새 hex·변수·텍스트 스타일 없음.
- 카드 높이 전 → 후: 23:20 130 → 108 (카테고리 줄 22 + 제목 20 + 설명 16 + 간격 8×2 + 패딩 32 + 선 2). 세트 35:82 안 다른 variant 35:69(92), 35:70(100)은 변경 없음.
- S7 영향(수정 안 함, 조회): 23:20 인스턴스는 S7 `screen/skills` 36:102(844 불변) 안 skill-list 36:121 (x16 y156) 의 skill-card 36:122, 36:133 두 개. 둘 다 컴포넌트를 따라 높이 130 → 108. skill-list는 자동 레이아웃(간격 24)이라 아래 카드가 올라와 위치가 바뀜: 36:128 (100 그대로, y 154 → 132), 36:133 (y 308 → 256, 130 → 108), 36:139 (100 그대로, y 432 → 388). skill-list 높이 532 → 488(이전 값은 높이·간격 합 계산치, 직접 조회 아님). 화면 높이 844은 그대로이고 하단 요소와 겹침은 없고 오히려 44 여유가 생김. 36:122 y0 불변. S7 노드는 수정하지 않았음. 판정 스크립트는 돌리지 않음
- 추가(사용자 요청, 텍스트 스타일 가이드 적용, 23:20만): 배지 글자 35:75(12 SemiBold) → `type/label`(12 SemiBold 140%), 카테고리 글자 35:74(12 Regular) → `type/caption`(12 Regular 140%). 크기·굵기가 가이드와 같아 둘 다 적용. 색 바인딩(fills)·문구·자간 0 유지. 줄 높이 AUTO → 140%(글자 높이 14 → 17). 맞지 않아 적용 못 한 글자 없음. 제목 35:71·설명 35:72와 다른 variant 글자는 건드리지 않음.
  - 높이 전 → 후: 배지 134:2 71×22 → 71×25(글자 줄 높이 때문에 HUG로 커짐, 폭 불변), category-row 139:36 22 → 25, 카드 23:20 108 → 111(HUG 유지, FIXED 없음). 요청 전 130 → 111.
  - S7 재조회(최종값, 위 S7 수치는 스타일 적용 전 값): skill-card 36:122 높이 111 y0, 36:128 100 y135, 36:133 111 y259, 36:139 100 y394, skill-list 36:121 높이 494(y156, 부모 content-area 높이 647). 화면 36:102 높이 844 불변은 이전 조회 기준, 이번엔 미재조회.

## 수정(사용자 요청, list-row·section/progress 텍스트 스타일 적용)
- 70행 A안(list-row 스타일 해제)을 이 범위에서 다시 뒤집음. 색 바인딩·문구·이름·ID 변경 없음. 컴포넌트 HUG 유지, FIXED 없음.
- 적용 매핑(원본 list-row 세트 35:90): 23:28 title(15 SemiBold) → type/link / 23:29 최근 수정일(13 Regular) → type/body-sm / 35:85 title(15 SemiBold) → type/link / 35:86 개수 요약(13 Regular) → type/body-sm / 35:89 화살표(17 SemiBold) → type/title
- section/progress 36:53: 제목 36:54('진행 현황', 18 Bold)는 이미 type/heading-4가 적용돼 있어 변경 없음(높이 24 그대로). list-row 인스턴스 36:56·36:62·36:68의 제목(I…;23:28)은 type/link, 수정일(I…;23:29)은 type/body-sm. 인스턴스 글자는 컴포넌트를 따라오지 않아 직접 적용.
- 높이 전 → 후: list-row 23:26·35:83 66 → 75 (title 18→23, 보조 16→20, row-info 34→43, 화살표 20→24). 세트 프레임 35:90은 66 그대로(variant가 세트 밖으로 자람). section/progress 36:53 290 → 317 (list 36:55 222 → 249, 행 75, 간격 12). 요청서의 전 287은 실제 조회 290.
- 홈 content-area 66:263 y 전 → 후: greeting 36:50 y16 그대로, section/progress 36:53 y91 그대로(h290→317), recommended-skills 36:74 y405 → 432, list-row 36:86 y557 → 584. 내부 list 행: 36:56 y0, 36:62 y78 → 87, 36:68 y156 → 174.
- 홈 하단 겹침 확인: 겹침 있음(미해결). content-area는 y99 높이 647 FIXED, clip 켬, 하단 패딩 32. 마지막 자식 36:86이 y584~650으로 content-area 높이 647을 3 넘고, 패딩 32를 더한 끝은 781로 footer 73:543(y746, 화면 좌표)과 35 겹침. 36:86 하단 화면 좌표 749가 footer 746을 3 침범하며 clip으로 잘릴 수 있음. 전(36:86 y557~623, 화면 좌표 722)에는 footer와 24 간격이 있었고 패딩 32 포함 끝 754로 패딩만 8 걸쳤음. S7 직접 수정 금지 범위라 고치지 않음. 사용자 결정 필요(요소 높이·간격 조정, 36:86 이동·제거 등).
- 미적용 글자: 없음(크기·굵기 맞는 스타일 모두 존재). status-badge 중첩 글자(I23:30;23:3 등)와 원본 23:19는 건드리지 않음.
- 다른 화면 조회(수정 안 함): list-row 인스턴스는 sale-request@unchecked 26:203의 26:261, @checked 26:274의 26:276도 있음. 컴포넌트를 따라 66 → 75, 글자 link/body-sm 적용됨. content-area(66:205, 66:234, 663 FIXED) 안 prohibited-guide y106 → 115, confirm-checkbox y322 → 331(끝 379, content-area 끝 662 안, footer y762와 겹침 없음). 스킬 라이브러리 36:102와 register 화면에는 list-row 인스턴스 없음, 변화 없음.
- 불일치 보고: 홈 36:86(kind=summary 인스턴스)은 글자 I36:86;35:85·35:86이 인스턴스 덮어쓰기로 컴포넌트 스타일이 따라오지 않아 스타일 없음(18/16 그대로), 화살표 I36:86;35:89만 type/title(24)로 바뀜. 높이 66 유지. 범위 밖이라 손대지 않음.
- 스크린샷은 확인 안 함, 노드 재조회 수치로만 확인. 판정 스크립트는 돌리지 않음.

## 수정(사용자 요청, nav footer 전체 영역 투명)
footer 세트 72:333의 type=nav 컴포넌트 안 바깥 영역 채움만 제거(투명). 컴포넌트에서 바꿨고 인스턴스가 따라옴.
- 변경 노드(전 → 후): 72:296 footer type=nav 390×98 채움 SOLID #ffffff(color/canvas 변수 22:5 바인딩) → 없음(fills=[]) / 72:323 nav 안 home-indicator 인스턴스 390×34(탭바 아래 영역) 채움 SOLID #ffffff(변수 22:5) → 없음. 72:323은 이 컴포넌트 안 인스턴스에서만 채움을 비움(home-indicator 메인 컴포넌트는 action footer가 같이 쓰므로 수정 안 함). 안 bar(I72:323;72:4, #141414 변수 22:4)는 그대로.
- 인스턴스 따라옴 확인: 73:543(홈)·73:572(스킬) 채움 0, 안 home-indicator I73:543;72:323·I73:572;72:323 채움 0. 인스턴스에 덮어쓴 채움 없음 → 덮어쓴 인스턴스 목록: 없음, 인스턴스 노드는 수정 안 함.
- 그대로: footer y746·390×98, 레이어 순서(맨 위), 화면 프레임 390×844, 홈 content-area 66:263 HUG(691).
- tab-bar(알약) 전→후 동일 조회(72:297, I73:543;72:297, I73:572;72:297): 채움 SOLID #ffffff color/canvas 22:5 바인딩, 외곽선 0, effects 1(그림자 예외), 반경 9999, 358×64 — 전 후 같음. 탭 글자·아이콘: 선택 탭 라벨 #141414(color/ink 22:4 바인딩), 비선택 #262626 — 전 후 같음(탭 노드는 수정 안 함). 복구 필요 없음.
- 안 건드림: action 타입 footer(73:509, 73:517, 73:525, 73:533)와 그 안 home-indicator·action-area 채움 흰색 유지. 새 hex·변수 없음. 판정 스크립트·스크린샷 미실행, 노드 재조회로 확인.

## 수정(사용자 요청, 컴포넌트 글자 텍스트 스타일 전체 적용)
- 조회 범위: S6 페이지 컴포넌트 안 TEXT 101개(중첩 인스턴스 글자 포함, 페이지에 떨어진 라벨 147:442 제외). 이전 단계에서 이미 type/*가 걸린 92개는 그대로 두고, 이번에 남은 글자 8개에 스타일 적용 → 100개 적용, 1개 미적용(147:442).
- 이번 적용 매핑 8개(노드 ID 기준, variant 소속은 높이 변화로 추정: 23:20 111→119는 35:71·35:72): 35:71 제목(17 SemiBold) → type/title, 35:72 설명(13 Regular) → type/body-sm, 35:76 (15 SemiBold) → type/link, 35:77 (13 Regular) → type/body-sm, 35:78 (17 SemiBold) → type/title, 35:79 (13 Regular) → type/body-sm, 35:81 카테고리(12 Regular) → type/caption / 중첩 인스턴스 글자 list-row 23:26 안 status-badge I23:30;23:3(12 SemiBold) → type/label. type/label-md(13 SemiBold)와 body·body-lg·heading-*에 해당하는 글자는 S6에 없음.
- 미적용 목록: 147:442 (S6 페이지 최상위 TEXT 'label', 12 SemiBold, 150%, 컴포넌트 아님, 범위 밖이라 손대지 않음, 스타일 type/label로 맞출 수 있음). 크기·굵기가 맞는 스타일이 없어 못 적용한 글자: 0개.
- 중첩 인스턴스 글자: list-row 23:26 안 배지 인스턴스 글자 I23:30;23:3은 원본 status-badge 글자(23:3, 스타일 있음)가 따라오지 않아(이전 A안 해제 때 인스턴스 쪽 스타일이 비워진 상태) 인스턴스 노드에 직접 type/label 지정(직접 지정 폴백 1개). 그 외 중첩 글자는 원본 컴포넌트 스타일이 따라옴(조회 시 스타일 없는 글자는 위 1개뿐이었고 이미 해소).
- 직접 지정(스타일 없음) 남은 노드: 147:442 1개뿐. 글자 색 바인딩·문구·이름·ID·패딩·간격 변경 없음, HUG 유지, FIXED 고정 없음.
- 높이 전 → 후(이번 수정분, 변화 있는 것만): skill-card compact 35:69 92 → 105, full verified=false 35:70 100 → 111, full verified=true 23:20 111 → 119(제목 35:71·설명 35:72 줄 높이 AUTO → 140%/150%). 세트 프레임 35:82는 크기 수정 안 함. 이전 단계에서 이미 반영된 list-row 23:26·35:83은 75, 변화 없음(배지 글자 줄 높이 변화는 배지 높이에 영향 없음).
- 높이 변화 없음(전 = 후): status-badge 7종(27/27/27/27/27/25/25), tab-bar 5종 64, text-input 2종 48, submit-button 2종 48, confirm-checkbox 2종 64, file-attach-row 60, visibility-selector seller 219 / non-seller 144, header 52, action-area 48, status-bar 47, footer nav 98 / action 82, home-indicator 34.
- status-badge 규격(rules.json status_badges) 영향: 없음. 배지 크기 전·후 동일(작성 중 76×27, 임시저장 84×27, 제출 완료 87×27, 검수 대기 87×27, 수정 요청 87×27, 승인됨 72×25, 반려 61×25). 배지 스타일·외곽선·글자색·아이콘 건드리지 않음. 단 list-row 인스턴스 안 배지 글자 I23:30;23:3만 type/label로 지정(12 SemiBold 그대로, 줄 높이 140%라 이론상 17로 커지나 배지 인스턴스 높이는 그대로 24 이상 확인 필요 시 S7 렌더 확인).
- S7 영향은 s7-screens.md 참고(조회만, S7 노드 수정 없음). 스크린샷·판정 스크립트 미실행, 노드 재조회 수치로 확인.

## 수정(사용자 요청, status-badge 높이 27 통일)
- 원인: 글자 줄 높이 17 + 상하 패딩 4+4 = 25. 외곽선 있는 variant(작성 중·임시저장·제출 완료·검수 대기·수정 요청)는 INSIDE 1px 외곽선이 auto layout 높이에 상하 1px씩 더해져 27. 승인됨·반려는 외곽선이 없어 25였음.
- 변경 노드·방법: 승인됨 23:13, 반려 23:16에 1px INSIDE 외곽선 추가, 색은 채움과 같은 변수에 바인딩(승인됨 color/ink VariableID:22:4, 반려 color/canvas-soft VariableID:22:6). 높이 HUG 유지(FIXED 아님), 패딩·간격·반경 9999·채움·글자 스타일(type/label)·아이콘 그대로. 외곽선이 채움과 같은 색이라 모양 변화 없음. 새 hex·새 간격 값 없음. 나머지 5개 variant는 수정하지 않음.
- 전→후 크기(너비×높이): 작성 중 23:2 76×27 → 76×27 / 임시저장 23:4 84×27 → 84×27 / 제출 완료 23:6 87×27 → 87×27 / 검수 대기 23:8 87×27 → 87×27 / 수정 요청 23:10 87×27 → 87×27 / 승인됨 23:13 72×25 → 74×27 / 반려 23:16 61×25 → 63×27. 전 variant 높이 27.
- 인스턴스 조회(전 페이지, 메인 컴포넌트 23:13·23:16): 0개. 화면(S7)·list-row에 승인됨·반려 인스턴스 없음. S7 노드는 수정하지 않음.

## 수정(사용자 요청, 약한 구분선 색 토큰 추가)
- 새 색 변수 `color/hairline-soft` VariableID:161:2 (tokens 컬렉션, COLOR, 값 #f0f0f0, scope는 color/hairline과 동일). docs/design.md Colors에 `{colors.hairline-soft}` #f0f0f0(Soft Hairline)이 이미 정의돼 있었으나 Figma tokens에는 없던 변수를 추가한 것이다. 이름은 design.md 이름과 일치. 새 hex 아님(rules.json palette 안 값, color/field 22:7과 값만 같고 별개 변수).
- 기존 변수 값 불변 확인: color/hairline 22:8 = #e0e0e0, color/field 22:7 = #f0f0f0 그대로. 기존 컴포넌트 수정 없음.
- 토큰 가이드 87:14 색 견본: 기존 형식(swatch 프레임 > chip 64×40 + 이름 + hex, 간격 16)을 hairline 견본 87:35 복제로 만들어 hairline 뒤에 삽입. `swatch/color/hairline-soft` 161:3 (chip 161:4 채움을 161:2에 바인딩, 이름 161:5 'color/hairline-soft', hex 161:6 '#f0f0f0'). 사용자 요청에 따라 기존 견본에 없던 용도 글자 161:7을 hex 뒤에 하나 추가: '1px 카드 외곽선, 가장 약한 선; 행 사이 약한 구분선에도 사용'(design.md 설명을 따름). 기존 견본에는 용도 줄이 없어 이 견본만 한 줄 더 길다(폭 642).
- 높이 전→후: color-swatches 87:18 456 → 508(+52 = 견본 40 + 간격 12), 가이드 87:14 2790 → 2842. 아래 요소 y(+52): accent 설명 87:55 689 → 741, Radius 제목 87:56 737 → 789, Spacing 제목 87:75 1129 → 1181, Typography 제목 87:112 1425 → 1477, Shadow 제목 103:382 2454 → 2506. 겹침 없음.
- 판정 스크립트는 돌리지 않음.

## 수정(사용자 요청, text-input·submit-button·action-area 높이 48→56)
docs/design.md text-input·button-primary 높이 56에 맞춤. 높이는 변수 없이 FIXED 값, 패딩·반경·채움·외곽선·글자·변수 바인딩·이름·ID 그대로, 새 변수 없음. 판정 스크립트는 돌리지 않음.
- text-input 세트 23:122: state=rest 23:118, state=focus 23:120 높이 48 → 56 (세로 FIXED, 패딩 12/16/12/16, 세로 가운데, 반경 radius/field 8, 포커스 링 1px INSIDE ink 유지). 세트 프레임 716×51 → 716×56
- submit-button 세트 23:117: variant=enabled 23:113, variant=disabled 23:115 높이 48 → 56. 세트 프레임 716×48 → 716×56
- action-area 세트 64:190: 세트 810×48 → 810×56, count=2 64:188·count=1 64:189 390×48 → 390×56. 버튼은 세로 FILL이라 따라옴: save-draft-button 64:178·register-button 64:176 175×48 → 175×56, submit-button[disabled] 64:181 358×48 → 358×56
- footer 세트 72:333: type=action 72:325 390×82 → 390×90 (안 action-area 인스턴스 72:326 56 y0 + home-indicator 72:331 34 y56). type=nav 72:296 390×98 그대로, 세트 프레임 810×98 그대로
- S6 footer 규칙 갱신: S7 인스턴스 기준 footer type=action은 y762 → y754 (높이 90). 위 '메모'의 y762·action-area 높이 48 표기는 이전 값

## 수정(사용자 요청, accent 적용 tab-bar 활성 아이콘·chip 컴포넌트)
docs/design.md Brand & Accent·Chips 갱신 기준. rules.json 수정 없음(accent max_per_frame 2, CTA 금지). 새 페이지·새 변수·새 hex 없음. 스크린샷은 열 수 없어 노드 재조회 수치로만 확인. 판정 스크립트는 돌리지 않음. 위 '메모'의 '칩은 컴포넌트 아님'·'accent 미사용' 표기는 이전 값.
- tab-bar 세트 23:53, variant 5개의 활성 탭 채워진 아이콘 벡터 `shape` 1개씩에만 color/accent(VariableID:22:12) 바인딩. 대상: 홈 23:32 = 44:5, 스킬 23:39 = 44:40, 내 자산 23:46 = 44:75, 자료 35:3 = 44:85, 내 학습 35:10 = 44:120. 변경 전: 채움·선 color/ink(22:4) 바인딩(자료 variant는 흰 선/채움 값이 있던 것을 같은 노드에서 accent로 바꿈). 변경 후: 같은 벡터의 채움·선 모두 accent 바인딩(노드 1개). 라벨·다른 탭·비활성 아이콘·icon-holder 그대로. variant당 accent 노드 1개.
- chip 세트 `chip` 175:382 (COMPONENT_SET, S6 페이지 x0 y2030, 180×44, 다른 세트와 같이 최상위 배치). variant `selected=false` 175:378, `selected=true` 175:380(x106). 공통: 가로 auto layout(가로 HUG·세로 FIXED 44, 가운데 정렬), 패딩 좌우 spacing/16(22:25)·상하 spacing/0(22:21), 간격 0, 네 모서리 radius/tab(22:17, 9999), 선·그림자·그라디언트 없음. 텍스트 `label` 175:379(false)·175:381(true): Pretendard SemiBold 13, 스타일 type/label-md(S:8889feaeffe6a49afb3d4e0abfd0b1849d825fb7,), 기본 문구 '전체 24', 인스턴스에서 덮어쓰기 가능. selected=false: 채움 color/canvas-soft(22:6), 글자 color/ink(22:4). selected=true: 채움 color/accent(22:12), 글자 color/canvas(22:5, on-primary). 크기 각 74×44(기본 문구 기준). accent 노드 수: selected=true 1(루트 채움).

## 수정(사용자 요청, tab/홈[selected] 라벨 accent)
새 페이지·새 변수·새 hex 없음. 판정 스크립트는 돌리지 않음.
- tab-bar 23:53 variant 홈(23:32) > tab/홈 44:2 > 라벨 '홈' 44:6: 글자색 color/ink(VariableID:22:4) → color/accent(VariableID:22:12) 바인딩. 크기·굵기(SemiBold 12)·텍스트 스타일·위치 그대로. 아이콘 44:5 accent 그대로.
- 다른 variant(스킬 23:39, 내 자산 23:46, 자료 35:3, 내 학습 35:10) 라벨은 변경 없음.
- accent 노드 수(홈 variant) = 아이콘 44:5 + 라벨 44:6 = 2. 다른 variant는 아이콘 1.

## 수정(사용자 요청, checkbox-box checked accent)
새 페이지·새 변수·새 hex 없음. 판정 스크립트는 돌리지 않음.
- confirm-checkbox 세트 23:112, variant checked=true 23:108 안 checkbox-box 23:109(24×24 원형): 채움 color/ink(VariableID:22:4, #141414) → color/accent(VariableID:22:12, #0066ff) 바인딩. 선 없음 그대로. 안 icon/check는 color/canvas(22:5) 흰색 그대로. 라벨·패딩·간격·반경 그대로.
- checked=false 23:105 (box 23:106, canvas 22:5 채움 + hairline 22:8 1px)는 변경 없음.
- accent 노드 수: confirm-checkbox checked=true variant 1(box 채움).
- visibility-selector는 이번에 건드리지 않음(상한 때문에 사용자 결정 대기).

## 수정(사용자 요청, visibility-selector 선택 행 accent A안)
새 페이지·새 변수·새 hex 없음. 판정 스크립트는 돌리지 않음. 사용자 결정 A안: 선택 행 외곽선 + 라디오 점만 accent, 라디오 링은 ink 유지.
- visibility-selector 세트 23:98의 선택 행(selected) 5개: 외곽선 color/ink(VariableID:22:4) → color/accent(VariableID:22:12) 바인딩(1px INSIDE 그대로), 안 radio-dot 채움 color/ink(22:4) → color/accent(22:12) 바인딩.
  - 23:54 → 행 23:55, 점 95:95 / 23:64 → 행 23:68, 점 95:100 / 23:74 → 행 23:81, 점 95:105 / 23:84 → 행 23:85, 점 95:107 / 23:91 → 행 23:95, 점 95:111
- 그대로: 라디오 링(radio 96:4 등, canvas 채움 + ink 1px), 선택 행 canvas 채움, 비선택 행(canvas-soft + hairline 링), label ink·description ink-soft, 반경·패딩·간격.
- accent 노드 수: variant 5개 모두 2(선택 행 외곽선 + 라디오 점). selected가 둘 이상인 variant 없음.

## 수정(사용자 요청, radio 선택 상태 6px 링)
새 페이지·새 변수·새 hex 없음. 판정 스크립트는 돌리지 않음. 스크린샷은 열람 못 해 노드 재조회 수치로만 확인.
- 선택 행 radio(20×20 ELLIPSE) 5개: 선 1px ink(VariableID:22:4) → 6px INSIDE color/accent(VariableID:22:12) 바인딩. 채움은 canvas(22:5) 그대로(가운데 흰 영역 8px). 23:54 → radio 96:4 / 23:64 → 96:8 / 23:74 → 96:12 / 23:84 → 96:13 / 23:91 → 96:16.
- 삭제한 노드: radio-dot 95:95, 95:100, 95:105, 95:107, 95:111 (5개). 가운데가 흰색이어야 해서 삭제, radio-wrap은 자식 1개(radio)로 남음, 구조 위험 없음.
- 그대로: 선택 행 외곽선(accent 1px), radio-wrap 20×20 위치·간격·패딩, option-text, 글자색, 반경, 비선택 행 라디오(canvas 채움 + hairline 1px).
- 높이 변화 없음: 선택 행 69, 비선택 67, visibility-selector seller 219 / non-seller 144.
- accent 노드 수: variant 5개 모두 2(선택 행 외곽선 1 + 라디오 링 1).

## 수정(사용자 요청, tab-bar 선택 라벨 전체 accent)
새 페이지·새 변수·새 hex 없음. 판정 스크립트는 돌리지 않음.
- tab-bar 23:53 나머지 variant 선택 탭 라벨 글자색 color/ink(VariableID:22:4) → color/accent(VariableID:22:12) 바인딩: 스킬 23:39 > tab/스킬[selected] 44:37 > 라벨 44:41 / 자료 35:3 > tab/자료[selected] 44:82 > 44:86 / 내 학습 35:10 > tab/내 학습[selected] 44:117 > 44:121 / 내 자산 23:46 > tab/내 자산[selected] 44:72 > 44:76. 홈 44:6은 이전 요청에서 완료.
- 그대로: 크기·굵기(SemiBold 12)·텍스트 스타일·위치, 비선택 탭 라벨(#262626 Regular 12), 아이콘 accent.
- accent 노드 수: variant 5개 모두 2(선택 아이콘 1 + 선택 라벨 1). 조회로 확인.
- S7 프레임별 accent 노드 수는 s7-screens.md 참고: skills 36:102 = 3(탭 아이콘 + 탭 라벨 + chip 175:574)으로 상한 2 초과, 되돌리지 않고 별도 결정 대기.

## 수정(사용자 요청, register-button·submit-button 독립 컴포넌트화)
색·모양·크기 변경 없음(accent 적용 안 함). 새 페이지·새 변수·새 hex 없음, 기존 변수 바인딩만. 판정 스크립트는 돌리지 않음. 스크린샷은 열지 않았고 노드 재조회 수치로 확인.
- 새 컴포넌트: `register-button` COMPONENT_SET 181:65 (S6 페이지 x0 y2138, 375×56). variant=enabled 181:62 (64:176 복제를 COMPONENT로 변환: 175×56, 가로 auto layout 가운데 정렬, 패딩 0, 채움 color/ink 22:4, 반경 radius/button-rect 120:408, 글자 '등록' Pretendard SemiBold 15 type/link, 색 color/canvas 22:5), variant=disabled 181:63 (enabled 복제에 submit-button disabled와 같은 규칙 적용: 흰 채움 22:5 + hairline 22:8 1px INSIDE 점선 [4,4], 글자 color/text-muted 22:10 #707070). 가로 FILL/세로 FIXED 56 쓰임은 인스턴스에서 layoutSizingHorizontal=FILL로 지정 가능(컴포넌트 자체는 가로 FIXED 175·세로 FIXED 56).
- submit-button 세트 23:117 variant=disabled 23:115를 action-area 64:181과 같은 모양으로 변경. 전: 채움 color/hairline 22:8(#e0e0e0, 점선 없음), 글자 color/ink-soft 22:9(#262626). 후: 채움 color/canvas 22:5(#ffffff), 외곽선 color/hairline 22:8 1px INSIDE 점선 [4,4], 글자 color/text-muted 22:10(#707070). 다른 속성(342×56, 패딩 0/16, 반경 8, 라벨 '제출하기', 글자 스타일)은 그대로. variant=enabled 23:113은 수정 없음. 23:113·23:115 인스턴스는 파일 전체 0개(조회)라 S7 화면 모양 변화 없음. 세트 23:117은 가로 FILL로 쓸 수 있고(인스턴스에서 FILL 지정) 크기 716×56 그대로.
- action-area 세트 64:190 변경 전 → 후 (이름·위치·크기 그대로, 높이 56·간격 8·패딩 16):
  - count=2 64:188: register-button 프레임 64:176(FRAME) → register-button 인스턴스 181:66(main 181:62, 199/175×56, 텍스트 '등록'). save-draft-button 64:178은 그대로(프레임, 175×56, x16). 폭 175/175를 맞추려고 인스턴스는 가로 FIXED 175로 두었고(save-draft가 FILL로 175), 인스턴스를 FILL로 하면 Figma가 둘을 176/174로 나눠(조회 확인) 175×56이 깨져 FIXED로 보류(보고)
  - count=1 64:189: submit-button[disabled] 프레임 64:181(358×56) → submit-button 인스턴스 181:68(main 23:115, 이름 `submit-button[disabled]`, 가로 FILL, x16 358×56, 텍스트 '판매 신청 제출'을 인스턴스에서 덮어쓰기). 안 글자는 23:116 기반
  - 폐기된 ID: 64:176, 64:177, 64:181, 64:182
- 모양 변화 없음 확인값(조회): register-button 인스턴스 채움 #141414(22:4), 글자 #ffffff, 반경 8, 175×56. submit-button[disabled] 인스턴스 채움 #ffffff, 외곽선 #e0e0e0 1px 점선 [4,4], 글자 #707070(22:10), 반경 8, 358×56. S7 footer 인스턴스 안에서 동일.
- 보고: (1) 위 register-button 가로 FIXED 175 결정, (2) register-button disabled variant는 현재 어느 화면에서도 쓰지 않음, (3) 이전 메모의 'submit-button(23:117)은 폭 342·disabled 채움이 달라 인스턴스로 쓰지 않음' 이유는 해소(disabled 채움 통일, 폭은 FILL)

## 수정(사용자 요청, option 선택 행 외곽선 2px)
새 페이지·새 변수·새 색 없음. 판정 스크립트·스크린샷 미실행, 노드 재조회 수치로 확인.
- visibility-selector 세트 23:98의 선택 행(selected) 5개 외곽선 두께 1px → 2px (색 color/accent VariableID:22:12 바인딩 그대로, INSIDE 유지, strokesIncludedInLayout true): 23:54 → 23:55 option/private[selected], 23:64 → 23:68 option/member-only[selected], 23:74 → 23:81 option/sale-request[selected], 23:84 → 23:85 option/private[selected], 23:91 → 23:95 option/member-only[selected].
- 선택 행 높이 69 → 71 (선이 레이아웃에 포함돼 +2). variant 높이: seller(23:54, 23:64, 23:74) 219 → 221, non-seller(23:84, 23:91) 144 → 146. 비선택 행 67 그대로.
- 그대로: 라디오 링(6px accent 안쪽, 20×20), 비선택 행(canvas-soft, 외곽선 없음), 글자색, 반경, 패딩 12/16/12/16, 간격. 레이아웃 값 변경 없음.
- accent 노드 수: variant 5개 모두 2(선택 행 외곽선 1 + 라디오 링 1) 그대로.

## 수정(사용자 요청, register-button·submit-button enabled accent)
새 페이지·새 변수·새 색 없음. 판정 스크립트·스크린샷 미실행.
- register-button 세트 181:65 variant=enabled 181:62: 채움 color/ink(VariableID:22:4) → color/accent(VariableID:22:12) 바인딩 (#141414 → #0066ff).
- submit-button 세트 23:117 variant=enabled 23:113: 같은 방식으로 채움 22:4 → 22:12.
- 글자('등록', label)는 canvas 흰색(VariableID:22:5) 그대로(대비 약 4.8:1). 높이 56, 반경 radius/button-rect 8(120:408), 패딩, 글자 스타일 그대로.
- 건드리지 않음: variant=disabled 181:63, 23:115, save-draft-button 64:178.
- accent 노드 수: 각 enabled variant 1(채움) 추가.

## 수정(사용자 요청, save-draft-button 컴포넌트화)
모양·색·크기 변경 없음(accent 적용 안 함). 새 페이지·새 변수·새 색 없음, 기존 변수 바인딩 그대로. 판정 스크립트·스크린샷 미실행, 노드 재조회 수치로 확인.
- 새 컴포넌트: `save-draft-button` COMPONENT_SET 186:41 (S6 페이지 22:2 최상위, x0 y2258, 175×56. 기존 register-button 181:65 아래 같은 열). variant=enabled 186:40 (64:178 복제를 COMPONENT로 변환: 175×56, 가로 auto layout 가운데 정렬, 패딩 0, 채움 color/canvas 22:5, 외곽선 color/hairline 22:8 1px INSIDE, 반경 radius/button-rect 120:408 = 8, 글자 '임시저장' Pretendard SemiBold 15 type/link 스타일, 색 color/ink 22:4). 컴포넌트 자체는 가로·세로 FIXED 175×56, 인스턴스에서 FILL 지정(register-button과 같은 방식). disabled variant는 만들지 않음: 임시저장은 항상 활성이라 쓰이는 곳 없음.
- action-area 세트 64:190 count=2 64:188 변경 전 → 후: save-draft-button 프레임 64:178(FRAME, FILL, 텍스트 64:179) → save-draft-button 인스턴스 186:42(main 186:40, 가로 FILL·세로 FILL, x16, 175×56, 텍스트 '임시저장'). 순서(좌)·간격 8·패딩 16 그대로. register-button 인스턴스 181:66은 FIXED 175 x199 유지.
- 모양 변화 없음 확인값(조회): 186:42 채움 #ffffff(22:5), 외곽선 #e0e0e0 1px(22:8), 반경 8, 175×56, 글자 '임시저장' #141414 SemiBold 15 type/link. 전과 동일. S7 footer 인스턴스 안에서도 동일(s7-screens.md 참고).
- 폐기된 ID: 64:178, 64:179
- 수정(사용자 요청, 배경 연한색 canvas-faint #fafafa 추가): tokens 컬렉션에 COLOR 변수 `color/canvas-faint` ID VariableID:190:2 신규(값 #fafafa, scope ALL_SCOPES = canvas-soft 22:6과 동일, 설명 '연한 배경색. 기존 canvas-soft(#f3f3f3)와 별도. 텍스트·선·accent 용도 금지'). 기존 canvas-soft 22:6(#f3f3f3)은 값·scope 그대로.
  - 토큰 가이드 87:14 Color 섹션 color-swatches 87:18에 견본 `swatch/color/canvas-faint` 190:3 추가(87:27 canvas-soft 견본 복제, canvas-soft 바로 뒤). chip 190:4 채움 190:2 바인딩(외곽선 hairline 22:8 그대로), 이름 190:5 'color/canvas-faint', 값 190:6 '#fafafa'. 기존 견본·내용 변경 없음.
  - 적용처 없음: 새 변수를 바인딩한 노드는 전 페이지 조회 결과 가이드 견본 chip 190:4 단 1개. 어떤 화면·컴포넌트·노드에도 적용하지 않음. 기존 변수 canvas-soft 22:6 사용 노드 40개 그대로(추가 후 조회, 값 #f3f3f3 불변), COLOR 변수 11 → 12개. 새 페이지 없음, 판정 스크립트 미실행.
- 수정(사용자 요청, list-row summary 연한 블루 accent-soft): tokens 컬렉션(VariableCollectionId:22:3)에 COLOR 변수 `color/accent-soft` ID VariableID:194:7 신규(값 #e6f0ff, scope ALL_SCOPES = canvas-faint 190:2와 동일, 설명 '연한 파랑 채움. list-row summary 전용. 텍스트·선·accent 용도 금지'). COLOR 변수 12 → 13개.
  - 환산 근거: S4 시안 screen/home#B 185:696 안 list-row 185:745는 #0066ff 채움 불투명도 10%. 흰(#ffffff) 위 합성 = 255 - 0.1×(255-c): R 255-25.5=229.5, G 255-0.1×153=239.7, B 255 → #e6f0ff (230,240,255). 투명 파랑은 accent 개수로 세어지므로 불투명 #e6f0ff 변수로 대체.
  - 토큰 가이드 87:14 Color 섹션 87:18에 견본 `swatch/color/accent-soft` 194:8 추가(canvas-faint 견본 190:3 복제, 바로 뒤). chip 194:9 채움 194:7 바인딩, 이름 194:10 'color/accent-soft', 값 194:11 '#e6f0ff'.
  - list-row kind=summary 35:83 채움: color/canvas-soft 22:6(#f3f3f3) → color/accent-soft 194:7(#e6f0ff). 글자·화살표 색(ink 22:4)·구조·반경 16·크기 358×75·icon/folder 127:7 그대로. kind=progress 23:26은 canvas 22:5 그대로 미수정.
  - 새 변수를 쓰는 노드(전 페이지 조회): 가이드 chip 194:9 / 컴포넌트 variant 35:83 / S7 인스턴스 36:86 / S4 인스턴스 185:889·153:185·153:271(아래 주의 참고). 기존 변수 canvas-soft 22:6(#f3f3f3)·canvas-faint 190:2(#fafafa) 값 변경 없음.
  - 주의: S4 페이지의 list-row summary 인스턴스 185:889, 153:185, 153:271은 S4 노드를 직접 수정하지 않았으나 컴포넌트를 따라 연한 파랑이 됨(시안 185:745의 의도와 같은 방향). 판정 스크립트 미실행.

- 수정(사용자 요청, progress-row 컴포넌트화): 새 컴포넌트 `progress-row` COMPONENT 197:52 (S6 페이지 22:2 최상위, x0 y2378, save-draft-button 186:41 아래 간격 64). 홈 진행 행 189:741을 복제해 COMPONENT로 변환. 356×90, 가로 auto layout(gap 16·패딩 16, 변수 spacing 22:25 바인딩 그대로), 세로 가운데, 채움 없음, clip. 새 변수·새 색·새 페이지 없음. 인스턴스에서 가로 FILL 지정(컴포넌트 자체는 356 FIXED, 세로 HUG 90).
  - 구조: thumb 197:46(56×56, 홈 현재 크기 56 그대로, 요청서의 54 아님. 반경 16 = 홈 현재 값(조회 시 12가 아니라 16), 채움 color/hairline 22:8 #e0e0e0 바인딩 자리표시자, 자식 없음. 이미지 채움으로 교체하기 쉬운 단일 프레임) + progress-info 197:47(세로 gap 8) = title 197:48(type/link, color/ink 22:4, 홈 텍스트 스타일 그대로) + meta-row 197:49(가로 gap 12) = updated 197:50(type/body-sm, color/text-muted 22:10) + status-badge 인스턴스 197:55(main 23:2 status=작성 중, 12×12 아이콘 icon/edit 포함 76×27).
  - 인스턴스 스왑: status-badge 인스턴스를 23:6(제출 완료)·23:8(검수 대기) 등 다른 variant로 swapComponent 가능. 홈 인스턴스에서 확인(아래 S7 참고).
  - 기본 문구는 복제 원본 그대로('업무 자동화 프롬프트 만들기' / '9월 28일 수정'). 판정 스크립트·스크린샷 미실행.

## 수정(사용자 요청, 토큰 가이드 accent 견본 추가)
새 변수·새 hex 없음, 기존 color/accent(VariableID:22:12, #0066ff) 바인딩만. 가이드는 87:14 하나로 유지. 판정 스크립트·스크린샷 미실행, 노드 재조회 수치로 확인.
- 새 견본 `swatch/color/accent` 201:2 (accent-soft 견본 194:8 복제, color-swatches 87:18 안 canvas-faint 190:3 다음·accent-soft 바로 앞, y208, 642×40). chip 201:3 채움 color/accent 22:12 바인딩(재조회로 확인), 이름 201:4 'color/accent', hex 201:5 '#0066ff', 용도 201:6 `use/color/accent`(hairline-soft 용도 161:7 복제, 폭 354 줄바꿈, 2줄) '상업 신호 전용, CTA 금지. 앱 예외: tab-bar 활성 아이콘·라벨, 선택된 chip, 선택 라디오, 체크박스, 등록 버튼'. 적용처는 위 accent 수정 기록(tab-bar 아이콘·라벨, chip, 선택 행 라디오, confirm-checkbox, register/submit enabled)과 design.md Brand & Accent 기준.
- 주석 87:55: '가이드에서는 견본을 만들지 않음' 삭제 → 'color/accent #0066ff: 상업 신호 전용, CTA 금지. 프레임당 최대 2개. 가이드 견본은 개수에서 제외' (한 줄, 높이 16 유지).
- 높이 전→후: color-swatches 87:18 612 → 664, 가이드 87:14 2946 → 2998 (+52, auto layout 자동 정렬).
- 이동한 노드 y(+52): accent-soft 194:8 208→260, field 87:31 260→312, hairline 87:35 312→364, hairline-soft 161:3 364→416, ink-soft 87:39 416→468, text-muted 87:43 468→520, text-faint 87:47 520→572, badge-overlay 87:51 572→624(87:18 안). 가이드 직속: 87:55 845→897, Radius 제목 87:56 893→945, radius-swatches 87:57 949→1001, 87:74 1237→1289, Spacing 제목 87:75 1285→1337, 87:76 1341→1393, Typography 제목 87:112 1581→1633, type-scale 87:113 1637→1689, Shadow 제목 103:382 2610→2662, 103:383 2666→2718, shadow-swatch 103:384 2714→2766, shadow-spec 103:387 2866→2918. 겹침 없음.
- 메모: 가이드 견본은 S7 화면이 아니므로 accent 개수 상한(프레임당 2)에 포함되지 않는다. 기존 견본·내용은 변경 없음(위치 이동만).

## 수정(사용자 요청, 토큰 가이드 표 구조)
새 변수·새 hex·새 스타일 없음. 견본은 모두 기존 tokens 변수·텍스트 스타일·효과 스타일 바인딩. 판정 스크립트 미실행, 조회로 확인. 이후 이 가이드의 노드 ID는 아래 새 값을 기준으로 삼는다.
- 확인한 실제 구조(조회): 변수 컬렉션 `tokens` 1개(Mode 1, 변수 31). 그룹 color(COLOR 13), radius(FLOAT 9: button, badge, toggle, tab, input, field, button-rect, card, none), spacing(FLOAT 9: 0·4·8·12·16·24·32·48·64). Styles: 텍스트 스타일 `type/*` 13개(폴더 type, 평면), 효과 스타일 `shadow/nav` 1개(폴더 shadow). 페인트·그리드 스타일 0.
- 가이드 87:14 (폭 720 유지, 세로 auto layout HUG). 제목 87:15, 안내문 87:16 유지. 직속 자식 2개 덩어리: `block/variables` 208:438 (제목 'Variables · 컬렉션 tokens', 부제 'Mode 1 · 변수 31'), `block/styles` 208:442 (제목 'Styles').
- 표(그룹 헤더 행 canvas-soft + 컬럼 헤더 행 canvas-faint + 변수/스타일 행, 행 사이 hairline-soft 1px 바인딩, 행은 auto layout 가로·셀 폭 FIXED, 첫 열 한 단계 들여쓰기 24):
  - color 그룹 208:15 / 표 208:16, 열 폭 96·160·160·240, 행 13 (표시 'color · COLOR 13'). 주석 87:55 표 아래 유지.
  - radius 그룹 208:131 / 표 208:132, 열 폭 96·160·120·280, 행 9 ('radius · FLOAT 9'). 주석 87:74 유지. 사용자가 변수 구조 그대로 따르라고 해 badge·toggle·tab을 포함(처음 기대 6행 → 9행).
  - spacing 그룹 208:218 / 표 208:219, 열 폭 160·248·248(용도 열 없음), 행 9 ('spacing · FLOAT 9'). spacing/0 예시는 막대 없이 빈칸(폭 0).
  - Text styles 그룹 208:297 / 표 208:298, 열 폭 276·120·148·112, 행 13 ('Text styles · type/* 13'). 예시 '허들링 스킬 라이브러리 Aa'에 type/* 적용, display만 예시 셀에서 2줄 줄바꿈(원본 폭 340 > 셀 폭).
  - Effect styles 그룹 208:416 / 표 208:417, 열 폭 168·120·200·168, 행 1 ('Effect styles · shadow/* 1'). 예시 흰 박스(radius/tab 바인딩)에 shadow/nav 적용, 예시 셀 배경 canvas-soft. 주석 103:387을 '불투명도는 변수로 바인딩할 수 없어 값으로 고정 (바인딩 시 100%가 됨)'으로 줄여 유지(값은 표로 이동).
- 이름 열은 전체 경로(color/ink 등), 텍스트는 type/label-md·body-sm·caption·heading-3, 색은 변수 바인딩(텍스트 대비: canvas-soft 위는 ink만 사용).
- 옮긴 항목: color 13(ink, canvas, canvas-soft, canvas-faint, accent, accent-soft, field, hairline, hairline-soft, ink-soft, text-muted, text-faint, badge-overlay), radius 9, spacing 9, type 13, shadow/nav 1. 용도는 accent·hairline-soft·radius/button·radius/button-rect·type/*·shadow/nav에 기존 글 이어서, 나머지 빈칸.
- 삭제한 옛 노드: 제목 87:17, 87:56, 87:75, 87:112, 103:382 / color-swatches 87:18, radius-swatches 87:57, spacing-steps 87:76, type-scale 87:113 / 103:383, shadow-swatch 103:384(안의 shadow-sample 103:385). 옛 용도 글은 새 표로 이동.
- 높이: 가이드 87:14 2998 → 3742. 조회: 텍스트 159개 폰트 Pretendard, 텍스트·사각형 채움 모두 변수 바인딩, 이름 열 줄바꿈 없음, 겹침·잘림 없음. 스크린샷으로 color 표 확인.

## 수정(사용자 요청, 토큰 가이드 2프레임 분리)
페이지 87:3 (토큰 가이드), 가로 나열, y 0 같음, 간격 80.
- 왼쪽 87:14 `token-guide/variables`: x0 y0, 720x2357 (세로 HUG). 제목 87:15, 안내문 87:16, block/variables 208:438만 둠.
- 오른쪽 210:2 `token-guide/styles` (새 프레임): x800 y0, 720x1440 (세로 HUG, 폭 고정 720). 패딩 32 4면, 간격 32, 채움 변수 VariableID:22:5(canvas) 바인딩, 반경 0, 테두리 없음, 클립 켬 (87:14와 동일). 안에 제목 210:3 `Styles`(87:15 복제 후 텍스트만 변경, Pretendard Bold 28, 채움 VariableID:22:4 바인딩 유지)와 block/styles 208:442.
- 이동한 노드: block/styles 208:442 (이동, 복제 아님). ID 변화 없음(208:442 그대로, 안의 표 노드도 동일). 폭은 FILL로 바뀌었고 값은 656 그대로.
- 확인: ① 위 이름·x·y·폭·높이, 페이지 최상위 노드는 이 두 프레임뿐이라 겹침 없음(왼쪽 0~720, 오른쪽 800~1520). ② 표 행 수는 이동 전후 같음. variables 안 color 표 15·radius 표 11·spacing 표 11 자식(헤더·주석 행 포함, 데이터 행 color 13·radius 9·spacing 9), styles 안 text-styles 표 15(데이터 Text styles 13), effect-styles 표 3(데이터 Effect styles 1 + 헤더·설명 행). ③ Figma 변수 31개 전부 variables 프레임 텍스트에 있고, 텍스트 스타일 13 + 효과 스타일 1 = 14개 전부 styles 프레임 텍스트에 있음(누락 0). ④ 자식 범위가 프레임 안에 들어가 잘림 없음. 오른쪽 프레임 스크린샷 확인.
- 높이: 87:14 3742(조회 시점 실제 3700) → 2357, 새 프레임 1440. 왼쪽 2357 = 32 + 33 + 32 + 16 + 32 + 2180 + 32 높이 일치.

## 수정(사용자 요청, 가이드 알약 전용 문구 삭제)
- 대상: 토큰 가이드 87:3 (87:14 token-guide/variables, 210:2 token-guide/styles). '알약 전용' 포함 TEXT 2개.
- 208:151 (row/radius/button 용도 셀): `알약 전용(배지·탭·토글·막대)` → `배지·탭·토글·막대`
- 87:74 (radius 표 아래 주석): `radius/badge, toggle, tab, 막대 = radius/button 9999 (알약 전용). 버튼은 radius/button-rect 8` → `radius/badge, toggle, tab, 막대 = radius/button 9999. 버튼은 radius/button-rect 8`
- 확인: 두 프레임 '알약 전용' 검색 0건. 스타일·색·위치·열 폭 불변. 행 row/radius/button(HORIZONTAL auto layout, 높이 65, 셀 64)과 group/radius(VERTICAL, 표 0+663, 주석 675+16) 겹침·잘림 없음. 변수·스타일·hex 변경 없음, 바인딩 유지.
- 변수 description에 '알약 전용' 남은 곳: 없음(0건).

## 수정(사용자 요청, 텍스트 스타일 예시 문구 변경)
- 대상: 토큰 가이드 token-guide/styles 210:2 > Text styles 그룹 208:297 > 표 208:298 예시 열 TEXT 13개. 변경 전 글은 모두 `허들링 스킬 라이브러리 Aa`, 변경 후 글은 모두 `텍스트 스타일 Text styles`.
- 변경 노드 ID(스타일): 208:284 type/display, 208:285 type/heading-1, 208:286 type/heading-2, 208:287 type/heading-3, 208:288 type/heading-4, 208:289 type/title, 208:290 type/body-lg, 208:291 type/body, 208:292 type/body-sm, 208:293 type/link, 208:294 type/label-md, 208:295 type/label, 208:296 type/caption
- 확인: 13개 모두 해당 type/* 텍스트 스타일 유지(풀림 없음, 재적용 불필요), 폰트·크기·행간·색 변수 바인딩 변경 없음. 글 변경 전 현재 폰트를 먼저 로드. 새 변수·스타일·hex 없음.
- 줄바꿈·높이: 13개 노드 모두 변경 전후 텍스트 높이와 행(cell/example) 높이 동일. 열 폭 불변(텍스트 244, 셀 276). 신규 줄바꿈 0건. 변경 전부터 2줄이던 행은 208:284(display, 높이 84), 208:285(heading-1, 72), 208:286(heading-2, 64)이며 전후 동일, 나머지 10행은 1줄. 겹침·잘림·가로 넘침 없음.
- 변경 후 `허들링 스킬 라이브러리 Aa`는 전 페이지 0건(토큰 가이드 페이지에 새 문구 13건). 다른 표·글자 미수정.
