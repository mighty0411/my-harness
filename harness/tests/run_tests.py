#!/usr/bin/env python3
"""판정 스크립트 검증: 규칙 픽스처 16개와 마크다운·덤프 게이트 케이스를 기대값과 비교한다.
종료 코드 0 = 전부 일치 (일치율 100%), 1 = 불일치 있음."""
import copy
import json
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "scripts"))
import judge  # noqa: E402

RULES = judge.load_rules()
FIX = HERE / "fixtures"
results = []


def record(name, ok, detail=""):
    results.append((name, ok, detail))


def load(name):
    return json.loads((FIX / name).read_text(encoding="utf-8"))


# ---- 1. 규칙 픽스처 ----
rep = judge.check_dump(load("pass.json"), RULES, "final", "S7 Screens")
record("pass.json 위반 0", not rep.violations, "; ".join(rep.messages()))
record("pass.json 판정 불가 0", not rep.unverifiable, str(rep.unverifiable))
for rule in judge.RULE_IDS:
    rep = judge.check_dump(load(f"fail-{rule}.json"), RULES, "final", "S7 Screens")
    got = {v["rule"] for v in rep.violations}
    record(f"fail-{rule} → {{{rule}}}만 실패", got == {rule}, f"실제 {sorted(got)}")


# ---- 2. 마크다운 게이트 ----
def write(out, rel, content):
    p = out / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")


SCREENS = ["홈", "스킬 라이브러리", "내 자산"]


def s1(competitors=3, drop_url=False):
    t = "## 경쟁사\n" + "".join(f"- 경쟁사{i}\n" for i in range(competitors))
    n = 0
    for s in SCREENS:
        t += f"## {s}\n"
        for _ in range(5):
            n += 1
            url = "" if (drop_url and n == 1) else "https://uibowl.io/x"
            t += f"- R-{n:03d} | 앱 | {s} | {url}\n"
    return t


def s2(bad_ref=False):
    t = ""
    n = 0
    for s in SCREENS:
        for _ in range(3):
            n += 1
            ref = "R-999" if (bad_ref and n == 1) else "R-001"
            t += f"- P-{n:03d} | {s} | 내용 | 근거: {ref}\n"
    return t


def s3(bad_term=False):
    t = ""
    for s in SCREENS:
        t += f"## {s}\n### 구성 요소\n- a\n### 상태\n- b\n### 상호작용\n- c\n"
    t += "공개 범위: 비공개, 멤버 공개, 판매 신청. 개인정보, 고객정보, 회사기밀, 타인 저작물 안내와 확인 체크박스 필요.\n"
    t += "허들링 픽 노출은 Phase 2라 제외한다.\n"
    if bad_term:
        t += "허들링 픽 노출 영역을 추가한다.\n"
    return t


def gate_case(name, gate, files, expect_pass):
    with tempfile.TemporaryDirectory() as d:
        out = Path(d)
        for rel, content in files.items():
            write(out, rel, content)
        r = judge.run_gate(gate, out, RULES)
        record(name, r["passed"] == expect_pass, "; ".join(r["messages"]))


R1, R2, R3 = "research/s1-references.md", "research/s2-analysis.md", "spec/s3-screen-spec.md"
gate_case("G1 통과", "G1", {R1: s1()}, True)
gate_case("G1 경쟁사 2개 → 실패", "G1", {R1: s1(competitors=2)}, False)
gate_case("G1 URL 누락 → 실패", "G1", {R1: s1(drop_url=True)}, False)
gate_case("G2 통과", "G2", {R1: s1(), R2: s2()}, True)
gate_case("G2 없는 근거 ID → 실패", "G2", {R1: s1(), R2: s2(bad_ref=True)}, False)
gate_case("G3 통과", "G3", {R3: s3()}, True)
gate_case("G3 MVP 제외 표현 → 실패", "G3", {R3: s3(bad_term=True)}, False)
S4MD = "design/s4-keyscreens.md"
gate_case("G5 통과", "G5", {S4MD: "- frame: 1:2 | a\n- frame: 1:5 | b\n", "run/s5-approval.md": "확정 프레임 ID: 1:2, 1:5\n"}, True)
gate_case("G5 승인 전 → 실패", "G5", {S4MD: "- frame: 1:2 | a\n"}, False)
gate_case("G5 S4에 없는 ID → 실패", "G5", {S4MD: "- frame: 1:2 | a\n", "run/s5-approval.md": "확정 프레임 ID: 1:99\n"}, False)


