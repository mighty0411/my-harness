# 알려진 미해결 항목 (2026-10-04)

## 결정
- 사람 결정: 화면 디자인과 컴포넌트는 수정하지 않는다.
- 그 결과 G8은 통과하지 못한 채로 둔다. D 규칙 위반은 사람 승인으로 넘길 수 없다 (r5-gates.md).
- state.json: S1~S5 passed, S6~S8 pending. S6 pending은 재작업 예정이 아니라 G8 실패의 기록이다.

## 판정 결과 (judge 재판정)
- G1~G7 통과, G8 실패 (위반 9건). V1·V2 위반 0건.
- 리포트: output/verdict/gate-G1.json ~ gate-G8.json, s8-report.json

## G8 위반 9건
| 규칙 | 프레임 | 내용 | 복귀 단계 |
|---|---|---|---|
| D09 | screen/home 196:1206 | itemSpacing 10 | S7 |
| D09 | screen/home 196:1208 | itemSpacing 6 | S7 |
| D03 | screen/skills | accent 사용 요소 5개 | S7 |
| D11 | register@seller 26:224 | 포커스 링이 1px #141414가 아님 | S7 |
| D12 | sale-request@unchecked I26:261;23:29 | 대비 4.31:1 (#707070 on #e6f0ff) | S6 |
| D12 | sale-request@unchecked I73:525;72:326;181:68;23:116 | 금지 조합 #adadad on #f0f0f0 | S6 |
| D12 | 같은 노드 | 대비 1.97:1 | S6 |
| D12 | sale-request@checked I26:276;23:29 | 대비 4.31:1 (list-row) | S6 |
| D03 | sale-request@checked I73:533;72:326;181:68 | CTA 버튼에 accent 사용 | S7 또는 S6 |

## 판정 불가 (위반 아님)
- D07 x4: screen/home 189:733, 189:735, 189:737, 189:739 (숨김 segment의 label 글자)
- D10 x1: screen/skills I73:572;72:297 (footer 안 tab-bar 높이)
- G4 V1: register@non-seller 키스크린 프레임이 S4 덤프에 없음

## 다시 열려면
- 디자인을 고치기로 하면 "S6부터 다시"로 시작한다. D12는 S6, 나머지는 S7에서 고친다.
- 또는 사람이 harness/rules.json의 해당 D 규칙을 직접 조정한다.
