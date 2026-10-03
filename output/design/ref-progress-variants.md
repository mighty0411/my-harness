# 홈 진행 현황 비교 시안 (참고용)

Figma 파일: https://www.figma.com/design/CNelXB5JxSwpeJNurQRm3L/Design-harness
페이지: S4 Keyscreens (19:2). 새 페이지는 만들지 않음(지시 변경으로 S4에 배치, 빈 페이지 생성 없음).

비교용 프레임이다. 확정 프레임 목록(82:75, 82:164, 19:3)과 S4 덤프(G4 대상)에 넣지 않는다. 기존 노드와 다른 페이지는 수정하지 않았다.

복제 원본: S7 확정 상태 홈 36:49 (S4 홈 82:75 아님). 원본은 그대로.
기존 82:75가 #A. 시안 A 내용이 `screen/home#B`, 시안 B 내용이 `screen/home#C`.

- frame: 153:166 | screen/home#B (시안 A 단계 진행 바 카드, x 3090 y 0, 390×844). 라벨 153:331 `proposal-label/home#B` (y -60)
- frame: 153:252 | screen/home#C (시안 B 상태 요약 칩 + 컴팩트 행, x 3520 y 0, 390×844). 라벨 153:334 `proposal-label/home#C` (y -60)

배치: S4 페이지 가장 오른쪽 끝(proposal/tab-bar-shadow-y0, 끝 3050)에서 간격 40.

## 공통
- 복제본에서 section/progress(153:173 / 153:259)만 변경. status-bar, header, 인사말, section/recommended-skills, 내 자산 요약 list-row, footer nav(투명)는 원본과 동일.
- section/progress: 채움·패딩·반경 제거(canvas-soft 카드 → 투명, 패딩 spacing/0, radius/none, 자식 간격 spacing/12). 제목 '진행 현황'(type/heading-4) 그대로 유지.
- 홈 content-area는 HUG·clip 해제, 프레임 390×844 유지.
- status-badge는 S6 컴포넌트 23:19의 variant 인스턴스(작성 중 23:2, 제출 완료 23:6)를 createInstance로 생성. 크기 변경 없음(76×27, 87×27, 76×27).
- 행 문구는 원본 그대로: 업무 자동화 프롬프트 만들기 / 9월 28일 수정 / 작성 중, 회의록 정리 스킬 제출 / 9월 25일 수정 / 제출 완료, Figma 화면 정리 실습 / 9월 22일 수정 / 작성 중.