# ---- 2b. 대상 화면 1개 (state.json input.screens) ----
def s1_one():
    t = "## 경쟁사\n- a\n- b\n- c\n## 내 자산\n"
    for i in range(1, 6):
        t += f"- R-{i:03d} | 앱 | 내 자산 | https://uibowl.io/x\n"
    return t


ONE = json.dumps({"input": {"screens": ["내 자산"]}}, ensure_ascii=False)
gate_case("G1 대상 화면 1개(내 자산) 통과", "G1", {R1: s1_one(), "run/state.json": ONE}, True)
gate_case("G1 대상 화면 3개인데 1개만 → 실패", "G1", {R1: s1_one()}, False)

# ---- 3. 덤프 게이트 ----
def to_page(d, page, keep=None):
    d = copy.deepcopy(d)
    if keep:
        d["frames"] = [f for f in d["frames"] if f["name"] in keep]
    for f in d["frames"]:
        f["page"] = page
    return d


def dump_case(name, gate, dumps, expect_pass, files=None):
    with tempfile.TemporaryDirectory() as t:
        out = Path(t)
        for rel, content in (files or {}).items():
            write(out, rel, content)
        for fname, content in dumps.items():
            write(out, f"verdict/dump/{fname}.json", json.dumps(content, ensure_ascii=False))
        r = judge.run_gate(gate, out, RULES)
        record(name, r["passed"] == expect_pass, "; ".join(r["messages"]))


P = load("pass.json")
KEY = ["screen/home", "screen/skills", "screen/my-assets/register@seller", "screen/my-assets/register@non-seller"]
dump_case("G4 통과", "G4", {"s4": to_page(P, "S4 Keyscreens", KEY)}, True)
dump_case("G4 화면 4개 → 실패", "G4", {"s4": to_page(P, "S4 Keyscreens")}, False)


def with_variants(d, tags, page="S4 Keyscreens"):
    """화면마다 tags 개수만큼 안(#A, #B…)으로 복제한 S4 덤프"""
    d = to_page(d, page, KEY)
    frames = []
    for tag in tags:
        for f in d["frames"]:
            g = copy.deepcopy(f)
            base, _, st = g["name"].partition("@")
            g["name"] = f"{base}#{tag}" + (f"@{st}" if st else "")
            g["id"] = f'{f["id"]}-{tag}'
            frames.append(g)
    d["frames"] = frames
    return d


VSTATE = {"run/state.json": json.dumps({"input": {"variants": 3}})}
dump_case("G4 안 3개 → 통과", "G4", {"s4": with_variants(P, "ABC")}, True, VSTATE)
dump_case("G4 안 1개뿐 → 실패", "G4", {"s4": with_variants(P, "A")}, False, VSTATE)
dump_case("G4 안 4개 → 실패", "G4", {"s4": with_variants(P, "ABCD")}, False, VSTATE)
dump_case("G4 안 구분 없음(variants=1) 기존 통과", "G4", {"s4": to_page(P, "S4 Keyscreens", KEY)}, True)
S4V = "- frame: 1:1 | screen/home#A\n- frame: 1:2 | screen/home#B\n- frame: 1:3 | screen/skills#A\n- frame: 1:4 | screen/skills#B\n- frame: 1:5 | screen/my-assets/register#A@seller\n- frame: 1:6 | screen/my-assets/register#B@seller\n"
gate_case("G5 안 방식 화면마다 하나 → 통과", "G5", {S4MD: S4V, "run/s5-approval.md": "확정 프레임 ID: 1:1, 1:4, 1:5\n", "run/state.json": json.dumps({"input": {"variants": 2}})}, True)
gate_case("G5 한 화면에 두 안 → 실패", "G5", {S4MD: S4V, "run/s5-approval.md": "확정 프레임 ID: 1:1, 1:2, 1:4, 1:5\n", "run/state.json": json.dumps({"input": {"variants": 2}})}, False)
gate_case("G5 화면 하나 빠짐 → 실패", "G5", {S4MD: S4V, "run/s5-approval.md": "확정 프레임 ID: 1:1, 1:4\n", "run/state.json": json.dumps({"input": {"variants": 2}})}, False)
dump_case("G7 통과", "G7", {"s7": P}, True)
dump_case("G8 통과", "G8", {"s7": P}, True)
dump_case("G8 V2 위반 → 실패", "G8", {"s7": load("fail-V2.json")}, False)


