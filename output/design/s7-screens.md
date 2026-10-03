# S7 화면 디자인

Figma 파일: https://www.figma.com/design/CNelXB5JxSwpeJNurQRm3L/Design-harness
페이지: S7 Screens (26:113)

확정 S4 키스크린(82:75, 82:164, 19:3)을 S6 컴포넌트 인스턴스로 교체한 완성본. 프레임 6개, 모두 390×844. 확정 S4와 맞지 않는 이전 프레임은 없어 삭제 없음(이전 실행의 sale-request 구조는 V2 필수 프레임으로 유지).

- frame: 36:49 | screen/home
- frame: 36:102 | screen/skills
- frame: 26:114 | screen/my-assets/register@seller
- frame: 26:161 | screen/my-assets/register@non-seller
- frame: 26:203 | screen/my-assets/sale-request@unchecked
- frame: 26:274 | screen/my-assets/sale-request@checked

## 수정 기록(사용자 요청, 홈 section/progress 텍스트 스타일)
36:53 안 list-row 인스턴스 36:56·36:62·36:68 글자에 type/link(제목)·type/body-sm(수정일) 적용, 제목 36:54는 이미 type/heading-4. section/progress 290 → 317, 아래 36:74 y405 → 432, 36:86 y557 → 584. 36:86 하단이 홈 content-area(647 FIXED)를 넘어 footer(y746)와 3 겹침, 미해결(보고). 상세는 s6-tokens-components.md 마지막 섹션.

## 수정 기록(사용자 요청, 홈 내 자산 요약 list-row 36:86 텍스트 스타일만)
간격·패딩·높이 고정·노드 이동/제거·컴포넌트·색 바인딩·문구·이름·ID는 건드리지 않음. 스크린샷 미확인, 노드 재조회 수치로만 확인. 판정 스크립트 안 돌림.
- 조회: 원본 list-row 23:28·35:85는 15 SemiBold = type/link, 23:29·35:86은 13 Regular = type/body-sm. 36:86 안 글자 두 개는 15 SemiBold / 13 Regular(18/16 크기 없음)라 같은 스타일이 맞음. 맞지 않아 적용 못 한 글자 없음.
- 변경 노드 및 적용 스타일: I36:86;35:85(title) → type/link, I36:86;35:86(개수 요약) → type/body-sm. 화살표 I36:86;35:89는 이미 type/title이라 그대로.
- 글자 높이: 35:85 18 → 23, 35:86 16 → 20 (줄 높이 AUTO → 150%). row-info 34 → 43, 화살표 y25.5 h24 그대로.
- 36:86 높이 66 → 75 (HUG 유지). y는 584 그대로(전 584 → 후 584). 높이 전 66 → 후 75.
- 최종 위치(수정 안 함, 기록만): 36:86은 content-area 66:263(y99, 높이 647 FIXED, 하단 패딩 32, clip 켬) 안 y584~659. 화면 좌표 y683 → 758. content-area 높이 647을 12 넘음(659 - 647), 패딩 기준선 615(647-32)보다 44 아래. footer 73:543(y746)에 대해 758 - 746 = 12 겹침. clip 때문에 36:86 아래 12 정도가 잘릴 수 있음. 직전 상태(높이 66, 하단 650, 화면 749)는 3 겹침이었으며 이번 변경으로 +9 늘어남. 사용자 결정 필요(높이·간격 조정, 36:86 이동·제거 등).
- 홈 다른 노드: 36:74 y432 h128(끝 560, 간격 24 → 36:86 y584) 변경 없음, 36:68 y174 h75.

### 오버라이드 해제 노드 목록 (방향 수정: 인스턴스 글자 오버라이드 해제 시도)
결과: 해제 불가, 직접 지정으로 폴백(위 적용 그대로 유지, 추가 변경 없음).
- 조회(instance.overrides): 36:56 → I36:56;23:28·I36:56;23:29, 36:62 → I36:62;23:28·23:29(characters 포함), 36:68 → I36:68;23:28·23:29(characters 포함), 36:86 → I36:86;35:85·35:86. 모두 textStyleId·fontName·fontSize·lineHeight·letterSpacing 오버라이드로 표시됨. 값은 원본 23:28·35:85(type/link, 15 SemiBold, 150%)와 23:29·35:86(type/body-sm, 13 Regular, 150%)과 같음.
- 해제 불가 이유: Plugin API에 인스턴스 안 글자 노드 단위 오버라이드 해제가 없음(TEXT 노드에 resetOverrides 없음). 인스턴스 단위 resetOverrides는 같은 인스턴스의 문구(36:62·36:68의 characters '제출 완료' 등 덮어쓴 값), 너비·높이 덮어쓰기, 중첩 배지 오버라이드까지 함께 되돌려 문구·크기 금지 조건을 어기므로 쓰지 않음. 원본 스타일 값과 같은 값으로 이미 지정돼 있어 화면 결과는 원본 스타일을 따라온 것과 동일(원본 스타일이 바뀌면 이 글자는 따라가지 않음).
- 해제한 노드: 없음. 직접 지정 유지 노드: I36:56;23:28·23:29, I36:62;23:28·23:29, I36:68;23:28·23:29, I36:86;35:85·35:86.

## 구조 (모든 프레임 공통)
status-bar(y0, 47) → header(y47, 52, 인스턴스, 타이틀만 덮어씀) → content-area(y99, 세로 auto layout, 패딩 상16·좌우16·하32, 간격 24) → footer 인스턴스(nav y746 / action y762). 직접 자식 4종, 겹침 없음.

## 노드 ID
- 26:114 register@seller: status-bar 66:144, header 66:160, content-area 66:143(끝 요소 y722), footer 73:509(action count=2). visibility-selector 26:234 안 option/private[selected], option/member-only, option/sale-request. 제목 text-input[focus] 26:224
- 26:161 register@non-seller: 66:175, 66:191, 66:174, footer 73:517. visibility-selector 26:254(role=non-seller)에 option/sale-request 노드 없음, visibility-note 26:196. text-input[focus] 26:244
- 26:203 sale-request@unchecked: 66:206, 66:222, 66:205, footer 73:525(action count=1, submit-button[disabled]). 금지 항목 4종 26:214~26:217(개인정보, 고객정보, 회사기밀, 타인 저작물), confirm-checkbox 26:269(checked=false)
- 26:274 sale-request@checked: 66:235, 66:251, 66:234, footer 73:533(제출 버튼 이름 submit-button, ink 채움). 금지 항목 4종 26:280~26:283, confirm-checkbox 26:284(checked=true)
- 36:49 home: 66:264, 66:280(root '홈'), 66:263, footer 73:543(nav, tab-bar active=홈). greeting 36:50, section/progress 36:53(list 36:55 안 list-row 36:56·36:62·36:68, status-badge 작성 중·제출 완료·작성 중), section/recommended-skills 36:74(skill-card compact 3개), 내 자산 요약 list-row 36:86
- 36:102 skills: 66:290, 66:306(root '스킬 라이브러리'), 66:289, footer 73:572(nav, tab-bar active=스킬). text-input 36:104, category-chips 36:106, skill-list 36:121(skill-card full 4개, 검증된 스킬 2장)

## 이번 실행 수정
- list-row 66 Hug 반영 확인: 홈 진행 행 36:56·36:62·36:68 높이 66, 요약 행 36:86 높이 66, 내 자산 sale-request 26:261·26:276 높이 66(y16~82). sale-request prohibited-guide는 y106으로 이미 아래에 배치돼 겹침 없음
- 홈 진행 list(36:55) 행 사이 간격 24 → 12(spacing 변수 22:24 바인딩). section/progress 높이 311 → 287. 하위 y: recommended-skills 426 → 402, 요약 행 571 → 547, 끝 y613(프레임 y712). content-area 하단 패딩 32(y615) 안에 들어가고 footer(nav y746)와 겹치지 않음(34px 여유, 변경 전 끝 y637은 패딩 침범)
- 홈 외 프레임(등록 seller 끝 722, 스킬 끝 694, 판매 신청 끝 429)은 footer·패딩과 겹치지 않아 변경 없음

