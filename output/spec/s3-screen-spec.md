# S3 화면 설계

기준: docs/prd.md 5절·6-5절, docs/story-service.md, output/research/s2-analysis.md (반영 포인트 P-001~P-020), harness/rules.json.
컴포넌트 이름은 skill-card, list-row, status-badge, tab-bar, visibility-selector, file-attach-row, confirm-checkbox와 기존 submit-button, text-input, 그리고 공통 UI 컴포넌트 status-bar, header, header-left, header-right, content-area, action-area, home-indicator, footer만 쓴다. 그 밖의 요소(칩, 카드 영역 등)는 기존 컴포넌트의 조합으로 설명한다. 공통 UI 이름에는 button, card, badge, input, toggle, tab 같은 역할 단어를 새로 넣지 않는다 (tab-bar는 기존 이름이라 예외). 화면 크기는 390×844, 좌우 패딩 16.
상태 표기는 [selected], [disabled], [focus]를 쓴다.
수정 이력: 사람의 수정 요청(공통 UI 2차, 1~6번)에 따라 header를 배경 없는 버튼과 Hug 높이 52로, content-area를 좌우 16·상단 16·하단 32로, 필드 간 세로 간격을 24로 통일했다. action-area는 버튼 2개를 좌우 배치(간격 8, 상하 여백 0)로, home-indicator는 영역 390×34 컴포넌트로 바꿨고, tab-bar + home-indicator, action-area + home-indicator를 footer로 묶었다.
수정 이력 (추가): 사람 결정으로 홈 진행 현황 영역의 list-row 행 사이를 24에서 12로 바꿨다. Figma 홈 화면에서 list-row가 상하 여백 16으로 높이 66이 되었기 때문이다. 섹션 간 24, 내 자산 목록, skill-card 등 다른 간격은 그대로다.
수정 이력 (추가): 입력창 포커스 링 2px → 1px, 사람 결정.

## 공통 UI

세 화면(홈, 스킬 라이브러리, 내 자산)과 내 자산의 등록·판매 신청 프레임 전부에 적용하는 화면 골격이다. 위에서 아래로 status-bar, header, content-area, footer 순서로 쌓인다. 영역의 y 범위는 겹치지 않고, footer는 content-area 밖 하단 영역이라 콘텐츠와 겹치지 않는다.

### 구성 요소
화면 골격 (세로, 기준 프레임 390×844 유지. rules.json frame, D01).

영역별 y 범위 (홈, 스킬 라이브러리)
| 순서 | 영역 | 컴포넌트 | y 범위 | 높이 |
|---|---|---|---|---|
| 1 | 상태 표시줄 | status-bar | 0~47 | 47 |
| 2 | 타이틀 영역 | header | 47~99 | 52 (Hug) |
| 3 | 콘텐츠 영역 | content-area | 99~746 | 647 |
| 4 | 하단 묶음 | footer (tab-bar 746~810 + home-indicator 810~844) | 746~844 | 98 |

영역별 y 범위 (내 자산 등록, 판매 신청)
| 순서 | 영역 | 컴포넌트 | y 범위 | 높이 |
|---|---|---|---|---|
| 1 | 상태 표시줄 | status-bar | 0~47 | 47 |
| 2 | 타이틀 영역 | header | 47~99 | 52 (Hug) |
| 3 | 콘텐츠 영역 | content-area | 99~762 | 663 |
| 4 | 하단 묶음 | footer (action-area 762~810 + home-indicator 810~844) | 762~844 | 82 |

영역별 y 범위 (내 자산 목록: action-area와 tab-bar가 함께 있다. 프레임은 없어도 문서에는 둔다)
| 순서 | 영역 | 컴포넌트 | y 범위 | 높이 |
|---|---|---|---|---|
| 1 | 상태 표시줄 | status-bar | 0~47 | 47 |
| 2 | 타이틀 영역 | header | 47~99 | 52 (Hug) |
| 3 | 콘텐츠 영역 | content-area | 99~698 | 599 |
| 4 | 하단 묶음 | footer (action-area 698~746 + tab-bar 746~810 + home-indicator 810~844) | 698~844 | 146 |