def comps(drop=None):
    names = RULES["gates"]["G6"]["components"]
    nodes = []
    for n in names:
        if n == drop:
            continue
        node = {"id": n, "name": n, "type": "FRAME", "fills": ["#ffffff"]}
        if n in ("status-badge", "tab-bar"):
            node["cornerRadius"] = 9999
        if n == "skill-card":
            node["cornerRadius"] = 24
        nodes.append(node)
    return {"variables": {"colors": ["#141414", "#ffffff"], "radius": [16, 24, 9999], "spacing": [8, 16]},
            "frames": [{"id": "c", "name": "components", "page": "S6 Components", "nodes": nodes}]}


dump_case("G6 통과", "G6", {"s6": comps()}, True)
dump_case("G6 컴포넌트 누락 → 실패", "G6", {"s6": comps(drop="list-row")}, False)


# ---- 4. Figma 읽기 결과 → 덤프 변환 ----
import copy as _copy  # noqa: E402
import figma_to_dump as f2d  # noqa: E402

FG = HERE / "fixtures" / "figma"


def convert(bundle):
    frames, vars_raw = f2d.parse_bundle(bundle)
    warn = []
    dump = {"frames": [f2d.convert_frame(f, warn) for f in frames]}
    v = f2d.parse_vars(vars_raw)
    if v is not None:
        dump["variables"] = v
    return dump, warn


real = ("### PAGE Dump Test\n### FRAME 7:3\n### META\n" + (FG / "dump-test.meta.xml").read_text(encoding="utf-8")
        + "### CODE\n" + (FG / "dump-test.code.jsx").read_text(encoding="utf-8"))
dump, warn = convert(real)
fr = dump["frames"][0]
nd = {n["name"]: n for n in fr["nodes"]}
record("변환: 프레임 390×844, 좌우 패딩 16", (fr["width"], fr["height"], fr["padding"]) == (390, 844, {"left": 16, "right": 16}))
record("변환: 경고 0", not warn, str(warn))
b = nd["button/primary"]
record("변환: 버튼 채움·반경·높이·패딩", (b["fills"], b["cornerRadius"], b["height"], b["padding"]["left"]) == (["#141414"], 9999, 48, 16))
c = nd["card/content"]
record("변환: 카드 선·반경·그림자", (c["strokes"], c["cornerRadius"], c["effects"]) == ([{"color": "#f0f0f0", "weight": 1, "style": "solid"}], 24, [{"type": "DROP_SHADOW"}]))
bd = nd["status-badge"]
record("변환: 배지 라벨·점선·색·굵기 접기", (bd["text"], bd["strokes"][0]["style"], bd["textColor"], bd["font"]["weight"], bd["icon"]) == ("작성 중", "dashed", "#707070", 600, None))
record("변환: 제목 폰트(Inter Bold 700, 28)", nd["heading"]["font"] == {"family": "Inter", "weight": 700, "size": 28} and nd["heading"]["letterSpacing"] == 0)
record("변환: 대문자·자간", (nd["upper"]["textCase"], nd["wide-spacing"]["letterSpacing"]) == ("UPPER", 2))
record("변환: #06f → #0066ff, 그라디언트", (nd["accent-dot"]["fills"], nd["decor"].get("gradient")) == (["#0066ff"], True))
record("변환: 글자 배경색 상속", (nd["muted-on-soft"]["bg"], nd["label"]["bg"]) == ("#ffffff", "#141414"))

# 변수(var(--이름,기본값))에 묶인 값, 컴포넌트 인스턴스, variant 자식 개별 읽기 (S6에서 확인된 실제 출력)
record("변환: var() 기본값 풀기", f2d.strip_var("rounded-[var(--radius\\/badge,9999px)] shadow-[var(--x,rgba(0,0,0,0.1))]") == "rounded-[9999px] shadow-[rgba(0,0,0,0.1)]")
lr = ("### PAGE S6 Components\n### FRAME 23:26\n### META\n" + (FG / "s6-list-row.meta.xml").read_text(encoding="utf-8")
      + "### CODE\n" + (FG / "s6-list-row.code.jsx").read_text(encoding="utf-8"))