## 시안 A (screen/home#B, 153:166)
(2차 수정으로 아래 '구성'·'progress-card'·'step-guide'·'섹션 높이'·'홈 하단 겹침'은 "2차 수정" 블록과 그 끝 "3차 수정"이 최종이다. 2차 안의 구분선(좌우 끝)·행 높이·섹션 높이·겹침 값은 3차가 덮어쓴다.)
구성: section/progress 153:173 > 제목 + card-list(세로 간격 12) > progress-card 3개(153:210, 153:224, 153:238).
- progress-card: 세로 auto layout 패딩 16, 간격 8, 채움 color/canvas, 외곽선 color/field 1px INSIDE, radius/card 24. 높이 126.
  - card-head(가로, 가운데 정렬, 간격 12): title(type/link, color/ink, FILL) + status-badge 인스턴스(153:213, 153:227, 153:241)
  - updated(type/body-sm, color/text-muted)
  - step-bar(가로 간격 4): step 4칸, 높이 4, 폭 FILL. 현재 단계까지 color/ink 채움(작성 중 1칸, 제출 완료 2칸), 나머지 color/hairline(#e0e0e0). 칸 이름 `step/작성[filled]` 등
  - (수정) 카드 안 step-caption 삭제. 카드 간격 8 유지, 카드 높이 126 → 101 (caption 17 + 간격 8 감소). 카드 3개 모두 동일.
- 안내 줄 `step-guide` 156:11 신규: section/progress 안, 제목 '진행 현황' 바로 아래·card-list 위에 한 번만. 문구 '작성 → 제출 → 검수 → 승인', type/caption(12 Regular), color/text-muted(22:10), 폭 FILL, 높이 17. 제목·안내·카드 사이 간격은 section 자식 간격 12.
- 섹션 높이: 392 (438 → 392, 원본 317 대비 +75). 계산: 제목 24 + 12 + 안내 17 + 12 + 카드 101×3 + 12×2 = 392.
- 홈 하단 겹침: recommended-skills y 515(content-area 기준, 이전 561), 요약 list-row y 680 h75, 끝 y 755 → 화면 y 854. footer(y746) 대비 겹침 154 → 108, 프레임 하단(844)을 넘는 양 56 → 10. 원본(겹침 33)보다 +75. content-area 높이 787(이전 833).

### 시안 A 2차 수정 (사용자 지시, 최종)
- 구성: section/progress 153:173 > 제목 153:174 + 바깥 카드 `progress-card-group`(153:209, 구 card-list) > 행 `progress-row` 3개(153:210, 153:224, 153:238). step-guide 156:11 삭제(안내 줄 없음). 제목-카드 간격 section 자식 간격 spacing/12 유지.
- 바깥 카드: 세로 auto layout, 패딩 0·간격 0, 채움 color/canvas, 외곽선 color/field 1px INSIDE, radius/card 24(변수 바인딩), 내용 clip. 358×301.
- 행: 기존 카드별 채움·외곽선·반경 제거(채움 없음, 반경 spacing/0 바인딩 0). 패딩 상하·좌우 16, 내부 간격(8, 헤더 12, 단계 바 4) 기존 그대로. 행 높이 99~100(가장 작은 행 99), 터치 영역 44 이상.
- 구분선: 행 1·2의 아래쪽 외곽선만 1px color/hairline(22:8) 바인딩, 행 3에는 없음(행 사이 2곳, 첫 행 위·마지막 행 아래 없음).
- 구분선 선택: 좌우 끝까지 닿게(inset 없음). 이유: 시안 C compact-list 구분선이 패딩 0 목록 폭 전체에 닿는 선례와 같고, 바깥 카드 안에서 행이 카드 폭을 꽉 채워 구분이 명확하다.
- 세 번째 행(Figma 화면 정리 실습, 제목·수정일 유지): 배지를 status-badge '검수 대기' variant 23:8 인스턴스(153:241, swapComponent, 87×27)로 교체. 단계 바 4칸 중 3칸 color/ink 채움(step/작성[filled] 153:247, step/제출[filled] 153:248, step/검수[filled] 153:249), 승인 153:250은 hairline. 첫째(1칸)·둘째(2칸) 행 그대로.
- 섹션 높이: 392 → 337 (제목 24 + 12 + 바깥 카드 301). 원본 317 대비 +20.
- 홈 하단 겹침: recommended-skills y 460, 요약 list-row y 625 h75(content-area 기준) 끝 y 700 → 화면 y 799. footer(y746) 대비 겹침 108 → 53, 프레임 하단 844을 넘지 않음(이전 10 넘음). content-area 높이 732 HUG(이전 787), 프레임 390×844 유지.
- 글자 전부 type/* 스타일 유지, 새 hex·그림자 없음, 모든 색 변수 바인딩.
- 수정일 글자 축소(사용자 지시): 행 3개의 updated(153:217, 153:231, 153:245)를 type/body-sm(13 Regular) → type/caption(12 Regular, 줄 높이 140%) 스타일로 교체(직접 지정 아님). 색 text-muted 유지, 문구·간격·구분선 그대로. 글자 높이 20 → 17.
  - 행 높이: 100/100/99 → 97/97/96
  - 바깥 카드 301 → 292, 섹션 높이 337 → 328
  - 홈 하단 겹침: 53 → 44 (recommended-skills y 460 → 451, list-row y 625 → 616, 끝 화면 y 799 → 790, footer y746). content-area 높이 732 → 723 HUG, 프레임 390×844 유지. 행 높이 96 이상으로 터치 영역 44 이상.

#### 3차 수정 (사용자 지시, 구분선 인셋·배지 아이콘 숨김·한 줄 진행바) — 최종
- 그룹 구조: progress-card-group 153:209 자식 = progress-row 153:210 · divider-wrap 159:20 · progress-row 153:224 · divider-wrap 159:22 · progress-row 153:238. 행 아래 외곽선 구분선은 제거(행 stroke 없음).
- 구분선: divider-wrap(가로 auto layout, 좌우 패딩 spacing/16·상하 spacing/0 변수, 폭 FILL, 높이 1) 안 divider(FILL 폭, 높이 1, 채움 color/hairline 바인딩) (각 divider-wrap의 첫 자식). 좌우 16 인셋이라 선 폭은 324(그룹 안쪽 폭 356에서 32 뺀 값)이고 글자 시작 x(17)부터 배지 우측 끝까지와 같다. 지시의 326은 외곽선 1px을 안쪽 폭 계산에서 빼지 않은 값이라 실제는 324. 두께 1px 유지.
- 배지 아이콘 숨김(visible=false, 이 프레임 인스턴스 안쪽만, 컴포넌트 원본 23:19 미수정): I153:213;123:408(icon/edit), I153:227;123:412(icon/send), I153:241;123:414(icon/clock). 배지 높이 27 유지. 너비 전→후: 작성 중 76 → 60, 제출 완료 87 → 71, 검수 대기 87 → 71.
- 진행바: 기존 step-bar(4칸) 3개 삭제. 행 안 card-head 아래에 meta-row(가로, SPACE_BETWEEN, 세로 가운데, 간격 12, 폭 FILL, 높이 17) 신규: 왼쪽 updated 날짜(type/caption 유지), 오른쪽 끝 progress-bar. progress-bar[25%] / [50%] / [75%] = 트랙 120×4 FIXED(채움 color/hairline, radius/badge 9999 바인딩, clip) + 안쪽 progress-fill(채움 color/ink 바인딩, radius/badge 바인딩) 폭 30 / 60 / 90 (작성 중 25%, 제출 완료 50%, 검수 대기 75%). 행 순서대로 153:210, 153:224, 153:238 안.
- 행 높이: 97/97/96 → 84/84/84 (단계 바 4 + 간격 8이 날짜 줄과 합쳐져 12 줄고 새 날짜 줄 17 안에 포함, 행 모두 84). 바깥 카드 292 → 256. 터치 영역 44 이상.
- 섹션 높이: 328 → 292.
- 홈 하단 겹침: 44 → 8 (recommended-skills y 451 → 415, list-row y 616 → 580, 끝 화면 y 790 → 754, footer y746). content-area 높이 723 → 687 HUG, 프레임 390×844 유지.
- 새 hex·그림자 없음, 글자는 type/* 유지, 색 모두 변수 바인딩.

#### 4차 수정 (사용자 지시, 진행바 240·채움 accent) — 최종
- 트랙 폭 120 → 240 FIXED(3행 모두), 높이 4·트랙 color/hairline·radius/badge 그대로. 채움(progress-fill) 폭: 작성 중 25% = 60, 제출 완료 50% = 120, 검수 대기 75% = 180 (이전 30/60/90).
- 채움 색: tokens에 color/accent(VariableID:22:12, #0066ff)가 있어 새로 만들지 않고 이 변수에 바인딩(직접 hex 아님). 조회된 색 변수 전체: color/ink 22:4, canvas 22:5, canvas-soft 22:6, field 22:7, hairline 22:8, ink-soft 22:9, text-muted 22:10, text-faint 22:11, accent 22:12(#0066ff), badge-overlay 22:13.
- 한 줄 수용 확인: meta-row 내용 폭 324. 날짜 글자 폭 70(행 1·2, '9월 28일 수정'·'9월 25일 수정'), 69(행 3) + 바 240 = 310·309, 남는 간격 14·14·15. 줄 깨짐·겹침 없음, 폭을 줄이지 않았다. 간격 14·15는 SPACE_BETWEEN이 남는 폭을 나눈 값이라 spacing 변수 단계(12·16)와 정확히 일치하지는 않으나 최소 간격(itemSpacing 12) 이상이다. 행 높이 84, 섹션 292, 홈 하단 겹침 8 변화 없음.
- 규칙 주의: harness/rules.json accent는 max_per_frame 2, cta 0이고, design.md는 #0066ff를 상업적 강조 용도로만 쓰도록 한정한다. 이번 시안은 채움 3개가 #0066ff라 프레임당 3개로 상한 2를 넘는다(비교용 프레임이라 judge 대상 아님, 채택 시 규칙 충돌).

#### 5차 수정 (사용자 지시, 구분선 약한 색·제목 줄 간격 16) — 최종
- 구분선 색: divider 159:21·159:23 채움을 color/hairline(#e0e0e0, 22:8) → 새 변수 color/hairline-soft(#f0f0f0, VariableID:161:2) 바인딩. 이 변수는 design.md Colors에 정의돼 있었으나 Figma tokens에 없던 것을 S6에서 추가(s6-tokens-components.md 참고). 두께 1px·좌우 16 인셋 324 그대로.
- 행 간격: progress-row 3개(153:210, 153:224, 153:238)의 auto layout itemSpacing 8 → 16, spacing/16(22:25) 변수 바인딩. card-head와 meta-row 사이 세로 간격이다(행 자식은 두 개뿐).
- 높이 전→후: 행 84/84/84 → 92/92/92, 바깥 카드 256 → 280(행 92×3 + 구분선 1×2 + 외곽선 2), 섹션 292 → 316, 홈 하단 겹침 8 → 32(list-row y 580 → 604, 끝 화면 y 754 → 778, footer y746), content-area 687 → 711 HUG, 프레임 390×844 유지, 터치 영역 44 이상.
- 주의: 그림이 오래된 값을 돌려준 적이 있어 수치는 Plugin API와 get_metadata(153:224: 행 y94 h92, meta-row y59)를 다시 조회해 확인했다(get_metadata가 한 번은 수정 전 값 84를 반환했으나 재조회에서 92로 일치).

## 시안 B (screen/home#C, 153:252)
구성: section/progress 153:259 > 제목 + summary-chips + compact-list.
- summary-chips(가로 간격 8): chip 2개, 높이 44, 좌우 패딩 16, radius/tab 9999, 글자 type/label-md.
  - `chip/작성 중[selected]` 153:296 '작성 중 2' (80×44): 채움 color/ink, 글자 color/canvas
  - `chip/제출 완료` 153:298 '제출 완료 1' (92×44): 채움 color/canvas, 외곽선 color/field 1px, 글자 color/ink
- compact-list(세로 간격 0): compact-row 3개(153:301, 153:311, 153:321), 높이 56 고정, 가로 간격 12, 세로 가운데. 카드 없음, 패딩 0.
  - 행 사이 구분선 1px color/hairline(#e0e0e0): 1·2행 아래쪽 외곽선만(3행 없음)
  - icon/file(S6 icon/file 127:5 복제, 20×20, 선 color/ink-soft) 153:302, 153:312, 153:322
  - row-info(세로, FILL): title(type/link, color/ink), updated(type/body-sm, color/text-muted)
  - status-badge 인스턴스(153:307, 153:317, 153:327)
- 섹션 높이: 260 (원본 317, -57). 계산: 제목 24 + 12 + 칩 44 + 12 + 행 56×3 + ... = 260.
- 홈 하단 겹침: recommended-skills y 383(원본 440), 요약 list-row y 548 h75, 끝 y 623 → 화면 y 722. footer(y746) 위 24 여유, 겹침 없음(원본 겹침 33 해소). content-area 높이 655.

## 사용한 변수·컴포넌트·스타일
- 컴포넌트: status-badge 23:19(variant 23:2, 23:6), icon/file 127:5 복제(시안 B), 복제 원본 홈 36:49 안 status-bar·header·list-row·skill-card·footer 인스턴스(그대로)
- 색 변수: color/ink 22:4, color/canvas 22:5, color/field 22:7, color/hairline 22:8, color/text-muted 22:10 (모든 채움·외곽선·글자 바인딩, 새 hex 없음)
- 반경 변수: radius/card 22:19, radius/tab 22:17, radius/none 22:20
- 간격 변수: spacing/0 22:21, /4 22:22, /8 22:23, /12 22:24, /16 22:25 (좌우 화면 패딩 16은 content-area 그대로)
- 텍스트 스타일: type/heading-4, type/link, type/body-sm, type/caption, type/label-md. 새로 만든 글자 전부 스타일 적용(스타일 없는 글자 0). 폰트 Pretendard Regular·SemiBold·Bold만
- 그림자·그라디언트·accent 사용 0

## 메모
- 지시의 'field 색 #e0e0e0 변수'는 변수 값이 맞지 않는다: color/field는 #f0f0f0, #e0e0e0은 color/hairline. 단계 바 미채움 칸과 행 구분선은 #e0e0e0(hairline), 카드·칩 외곽선은 지시대로 color/field(#f0f0f0, skill-card와 동일)를 썼다. 칩 외곽선이 연해 보이면 hairline으로 바꾸는 것을 사용자 결정에 맡긴다.
- 터치 영역: 칩 높이 44, 행 56, 카드 126(모두 44 이상).
- 스크린샷 URL(단기 유효): 153:166 https://www.figma.com/api/mcp/asset/779c62e4-1352-4730-a363-a3edf25317cb.png / 153:252 https://www.figma.com/api/mcp/asset/a03d0351-83cb-43dc-b032-cfd14c1b9f30.png. 이미지를 열 수단이 없어 육안 확인은 못 했고 노드 수치로 확인
- 판정 스크립트·덤프는 건드리지 않음