- 합계 검산: 홈·스킬 47+52+647+98=844. 등록·판매 신청 47+52+663+82=844. 목록 47+52+599+146=844
- footer 높이 검산: 내비 footer 64+34=98. 액션 footer 48+34=82. 목록 footer 48+64+34=146
- status-bar, footer 안 영역의 높이는 고정값이다. header는 Hug(내용에 맞춤)다. 안의 요소는 패딩 없이 가운데 정렬하거나 허용 단계(0, 4, 8, 12, 16, 24, 32, 48, 64)의 패딩만 쓴다

status-bar (iPhone 12 스타일, 독립 영역)
- 폭 390, 높이 47 (iPhone 12 상태 표시줄 높이). 배경 #ffffff. content-area와 분리된 독립 영역이며 콘텐츠가 이 안에 들어오지 않는다
- 중앙: 노치. 상단 중앙에 붙은 #141414 도형, 폭 약 209, 높이 약 30, 위쪽 모서리는 직각으로 화면 위 끝에 붙고 아래 두 모서리만 둥글다. 다이내믹 아일랜드 알약은 쓰지 않는다
- 좌측: 시간 (예: 9:41). 좌측 여백 16. 노치 왼쪽 빈 자리(x 16~90)에 세로 가운데 정렬
- 우측: 신호, 와이파이, 배터리 아이콘. 색 #141414, 우측 여백 16. 노치 오른쪽 빈 자리(x 300~374)에 세로 가운데 정렬
- 시간 글자는 Pretendard SemiBold, 15, 색 #141414만 쓴다 (D07)
- 그림자와 그라디언트는 쓰지 않는다

header (공통 컴포넌트, 타이틀 영역)
- 폭 390, 높이는 Hug(고정값 없음), 배경 #ffffff. 버튼 높이 44 + 위 패딩 4 + 아래 패딩 4 = 52. status-bar 아래(y 47)에서 시작해 y 99에서 끝난다. content-area와 분리되고 content-area 요소는 header 안에 들어오지 않는다
- 타이틀: 가로 중앙 정렬 (화면 가운데 x 195). Pretendard SemiBold 17, #141414. 화면 이름을 쓴다
- 양쪽에 버튼을 둔다. 좌측 header-left (x 16~60), 우측 header-right (x 330~374). 좌우 여백 16
- header-left, header-right: 배경 채움 없음(투명). 아이콘 24×24, #141414만 보인다. 터치 대상은 44×44 투명 영역이다 (D10). 버튼 위아래 패딩 4
- 이름 규칙: 판정 도구가 역할을 오인식하지 않도록 이름에 button이라는 단어를 넣지 않는다. 높이 44 이상은 header-left, header-right가 같은 규칙으로 지킨다
- 화면별 타이틀과 버튼
  | 화면 | 타이틀 | header-left | header-right |
  |---|---|---|---|
  | 홈 | 홈 | 메뉴 | 알림 |
  | 스킬 라이브러리 | 스킬 라이브러리 | 메뉴 | 알림 |
  | 내 자산 목록 | 내 자산 | 메뉴 | 알림 |
  | 내 자산 등록 | 자산 등록 | 뒤로 | 더보기 |
  | 판매 신청 | 판매 신청 | 뒤로 | 더보기 |
- 그림자와 그라디언트는 쓰지 않는다

content-area (콘텐츠 영역)
- header 바로 아래(y 99)에서 시작한다. 좌우 여백 16 (rules.json spacing.screen_side_padding), 상단 여백 16 (첫 요소 y 115), 하단 여백 32
- 하단 여백 32의 의미: 스크롤 콘텐츠의 마지막 요소 아래에 32의 여백을 둔다. 끝까지 스크롤했을 때 마지막 요소와 footer 위 끝 사이가 32 떨어진다
- 영역 안에서 세로로 스크롤하고 영역 밖으로 나온 콘텐츠는 잘린다 (clip). header와 footer 안으로 콘텐츠가 들어가지 않는다
- 아래 끝은 footer의 위 끝에서 끝난다. 겹치지 않는다
- 세로 간격 규칙: 같은 영역 안에서 세로로 쌓이는 field와 field, 섹션, 목록 항목 사이는 24 (rules.json spacing.steps). 단, 홈 진행 현황 영역의 list-row 행 사이만 12다. 한 field 안 라벨과 입력창 사이는 8