ld, lw = convert(lr)
ln = {n["id"]: n for n in ld["frames"][0]["nodes"]}
record("변환(변수): 인스턴스 경고 0", not lw, str(lw))
record("변환(변수): 배지 인스턴스 반경 9999·점선·#e0e0e0·흰 채움",
       (ln["23:30"]["cornerRadius"], ln["23:30"]["fills"], ln["23:30"]["strokes"]) == (9999, ["#ffffff"], [{"color": "#e0e0e0", "weight": 1, "style": "dashed"}]))
record("변환(변수): 제목 글자 폰트·색", (ln["23:28"]["font"], ln["23:28"]["textColor"]) == ({"family": "Pretendard", "weight": 600, "size": 15}, "#141414"))
record("변환(변수): 행 패딩 16·12", ld["frames"][0]["padding"] == {"left": 16, "right": 16})
cb_meta = """<symbol id="23:108" name="confirm-checkbox" x="0" y="0" width="342" height="72">
  <frame id="23:109" name="checkbox-box" x="16" y="24" width="24" height="24"><text id="23:110" name="check" x="6" y="4" width="12" height="17" /></frame>
  <text id="23:111" name="label" x="52" y="12" width="274" height="48" />
</symbol>
"""
cb = ("### PAGE S6 Components\n### FRAME 23:108\n### META\n" + cb_meta + "### CODE\n"
      + (FG / "s6-checkbox-checked.code.jsx").read_text(encoding="utf-8"))
cd_, cw = convert(cb)
cn = {n["id"]: n for n in cd_["frames"][0]["nodes"]}
record("변환(변수): variant 개별 코드에서 스타일 읽힘, 경고 0", not cw, str(cw))
record("변환(변수): 체크박스 채움 #141414·반경 9999, 체크 글자 #ffffff",
       (cn["23:109"]["fills"], cn["23:109"]["cornerRadius"], cn["23:110"]["textColor"]) == (["#141414"], 9999, "#ffffff"))

# variant 별 메타 병합 (세트 메타에는 자식이 없다), +root (컴포넌트 루트 검사)
vb = ("### PAGE S6 Components\n### FRAME 23:98\n### META\n" + (FG / "s6-vis-set.meta.xml").read_text(encoding="utf-8")
      + "### META\n" + (FG / "s6-vis-variant.meta.xml").read_text(encoding="utf-8") + "### CODE\n")
vd, _vw = convert(vb)
vn = {n["id"]: n for n in vd["frames"][0]["nodes"]}
record("변환(메타 병합): 세트 안 variant 자식(option/*) 3개가 노드로 들어옴",
       {"23:55", "23:58", "23:61"} <= set(vn) and vn["23:55"]["name"] == "option/private" and vn["23:55"]["selected"] is True and vn["23:58"]["selected"] is False)
record("변환(메타 병합): 자식 없는 다른 variant 심볼은 그대로", "23:64" in vn and "23:65" not in vn)
lr_root = lr.replace("### FRAME 23:26", "### FRAME 23:26 +root", 1)
rd, _rw = convert(lr_root)
rn = {n["id"]: n for n in rd["frames"][0]["nodes"]}
record("변환(+root): 컴포넌트 루트가 노드로 검사됨, 옵션 없으면 빠짐",
       "23:26" in rn and rn["23:26"]["fills"] == ["#ffffff"] and "23:26" not in {n["id"] for n in ld["frames"][0]["nodes"]})

