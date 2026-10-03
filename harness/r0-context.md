# R0. 준비물 확인

## 기준 문서 (SSOT)
| 문서 | 역할 |
|---|---|
| docs/story-service.md | 서비스 맥락, 어기면 안 되는 것 2개 |
| docs/prd.md | 기능·범위 기준 (2026-09-26 MVP 범위 결정 포함) |
| docs/design.md | 시각 규칙 |
| docs/story-work.md | 사람이 하던 7단계, 게이트, 도구 경계 |

## 충돌 시 우선순위
story-service "어기면 안 되는 것" > prd (2026-09-26 범위 결정) > design.md > story-work.md

## design.md 처리 (문서는 수정하지 않음)
- 규범: Colors, Typography, Shapes, Do's and Don'ts
- 참고용: `ex-*` 예시 (그림자·색 반전·대문자·다크 모드 언급은 무시)
- 입력창(text-input) 높이: 한 줄 입력창은 상태(rest·focus)와 관계없이 56 고정 (사용자 결정, 2026-10-02 48→56, 문서 규칙. rules.json은 높이를 검사하지 않고 D10 터치 타깃 44 이상만 본다). design.md text-input 정의에 반영
- submit-button·action-area 높이: 56 (사용자 결정, 2026-10-02 48→56, text-input과 맞춤). 문서 규칙이며 rules.json은 높이를 검사하지 않는다. design.md button-primary에 반영
- 컬러 규칙 (사용자 결정, 2026-10-03): 초안(S1~S8)은 처음 지정한 컬러(rules.json colors·accent, accent는 CTA 금지·프레임당 2개)를 반드시 그대로 쓴다. 디자인이 완료된 뒤(S8 passed)에 컬러 변경이 필요하면 'S8 이후 컬러 변경' 절차(r2-stages.md)로만 바꾼다. 초안 단계에서 색 예외를 만들지 않는다
- 컬러 변경 1회차 (2026-10-03, S8 통과 후): accent 적용 3곳 후보 중 tab-bar 활성 필 아이콘·chip selected(채움 accent + 글자 #ffffff)를 적용한다. action-area 활성 버튼은 D03(CTA 금지) 때문에 보류, 규칙 변경 승인 대기. 프레임당 상한 2 유지
- chip은 컴포넌트로 만든다(S6, selected true/false). 이전 'S7 pill 프레임 조립'을 대체. 새 Figma 페이지는 만들지 않고 S6·S7에서 수정 후 게이트 재판정
- register-button·submit-button은 독립 컴포넌트로 둔다 (사용자 결정, 2026-10-03). action-area는 이 컴포넌트의 인스턴스를 쓰고, 버튼 수정·색 변경은 컴포넌트에서 하면 모든 화면에 따라온다. 색(accent) 적용은 D03(CTA 금지) 규칙 결정이 있을 때만 한다
- 배경 연한색 추가 (사용자 결정, 2026-10-03): #fafafa를 새 배경 색(canvas-faint)으로 추가한다. 기존 배경 #f3f3f3(canvas-soft)은 그대로 유지한다. design.md Surface에 반영, rules.json colors에 #fafafa 추가, Figma tokens에 color/canvas-faint 변수. 적용 위치는 사용자가 요청할 때 정한다
- 연한 파랑 추가 (사용자 결정, 2026-10-03): #e6f0ff를 accent-soft로 추가한다(시안 list-row 185:745의 #0066ff 10%와 같은 톤). list-row summary variant 채움에만 쓴다. design.md Surface, rules.json colors, Figma tokens color/accent-soft에 반영. accent 개수에는 세지 않는다
- footer는 sticky로 content 위 레이어에 놓이며, content-area 끝 요소가 footer와 겹쳐도 허용 (사용자 결정, 2026-10-03). 56 반영으로 늘어난 register·skills 넘침·겹침은 수정하지 않는다
- 입력창(text-input) 반경 예외: 8 (사용자 결정, design.md의 rounded.sm 16 대신). 목록 행·카드·FAQ 행은 16 그대로. 규칙은 rules.json radius.input
- 버튼 반경 예외: 8 (사용자 결정, 사각 라운드). 배지·탭·토글·tab-bar는 알약(9999) 그대로. design.md의 Shapes·Components·Do's를 이에 맞춰 수정했다(사용자 승인). 규칙은 rules.json radius.button
- 그림자 예외: segmented-control-active, 하단 tab-bar(shadow/nav 하나, 사용자 결정) 두 곳만 허용. design.md 본문은 수정하지 않고 rules.json이 예외를 정한다

## 알려진 문제 (미해결)
| # | 문제 | 처리 라운드 |
|---|---|---|
| 1 | 앱 컴포넌트 없음 (스킬 카드, 미션 카드, 목록 행, 파일 첨부, 검수 체크리스트, 하단 탭 바) | R3 |
| 2 | 상태 6종 표현 규칙 없음 (작성 중/제출 완료/검수 대기/수정 요청/승인됨/반려) | R3 |
| 3 | ex-* 예시가 규칙과 충돌 (ex-pricing-tier-featured, ex-modal-card, ex-toast, ex-data-table-cell) | 규칙으로 무시 처리 |
| 4 | 그림자 예외가 Don't에 없음 | 위 "그림자 예외"로 처리 |
| 5 | "모든 인터랙티브 요소 rounded.full" vs 입력창·FAQ 행 rounded.sm | R3 |
| 6 | 데스크톱 전제 서술 (4열 masonry, 3-up, Desktop nav) | MVP 범위 밖으로 처리 |
| 7 | text-faint(#adadad) 흰 배경 대비 약 2.2:1 (수기 계산) | R4에서 스크립트로 검증 |
| 8 | prd.md 14·15장에 피드백 언급 잔존 (MVP는 피드백 제외) | 범위 결정 우선 |

## 외부 도구
| 도구 | 상태 |
|---|---|
| uibowl MCP | 연결됨 |
| Figma | 기존 파일 `Design-harness` 사용, URL은 실행 시 기록. 연결 계정 mighty0411@gmail.com |
| Pretendard | 설치됨 (9개 굵기), Figma 데스크톱 앱 재시작 후 use_figma 에서도 로드 확인 |

## 1회 실행 단위
- 키스크린 2~3개 세트, 390×844 (story-work 4번)
- 이번 대상: 홈, 스킬 라이브러리, 내 자산(판매 신청)
- 경쟁사: 지정하면 사용, 미지정 시 uibowl 검색 상위 3개 자동 사용