## 검사 메모
- V1: option/private[selected] 1개씩(seller·non-seller), option/sale-request 노드는 register@seller(I26:234;23:61)에만 존재, non-seller 0개
- V2: 금지 항목 4종 텍스트, confirm-checkbox, @unchecked 안 submit-button[disabled](점선 hairline, 글자 #707070, 흰 배경)
- MVP 제외 표현(허들링 픽, 구매, 피드백, 판매 중, 판매 중지) S7 텍스트 노드 0건
- 페이지 스캔: 폰트 Pretendard SemiBold·Regular·Bold만, #adadad 글자 0, accent #0066ff 0, 그림자·그라디언트 0, 대문자 표기 0
- 배지는 S6 status-badge 인스턴스 그대로(rules.json status_badges 스타일). 새 색·반경·간격 값 없음
- 수정(사용자 요청): file-attach-row 인스턴스 26:228(26:124 안, 26:114 화면)·26:248(26:171 안, 26:161 화면)의 불리언 속성 plus-icon을 false로 설정해 '삭제' 앞 + 아이콘 숨김(S6 23:99 속성, 기본 true). button/attach 폭 78 → 58(Hug), 높이 44·인스턴스 358×60 그대로, 문구·색·반경 변경 없음
- 수정(사용자 요청, add-file-button + 아이콘): add-file-button 26:132(26:114 seller 화면), 26:179(26:161 non-seller 화면)의 라벨 '파일 추가'(26:133, 26:180) 왼쪽에 icon/plus 추가. 새 아이콘 ID 110:2(26:132 안), 110:4(26:179 안). S6 icon/plus 108:402를 복제, 내부 벡터 shape, 16×16, 선 2px 둥근 끝, 선 색은 color/ink 변수 바인딩(라벨 글자색 #141414와 동일). 버튼 itemSpacing 0 → spacing/4 변수(4) 바인딩, 가로 가운데 정렬 유지.
  - 변경 전: 버튼 자식 라벨 1개, 간격 0. 변경 후: 자식 icon/plus + 라벨, 간격 4, 아이콘+라벨 묶음 중앙.
  - 버튼 358×44, 흰 채움, 스트로크, 반경, 라벨 문구·폰트는 그대로. S6 23:99(file-attach-row)와 plus-icon 속성은 건드리지 않음.
- 수정(사용자 요청, 텍스트 스타일 적용): 6개 화면의 인스턴스 밖 TEXT 32개 중 17개에 적용 후 홈 2개 되돌림 → 순적용 15개. 인스턴스 안쪽 글자는 컴포넌트를 따라옴(S6에서 적용, 컴포넌트 높이 변화가 인스턴스에 반영됨). 글자 색·크기·굵기·문구·이름·ID 변경 없음.
  - 순적용: sale-request@checked 5(26:278 heading-4, 26:280~26:283 body) / @unchecked 5(26:212, 26:214~26:217) / register@non-seller 2(26:180 파일 추가, 26:196 visibility-note) / register@seller 1(26:133) / skills 0 / home 2(36:54 등 section 제목 heading-4 18/Bold; section/recommended-skills 제목 포함)
  - 미적용(스타일 없는 13 SemiBold, 15개): 26:164 제목, 26:168 설명, 26:172 첨부 파일, 26:182 공개 범위 (non-seller) / 26:117 제목, 26:121 설명, 26:125 첨부 파일, 26:135 공개 범위 (seller) / chip 텍스트 36:108 전체 24, 36:110 AI 실무 8, 36:112 Figma + AI 5, 36:114 바이브코딩 4, 36:116 자동화 3, 36:118 콘텐츠 제작 2, 36:120 1인 사업가 운영 2 (모두 13 SemiBold, 스타일 없음)
  - 되돌림(홈 content-area 넘침 방지): 홈의 인사말 36:51(24 Bold)·미션 요약 36:52(15 Regular) 스타일 해제, 줄 높이 AUTO 복원. 홈 list-row 인스턴스 4개(36:56, 36:62, 36:68, 36:86)의 title·수정일/개수 요약 텍스트 8개(I36:56;23:28, I36:56;23:29, I36:62;23:28, I36:62;23:29, I36:68;23:28, I36:68;23:29, I36:86;35:85, I36:86;35:86) 스타일 오버라이드 해제 + 줄 높이 AUTO. 해제 전 홈 마지막 행이 y601+75=676으로 content-area(h647)를 29 넘어 잘림 → 해제 후 끝 y632, 행 높이 66. 이 8개는 컴포넌트와 스타일이 어긋난 상태(보고 대상)
  - 높이 변화(스타일 적용 전→후, 되돌림 반영 후 최종): 프레임 6개 모두 844 그대로. 하위: 홈 greeting 51 유지, 홈 recommended-skills 124 → 137(compact skill-card 88→101), skills skill-card 4장 92→103(skill-list 끝 y639, 이전 595 추정), sale-request prohibited-guide 168 → 192(제목 20→24, 항목 18→23), 등록 field-visibility non-seller 192 → 196(visibility-note 16→20), 파일 추가 라벨 18→23(버튼 44 유지)
  - 겹침·어긋남 최종: 화면 6개 content-area 안 자식 겹침 0. 홈 끝 y632(content-area 하단 패딩 32 기준 615보다 17 아래, footer 746까지 15 여유, 클립 없음), skills 끝 y639(패딩 8 침범, footer와 겹침 없음, 클립 없음), sale-request 379, register seller 613·non-seller 566. 스크린샷은 이미지 열람 수단이 없어 육안 확인 못 함, 노드 좌표 재조회로 확인
- 수정(사용자 결정 A안, list-row·skill-card 스타일 되돌림, type/label-md 추가): (1) type/label-md(S:8889feaeffe6a49afb3d4e0abfd0b1849d825fb7,)를 13 SemiBold 글자 15개에 적용: register@non-seller 26:164, 26:168, 26:172, 26:182 / register@seller 26:117, 26:121, 26:125, 26:135 / skills 칩 36:108, 36:110, 36:112, 36:114, 36:116, 36:118, 36:120. 되돌린 노드 없음. 높이 변화: 필드 wrapper(field-title/desc/file/visibility) 글자 16→18로 각 +2(field-title 75→77, field-desc 71→73, field-file 136→138, field-visibility seller 243→245·non-seller 196→198), 칩 글자 16→18이나 칩 높이 44 그대로(고정, 변화 0). register content-area(h663, 하단 패딩 32) 안 마지막 요소 끝 seller y621·non-seller y574, 겹침·잘림 없음. (2) 홈 36:49·스킬 36:102의 list-row·skill-card 인스턴스 안 글자는 컴포넌트와 같은 상태(스타일 없음, AUTO, 자간 0)로 조회 확인. 직전 되돌린 인스턴스 글자 8개와 인사말 36:51, 미션 요약 36:52 모두 스타일 없음·AUTO로 컴포넌트와 일치. 예외(변경 안 함): 홈 list-row 36:62의 중첩 status-badge 글자 I36:62;23:30;23:7 '제출 완료'는 status-badge 컴포넌트 variant(23:7) 자체 스타일(type/label)을 따라 스타일이 남아 있음(status-badge 유지 지시). (3) 높이: 홈 list-row 인스턴스 66, skill-card compact 88, skills skill-card 4장 92, 홈 recommended-skills 124 · progress list 222. 홈 content-area(h647) 마지막 요소 list-row 36:86 끝 y619(프레임 y718, 647 안, 기준선 615보다 4 아래, footer y746까지 28 여유, 잘림 없음. 4px 차이는 section 제목 36:54·36:75가 heading-4 스타일 유지로 21→24 커진 것 합 6 중 일부; 이 스타일은 건드리지 않음). skills skill-list 36:121 끝 y595(이전 약 594 부근 복귀, 639에서 감소), 겹침·잘림 0. 스크린샷 육안 확인 못 함, 노드 좌표 재조회로 확인.
- 스크린샷 URL은 받았으나 이미지 열람 수단이 없어 육안 비교는 못 했고, 노드 좌표·크기 재조회로 확인했다

## 수정(사용자 요청, text-input 상태별 높이 통일)
S6 text-input rest·focus 높이를 48로 통일(S6 기록 참고). 인스턴스는 세로 FIXED 덮어쓴 크기(47/51)를 가지고 있어 48로 맞춤(컴포넌트 높이와 같음, 반경 8·1px 링·패딩 12 그대로).
- 변경 전 → 후 높이: 26:224(focus, register@seller 제목) 51 → 48 / 26:226(rest, 설명) 47 → 48 / 26:244(focus, register@non-seller 제목) 51 → 48 / 26:246(rest, 설명) 47 → 48 / 36:104(rest, skills 검색창) 47 → 48. 설명 입력창은 한 줄 높이 그대로(80 같은 큰 높이 덮어쓰기 없음). rest·focus 높이 서로 같음(48)
- 레이아웃: register@seller field-title 26:116 77 → 74, field-desc 26:120 73 → 74(내부 입력창 y26 그대로), 이후 field-file 26:124 y212, field-visibility 26:134 y374(끝 619). content-area 66:143(h663, 하단 패딩 32 기준선 631) 마지막 끝 y621 → 619(12 여유), non-seller 574 → 572. skills 36:102 content-area 66:289(h647) 검색창 끝 y64(전 y63), category-chips y88, skill-list 36:121 끝 y596(전 595), footer y746까지 겹침 없음. 같은 content-area 안 자식 겹침 0, 잘림 0
- 변경 안 함: 이름·ID·변수 바인딩·색·문구. 판정 스크립트는 돌리지 않음

## 수정(사용자 요청, 버튼 반경 8)
새 변수 `radius/button-rect`(8) VariableID:120:408(tokens, S6 기록 참고)을 버튼에 바인딩. 높이·채움·외곽선·글자·아이콘·이름·ID 그대로.
- 직접 변경(9999, 변수 없음 → 8, 120:408): add-file-button 26:132(26:114 seller 화면 안), 26:179(26:161 non-seller 화면 안). 안 icon/plus 110:2·110:4 변경 없음
- 인스턴스(컴포넌트를 따라옴, 반경 덮어쓰기 없음 → 풀 것 없음): submit-button I73:525;72:326;64:181(@unchecked, submit-button[disabled]), I73:533;72:326;64:181(@checked, submit-button), 등록 action-area 버튼 I73:509;72:326;64:178·64:176(seller), I73:517;72:326;64:178·64:176(non-seller), button/attach I26:228;23:103(26:114 안), I26:248;23:103(26:161 안). 모두 조회 결과 반경 8, 변수 120:408
- 안 바꾼 것: header-left/right(I66:222;64:169 등 투명 44×44 터치 영역), checkbox-box, status-badge, bar(home-indicator), tab-bar·icon-holder, 칩은 알약 그대로

## 수정(사용자 요청, status-badge 4종 아이콘)
(아이콘 16×16은 이후 12×12로 변경, 아래 '수정(사용자 결정, 배지 아이콘 12×12로 변경)' 참고. 아래 폭 수치는 16×16 시점 기록)
S7 노드는 수정하지 않고 조회만 했다. 인스턴스가 컴포넌트를 따라 아이콘 프레임이 나타남(덮어쓴 값 없음).
- 홈 list-row 36:56(작성 중, 배지 I36:56;23:30): icon/edit 나타남, 폭 60 → 80. 36:62(제출 완료, I36:62;23:30): icon/send, 71 → 91. 36:68(작성 중, I36:68;23:30): icon/edit, 60 → 80. 배지 높이는 기존 덮어쓴 값 그대로(작성 중 26, 제출 완료 27)
- 내 자산 sale-request 두 화면 list-row 26:261(I26:261;23:30), 26:276(I26:276;23:30)(임시저장): icon/save 나타남, 68 → 88
- list-row 영향: 모두 높이 66 유지. 줄바꿈 없음(제목 18, 보조 글 16 한 줄 그대로, row-info 폭만 줄어듦: 홈 202/191/202, sale-request 226 그대로), 배지와 겹침 없음. 홈 배지 오른쪽 끝 310 = 행 폭 326 - 16 유지

## 수정(사용자 결정, 배지 아이콘 12×12로 변경)
S7 노드는 수정하지 않고 조회만 했다. S6 status-badge 아이콘이 12×12로 바뀌어 인스턴스가 따라옴(덮어쓴 값 없음).
- 홈 36:56 안 I36:56;23:30 icon/edit 12×12(배지 80 → 76, 높이 24), 36:62 안 I36:62;23:30 icon/send 12×12(91 → 87, 높이 27), 36:68 안 I36:68;23:30 icon/edit 12×12(80 → 76, 높이 24)
- sale-request@unchecked 26:203 안 I26:261;23:30, @checked 26:274 안 I26:276;23:30 icon/save 12×12(88 → 84, 높이 27)
- list-row 36:56·36:62·36:68·36:86, 26:261·26:276 모두 높이 66 유지, 배지가 줄어 row-info 폭만 4 늘어남(줄바꿈·겹침 없음 가정, 조회상 높이 66 불변). 배지 오른쪽 끝은 행 폭 - 16 유지
- 수정(S6 list-row 앞 20px 아이콘, 사용자 요청): S7 노드 미수정, 조회만. 인스턴스 6개 모두 컴포넌트를 따라 아이콘 표시(progress 5개 I36:56;127:5 등, summary 36:86 I36:86;127:7), 덮어쓴 값 없음, 높이 66, 제목·보조 글 한 줄. 홈 content-area 66:263(y99, h647) 마지막 요소 list-row 36:86이 화면 y652~718(content-area 안 553~619)로 647 안.

## 수정(사용자 요청, 삭제 버튼 X 아이콘)
S6 file-attach-row 23:99에 button/delete 131:436(44×44, 반경 radius/button-rect 120:408, 안 icon/x 131:437 16×16)과 불리언 속성 show-attach/show-delete 추가(S6 기록 참고).
- 인스턴스 26:228(26:114 seller 안 field-file 26:124), 26:248(26:161 non-seller 안 field-file 26:171): show-attach=false, show-delete=true, plus-icon=true(기본 복원). button/attach 안 덮어쓴 텍스트 '삭제'는 '파일 선택'으로 되돌림(숨김). 인스턴스 안 button/delete: I26:228;131:436, I26:248;131:436 (44×44, 반경 8). 파일명 'prompt-pack.zip'·'2.4MB' 유지
- 레이아웃: 행 358×60 불변, field-file 138 불변, texts 폭 264 → 278(버튼 58 → 44). content-area 66:143 높이 663, 마지막 요소(field-visibility) 끝 y 619 (631 이하) 불변

## 수정(사용자 요청, 삭제 버튼 배경 제거·X 검정)
S7 노드는 수정하지 않고 조회만 했다. 인스턴스 I26:228;131:436, I26:248;131:436 모두 컴포넌트를 따라 채움 없음(투명), X 벡터 선 color/ink 22:4(#141414) 바인딩, 44×44 유지. 덮어쓴 값 없음. 행 26:228·26:248 높이 60, 파일명 텍스트·field-file 138 불변.

## 수정(사용자 요청, skill-card 카테고리 12px·연하게·타이틀 위)
S7 노드는 수정하지 않고 조회만 했다.
- 스킬 화면 36:102 skill-card 4장: 36:122·36:133(verified=true) 카테고리가 맨 위로, 높이 92 → 110. 36:128·36:139(verified=false)는 카테고리 맨 위, 높이 92 유지. 카테고리 문구 덮어쓴 값 유지, 12px Regular #707070 그대로, 어긋남 없음
- skill-list 끝 y: 이전 약 595 → 632(content-area 기준, 카드 +18 ×2). 기준선 615(647-32)보다 17 넘음, content-area 높이 647 안(바닥 여백 15). 수정 필요 여부는 오케스트레이터 판단
- 홈 36:49 compact 3장(36:77, 36:80, 36:83): 카테고리 없는 구조라 변화 없음, 높이 88, content-area 마지막 요소 끝 y 619 유지, 가로 스크롤 폭 616 구조 유지

## 수정(사용자 요청, skill-card 검증됨 배지·텍스트 간격 8)
S7 노드는 수정하지 않고 조회만 했다. 새 노드 ID는 S6 badge/verified 134:2(S6 기록 참고).
- 스킬 화면 36:102 skill-card 4장 모두 컴포넌트를 따라옴(gap 8). 36:122·36:133(verified=true, main 23:20) 높이 110 → 130, 36:128·36:139(verified=false, main 35:70) 92 → 100. 배지는 인스턴스 안에 따라옴.
- 홈 36:49 compact 3장(36:77, 36:80, 36:83, main 35:69) 높이 88 → 92(HUG), 추천 strip 36:76 92, section/recommended-skills 36:74 128. 홈 마지막 요소 list-row 36:86 끝 y 619 → 623(content-area 647 안, 기준선 615는 8 넘음, 잘림 없음).
- 넘침(잘림 발생): 스킬 화면 skill-list 36:121 y156, 높이 532, 끝 y 688(이전 632). content-area 66:289 높이 647(clips=true)을 41 넘어, 마지막 카드 36:139(y588~688)의 아래 41이 잘림. 하단 패딩 32 기준선 615보다 73 아래. 수정하지 않음, 사용자 결정 필요.

## 수정(content-area HUG) 홈 36:49
- 사용자 지시: content-area는 늘어나도 상관없음. 홈 content-area 66:263 세로 FIXED 647 → HUG, clipsContent true → false(끝 내용이 잘리지 않게 해제).
- 구조 확인: 화면 프레임 36:49는 auto layout 아님(NONE, 390×844, clip 켬). 자식 순서 status-bar, header, content-area(y99), footer 73:543(y746, 절대 위치 아닌 일반 자식, 마지막 인덱스 = 맨 위 레이어). footer y746 변경 없음.
- 결과 수치: content-area 높이 647 → 691(마지막 요소 끝 659 + 하단 패딩 32), 끝 y 화면 790. 자식 위치·간격·패딩 변경 없음(36:50 y16, 36:53 y91 h317, 36:74 y432 h128, 36:86 y584 h75).
- 마지막 list-row 36:86 하단 화면 좌표 y758(99+584+75). footer 상단 y746과 12px 겹침, 위 레이어는 footer(36:86과 content-area 모두 footer 아래). content-area 하단 자체는 footer와 44px 겹침(790 - 746).
- 화면 프레임 크기 390×844 유지(auto layout 아니라 깨지지 않음). 되돌림 없음. clip 해제로 content-area 밖 넘침은 보이지만 footer가 덮는 12px 구간은 가려짐. 겹침 12는 미해결(보고).

## 수정(사용자 요청, nav footer 전체 영역 투명)
S7 노드는 수정하지 않고 S6 footer type=nav 72:296(바깥 채움)과 그 안 home-indicator 72:323의 채움을 비웠고, 인스턴스가 따라왔다(덮어쓴 값 없음). 홈 36:49의 footer 73:543, 스킬 36:102의 footer 73:572는 바깥 영역(390×98, 탭바 아래 34 포함)이 투명이라 content-area 내용이 비쳐 보이며, 탭바 알약(358×64, 흰 채움·그림자)은 그대로 내용을 덮는다. footer y746·크기·맨 위 레이어, 프레임 390×844, 홈 content-area HUG(691) 변경 없음. 홈 36:86 하단(y758)과 footer 겹침 12는 이제 탭바 알약 위로 보이는 겹침이 아니라 알약이 덮는 구간 여부에 따라 달라짐(알약 y746~810). action footer 4개는 그대로.

## 수정(사용자 요청, S6 컴포넌트 글자 텍스트 스타일 전체 적용) 영향
S7 노드는 수정하지 않고 조회만 했다. skill-card 세트 variant(35:69 88→105, 35:70 100→111, 23:20 111→119)의 높이가 커져 S7이 영향을 받았다. 스킬 36:102는 skill-list 36:121(y156)이 h532(전 494)가 되어 화면 좌표 끝 688+99=787로 content-area(h647, 화면 끝 746)와 footer 73:572(y746)를 41 넘는다(카드 36:122 h119 y0, 36:128 h111 y143, 36:133 h119 y278, 36:139 h111 y421). 홈 36:49 content-area 66:263은 HUG라 h704(전 691, list-row 36:86 y597 h75, 하단 패딩 32), 화면 끝 803로 footer 73:543(y746)과 겹침(허용 상태 그대로 둠). 등록·판매 신청 4개 화면(26:114, 26:161, 26:203, 26:274)은 높이·y 변화 없음(content-area 663, footer y762 h82, sale-request의 list-row 26:261 h75·prohibited-guide y115·confirm-checkbox y331 이전 수정 값 그대로). 6개 프레임 모두 높이 844 불변. 스킬 화면 하단 겹침은 사용자 결정 필요.

## 수정(사용자 요청, S7 화면 글자 텍스트 스타일 적용)
S7 Screens 페이지만 수정. 색 바인딩·문구·이름·ID·간격·패딩 변경 없음, FIXED 고정 없음. 스크린샷 육안 확인 없이 노드 재조회 수치로 확인. 판정 스크립트 안 돌림.
- 조회 결과: 화면 6개가 직접 가진 TEXT 32개 중 30개는 이미 type/* 스타일이 적용돼 있었음(heading-4 / label-md / body / body-sm / link / title 등, 크기·굵기 일치). 이번에 새로 적용한 노드는 홈 2개.
- 화면별 적용 노드 수(이번 신규 / 화면 직접 TEXT 전체): 홈 36:49 2 / 4, 스킬 36:102 0 / 7, 등록 seller 26:114 0 / 5, 등록 non-seller 26:161 0 / 6, 판매 신청 @unchecked 26:203 0 / 5, @checked 26:274 0 / 5 (합계 신규 2 / 전체 32)
  - 홈 신규: 36:51 인사말 24 Bold → type/heading-2(높이 29 → 32), 36:52 미션 요약 15 Regular → type/body(높이 18 → 23). 글자 색 채움 전후 동일 확인. 기존 36:54, 36:75는 heading-4 유지.
- 미적용 목록: 없음(맞는 스타일 없는 글자 0개).
- 직접 지정이 남은 인스턴스 글자(overrides에 textStyleId·fontName·fontSize 표시, 값은 컴포넌트와 같음, 변경 안 함): I36:56;23:28, I36:56;23:29, I36:62;23:28, I36:62;23:29, I36:68;23:28, I36:68;23:29, I36:86;35:85, I36:86;35:86 (홈 list-row 4개의 title·보조 글, 총 8개). 다른 인스턴스 글자는 오버라이드 없음.
- 홈 content-area 66:263(세로 HUG, 클립 해제 그대로): 높이 704 → 712. 마지막 요소 36:86 y597 → 605, 높이 75 그대로(끝 672 → 680). 위 노드 y: 36:50 y16 h51 → h59, 36:53 y91 → 99(h317), 36:74 y432 → 440(h141). 인사말·미션 합 +8. footer 73:543(y746) 대비 36:86 끝 화면 y 779(전 771), 겹침 33(전 25), footer 위 레이어(투명 바깥 영역)라 탭바 알약 뒤로 내용이 비침, 사용자 결정(허용) 범위.
- 스킬 content-area 66:289 변경(사용자 결정): 세로 FIXED 647 → HUG, clipsContent true → false. 높이 647 → 720(끝 요소 skill-list 36:121 y156 h532, 끝 688 + 하단 패딩 32). 자식 y 불변(36:104 y16, 36:106 y88, 36:121 y156, 끝 688 불변). skill-list 이제 잘리지 않음. 화면 프레임 36:102 390×844 불변, footer 73:572 y746 불변(투명, content 끝 화면 y787이 footer 41 겹쳐 탭바 뒤로 비침, 사용자 결정 반영).
- 등록·판매 신청 content-area 높이·마지막 요소 y 전→후(변경 없음): 66:143 h663 마지막 26:134 y374 h245 끝 619 → 619 / 66:174 h663 26:181 y374 h198 끝 572 → 572 / 66:205 h663 26:269 y331 h48 끝 379 → 379 / 66:234 h663 26:284 y331 h48 끝 379 → 379. 건드리지 않음.

## 수정(사용자 요청, skill-list 카드 간격 24→12)
S7 Screens 페이지만 수정. 스킬 화면 36:102 내 skill-list 36:121(세로 auto layout, 카드 4개)의 itemSpacing 24 → 12, 변수 spacing/12(VariableID:22:24) 바인딩(전 VariableID:22:26). 다른 노드 변경 없음(content-area 자식 간격 24, input·chips, skill-card 컴포넌트·글자, 다른 화면·페이지, S4 82:164 미수정). 판정 스크립트 안 돌림.
- skill-list 36:121: y156 유지, 높이 532 → 496(간격 3칸 × 12 감소 = 36). 세로 HUG 유지.
- 카드 y·높이 전 → 후(skill-list 기준 y): 36:122 y0 h119 → y0 h119 / 36:128 y143 h111 → y131 h111 / 36:133 y278 h119 → y254 h119 / 36:139 y421 h111 → y385 h111. 카드 높이 불변.
- skill-list 끝(content-area 기준) 688 → 652.
- content-area 66:289: 높이 720 → 684(HUG 유지, clipsContent false 유지, 자식 간격 24 유지, y99 유지). 프레임 36:102 390×844 유지, FIXED 고정 없음.

- 마지막 카드 36:139 끝 화면 y 787 → 751, footer 73:572(y746) 겹침 41 → 5(content-area 끝 화면 y 783). 겹침 5는 투명 footer 위 바깥 영역이며 사용자 결정(허용) 범위.

## 수정(사용자 요청, text-input·submit-button·action-area 높이 48→56)
S6 높이 변경(s6-tokens-components.md 참고)에 맞춰 컴포넌트를 따라오지 않는 세로 FIXED 덮어쓰기 인스턴스를 직접 56으로 맞춤. 간격(24)·라벨-입력창 간격(8)·패딩·색·변수 바인딩 변경 없음, 새 값 없음. 스크린샷 육안 확인 없이 노드 재조회 수치로 확인. 판정 스크립트 안 돌림.
- text-input 인스턴스 높이 48 → 56: 26:224(focus, seller 제목), 26:226(rest, seller 설명), 26:244(focus, non-seller 제목), 26:246(rest, non-seller 설명), 36:104(rest, skills 검색). 설명 입력창은 한 줄(48)이었고 80 같은 여러 줄 덮어쓰기는 없음
- action footer 인스턴스 73:509(seller), 73:517(non-seller), 73:525(@unchecked), 73:533(@checked): 높이는 컴포넌트를 따라 이미 90(안 action-area 56 + home-indicator 34), y 762 → 754(끝 844). 안 버튼 save-draft·register 175×56, submit-button[disabled]/submit-button 358×56(세로 FILL, 따라옴). nav footer 73:543·73:572 변경 없음(y746, 98)
- content-area 66:143, 66:174, 66:205, 66:234: 세로 FIXED 663 → 655 (y99 → 끝 754 = footer y754)
- 재배치 y(content-area 기준, 전 → 후): register@seller field-title 26:116 h74 → 82 / field-desc 26:120 y114 → 122, h74 → 82 / field-file 26:124 y212 → 228 / field-visibility 26:134 y374 → 390(h245) 끝 619 → 635. non-seller: 26:163 h82, 26:167 y122, 26:171 y228, 26:181 y390(h198) 끝 572 → 588. 변경 없음(전 = 후): sale-request 두 화면 마지막 요소 끝 379, list-row 26:261·26:276 y16 h75, prohibited-guide y115 h192, confirm-checkbox y331 h48
- skills 36:102: 검색창 36:104 y16 h56(끝 72), category-chips 36:106 y88 → 96, skill-list 36:121 y156 → 164(h496, 끝 652 → 660), content-area 66:289 HUG 684 → 692(끝 화면 y 783 → 791), footer 73:572(y746)와 겹침 5 → 45(투명 footer 위 바깥 영역, 기존 사용자 결정 허용 범위 안의 연장, 보고)
- 겹침·잘림: 4개 등록·판매 신청 화면 content-area 안 자식 겹침 0, 마지막 요소 끝(화면 좌표)이 footer y754 위(seller 99+635=734, 20 여유), 잘림 0
- 넘침 보고(값은 바꾸지 않음): register@seller content-area 66:143 마지막 요소 field-visibility 26:134 끝 y635, 하단 패딩 32 기준선 = 655 - 32 = 623, 넘친 양 12px(content-area 높이 655 안, 하단 여유 20, footer와는 겹침 0). 전 상태는 끝 619 / 기준선 631로 12 여유였음. register@non-seller 66:174는 끝 588 ≤ 기준선 623으로 넘침 없음(35 여유). sale-request 두 화면 끝 379, 넘침 없음. 간격 24·패딩 값 새로 만들지 않음, 변경은 사람 결정 필요

## 수정(사용자 요청, accent 적용 tab-bar 활성 아이콘·chip 컴포넌트)
docs/design.md Brand & Accent·Chips 기준. 스크린샷은 열 수 없어 노드 재조회 수치로만 확인. 판정 스크립트는 돌리지 않음. 위 '검사 메모'의 'accent #0066ff 0'은 이전 값.
- skills 36:102 category-chips 36:106(x16 y96, 가로 auto layout 간격 8, clip 끔, 715×44 그대로): 컴포넌트 밖 pill 프레임 7개(36:107, 36:109, 36:111, 36:113, 36:115, 36:117, 36:119)를 S6 chip 세트 175:382 인스턴스로 교체. 새 인스턴스: 175:574 `chip/전체 24[selected]`(selected=true, 74×44), 175:576 `chip/AI 실무 8`(82), 175:578 `chip/Figma + AI 5`(107), 175:580 `chip/바이브코딩 4`(100), 175:582 `chip/자동화 3`(78), 175:584 `chip/콘텐츠 제작 2`(103), 175:586 `chip/1인 사업가 운영 2`(123). 나머지 6개 selected=false. 변경 전: 전체 24 = ink 채움(22:4)+흰 글자, 나머지 canvas-soft+ink 글자. 변경 후: 전체 24 = accent 채움(22:12)+canvas 글자, 나머지 canvas-soft+ink 글자. 폭·높이·간격·문구·위치(y96) 전과 동일(숫자 일치 확인). 글자 노드 ID는 인스턴스 안으로 바뀜(36:108 등 폐기).
- tab-bar 인스턴스 I73:543;72:297(홈 36:49), I73:572;72:297(스킬 36:102): 컴포넌트를 따라 활성 아이콘 벡터가 accent로 바뀜(홈 I73:543;72:297;44:5, 스킬 I73:572;72:297;44:40). 덮어쓰기 없음, 직접 맞춘 노드 없음.
- 프레임별 accent(color/accent 바인딩 노드) 수: home 36:49 = 1(탭 아이콘), skills 36:102 = 2(탭 아이콘 I73:572;72:297;44:40 + chip 175:574), register@seller 26:114 = 0, register@non-seller 26:161 = 0, sale-request@unchecked 26:203 = 0, @checked 26:274 = 0. 모두 2 이하. action-area·submit-button 미수정.

## 수정(사용자 요청, tab/홈[selected] 라벨 accent)
- home 36:49의 tab-bar 인스턴스 I73:543;72:297, 라벨 I73:543;72:297;44:6: 컴포넌트(44:6)를 따라 color/ink(22:4) → color/accent(VariableID:22:12)로 바뀜 확인. 덮어쓰기 없음, 직접 맞춘 노드 없음. skills 36:102 등 다른 variant 인스턴스는 변경 없음.
- 프레임별 accent 노드 수(조회): home 36:49 = 2(아이콘 I73:543;72:297;44:5 + 라벨 I73:543;72:297;44:6), skills 36:102 = 2(탭 아이콘 + chip 175:574), register@seller 26:114 = 0, @non-seller 26:161 = 0, sale-request@unchecked 26:203 = 0, @checked 26:274 = 0. 모두 상한 2 이하.

## 수정(사용자 요청, checkbox-box checked accent)
S6 confirm-checkbox 23:112 checked=true(box 23:109)의 채움 변경(ink 22:4 → color/accent VariableID:22:12)을 따라 S7 인스턴스가 바뀜. 판정 스크립트는 돌리지 않음.
- sale-request@checked 26:274 > confirm-checkbox 26:284(checked=true), box I26:284;23:109: 채움 accent(22:12) 바인딩으로 따라옴 확인, 선 없음, 덮어쓰기 없음, 직접 맞춘 노드 없음. 인스턴스 안 icon/check는 canvas 흰색 그대로.
- sale-request@unchecked 26:203 > confirm-checkbox 26:269(checked=false), box I26:269;23:106: canvas(22:5) 채움 + 선 1px 그대로, 변경 없음.
- 프레임별 accent 노드 수(조회): home 36:49 = 2(변경 없음), skills 36:102 = 2(변경 없음), register@seller 26:114 = 0, @non-seller 26:161 = 0, sale-request@unchecked 26:203 = 0, @checked 26:274 = 1(box I26:284;23:109). 모두 상한 2 이하.

## 수정(사용자 요청, visibility-selector 선택 행 accent A안)
새 페이지·새 변수·새 hex 없음. 판정 스크립트는 돌리지 않음.
- register@seller 26:114의 visibility-selector 26:234(main 23:54), register@non-seller 26:161의 26:254(main 23:84)는 컴포넌트를 따라 바뀜(덮어쓰기 없음, 직접 수정 없음). 선택 행 option/private[selected] 외곽선(I26:234;23:55, I26:254;23:85)과 radio-dot(I26:234;95:95, I26:254;95:107)이 color/accent(VariableID:22:12) 바인딩. 변경 전 ink(VariableID:22:4) → 후 accent. 라디오 링은 ink 그대로.
- 프레임별 accent 노드 수(조회): register@seller 26:114 = 2 / register@non-seller 26:161 = 2 / home 36:49 = 2 / skills 36:102 = 2 / sale-request@unchecked 26:203 = 0 / @checked 26:274 = 1. 모두 상한 2 이하.

## 수정(사용자 요청, radio 선택 상태 6px 링)
S6 visibility-selector 선택 행 radio 변경(s6-tokens-components.md 참고)을 S7 인스턴스가 따라옴. 덮어쓰기 없음, 직접 수정 없음. 새 변수·새 색 없음. 판정 스크립트 안 돌림.
- register@seller 26:114의 26:234: option/private[selected] 안 radio I26:234;96:4 = 6px INSIDE, 선 color/accent(VariableID:22:12), 채움 canvas. radio-dot 없음. register@non-seller 26:161의 26:254: radio I26:254;96:13 동일. 비선택 radio(I26:234;96:5, 96:6, I26:254;96:14)는 1px hairline(22:8) 그대로.
- 높이 변화 없음: 선택 행 69, 26:234 219, 26:254 144.
- 삭제/변경한 S7 노드: 없음(조회만).
- 프레임별 accent 노드 수(조회): register@seller 26:114 = 2(행 외곽선 + radio 링) / register@non-seller 26:161 = 2 / home 36:49 = 2(탭 아이콘 + 라벨) / skills 36:102 = 2(탭 아이콘 + chip 175:574) / sale-request@unchecked 26:203 = 0 / @checked 26:274 = 1. 모두 상한 2 이하.

## 수정(사용자 요청, tab-bar 선택 라벨 전체 accent)
새 페이지·새 변수·새 색 없음. 판정 스크립트 안 돌림. S7 직접 수정 없음, 조회만.
- skills 36:102 tab-bar 인스턴스 I73:572;72:297 라벨 I73:572;72:297;44:41 '스킬': 컴포넌트를 따라 color/ink → color/accent(VariableID:22:12)로 바뀜(조회: #0066ff). 덮어쓰기 없음. home 36:49는 이전 요청대로 accent 유지.
- 프레임별 accent 노드 수(조회, 노드 단위): home 36:49 = 2(탭 아이콘 + 탭 라벨) / skills 36:102 = 3(탭 아이콘 + 탭 라벨 + 선택 chip 175:574) / register@seller 26:114 = 2 / register@non-seller 26:161 = 2 / sale-request@unchecked 26:203 = 0 / @checked 26:274 = 1.
- 주의: skills 36:102는 3으로 상한 2 초과. 사용자 지시에 따라 값을 되돌리거나 다른 요소를 바꾸지 않음. 규칙 상한 처리는 별도 결정 대기.

## 수정(사용자 요청, register-button·submit-button 독립 컴포넌트화)
S6 action-area 64:190 안 버튼을 컴포넌트 인스턴스로 바꾼 것(s6-tokens-components.md 참고)이 S7 footer type=action 4개에 따라옴. 색·모양·크기 변화 없음. 화면 프레임·footer 위치·content-area 변경 없음(6개 모두 390×844, footer y754 h90, content-area y99 h655 그대로). 판정 스크립트·스크린샷 미실행, 노드 재조회 수치로 확인.
- 변경 전 → 후 노드 (footer 안 action-area 인스턴스):
  - register@seller 73:509: register-button 프레임 I73:509;72:326;64:176 → register-button 인스턴스 I73:509;72:326;181:66 (199/175×56, 채움 #141414, 글자 '등록' #ffffff, 반경 8). save-draft-button 그대로
  - register@non-seller 73:517: 같은 구조, I73:517;72:326;181:66
  - sale-request@unchecked 73:525: submit-button[disabled] 프레임 I73:525;72:326;64:181 → submit-button[disabled] 인스턴스 I73:525;72:326;181:68 (main 23:115, 16/358×56, 흰 채움 + #e0e0e0 1px 점선 [4,4], 글자 '판매 신청 제출' #707070, 반경 8)
  - sale-request@checked 73:533: 같은 인스턴스 I73:533;72:326;181:68의 variant 속성만 enabled로 지정(main 23:113), 이름 `submit-button`. 조회: 채움 #141414(22:4 바인딩), 외곽선 없음, 글자 #ffffff, 358×56 x16, 반경 8, 글자 '판매 신청 제출' 유지. 전(프레임 I73:533;72:326;64:181 직접 덮어쓰기)과 같은 모양
- 이전 덮어쓰기(프레임 채움·이름·글자색 직접 수정)는 인스턴스 variant 선택으로 대체됨. 이제 버튼 색·모양 변경은 S6 submit-button(23:117)·register-button(181:65) 한 곳에서 하면 4개 화면에 따라옴(save-draft-button은 아직 프레임)
- 보고: 인스턴스 안 텍스트('판매 신청 제출')와 variant 선택, 이름은 S7 인스턴스에서 덮어쓴 값으로 남음

## 수정(사용자 요청, option 선택 행 외곽선 2px)
S7 직접 수정 없음, 조회만. 새 페이지·새 변수·새 색 없음. 판정 스크립트·스크린샷 미실행.
- register@seller 26:114의 26:234(main 23:54), register@non-seller 26:161의 26:254(main 23:84)는 컴포넌트를 따라 바뀜(덮어쓰기 없음). 선택 행 I26:234;23:55, I26:254;23:85 외곽선 2px INSIDE, 선 높이 69 → 71, color/accent 바인딩 그대로.
- visibility-selector 높이: 26:234 219 → 221, 26:254 144 → 146. field-visibility 26:134 245 → 247, 26:181 198 → 200 (seller 안 행 y: private 0 h71, member-only 79, sale-request 154 / non-seller private 0, member-only 79).
- content-area(66:143, 66:174) y99 h655 그대로(고정). 마지막 요소 field-visibility 끝 y(content-area 안): seller 635 → 637, non-seller 588 → 590. 화면 기준 seller 736, non-seller 689. content-area 하단 기준선(화면 y754, footer 시작)까지 seller 18, non-seller 65 여유라 겹침 없음.
- 프레임별 accent 노드 수: register@seller 26:114 = 2, register@non-seller 26:161 = 2 (변함없음).

## 수정(사용자 요청, register-button·submit-button enabled accent)
S7 직접 수정 없음, 조회만(컴포넌트를 따라 바뀜, 덮어쓰기 없음). 변경은 S6 181:62, 23:113 채움 color/ink → color/accent(VariableID:22:12).
- 따라온 노드: I73:509;72:326;181:66, I73:517;72:326;181:66(register-button, register@seller·non-seller footer), I73:533;72:326;181:68(submit-button, sale-request@checked footer). 모두 채움 accent 바인딩.
- 73:525(sale-request@unchecked, submit-button disabled)는 변경 없음, accent 0.
- 프레임별 accent 노드 수(채움·외곽선 노드 단위, 인스턴스 안 포함): home 36:49 = 2, skills 36:102 = 3, register@seller 26:114 = 3 (선택 행 외곽선 + 라디오 링 + register-button), register@non-seller 26:161 = 3, sale-request@unchecked 26:203 = 0, sale-request@checked 26:274 = 2 (체크박스 + submit-button).
- 상한(프레임당 2개 이하) 초과: skills 3, register@seller 3, register@non-seller 3. 되돌리지 않음, 처리는 별도 결정. 이전 기록의 register 2개 → 3개.

## 수정(사용자 요청, save-draft-button 컴포넌트화)
S7 직접 수정 없음, 조회만. S6 action-area 64:188 안 save-draft-button 프레임 64:178 → 인스턴스 186:42(main 186:40)로 바뀐 것이 footer type=action(73:509, 73:517)에 따라옴. 판정 스크립트·스크린샷 미실행.
- 따라온 노드: I73:509;72:326;186:42(register@seller), I73:517;72:326;186:42(register@non-seller). 변경 전 I73:509;72:326;64:178, I73:517;72:326;64:178은 폐기.
- 조회(모양 변화 없음): 두 인스턴스 모두 x16, 175×56, 흰 채움(color/canvas 22:5), hairline 1px(22:8 #e0e0e0), 반경 8, 글자 '임시저장' ink #141414, 덮어쓰기 없음. register-button I73:*;72:326;181:66 x199 175×56 그대로. footer 73:509·73:517 y754 h90 그대로(레이아웃 변화 없음).
- accent 노드 수: register@seller 3, register@non-seller 3, sale-request@checked 2, sale-request@unchecked 0 그대로. 새로 늘어난 것 없음(save-draft-button은 accent 미사용). 참고: 이번 조회 방식(채움·외곽선 accent 바인딩 노드 전수 집계)에서 home 3, skills 4로 나와 위 기록(2, 3)과 집계 방식이 다름. 이번 작업과 무관(home·skills는 건드리지 않음), 기준 확인 필요.

## 수정(사용자 요청, 홈 배경·프로필 캐릭터·진행 현황 이미지 적용)
S7 screen/home 36:49만 수정. S4(185:696 등)·S6·다른 화면은 수정 안 함. 참고 시안 185:696(home#B/#D)은 읽기만. 새 변수·새 색·새 페이지 없음(기존 tokens 변수 바인딩). 판정 스크립트 안 돌림.
- 배경: 36:49 채움 color/canvas #ffffff → color/canvas-soft(22:6) #f3f3f3. 시안 #fafafa는 허용 값 #f3f3f3으로 치환. status-bar 66:264, header 66:280 인스턴스 채움 흰색 → canvas-soft 바인딩(흰 띠가 배경 위에서 어색해 같은 배경으로 맞춤). footer 73:543은 투명 그대로, tab-bar 흰 배경+그림자 유지.
- 프로필: 185:857을 복제해 greeting 36:50 맨 왼쪽에 profile-character 189:24 (56×56 원형, 반경 28, visible=true 이미지 채움 1개만 남김, 선 1px color/hairline 22:8 #e0e0e0; 시안 선 #e5e5e5 → #e0e0e0 치환). greeting 36:50을 가로 auto layout(간격 12 spacing/12, 세로 가운데, 가로 FILL)으로 바꾸고, 인사말 36:51·미션 요약 36:52를 greeting-text 189:25(세로 gap 4, FILL)로 묶어 오른쪽에 배치. 36:51·36:52 텍스트 가로 FILL, 높이 HEIGHT 자동. greeting 높이 59 유지.
- 진행 현황 36:53(section/progress): 채움 #f3f3f3 → 없음, 패딩 16 → 0, 반경 0, gap 12 유지, 높이 317 → 374. 제목 36:54 유지. 기존 list 36:55와 list-row 인스턴스 36:56·36:62·36:68 삭제(list-row 컴포넌트는 안 건드림).
  - segment 189:731(358×52, 알약, 채움 color/field 22:7 #f0f0f0, 패딩 4): segment-item 4개 FILL×44(높이 44, 가로는 (358-8)/4=87.5, 시안 88과 0.5 차이), 문구 185:706~709에서 읽음: 전체(선택, ink 22:4 채움+canvas 흰 글자) / 작성중 2 / 제출 완료 1 / 검수 대기 1. 글자 type/label-md(13 SemiBold). 시안 항목은 컴포넌트 인스턴스(문구가 속성에 있음)였으나 외부 변수라 로컬 프레임으로 새로 만듦.
  - progress-group 189:740(흰 그룹, 채움 color/canvas 22:5, 선 1px color/field 22:7 #f0f0f0, 반경 radius/card 24, clip, 행 3개, 사이 divider-wrap 1px #f0f0f0 2개(185:719 복제)). 높이 274.
  - progress-row 3개(가로 gap 16·패딩 16, 세로 가운데): thumb 54×54 반경 16 + progress-info(세로 gap 8) = title(type/link 15 SemiBold) + meta-row(가로 gap 12: status-badge 인스턴스 185:714·185:724·185:734 복제 + updated type/body-sm 13 Regular #707070). 시안은 제목과 배지가 한 줄이었으나 배지 아이콘 때문에 254 폭을 넘어(182+12+76) 배지를 수정일 옆 줄로 내림. 문구: 업무 자동화 프롬프트 만들기 / 9월 28일 수정 / 작성 중, 회의록 정리 스킬 제출 / 9월 25일 수정 / 제출 완료, Figma 화면 정리 실습 / 9월 22일 수정 / 검수 대기. 진행 막대(progress-bar)는 사용자 요청에 없어 넣지 않음.
  - 이름: segment, segment-item, label, progress-group, progress-row, progress-info, meta-row, title, updated, divider-wrap, divider, thumb-placeholder, greeting-text, profile-character. 역할 단어(button·card·badge·input·toggle·tab·media) 신규 없음(status-badge는 기존 컴포넌트 인스턴스 이름).
- 이미지: 출처 Unsplash — Hands typing on a laptop with a spreadsheet on screen (https://unsplash.com/photos/hands-typing-on-a-laptop-with-a-spreadsheet-on-screen-iDqNlr1Y1_w ), 이미지 URL https://images.unsplash.com/photo-1759752393975-7ca7b302fcc6?fm=jpg&q=60&w=600&auto=format&fit=crop . 적용 실패: use_figma 안에서 figma.createImageAsync 호출 시 오류 `"createImageAsync" is not a supported API`, 대안 fetch는 `'fetch' is not defined`(바이트 확보 불가). 그래서 첫 행 썸네일도 자리표시자.
- 자리표시자 3개(요청은 2개 + 첫 행 폴백): thumb-placeholder 첫 행·둘째 행(회의록)·셋째 행(Figma), 채움 color/hairline 22:8 #e0e0e0, 반경 16, 54×54. 첫 행은 이미지 들어갈 자리(이름도 이미지 성공 시 thumb로 바꾸려 했으나 실패해 thumb-placeholder).
- 위치 변화: content-area 66:263 높이 712 → 769(HUG). 36:50 y16 h59, 36:53 y99 h374, 36:74 y497(전 440) h141 그대로, 36:86 y662(전 605) h75 그대로. footer 73:543 y746. 36:86 끝 화면 y836 → footer와 90 겹침(전 33), content-area 끝 화면 y868이 프레임 844을 24 넘음. 프레임 390×844 유지. 세로 스크롤·footer sticky 겹침 허용(사용자 결정).
- 색 목록(36:49 안 사용): #f3f3f3 #141414 #e0e0e0 #707070 #f0f0f0 #ffffff #0066ff #262626 + 이미지 채움(profile-character) 1개. 모두 허용 집합.
- accent: 탭 아이콘 I73:543;72:297;44:5 + 탭 라벨 I73:543;72:297;44:6 = 2(변경 없음, 이번 작업에서 늘리지 않음). 아이콘이 채움·선 둘 다 accent라 채움/선 단위로 세면 3.
- 보고(직전 기록 계속): (1) 36:86 list-row(summary)와 36:74 skill-card 중 36:86은 채움이 #f3f3f3이라 새 배경 #f3f3f3과 같아 박스 윤곽이 사라짐(지시대로 안 건드림, 필요하면 흰 배경 또는 hairline 결정 필요). skill-card 36:77은 흰 채움이라 구분됨. (2) 이미지 채움 실패로 첫 행 썸네일 자리표시자. (3) 세그먼트 항목은 시안 88 대신 87.5.

## 수정(사용자 수동, screen/home 직접 수정)
Figma는 수정하지 않고 읽기 전용으로 36:49 전체를 조회했다. 변경 전후 확정이 어려운 곳은 '조회 시점 현재 상태'로 적는다. 판정 스크립트·스크린샷 미실행. 조회 중 header가 바뀌었다(1 참고): 첫 조회에는 66:280과 191:1044가 둘 다 있었고, 이어진 조회에는 66:280이 없고 191:1044만 있었다(사용자 편집 중으로 보임, 추측).
1) 채움·바인딩(조회 시점 현재 상태)
- 프레임 36:49: #fafafa, 변수 color/canvas-faint VariableID:190:2 바인딩 확인. 390×844 반경 0.
- status-bar 66:264: #f3f3f3 color/canvas-soft(22:6) 바인딩, y0 h47. 직전과 같음.
- header: 66:280(#f3f3f3 canvas-soft)은 마지막 조회에서 사라졌다. 현재 header는 191:1044(인스턴스, y47 390×52, 채움 #ffffff color/canvas 22:5 바인딩). 직전의 canvas-soft에서 흰색으로 바뀜. status-bar #f3f3f3, header #ffffff, 프레임 #fafafa로 세 띠 색이 서로 다름. 66:280 ID는 더 안 쓴다.
- content-area 66:263: 채움 없음, x0 y99 390×705, 세로 auto layout gap 24, 패딩 16/16/16/32.
- footer 73:543: 채움 없음(투명), y746 h98(tab-bar 64 + home-indicator 34). 직전 기록 h90과 다름.
2) 구조
- greeting 36:50: x16 y16 358×59, 가로 gap12. profile-character 189:24 56×56 반경 28, 채움 IMAGE 1개(보임, FILL), 선 1px color/hairline #e0e0e0. greeting-text 189:25 x68 290×59 gap4: 인사말 36:51(24 Bold ink), 미션 요약 36:52(15 Regular #707070). 직전과 같음.
- section/progress 36:53: y99 358×310(직전 374), gap12, 채움 없음. 제목 36:54. segment 189:731은 HIDDEN(직전에는 보임), 그래서 높이가 줄고 progress-group 189:740이 y36에 위치. progress-group 358×274 흰(canvas) 채움, 1px #f0f0f0 선, 반경 24, 행 3개(각 356×90), divider 2개(color/hairline-soft 161:2 #f0f0f0).
- 행 3개: thumb 54×54는 모두 thumb-placeholder(189:742, 189:753, 189:764), 채움 #e0e0e0 color/hairline, 이미지 채움 없음(자리표시자). 반경 12(직전 기록 16). meta-row 안 순서는 updated(왼쪽) → status-badge(오른쪽). 배지: 작성 중 189:746 60×27, 제출 완료 189:757 71×27, 검수 대기 189:768 71×27. 문구 직전과 같음. 배지 순서가 직전과 다른지는 직전 기록이 모호해 확정 못 함.
- section/recommended-skills 36:74: y433(직전 497) 358×141, skill-card 3개 200×105 흰 채움 + 1px #f0f0f0, 반경 24. 위로 올라온 것은 36:53 높이 감소 때문.
- list-row 36:86(내 자산 요약): x16 y598(직전 662) 358×75 반경 16, 채움 #f3f3f3 color/canvas-soft 바인딩(직전과 같음, #fafafa 배경 위에서 윤곽은 구분됨). 글자 변화 없음. 끝 content-area 안 673, 화면 y772.
3) 색(36:49 안 전체)
- 사용 hex: #fafafa(프레임, 바인딩), #f3f3f3(status-bar·36:86, 바인딩), #141414, #ffffff(header·progress-group·skill-card·tab-bar·진행 배지), #e0e0e0, #707070, #f0f0f0, #0066ff(모두 바인딩), #262626(tab 자료·스킬·내 학습·내 자산의 선·라벨, 변수 바인딩 없음), 이미지 채움 1개(189:24). 그림자 1개: tab-bar rgba(20,20,20,0.10) y4 blur16.
- 변수에 묶이지 않은 직접 색: I73:543;72:297;44:10, 44:15, 44:20, 44:25(아이콘 선 #262626 w2), 44:11, 44:16, 44:21, 44:26(라벨 글자 #262626). 모두 tab-bar 인스턴스 안(S6 컴포넌트 값, 이번 수정과 무관해 보이나 확정 못 함).
- 허용 집합 밖 색: 없음.
- accent 노드: I73:543;72:297;44:5(홈 아이콘 shape, 채움·선) + I73:543;72:297;44:6(홈 라벨) = 2개.
4) 높이·겹침
- 프레임 844, content-area 705(y99~804, 직전 769). 프레임 안에 들어감.
- footer y746. content-area 끝 804와 58 겹침, 마지막 요소 36:86 끝 y772와 26 겹침(직전 90).
- 직전 대비 달라진 점: 배경 #f3f3f3 → #fafafa(canvas-faint 190:2), header canvas-soft → canvas 흰(66:280 → 191:1044), segment 숨김, 36:53 높이 374 → 310, thumb 반경 16 → 12, 36:74 y497 → 433, 36:86 y662 → 598, content-area 769 → 705, footer h90 → 98.
- 수정(사용자 요청, list-row summary 연한 블루 accent-soft): S7 노드 직접 수정 없음, 조회만. 홈 36:86(kind=summary 인스턴스)은 덮어쓰기 없이 컴포넌트 35:83을 따라 채움이 canvas-soft(#f3f3f3) → color/accent-soft(VariableID:194:7, #e6f0ff)로 바뀜. 글자·화살표·구조 그대로. sale-request 26:261, 26:276(kind=progress)은 canvas 22:5 바인딩 그대로 변경 없음. 홈 accent(#0066ff) 채움 노드 2개 그대로(변화 없음). 시안 #0066ff 10% → #e6f0ff 환산은 s6-tokens-components.md 참고. 홈 다른 부분 미수정.
- 규칙 밖 값 보고: 색은 없음. thumb 반경 12는 rules.json radius(media 0/16/24, card 24 등)에 없는 값으로 보임(189:742, 189:753, 189:764). profile-character 반경 28(원형)도 목록에 없는 값이라 판정에서 확인 필요. 변수 미바인딩 #262626(위 8개)도 확인 필요.

- 수정(사용자 요청, progress-row 컴포넌트화): screen/home 36:49의 progress-group 189:740 안 행 3개만 교체. 배경·status-bar·header·프로필·숨긴 segment 189:731·추천 스킬·내 자산 요약·divider-wrap 189:750·189:761·그룹 자체는 미수정. 새 컴포넌트는 S6 progress-row 197:52(s6-tokens-components.md 참고). 판정 스크립트·스크린샷 미실행.
  - 교체 전(되돌릴 때 참고, 폐기된 ID): 행 FRAME 189:741(thumb-placeholder 189:742, progress-info 189:743, title 189:744, meta-row 189:745, updated 189:749, status-badge 189:746 = 23:2 인스턴스 60×27 아이콘 없음) / 189:752(thumb-placeholder 189:753 + 숨긴 icon/file 191:1182·shape 191:1183·Group 191:1184, progress-info 189:754, title 189:755, meta-row 189:756, updated 189:760, status-badge 189:757 = 23:6 71×27 아이콘 없음) / 189:763(thumb-placeholder 189:764, progress-info 189:765, title 189:766, meta-row 189:767, updated 189:771, status-badge 189:768 = 23:8 71×27 아이콘 없음). 구조: 가로 gap16·패딩16, thumb 56×56 반경 16(조회 시 이미지 채움 있음, 첫 행은 숨김 이미지 채움 1개 + 보이는 이미지 1개), progress-info 세로 gap8 = title + meta-row(updated 왼쪽, status-badge 오른쪽). 각 행 356×90.
  - 교체 후: progress-row 인스턴스 197:382(작성 중) / 197:392(제출 완료) / 197:405(검수 대기). 모두 main 197:52, 가로 FILL, 356×90, 그룹 안 순서·x1 그대로. 내부: thumb I197:382;197:46 / I197:392;197:46 / I197:405;197:46, title I…;197:48, updated I…;197:50, status-badge I197:382;197:55 / I197:392;197:55 / I197:405;197:55.
  - 오버라이드: 제목·수정일 텍스트(업무 자동화 프롬프트 만들기 9월 28일 수정 / 회의록 정리 스킬 제출 9월 25일 수정 / Figma 화면 정리 실습 9월 22일 수정), 배지 variant 스왑(23:2 / 23:6 / 23:8 아이콘 icon/edit·icon/send·icon/clock 포함), 썸네일 이미지 채움(교체 전 thumb-placeholder의 fills를 그대로 복사, 첫 행은 숨김 채움까지 2개 복사).
  - 변화 수치: 배지 폭 60→76(작성 중), 71→87(제출 완료·검수 대기)(아이콘 12 + 간격 4). 배지 높이 27 그대로. meta-row 안 updated가 FILL이라 줄 바꿈 없음(updated 폭 180 → 164 안팎, 한 줄 20). 행 높이 90 그대로, progress-group 358×274 y100 그대로, section/progress 높이 변화 없음. 홈 다른 노드 y 변화 없음.
  - 이름: 새 노드 이름 thumb, progress-info, title, meta-row, updated(기존 이름 재사용 + thumb-placeholder → thumb), progress-row, status-badge(인스턴스). 역할 단어 신규 없음.
  - accent: 홈 2개 그대로(탭 아이콘 I73:543;72:297;44:5 + 탭 라벨 I73:543;72:297;44:6). 새 accent 없음.
  - 보고: (1) 요청서의 썸네일 54×54·반경 12·자리표시자는 조회 시점에 이미 56×56·반경 16·이미지 채움으로 바뀌어 있어(사용자 추가 편집으로 보임) 현재 값을 따름. 컴포넌트 thumb는 #e0e0e0 hairline 자리표시자, 반경 16, 56. (2) 규칙 반경 확인 필요: thumb 16은 rules.json radius에 있는 media 16과 같음(조회 기준, 판정 확인 필요).