# 글자 색·폰트는 부모 div 에 붙어 나온다 (CSS 상속) — S6 option 카드, 아이콘 배지의 실제 형태
inh_meta = """<frame id="23:55" name="option/private[selected]" x="0" y="0" width="342" height="71">
  <text id="23:56" name="label" x="16" y="12" width="310" height="23" />
  <text id="23:57" name="description" x="16" y="39" width="310" height="20" />
</frame>
"""
inh_code = """<div className="bg-[var(--color\\/ink,#141414)] flex flex-col relative rounded-[var(--radius\\/input,16px)] text-[color:var(--color\\/canvas,white)] w-full" data-node-id="23:55" data-name="option/private[selected]">
  <p className="font-['Pretendard:SemiBold'] relative shrink-0 text-[15px] w-full" data-node-id="23:56">
    비공개
  </p>
  <p className="font-['Pretendard:Regular'] relative shrink-0 text-[13px] w-full" data-node-id="23:57">
    나만 볼 수 있어요
  </p>
</div>
"""
idt, _iw = convert("### PAGE S6 Components\n### FRAME 23:55\n### META\n" + inh_meta + "### CODE\n" + inh_code)
inn = {n["id"]: n for n in idt["frames"][0]["nodes"]}
record("변환(상속): 부모 글자색을 자식 글자가 이어받고 자체 폰트는 유지",
       (inn["23:56"]["textColor"], inn["23:56"]["font"], inn["23:57"]["textColor"], inn["23:57"]["font"])
       == ("#ffffff", {"family": "Pretendard", "weight": 600, "size": 15}, "#ffffff", {"family": "Pretendard", "weight": 400, "size": 13}))
bd_meta = """<symbol id="23:16" name="status=반려" x="0" y="0" width="60" height="27">
  <text id="23:17" name="icon/close" x="12" y="4" width="10" height="17" />
  <text id="23:18" name="label" x="26" y="4" width="22" height="17" />
</symbol>
"""
bd_code = """<div className={className || '[word-break:break-word] bg-[var(--color\\/canvas-soft,#f3f3f3)] flex font-["Pretendard:SemiBold"] gap-[var(--spacing\\/4,4px)] px-[var(--spacing\\/12,12px)] relative rounded-[var(--radius\\/badge,9999px)] text-[12px] text-[color:var(--color\\/ink,#141414)]'} data-node-id="23:16">
  <p className="font-semibold relative shrink-0" data-node-id="23:17">✕</p>
  <p className="not-italic relative shrink-0" data-node-id="23:18">반려</p>
</div>
"""
bdd, _bw = convert("### PAGE S6 Components\n### FRAME 23:16\n### META\n" + bd_meta + "### CODE\n" + bd_code)
bn = {n["id"]: n for n in bdd["frames"][0]["nodes"]}
record("변환(상속): 아이콘 배지 글자가 부모의 폰트·색을 이어받음",
       (bn["23:18"]["textColor"], bn["23:18"]["font"]) == ("#141414", {"family": "Pretendard", "weight": 600, "size": 12}))

sx, _c = f2d.parse_code("""<p className="font-semibold relative shrink-0" data-node-id="23:17" style={{ fontVariationSettings: '"CTGR" 0, "wdth" 100' }}>
  ✕
</p>""")
record("변환: style={{ }} 중첩 중괄호가 있는 태그도 읽힘 (아이콘 글리프 ✕)", sx.get("23:17", {}).get("text") == "✕")

# 인스턴스 안쪽 노드(I26:234;23:55 ...)는 메타에 없고 코드에만 있다
im_meta = """<frame id="26:114" name="screen/my-assets/register@seller" x="0" y="0" width="390" height="844">
  <instance id="26:234" name="visibility-selector" x="24" y="200" width="342" height="229" />
  <instance id="26:261" name="status-badge" x="24" y="500" width="60" height="27" />
</frame>
"""
im_code = """<div className="bg-[var(--color\\/canvas,white)] relative size-full" data-node-id="26:114" data-name="screen/my-assets/register@seller">
  <div className="content-stretch flex flex-col relative w-[342px]" data-node-id="26:234" data-name="visibility-selector">
    <div className="bg-[var(--color\\/ink,#141414)] flex flex-col relative rounded-[var(--radius\\/input,16px)] text-[color:var(--color\\/canvas,white)] w-full" data-node-id="I26:234;23:55" data-name="option/private[selected]">
      <p className="font-['Pretendard:SemiBold'] text-[15px] w-full" data-node-id="I26:234;23:56">비공개</p>
    </div>
    <div className="bg-[var(--color\\/canvas-soft,#f3f3f3)] flex flex-col relative rounded-[var(--radius\\/input,16px)] w-full" data-node-id="I26:234;23:58" data-name="option/member-only">
      <p className="font-['Pretendard:SemiBold'] text-[15px] text-[color:var(--color\\/ink,#141414)] w-full" data-node-id="I26:234;23:59">멤버 공개</p>
    </div>
  </div>
  <div className="bg-[var(--color\\/canvas,white)] border border-[var(--color\\/hairline,#e0e0e0)] border-dashed flex rounded-[var(--radius\\/badge,9999px)]" data-node-id="26:261" data-name="status-badge">
    <p className="font-['Pretendard:SemiBold'] text-[12px] text-[color:var(--color\\/text-muted,#707070)]" data-node-id="I26:261;23:3">임시저장</p>
  </div>
</div>
"""
imd, imw = convert("### PAGE S7 Screens\n### FRAME 26:114\n### META\n" + im_meta + "### CODE\n" + im_code)
imn = {n["id"]: n for n in imd["frames"][0]["nodes"]}
record("변환(인스턴스 안쪽): 메타에 없는 I 노드가 덤프에 들어오고 경고 없음", {"I26:234;23:55", "I26:234;23:58", "I26:234;23:56"} <= set(imn) and not imw, str(imw))
record("변환(인스턴스 안쪽): option 이름·selected·반경",
       (imn["I26:234;23:55"]["name"], imn["I26:234;23:55"]["selected"], imn["I26:234;23:55"]["cornerRadius"], imn["I26:234;23:58"]["selected"]) == ("option/private", True, 16, False))
