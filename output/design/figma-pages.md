# Figma 페이지 정리

Figma: https://www.figma.com/design/CNelXB5JxSwpeJNurQRm3L/Design-harness

## 페이지 이름 변경 (ID 유지, 내용 이동·삭제·수정 없음)
- 19:2 | `S4 Keyscreens` -> `S4 Keyscreens (키스크린 시안)`
- 22:2 | `S6 Components` -> `S6 Components (토큰·컴포넌트)`
- 26:113 | `S7 Screens` -> `S7 Screens (화면 디자인)`
- 22:2 | `S6 Components (토큰·컴포넌트)` -> `S6 Components (컴포넌트)` (사용자 요청, 토큰은 파일 변수·87:3 토큰 가이드 페이지에 있어 컴포넌트 페이지 이름에서 뺌)

## 신설 페이지
- 87:2 | `S5 Approval (확정 시안)` / 프레임 87:4 `s5-approval-guide` (720폭 안내 프레임). 확정 일시 2026-10-01 13:56:35, 확정 프레임 참조 ID 82:75 screen/home, 82:164 screen/skills, 19:3 screen/my-assets/register@seller, 메모. 복제본 없음
- 87:3 | `토큰 가이드 (Token Guide)` / 프레임 87:14 `token-guide` (720폭). 색 견본 9종(accent 제외, 텍스트 설명만), 반경 4종, 간격 0~64 9단계, 타이포 12단계(Pretendard Light/Regular/SemiBold/Bold). 견본 채움·외곽선·반경·막대 폭은 tokens 변수 바인딩, 텍스트는 Pretendard, 그림자·그라디언트 없음
  - 수정(사용자 요청): 87:14는 `token-guide/variables`(x0 y0 720x2357)로 이름 변경해 block/variables만 두고, 새 `token-guide/styles`(210:2, x800 y0 720x1440)에 block/styles(208:442)를 이동. 가로 간격 80
  - 표 구조 재작성(사용자 요청): 87:14는 `block/variables` 208:438(tokens 컬렉션 그룹 color 13·radius 9·spacing 9)과 `block/styles` 208:442(Text styles 13·Effect styles 1) 두 덩어리, 예시|이름|값|용도 표. 높이 2998→3742. 이 가이드의 노드 ID는 이후 새 값 기준(상세: s6-tokens-components.md 마지막 섹션)
  - 수정(사용자 요청, 폰트 가이드 보강): 로컬 텍스트 스타일 type/* 12개 신규, Typography 견본 87:114~87:149에 적용, 라벨에 줄 높이·자간 추가, 용도 한 줄(use/*) 추가. type-scale 613 → 875, 가이드 높이 2310 → 2572, Shadow 섹션 y +262(1974 → 2236). 상세는 s6-tokens-components.md
  - 수정(사용자 결정 A안): 타이포 견본에 type/label-md(13px · 600 SemiBold · 140% · 0) 프레임 119:3 추가(type/link 뒤), type-scale 875 → 941, 가이드 높이 2572 → 2638, Shadow 섹션 y 2236 → 2302. 타이포 13단계

## S5 확정본 복제 (87:2, 원본 이동·수정·삭제 없음, 프레임 간격 40)
- 88:2 | `confirmed/screen/home` (원본 82:75) / 라벨 88:90 / x0 y40
- 88:91 | `confirmed/screen/skills` (원본 82:164) / 라벨 88:174 / x430 y40
- 88:175 | `confirmed/screen/my-assets/register@seller` (원본 19:3) / 라벨 88:248 / x860 y40
- 안내 프레임 87:4는 복제본 아래(x0 y924)로 이동. 위 87:4 설명의 "복제본 없음"은 이 절로 대체
- 라벨 텍스트 '확정본 · 원본 ID <ID>' Pretendard Regular 12

## 삭제
- 7:2 `Dump Test` 페이지 삭제 (삭제 전 get_metadata로 프레임 7:3 screen/dump-test 하나만 있음을 확인)

## 최종 페이지 순서 (삭제 후 조회 확인)
Page 1 (0:1), S4 (19:2) -> S5 (87:2) -> S6 (22:2) -> S7 (26:113) -> 토큰 가이드 (87:3)
(2026-10-01 페이지 순서만 변경: 토큰 가이드를 맨 아래로 이동. 변경 전 조회 순서는 S5 -> 토큰 가이드 -> S6 -> S7. 이름·노드 변경 없음. 변경 후 조회로 확인)

## 프레임 배치(왼쪽→오른쪽, 패널 순서)
위치(x,y)와 최상위 자식 순서만 변경. 이름·ID·크기·내용 변경 없음. 패널은 위→아래가 캔버스 읽기 순서. 프레임 다음에 그 라벨이 바로 아래에 온다. 변경 후 조회로 확인, 겹침 없음.
- S7 (26:113), y0, 간격 80: 36:49 screen/home x0 -> 36:102 screen/skills x470 -> 26:114 register@seller x940 -> 26:161 register@non-seller x1410 -> 26:203 sale-request@unchecked x1880 -> 26:274 sale-request@checked x2350
- S4 (19:2), y0: 82:75 screen/home x0 -> 82:164 screen/skills x470 -> 19:3 register@seller x940 -> 94:4 register#B x1370 / 94:90 label (y-60) -> 94:93 register#C x1800 / 94:174 label -> 101:4 tab-bar-shadow x2230 / 101:32 label -> 105:29 tab-bar-shadow-y0 x2660 / 105:57 label (제안 프레임·라벨 위치 유지)
- S5 (87:2), 위치 유지: 88:2 home x0 / 88:90 -> 88:91 skills x430 / 88:174 -> 88:175 register@seller x860 / 88:248 -> 87:4 s5-approval-guide (x0 y924, 패널 맨 아래). 토큰 가이드 87:3은 변경 없음
- S6 (22:2), 위치 유지(세로 한 열), 위→아래: status-badge 23:19, skill-card 35:82, list-row 35:90, tab-bar 23:53, visibility-selector 23:98, file-attach-row 23:99, confirm-checkbox 23:112, submit-button 23:117, text-input 23:122, status-bar 64:184, header 64:187, action-area 64:190, home-indicator 64:191, footer 72:333 (x0, y 0/91/309/441/561/854/978/1106/1218/1330/1420/1530/1720/1834)