action-area (액션 영역, footer 안)
- 폭 390, 배경 #ffffff. 좌우 여백 16, 위아래 패딩 0 (상하 여백 없음). 높이 = 버튼 높이 48
- 버튼 1개: 폭 358 (390에서 양쪽 여백 16씩), 높이 48, 반경 9999 (D04)
- 버튼 2개: 좌우로 나란히 놓는다. 버튼 사이 간격 8, 각 버튼 폭 175 (=(358−8)/2), 높이 48, 반경 9999. 좌측 임시저장(보조, x 16~191), 우측 등록(주, x 199~374)
- 대상 화면: 내 자산 등록 (임시저장, 등록), 판매 신청 (제출), 내 자산 목록 (새 자산 등록). 홈, 스킬 라이브러리는 action-area가 없다
- 스크롤해도 제자리에 고정된다

tab-bar (footer 안)
- 콘텐츠 안이 아니라 footer 안에 있다. 폭 358 (가로 풀사이즈 390에서 양쪽 여백 16만 적용), x 16, 높이 64. 채움 #f3f3f3, 반경 9999 (D04), 그림자 없음. tab-bar 바깥 양옆 16은 #ffffff
- 탭 5개 고정 (홈, 자료, 스킬, 내 학습, 내 자산). 각 탭은 위에 아이콘, 아래에 라벨
- 활성 탭: icon-holder 배경(검정 알약)을 없앤다. 아이콘 내부를 #141414로 채운 채움 글리프와 #141414 SemiBold 라벨 (12)로 표시
- 비활성 탭: 채움 없는 선 아이콘(#262626)과 #262626 라벨 (12, Regular). #f3f3f3 위 대비 4.5 이상을 만족한다
- 각 탭의 터치 대상 높이 44 이상
- tab-bar는 홈, 스킬 라이브러리, 내 자산 목록 화면에 있다. 내 자산의 등록·판매 신청 프레임에는 없다

home-indicator (컴포넌트)
- 영역: 가로 풀사이즈 390, 세로 34, 배경 #ffffff. 영역 안 검은 바는 폭 134, 높이 5, 색 #141414, 반경 9999 (크기 유지)
- 검은 바 위치: 가로 중앙 (x 128~262), 영역 하단에서 8 위. 영역 안 y 21~26, 화면 기준 y 831~836 (영역 y 810~844)
- 모든 화면에 표시한다. footer 안에서 tab-bar 또는 action-area 아래 맨 끝에 온다. 다른 영역과 겹치지 않는다

footer (컴포넌트 그룹, 콘텐츠 영역 밖 하단)
- 세로로 묶은 그룹이다. 폭 390, 배경 #ffffff. 이름은 `footer`다. content-area와 겹치지 않고 스크롤해도 고정된다
- 내비 footer (홈, 스킬 라이브러리): tab-bar (358×64, x 16, y 746~810) + home-indicator (390×34, y 810~844). 높이 98 (y 746~844)
- 액션 footer (내 자산 등록, 판매 신청): action-area (390×48, 버튼 좌우 여백 16, y 762~810) + home-indicator (390×34, y 810~844). 높이 82 (y 762~844)
- 목록 footer (내 자산 목록): action-area (y 698~746) + tab-bar (y 746~810) + home-indicator (y 810~844). 높이 146 (y 698~844). 위에서 아래로 action-area, tab-bar, home-indicator 순서

### 상태
- 기본: status-bar, header, footer가 모든 화면에 항상 표시된다. 스크롤해도 status-bar, header, footer(tab-bar, action-area, home-indicator)는 제자리에 고정되고 content-area만 스크롤한다
- tab-bar 활성 탭: 현재 화면의 탭 하나만 채움 글리프 + SemiBold 라벨. 나머지는 선 아이콘 + Regular 라벨. 두 상태 모두 아이콘 배경 알약은 없다
- 화면별 활성 탭: 홈 = 홈, 스킬 라이브러리 = 스킬, 내 자산 목록 = 내 자산
- 내 자산 등록·판매 신청 프레임: tab-bar 없음, 액션 footer (action-area + home-indicator)
- 불러오는 중: status-bar, header, footer는 그대로 표시한다
- 결정 사항 (사람 확인 필요)
  - 결정: header 높이는 고정값이 아니라 Hug다. 44×44 터치 대상 + 위아래 패딩 4 = 52 (y 47~99). 이전 고정 48에서 4 늘었고, 그만큼 content-area 시작이 y 95에서 99로 내려갔다
  - 결정: header-left, header-right의 #f3f3f3 원형 채움은 없앤다. 아이콘 24×24 #141414만 보이고 터치 대상 44×44는 투명 영역으로 유지한다 (D10)
  - 결정: content-area 하단 32는 스크롤 콘텐츠 마지막 요소 아래의 여백이다. 영역 자체의 높이는 footer 위 끝까지이며 하단 32는 영역 안 패딩으로 본다
  - 결정: 필드 간 24 적용 범위는 같은 영역 안에서 세로로 쌓이는 field, 섹션, 목록 항목(skill-card, list-row 행 사이 포함) 사이다. 한 field 안 라벨과 입력창은 8 유지. 섞여 있던 16/24는 24로 통일했다. 예외: 홈 진행 현황 영역의 list-row 행 사이만 12다 (사람 결정: Figma 홈 화면에서 list-row가 상하 여백 16으로 높이 66이 되어 12로 확정, 12는 spacing.steps 안의 값). 홈의 섹션 간 24와 내 자산 목록 등 다른 간격은 24 그대로다
  - 결정: tab-bar는 지금도 폭 358, x 16이라 치수 변경은 없다. "가로 풀사이즈에서 양쪽 여백 16만"은 footer 폭이 390이고 tab-bar가 양옆 16만 띄운 '떠 있는 알약' 형태라는 뜻으로 해석했다 (알약 규칙, 반경 9999 유지). 높이 64 유지
  - 가정: action-area 버튼 2개의 순서는 좌 임시저장(보조), 우 등록(주)이다 (이전 세로 쌓기의 위 등록·아래 임시저장과 다르다). 각 폭 175, 높이 48, 간격 8, 위아래 패딩 0이라 action-area 높이는 48이다
  - 가정: 위아래 패딩 0 때문에 action-area는 tab-bar, home-indicator와 붙는다. 세로 여백은 home-indicator 영역(34)이 만든다
  - 결정: footer 높이는 내비 98, 액션 82, 목록 146이다. 옛 footer(높이 88, 이전 요청에서 폐기)와 달리 이번 footer는 tab-bar 또는 action-area를 home-indicator와 묶은 그룹이며 사람이 요청한 구조다
  - 결정: footer 이름은 역할 단어 없이 `footer`만 쓴다
  - 결정: home-indicator 컴포넌트는 영역 390×34이고 검은 바는 134×5 그대로다. 바 위치만 영역 하단에서 8 위(화면 y 831~836)다. 이전 영역 24(y 820~844)에서 34로 바뀌었다
  - 결정: status-bar 높이는 47이다 (iPhone 12). 47은 rules.json spacing.steps에 없지만 spacing.steps와 D09는 gap·padding이 대상이고 영역 고정 높이는 대상이 아니라고 판단했다. status-bar 안은 padding 없이 가운데 정렬로 만든다. 판정 도구가 영역 높이에도 단계를 적용하면 걸릴 수 있어 사람 확인이 필요하다. 틀리면 48로 바꾸고 나머지 y를 1씩 조정한다
  - 결정: 노치 도형은 #141414 (순수 검정 #000000은 허용 색 아님). tab-bar 비활성 탭은 #262626 (#707070은 #f3f3f3 위에서 D12 위반)
  - 결정: header 타이틀은 화면 이름이다. 스킬·내 자산의 기존 화면 제목 자리는 content-area에 남기지 않고 header 타이틀로 옮긴다. 홈의 인사말과 미션 요약은 content-area에 둔다
  - 결정: 내 자산 목록의 header도 메뉴/알림으로 맞춘다. action-area는 목록에서 tab-bar 위에 놓는다
  - 주의: content-area는 상단 16 + 하단 32가 들어가 실사용 높이가 홈·스킬 599, 등록·판매 신청 615, 목록 551이다. 홈, 스킬 목록, 내 자산 등록은 24 간격까지 더해 한 화면에 넘칠 수 있으므로 content-area 안 세로 스크롤을 전제한다

### 상호작용
- status-bar와 home-indicator는 정적 요소다. 탭 대상이 아니다
- header 타이틀은 정적 텍스트다. header-left, header-right는 탭 대상이다 (메뉴 → 메뉴 열기, 알림 → 알림 목록으로 이동, 뒤로 → 이전 화면으로 이동, 더보기 → 도움말 시트 열기). 배경이 없어도 44×44 영역 전체가 탭 대상이다
- tab-bar 탭 → 해당 탭 화면으로 이동. 현재 탭을 다시 탭하면 화면 맨 위로 이동
- content-area를 스크롤해도 status-bar, header, footer는 움직이지 않는다
- 모든 터치 대상은 높이 44 이상

## 홈

주 진입점은 위에서 아래로 큰 영역 1개(진행 현황)와 보조 영역 2개(추천 스킬, 내 자산 요약)로 위계를 나눈다 (P-012). 선택지가 이 3개 영역과 tab-bar를 넘지 않게 한다.

### 구성 요소
- status-bar (공통 UI, y 0~47)
- header (공통 UI, y 47~99, Hug 52): 타이틀 '홈', header-left 메뉴, header-right 알림. 버튼 배경 없음
- content-area (y 99~746, 높이 647, 좌우 16, 상단 16이라 첫 요소 y 115부터, 하단 32). header 안에 삽입되지 않는다
- 영역 사이 세로 간격 24: 인사 영역 → 진행 현황 영역 → 추천 스킬 영역 → 내 자산 요약 영역 (섹션 간 24 유지)
- 인사 영역 (P-010): 인사말에 회원 이름, 이번 달 미션 한 줄 요약. content-area 맨 위
- 진행 현황 영역 = 큰 영역 1개 (P-010): 인사 영역 바로 아래, 화면에서 가장 크다. list-row 2~3개 (미션 제목, 최근 수정일, 우측 status-badge). list-row 행 사이 12 (사람 결정, 섹션 간 24와 다르다). list-row는 상하 여백 16으로 높이 66
- 추천 스킬 영역 = 보조 영역 1 (P-011): 가로 스크롤 skill-card 3~4개 (스킬 제목, 한 줄 설명). 다음 카드가 일부 보이게 두어 스크롤할 수 있음을 알린다
- 내 자산 요약 영역 = 보조 영역 2 (P-013): 전체 자산 개수와 임시저장·검수 대기·승인됨 개수를 한 줄로 표시. 한 줄 전체가 list-row 한 개처럼 탭 대상이고, 우측에 내 자산으로 가는 화살표를 둔다
- footer (내비 footer, y 746~844, 높이 98): tab-bar (358×64, x 16, y 746~810) + home-indicator (390×34, y 810~844) (P-015). 탭 5개 고정 (홈, 자료, 스킬, 내 학습, 내 자산). 현재 탭인 홈만 채움 글리프 아이콘과 SemiBold 라벨로 표시하고 icon-holder 배경은 없다
- action-area는 없다
- 빈 상태용 submit-button: 학습 항목이 없을 때만 진행 현황 영역 안에 표시
- 무료·유료 자료 구분은 "자료" 탭 안 필터에서 다루므로 홈에는 별도 탭을 두지 않는다

### 상태
- 기본: 진행 현황 list-row, 추천 skill-card, 내 자산 요약이 모두 표시. tab-bar는 홈 [selected]
- 진행 현황 list-row의 status-badge: 작성 중, 제출 완료
- 내 자산 요약에 쓰는 개수 표시 상태 이름: 임시저장, 검수 대기, 승인됨 (배지 라벨과 같은 이름을 쓴다)
- 빈 상태 (P-014): 학습 항목이 없으면 진행 현황 영역에 안내 문구 한 줄과 "자료" 탭으로 가는 submit-button 표시. 추천 스킬, 내 자산 요약, footer는 그대로 둔다
- 자산이 0개인 경우: 내 자산 요약 한 줄에 개수 0을 표시하고 탭하면 내 자산의 빈 화면으로 이동한다
- 불러오는 중: skill-card, list-row 자리에 회색 자리표시 블록 표시. status-bar, header, footer는 그대로 표시
- 넘침: 네 영역과 섹션 간 24 간격(진행 현황 list-row 행 사이는 12), 상단 16, 하단 32를 합치면 647을 넘을 수 있다. 넘치면 content-area 안에서 세로 스크롤하고 footer와는 겹치지 않는다
- 이 화면의 skill-card에는 status-badge를 쓰지 않는다

### 상호작용
- header-left 메뉴 탭 → 메뉴 열기. header-right 알림 탭 → 알림 목록으로 이동
- 진행 현황 list-row 탭 → 해당 미션 또는 제출물로 이동
- 추천 skill-card 탭 → 스킬 라이브러리의 해당 스킬 상세로 이동 (P-011)
- 추천 스킬 영역 가로 스와이프 → 다음 skill-card 표시
- 내 자산 요약 탭 → 내 자산 화면으로 이동 (P-013)
- 빈 상태의 submit-button 탭 → "자료" 탭으로 이동 (P-014)
- tab-bar 탭 → 해당 탭 화면으로 이동. 현재 탭을 다시 탭하면 화면 맨 위로 이동
- content-area만 세로 스크롤한다. status-bar, header, footer는 고정
- 모든 터치 대상은 높이 44 이상

## 스킬 라이브러리

### 구성 요소
- status-bar (공통 UI, y 0~47)
- header (공통 UI, y 47~99, Hug 52): 타이틀 '스킬 라이브러리' (P-016), header-left 메뉴, header-right 알림. 버튼 배경 없음. 화면 제목은 header 타이틀이 맡으므로 content-area에 따로 두지 않는다
- content-area (y 99~746, 높이 647, 좌우 16, 상단 16이라 첫 요소 y 115부터, 하단 32). header 안에 삽입되지 않는다
- 세로 간격 24: 검색 입력창 → 칩 목록 → skill-card 목록 사이, skill-card와 skill-card 사이
- 검색 입력창 (P-016): text-input. 기본 상태 테두리 없음, 포커스 시 text-input[focus] 1px 링. content-area 맨 위
- 카테고리 필터 칩 가로 스크롤 목록 (P-016, P-018): 검색 입력창 바로 아래. 칩은 별도 컴포넌트 없이 pill 모양 요소에 라벨과 개수를 담아 만든다. 예: 전체 24, AI 실무 8, Figma + AI 5, 바이브코딩 4, 자동화 3, 콘텐츠 제작 2, 1인 사업가 운영 2. 선택한 칩만 채운 [selected] 상태
- skill-card 세로 목록 (P-017): 카드 한 장에 스킬 제목, 한 줄 설명, 카테고리, 유형(스킬 또는 프롬프트)을 담는다. 검증된 스킬에는 "검증된 스킬" 표시를 카드 안 텍스트로 붙인다. 제목 예시는 '프롬프트 모음'
- 빈 화면 (P-019): 안내 문구와 필터 초기화 submit-button (content-area 안)
- footer (내비 footer, y 746~844, 높이 98): tab-bar (358×64, x 16) + home-indicator (390×34). 스킬 탭 [selected] (채움 글리프 아이콘 + SemiBold 라벨, icon-holder 배경 없음)
- action-area는 없다

### 상태
- 기본: 전체 [selected], 전체 카테고리의 skill-card 목록
- 필터 적용 (P-016, P-018): 선택한 칩만 채워진 [selected] pill로 표시하고 목록을 해당 카테고리로 좁힘. 칩의 개수는 그대로 유지
- 검색 적용: 입력한 검색어에 맞는 skill-card만 표시. text-input은 [focus] 상태에서 1px 링
- 결과 없음 (P-019): 검색 결과나 필터 결과가 0건이면 목록 대신 안내 문구와 필터 초기화 submit-button 표시. 초기화할 조건이 없으면 submit-button은 [disabled]
- 불러오는 중: skill-card 자리표시 블록. status-bar, header, 칩, footer는 그대로 표시
- 넘침: skill-card 목록은 24 간격 때문에 첫 화면에 카드 2장 안팎만 보일 수 있다. 나머지는 content-area 안 세로 스크롤이며 마지막 카드 아래 32 여백을 둔다
- 이 화면의 skill-card에는 status-badge를 쓰지 않는다 (P-020, 검수 상태는 내 자산에서만 보여 준다)

### 상호작용
- header-left 메뉴 탭 → 메뉴 열기. header-right 알림 탭 → 알림 목록으로 이동
- 칩 탭 → 해당 카테고리로 목록 갱신 (P-018)
- 선택된 같은 칩을 다시 탭 → 선택 해제, 전체 목록으로 돌아감 (P-018)
- 칩 가로 스와이프 → 가려진 칩 표시
- 검색어 입력 → 제목과 설명 기준으로 목록 좁힘. 칩 선택과 함께 적용하면 두 조건을 모두 만족하는 카드만 표시
- 필터 초기화 submit-button 탭 → 검색어와 칩을 비우고 전체 목록 표시 (P-019)
- skill-card 탭 → 스킬 상세로 이동해 내용 확인과 파일 내려받기 (P-020)
- tab-bar 탭 → 해당 탭 화면으로 이동
- content-area만 세로 스크롤한다. status-bar, header, footer는 고정
- 모든 터치 대상은 높이 44 이상

## 내 자산

목록 화면과 등록 화면, 판매 신청 화면으로 구성한다. Figma 프레임 이름은 screen/my-assets/register, screen/my-assets/sale-request를 쓴다.

### 구성 요소
모든 프레임(목록, 등록, 판매 신청)에 status-bar(y 0~47), header(y 47~99, Hug 52, 버튼 배경 없음), content-area(y 99부터, 좌우 16, 상단 16, 하단 32), 최하단 footer를 둔다 (공통 UI). content-area는 header 안에 삽입되지 않는다. footer 안 맨 끝은 home-indicator(390×34, y 810~844)다.

목록 영역 (y 범위: content-area 99~698, footer 698~844)
- header: 타이틀 '내 자산', header-left 메뉴, header-right 알림
- 상단 요약: 전체 자산 개수, 임시저장·검수 대기·승인됨 개수, 마지막 갱신 시각 (P-001)
- 공개 범위 필터 칩 (P-002): 전체, 비공개, 멤버 공개, 판매 신청
- list-row 자산 목록 (P-003): 좌측에 제목, 유형, 최근 수정일, 공개 범위 표시. 우측에 status-badge. 요약, 칩, 목록, 행과 행 사이 세로 간격 24
- footer (목록 footer, 높이 146): action-area (698~746, 새 자산 등록 버튼 1개 P-007, 폭 358, 높이 48, 좌우 여백 16, 위아래 패딩 0) + tab-bar (746~810, 358×64, x 16, 내 자산 탭 선택 표시: 채움 글리프 아이콘 + SemiBold 라벨, icon-holder 배경 없음) + home-indicator (810~844)

등록 화면 (screen/my-assets/register)
- header: 타이틀 '자산 등록', header-left 뒤로, header-right 더보기
- content-area (y 99~762, 높이 663, 상단 16이라 첫 요소 y 115, 하단 32). 필드 사이 세로 간격 24, 한 field 안 라벨과 입력창 사이 8
  - 제목 입력창, 설명 입력창 (text-input, 기본 상태 테두리 없음, 포커스 시 1px 링). 제목 → 설명 → 파일 첨부 → 공개 범위 사이 24
  - file-attach-row: 첨부 파일 이름, 크기, 삭제 버튼. 추가 버튼 포함
  - visibility-selector: 공개 범위 3옵션
    - option/private: 비공개 (기본 선택)
    - option/member-only: 멤버 공개
    - option/sale-request: 판매 신청 (판매 승인 회원 seller에게만 보인다)
- footer (액션 footer, y 762~844, 높이 82): action-area (762~810, 높이 48) + home-indicator (810~844). tab-bar는 없다
  - action-area: 버튼 2개를 좌우로 나란히 놓는다. 좌 임시저장(보조, 폭 175), 우 등록(주, 폭 175). 간격 8, 높이 48, 좌우 여백 16, 위아래 여백 없음

판매 신청 화면 (screen/my-assets/sale-request)
- header: 타이틀 '판매 신청', header-left 뒤로, header-right 더보기
- content-area (y 99~762, 높이 663, 상단 16이라 첫 요소 y 115, 하단 32). 요소 사이 세로 간격 24
  - 신청 대상 자산 요약 list-row
  - 금지 항목 안내 문구: "다음 항목은 판매 자산에 포함할 수 없어요" 아래에 4종을 나열
    - 개인정보
    - 고객정보
    - 회사기밀
    - 타인 저작물
  - confirm-checkbox: "위 금지 항목이 포함되어 있지 않음을 확인했어요" 확인 체크박스
  - 세 덩어리(자산 요약, 안내 문구, 확인 체크박스) 사이는 24. 안내 문구 제목과 4종 나열 사이는 8
- footer (액션 footer, y 762~844, 높이 82): action-area (762~810) + home-indicator (810~844). action-area에 submit-button 1개, 판매 신청 제출. 폭 358, 높이 48, 좌우 여백 16. tab-bar는 없다

### 상태
공개 범위 규칙 (V1)
- 공개 범위 선택은 비공개, 멤버 공개, 판매 신청 3옵션이다
- 새 자산과 제출물에서 전환된 자산 모두 기본 선택은 비공개다
- 판매 신청 옵션은 판매 승인 회원(seller)에게만 보인다

화면 상태 변형 (프레임 이름 접미사)
| 프레임 | 변형 | 표시 내용 |
|---|---|---|
| screen/my-assets/register@seller | seller | visibility-selector에 option/private[selected], option/member-only, option/sale-request 3개 표시 |
| screen/my-assets/register@non-seller | non-seller | option/private[selected], option/member-only 2개만 표시. option/sale-request 노드 없음. "판매 신청은 판매 승인 회원만 쓸 수 있어요" 안내 한 줄 (P-008) |
| screen/my-assets/sale-request@unchecked | 체크 전 | confirm-checkbox 해제, action-area 안 submit-button[disabled] (비활성) |
| screen/my-assets/sale-request@checked | 체크 후 | confirm-checkbox 체크됨, action-area 안 submit-button 활성 |

- 네 변형 모두 status-bar, header, content-area, footer(action-area + home-indicator) 골격은 같다
- 등록 화면 넘침: 제목·설명·파일 첨부·공개 범위를 24 간격으로 쌓고 상단 16, 하단 32를 더하면 content-area 663을 넘을 수 있다 (seller 3옵션 기준). 넘치면 content-area 안 세로 스크롤이며 action-area와 겹치지 않는다. non-seller는 옵션 1개가 적고 안내 한 줄이 더해진다
- 판매 신청 화면은 요소가 적어 대체로 한 화면에 들어간다. 금지 항목 4종 안내와 확인 체크박스는 스크롤 없이 보이게 두고, 넘치면 submit-button이 footer에 고정되어 있어도 체크박스가 스크롤로 닿을 수 있어야 한다

목록 상태
- 자산 상태 배지는 status-badge 7종 이름만 쓴다: 작성 중, 임시저장, 제출 완료, 검수 대기, 수정 요청, 승인됨, 반려
- 판매 신청 흐름의 상태: 임시저장 → 검수 대기 → 수정 요청 또는 승인됨 또는 반려. 최종 상태는 승인됨 (P-005)
- 색만으로 구분하지 않고 배지 라벨 텍스트를 항상 함께 쓴다. 수정 요청은 ! 아이콘, 승인됨은 ✓ 아이콘, 반려는 ✕ 아이콘을 넣는다
- 빈 상태: 아이콘, 안내 문구 (content-area 안). 새 자산 등록 버튼은 footer의 action-area에 그대로 둔다 (P-006)
- 불러오는 중: list-row 자리표시 블록. status-bar, header, footer는 그대로 표시

### 상호작용
- header-left 뒤로 탭 → 이전 화면으로 이동 (등록·판매 신청). 목록의 메뉴/알림은 홈과 같다
- 공개 범위 필터 칩 탭 → 해당 공개 범위 자산만 목록에 표시
- list-row 탭 → 자산 상세로 이동
- action-area의 새 자산 등록 버튼 탭 → 등록 화면으로 이동. 공개 범위는 비공개가 선택된 상태로 열린다
- file-attach-row의 추가 버튼 탭 → 파일 선택, 삭제 버튼 탭 → 첨부 해제
- visibility-selector에서 옵션 탭 → 한 번에 하나만 선택
  - seller가 option/sale-request를 선택하면 판매 신청 화면으로 이동한다
  - non-seller에게는 option/sale-request가 없어 선택할 수 없다
- 판매 신청 화면
  - 진입 직후 confirm-checkbox는 해제, action-area 안 submit-button은 비활성이다
  - confirm-checkbox를 체크하면 submit-button이 활성화된다. 체크를 해제하면 다시 비활성이 된다
  - 활성화된 submit-button 탭 → 검수 대기 상태로 접수하고 내 자산 목록으로 돌아간다. 해당 행에 status-badge 검수 대기 표시
- 검수 결과가 수정 요청이면 해당 list-row 탭으로 수정 후 다시 제출할 수 있다
- 등록 화면의 action-area 좌측 임시저장 탭 → 임시저장 배지로 목록에 추가. 우측 등록 탭 → 선택한 공개 범위로 등록
- 콘텐츠는 content-area만 스크롤한다. footer(action-area, home-indicator)는 고정
- 모든 버튼·칩·행은 높이 44 이상