record("변환(인스턴스 안쪽): 글자가 조상 글자색·굵기·크기를 이어받고 배경 bg 를 따름",
       (imn["I26:234;23:56"]["textColor"], imn["I26:234;23:56"]["font"]["weight"], imn["I26:234;23:56"]["bg"]) == ("#ffffff", 600, "#141414"))
record("변환(인스턴스 안쪽): 인스턴스 안 글자가 배지 라벨로 접힘",
       (imn["26:261"]["text"], imn["26:261"]["textColor"], imn["26:261"]["strokes"][0]["style"]) == ("임시저장", "#707070", "dashed"))

# 화면 좌우 패딩: 루트에 없고 content-area 에 있으면 content-area 값을 쓴다
ca_meta = """<frame id="61:1" name="screen/home" x="0" y="0" width="390" height="844">
  <frame id="61:2" name="content-area" x="0" y="95" width="390" height="661">
    <text id="61:3" name="제목" x="16" y="16" width="100" height="18" />
  </frame>
</frame>
"""
ca_code = """<div className="bg-white relative size-full" data-node-id="61:1" data-name="screen/home">
  <div className="flex flex-col px-[var(--spacing\\/16,16px)] pt-[var(--spacing\\/16,16px)] relative w-full" data-node-id="61:2" data-name="content-area">
    <p className="font-['Pretendard:SemiBold'] text-[15px] text-[#141414]" data-node-id="61:3">제목</p>
  </div>
</div>
"""
cad, _cw = convert("### PAGE S4 Keyscreens\n### FRAME 61:1\n### META\n" + ca_meta + "### CODE\n" + ca_code)
record("변환(패딩): 루트에 좌우 패딩이 없으면 content-area 의 좌우 패딩 16을 화면 패딩으로 씀", cad["frames"][0]["padding"] == {"left": 16, "right": 16}, str(cad["frames"][0]["padding"]))
ca_root = ca_code.replace('className="bg-white relative size-full"', 'className="bg-white relative size-full px-[8px]"')
cad2, _cw2 = convert("### PAGE S4 Keyscreens\n### FRAME 61:1\n### META\n" + ca_meta + "### CODE\n" + ca_root)
record("변환(패딩): 루트에 좌우 패딩이 있으면 루트 값을 그대로 씀", cad2["frames"][0]["padding"] == {"left": 8, "right": 8}, str(cad2["frames"][0]["padding"]))

