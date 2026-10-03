# R3. 규칙 (판정 스크립트가 세는 형태)

기준: docs/design.md (규범 절), R0 우선순위. 수치 원본은 `rules.json` (SSOT). 이 문서는 규칙 ID와 의미만 둔다.

## 판정 규칙
| ID | 항목 | 의미 |
|---|---|---|
| D01 | 프레임 크기 | 기준 프레임 크기와 일치 |
| D02 | 색 | 사용한 채움·선·글자색이 허용 hex 집합 안에 있음 (on-primary = #ffffff로 확정) |
| D03 | accent | 프레임당 사용 개수 상한, CTA에는 사용 금지 |
| D04 | 반경 | 요소 종류별 허용 반경 (버튼·배지·토글·탭 / 입력창·FAQ 행 / 카드 / 미디어 / 앱 아이콘) |
| D05 | 그림자 | 금지 (예외: segmented-control-active, tab-bar의 shadow/nav. 값은 rules.json shadow.tokens) |
| D06 | 그라디언트 | UI 요소에 금지 |
| D07 | 폰트 | 패밀리, 굵기, 크기가 허용 집합 안에 있음 |
| D08 | 자간·대문자 | 자간 0, 대문자 표기 금지 |
| D09 | 스페이싱 | gap·padding이 허용 단계 안에 있음, 화면 좌우 패딩 고정 |
| D10 | 터치 타깃 | 인터랙티브 요소 최소 높이 |
| D11 | 입력창 | 기본 상태 테두리 없음, 포커스 링만 허용 |
| D12 | 텍스트 대비 | 본문·캡션 최소 대비를 계산으로 검사 (placeholder 제외). 금지 조합은 rules.json `contrast.forbid` 참조 (#707070 on #f3f3f3·#f0f0f0, #adadad 본문) |

## 상태 표현 (7종)
- 작성 중, 임시저장, 제출 완료, 검수 대기, 수정 요청, 승인됨, 반려
- 배지 스타일은 rules.json의 `status_badges` 참조 (작성 중·임시저장은 흰 배경 + 점선 외곽선, D12 대비 충돌 해소)
- 공통: 텍스트 라벨 포함, accent 사용 금지, 형태 = pill, 글자 = label

## 신규 앱 컴포넌트 (S6에서 제작)
skill-card, list-row, status-badge, tab-bar, visibility-selector, file-attach-row, confirm-checkbox
- tab-bar: 플로팅 pill, 탭 5개 (홈, 자료, 스킬, 내 학습, 내 자산). 무료·유료 자료는 "자료" 탭 안 필터
- 공통 조건: D02, D04, D07, D09를 만족 (design.md에 없는 값 0개)

## 판정 제외 (S5에서 사람이 볼 참고 체크리스트)
- 갤러리 화이트 느낌 유지, 직관적 정보 구조, 실험실·자산 라이브러리 분위기, 사진 톤(그레이스케일 인물)

## 확인 메모
- D12를 4.5:1로 유지 (선택지 A). 스크립트 계산값: #707070 on #f3f3f3 = 4.46, on #f0f0f0 = 4.35, on #ffffff = 4.95, #adadad on #ffffff = 2.24