# 함수 컴포넌트 인스턴스(<ActionArea .../>): 정의 안 노드를 인스턴스 아래에 넣는다 (변형 분기가 있으면 넣지 않는다)
fc_meta = """<frame id="26:203" name="screen/my-assets/sale-request@unchecked" x="0" y="0" width="390" height="844">
  <instance id="66:230" name="action-area" x="0" y="748" width="390" height="72" />
</frame>
"""
fc_code = """function ActionArea({ className, count = "1" }: ActionAreaProps) {
  return (
    <div className={className || "bg-[var(--color\\/canvas,white)] flex flex-col h-[72px] px-[var(--spacing\\/16,16px)] relative w-[390px]"} data-node-id="64:189">
      <div className="bg-[var(--color\\/canvas,white)] border border-[var(--color\\/hairline,#e0e0e0)] border-dashed flex h-[48px] items-center justify-center relative rounded-[var(--radius\\/button,9999px)] w-full" data-node-id="64:181" data-name="submit-button[disabled]">
        <p className="font-['Pretendard:SemiBold'] text-[15px] text-[color:var(--color\\/text-muted,#707070)]" data-node-id="64:182">판매 신청 제출</p>
      </div>
    </div>
  );
}

export default function ScreenSaleRequest() {
  return (
    <div className="bg-white relative size-full" data-node-id="26:203" data-name="screen/my-assets/sale-request@unchecked">
      <ActionArea className="absolute bg-white flex flex-col h-[72px] px-[16px] relative w-[390px]" />
    </div>
  );
}
"""
fcd, fcw = convert("### PAGE S7 Screens\n### FRAME 26:203\n### META\n" + fc_meta + "### CODE\n" + fc_code)
fcn = {n["id"]: n for n in fcd["frames"][0]["nodes"]}
record("변환(함수 컴포넌트 인스턴스): 안쪽 제출 버튼이 인스턴스 아래 I 노드로 들어오고 disabled 로 읽힘",
       "I66:230;64:181" in fcn and fcn["I66:230;64:181"].get("variant") == "disabled" and fcn["I66:230;64:181"]["cornerRadius"] == 9999, str(fcw))
record("변환(함수 컴포넌트 인스턴스): 안쪽 글자가 폰트·색과 함께 들어옴",
       fcn["I66:230;64:182"]["textColor"] == "#707070" and fcn["I66:230;64:182"]["font"]["weight"] == 600)
mx_code = fc_code.replace('data-node-id="64:181"', 'data-node-id="64:181"').replace('function ActionArea({ className, count = "1" }: ActionAreaProps) {',
          'function ActionArea({ className, count = "1" }: ActionAreaProps) {\n  const isTwo = count === "2";')
mxd, _mw = convert("### PAGE S7 Screens\n### FRAME 26:203\n### META\n" + fc_meta + "### CODE\n" + mx_code)
record("변환(함수 컴포넌트 인스턴스): 변형 분기가 있는 함수는 안쪽 노드를 넣지 않음", not any(n["id"].startswith("I66:230;") for n in mxd["frames"][0]["nodes"]))

rules_t = _copy.deepcopy(RULES)
rules_t["figma"]["pages"] = ["Dump Test"]
rules_t["figma"]["frames"] = ["screen/dump-test"]
rules_t["radius"]["input"] = 16  # 이 실제 샘플은 입력창 반경이 16이던 때 읽은 것이다
rules_t["radius"]["button"] = 9999  # 버튼 반경이 알약(9999)이던 때 읽은 샘플이다
for _k in ("작성 중", "임시저장", "제출 완료", "검수 대기"):  # 이 실제 샘플은 아이콘 없는 배지이던 때 읽은 것이다
    rules_t["status_badges"][_k].pop("icon", None)
rep = judge.check_dump(dump, rules_t, "key", "Dump Test")
got = {v["rule"] for v in rep.violations}
record("변환→판정: 실제 샘플에서 D05·D06·D07·D08만 위반", got == {"D05", "D06", "D07", "D08"}, f"실제 {sorted(got)}")

pc = f2d.parse_classes("font-['Pretendard:SemiBold'] text-[17px] tracking-[0.02em]")
record("변환: Pretendard SemiBold → 600", (pc["family"], pc["style"], pc["weight"]) == ("Pretendard", "SemiBold", 600))
record("변환: Medium → 500 (허용 굵기 밖이 되도록 계산)", f2d.parse_classes("font-['Pretendard:Medium']")["weight"] == 500)

tags_bundle = """### PAGE S7 Screens
### FRAME 1:1
### META
<frame id="1:1" name="screen/my-assets/register@seller" width="390" height="844">
  <frame id="1:2" name="visibility-selector" width="358" height="48">
    <frame id="1:3" name="option/private[selected]" width="100" height="40" />
    <frame id="1:4" name="option/member-only" width="100" height="40" />
  </frame>
  <frame id="1:5" name="submit-button[disabled]" width="358" height="48" />
  <frame id="1:6" name="text-input[focus]" width="358" height="48" />
  <frame id="1:7" name="status-badge" width="60" height="24">
    <text id="1:8" name="badge-label" width="40" height="15" />
    <frame id="1:9" name="icon/check" width="12" height="12" />
  </frame>
</frame>
### CODE
<div className="bg-white flex px-[16px]" data-node-id="1:1">
  <div className="bg-[#f3f3f3]" data-node-id="1:2">
    <div className="bg-[#141414] rounded-[9999px]" data-node-id="1:3"></div>
    <div className="bg-white rounded-[9999px]" data-node-id="1:4"></div>
  </div>
  <div className="bg-[#141414] rounded-[9999px]" data-node-id="1:5"></div>
  <div className="bg-[#f0f0f0] rounded-[16px] border-2 border-[#141414]" data-node-id="1:6"></div>
  <div className="bg-[#141414] rounded-[9999px] px-[8px]" data-node-id="1:7">
    <p className="font-['Pretendard:SemiBold'] text-[12px] text-white" data-node-id="1:8">승인됨</p>
  </div>
</div>
"""
td, tw = convert(tags_bundle)
tn = {n["name"]: n for n in td["frames"][0]["nodes"]}
record("상태 표기: [selected] → 이름에서 떼고 selected=true, 기본은 false", (tn["option/private"]["selected"], tn["option/member-only"]["selected"]) == (True, False))
record("상태 표기: [disabled] → variant=disabled", tn["submit-button"]["variant"] == "disabled")
record("상태 표기: [focus] → state=focus, 포커스 링 2px #141414", (tn["text-input"]["state"], tn["text-input"]["strokes"]) == ("focus", [{"color": "#141414", "weight": 2, "style": "solid"}]))
record("상태 표기: 배지 icon/check → ✓, 라벨 승인됨", (tn["status-badge"]["icon"], tn["status-badge"]["text"], tn["status-badge"]["textColor"]) == ("✓", "승인됨", "#ffffff"))
vd = f2d.parse_vars('{"color/ink": "#141414", "radius/card": 24, "space/md": "16px", "note": "x"}')
record("변환: 변수 분류(색·반경·간격)", vd == {"colors": ["#141414"], "radius": [24], "spacing": [16]})

# ---- 변환기: drop-shadow-[…]도 그림자로 읽는다 ----
_sd, _sw = convert("### PAGE S7 Screens\n### FRAME 1:2\n### META\n<frame id=\"1:2\" name=\"screen/home\" x=\"0\" y=\"0\" width=\"390\" height=\"844\"><frame id=\"1:3\" name=\"tab-bar\" x=\"16\" y=\"0\" width=\"358\" height=\"64\" /></frame>\n### CODE\nexport default function X() { return (<div className=\"bg-white size-full\" data-node-id=\"1:2\" data-name=\"screen/home\"><div className=\"bg-white drop-shadow-[0px_4px_8px_rgba(20,20,20,0.1)] size-full\" data-node-id=\"1:3\" data-name=\"tab-bar\" /></div>); }\n")
record("변환: drop-shadow-[…] → effects DROP_SHADOW", any(e.get("type") == "DROP_SHADOW" for n in _sd["frames"][0]["nodes"] for e in (n.get("effects") or [])), str(_sw))

# ---- 그림자 예외: tab-bar만 허용, 다른 노드는 D05 ----
def _with_shadow(node_name):
    d = copy.deepcopy(load("pass.json"))
    n = next(x for x in d["frames"][0]["nodes"] if x.get("name") and not x.get("effects"))
    n["name"] = node_name
    n["effects"] = [{"type": "DROP_SHADOW"}]
    return d


rep = judge.check_dump(_with_shadow("tab-bar"), RULES, "final", "S7 Screens")
record("D05 예외: tab-bar 그림자는 통과", not any(v["rule"] == "D05" for v in rep.violations), "; ".join(rep.messages()))
rep = judge.check_dump(_with_shadow("skill-card"), RULES, "final", "S7 Screens")
record("D05: tab-bar 아닌 노드의 그림자는 실패", any(v["rule"] == "D05" for v in rep.violations), "; ".join(rep.messages()))

bad = 0
for name, ok, detail in results:
    print(("PASS " if ok else "FAIL ") + name + ("" if ok else f"  ← {detail}"))
    bad += 0 if ok else 1
print(f"\n{len(results) - bad}/{len(results)} 일치")
sys.exit(1 if bad else 0)
