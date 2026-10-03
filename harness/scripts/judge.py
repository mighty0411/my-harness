#!/usr/bin/env python3
"""판정 스크립트: dump JSON을 rules.json과 대조하고 게이트 G1~G8을 판정한다.

사용법
  judge.py check <dump.json> [--mode key|final|components] [--page 페이지] [--out 리포트.json]
  judge.py gate G1..G8 [--output output 폴더]

종료 코드: 0 = 통과, 1 = 위반 또는 게이트 실패

dump JSON 형식 (Figma 조회 결과를 save_dump.py로 저장한 것)
{
  "variables": {"colors": [...], "radius": [...], "spacing": [...]},   # S6 dump에만
  "frames": [{
    "id": "1:2", "name": "screen/home", "page": "S7 Screens",
    "width": 390, "height": 844, "padding": {"left": 16, "right": 16},
    "nodes": [{
      "id": "1:3", "name": "button/primary", "type": "FRAME|TEXT|...",
      "role": "button|badge|toggle|tab|input|faq_row|card|media|app_icon|placeholder",  # 없으면 이름으로 추정
      "fills": ["#141414"], "strokes": [{"color": "#e0e0e0", "weight": 1, "style": "solid|dashed"}],
      "cornerRadius": 9999, "cornerRadiusPct": 30, "height": 48, "interactive": true,
      "padding": {"left": 16, "right": 16, "top": 0, "bottom": 0}, "itemSpacing": 8,
      "effects": [{"type": "DROP_SHADOW"}], "gradient": false,
      "text": "내용", "textColor": "#141414", "bg": "#ffffff",
      "font": {"family": "Pretendard", "weight": 700, "size": 28},
      "letterSpacing": 0, "textCase": "ORIGINAL",
      "state": "rest|focus", "variant": "disabled", "selected": true, "icon": "✓"
    }]
  }]
}
필드가 없으면 위반이 아니라 "판정 불가(unverifiable)"로 기록한다.
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RULES_PATH = ROOT / "harness" / "rules.json"
RULE_IDS = [f"D{i:02d}" for i in range(1, 13)] + ["V1", "V2", "badge"]
COMPONENT_RULES = {"D02", "D04", "D07", "D09"}
SCREEN_KEYS = ["홈", "스킬 라이브러리", "내 자산"]

ROLE_HINTS = [
    ("status-badge", "badge"), ("badge", "badge"), ("toggle", "toggle"),
    ("tab-bar/tab", "tab"), ("tab-bar", "tab"), ("button", "button"),
    ("input", "input"), ("faq-row", "faq_row"), ("skill-card", "card"),
    ("card", "card"), ("app-icon", "app_icon"), ("media", "media"),
]


# ---------- 공통 ----------
def load_rules(path=None):
    with open(path or RULES_PATH, encoding="utf-8") as f:
        return json.load(f)


def read_text(p):
    p = Path(p)
    return p.read_text(encoding="utf-8") if p.exists() else None


def read_json(p):
    t = read_text(p)
    return json.loads(t) if t is not None else None


def norm_color(c):
    c = re.sub(r"\s+", "", str(c)).lower()
    if re.fullmatch(r"#[0-9a-f]{3}", c):
        c = "#" + "".join(ch * 2 for ch in c[1:])
    return c


def is_hex(c):
    return bool(re.fullmatch(r"#[0-9a-f]{6}", c))


def luminance(hexc):
    h = hexc.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))

    def f(v):
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4

    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def contrast(fg, bg):
    a, b = sorted((luminance(fg), luminance(bg)), reverse=True)
    return (a + 0.05) / (b + 0.05)


def role_of(n):
    if n.get("role"):
        return n["role"]
    name = str(n.get("name", "")).lower()
    for key, role in ROLE_HINTS:
        if key in name:
            return role
    return None


def node_colors(n):
    out = []
    for c in n.get("fills") or []:
        out.append(("fill", c))
    for s in n.get("strokes") or []:
        out.append(("stroke", s.get("color")))
    if n.get("textColor"):
        out.append(("text", n["textColor"]))
    return [(k, norm_color(c)) for k, c in out if c]


class Report:
    def __init__(self):
        self.violations = []
        self.unverifiable = []
        self._seen = set()

    def violate(self, rule, frame, node, msg):
        key = (rule, frame, node, msg)
        if key in self._seen:
            return
        self._seen.add(key)
        self.violations.append({"rule": rule, "frame": frame, "node": node, "message": msg})

    def unknown(self, rule, frame, node, missing):
        self.unverifiable.append({"rule": rule, "frame": frame, "node": node, "missing": missing})

    def counts(self):
        c = {r: 0 for r in RULE_IDS}
        for v in self.violations:
            c[v["rule"]] = c.get(v["rule"], 0) + 1
        return c

    def messages(self, only=None):
        return [f'{v["rule"]} [{v["frame"]}] {v["node"] or ""}: {v["message"]}'
                for v in self.violations if only is None or v["rule"] in only]


# ---------- 프레임 선택 ----------
def base_name(name):
    """화면 기준 이름. 상태(@seller)와 안 표시(#A)를 뗀다: screen/home#A → screen/home"""
    return str(name).split("@")[0].split("#")[0]


def variant_of(name):
    """안 표시. 'screen/home#A' → 'A', 없으면 ''"""
    head = str(name).split("@")[0]
    return head.split("#", 1)[1] if "#" in head else ""


def page_key(name):
    """페이지 이름 비교용. 'S7 Screens (화면 디자인)' 처럼 괄호 설명이 붙어도 'S7 Screens'로 본다"""
    return (name or "").split(" (")[0].strip()


def select_frames(dump, rules, mode, page=None):
    fg = rules["figma"]
    pages = [page_key(p) for p in fg["pages"]]
    out = []
    for f in dump.get("frames", []):
        fpage = page_key(f.get("page"))
        if page and fpage != page_key(page):
            continue
        if mode == "components":
            if fpage == "S6 Components":
                out.append(f)
        elif fpage in pages and base_name(f.get("name", "")) in fg["frames"]:
            out.append(f)
    return out


# ---------- 규칙 검사 ----------
def check_dump(dump, rules, mode="final", page=None):
    rep = Report()
    comp = mode == "components"
    active = COMPONENT_RULES if comp else set(RULE_IDS)
    frames = select_frames(dump, rules, mode, page)

    allowed = {norm_color(c) for c in rules["colors"]}
    accent = norm_color(rules["accent"]["hex"])
    rad = rules["radius"]
    radius_expect = {
        "button": [rad["button"]], "badge": [rad["badge"]], "toggle": [rad["toggle"]],
        "tab": [rad["tab"]], "input": [rad["input"]], "faq_row": [rad["faq_row"]],
        "card": [rad["card"]], "media": list(rad["media"]),
    }
    font = rules["font"]
    steps = set(rules["spacing"]["steps"])
    side = rules["spacing"]["screen_side_padding"]
    fsize = rules["frame"]
    forbid = [(norm_color(x["fg"]), norm_color(x["bg"])) for x in rules["contrast"]["forbid"]]

    for fr in frames:
        fname = fr.get("name", "?")
        nodes = fr.get("nodes", []) or []

        if "D01" in active and (fr.get("width") != fsize["width"] or fr.get("height") != fsize["height"]):
            rep.violate("D01", fname, None, f'프레임 크기 {fr.get("width")}×{fr.get("height")}')
        if "D09" in active and not comp:
            pad = fr.get("padding")
            if pad is None:
                rep.unknown("D09", fname, None, "frame.padding")
            elif pad.get("left") != side or pad.get("right") != side:
                rep.violate("D09", fname, None, f"화면 좌우 패딩 {pad.get('left')}/{pad.get('right')}")

        accent_nodes = 0
        for n in nodes:
            nid = n.get("id") or n.get("name")
            role = role_of(n)
            colors = node_colors(n)

            if "D02" in active:
                for kind, c in colors:
                    if c not in allowed:
                        rep.violate("D02", fname, nid, f"허용되지 않은 {kind} 색 {c}")

            if "D03" in active:
                if any(c == accent for _, c in colors):
                    accent_nodes += 1
                    if role == "button":
                        rep.violate("D03", fname, nid, "CTA 버튼에 accent 사용")

            if "D04" in active:
                if role in radius_expect:
                    cr = n.get("cornerRadius")
                    if cr is None:
                        rep.unknown("D04", fname, nid, "cornerRadius")
                    elif cr not in radius_expect[role]:
                        rep.violate("D04", fname, nid, f"{role} 반경 {cr}, 허용 {radius_expect[role]}")
                elif role == "app_icon":
                    pct = n.get("cornerRadiusPct")
                    if pct is None:
                        rep.unknown("D04", fname, nid, "cornerRadiusPct")
                    elif pct != rad["app_icon_pct"]:
                        rep.violate("D04", fname, nid, f"앱 아이콘 반경 {pct}%")

            if "D05" in active:
                for e in n.get("effects") or []:
                    if "SHADOW" in str(e.get("type", "")).upper():
                        if not any(x in str(n.get("name", "")) for x in rules["shadow"]["exceptions"]):
                            rep.violate("D05", fname, nid, "그림자 사용")

            if "D06" in active and n.get("gradient") and role != "media":
                rep.violate("D06", fname, nid, "UI 요소에 그라디언트")

            if n.get("type") == "TEXT":
                if "D07" in active:
                    f = n.get("font")
                    if not f:
                        rep.unknown("D07", fname, nid, "font")
                    else:
                        if f.get("family") != font["family"]:
                            rep.violate("D07", fname, nid, f'폰트 {f.get("family")}')
                        if f.get("weight") not in font["weights"]:
                            rep.violate("D07", fname, nid, f'굵기 {f.get("weight")}')
                        if f.get("size") not in font["sizes"]:
                            rep.violate("D07", fname, nid, f'크기 {f.get("size")}')
                if "D08" in active:
                    if n.get("letterSpacing") not in (None, 0):
                        rep.violate("D08", fname, nid, f'자간 {n.get("letterSpacing")}')
                    if str(n.get("textCase", "ORIGINAL")).upper() == "UPPER":
                        rep.violate("D08", fname, nid, "대문자 표기")
                if "D12" in active and role != "placeholder" and n.get("textColor"):
                    fg = norm_color(n["textColor"])
                    bg_raw = n.get("bg") or (n.get("fills") or [None])[0]
                    if not bg_raw:
                        rep.unknown("D12", fname, nid, "bg")
                    else:
                        bg = norm_color(bg_raw)
                        if (fg, bg) in forbid:
                            rep.violate("D12", fname, nid, f"금지 조합 {fg} on {bg}")
                        if is_hex(fg) and is_hex(bg):
                            ratio = contrast(fg, bg)
                            if ratio < rules["contrast"]["text_min"]:
                                rep.violate("D12", fname, nid, f"대비 {ratio:.2f}:1")
                        else:
                            rep.unknown("D12", fname, nid, "hex 색이 아님")

            if "D09" in active:
                if n.get("itemSpacing") is not None and n["itemSpacing"] not in steps:
                    rep.violate("D09", fname, nid, f'itemSpacing {n["itemSpacing"]}')
                for k, v in (n.get("padding") or {}).items():
                    if v not in steps:
                        rep.violate("D09", fname, nid, f"padding.{k} {v}")

            if "D10" in active and (n.get("interactive") or role in ("button", "tab", "input", "toggle")):
                h = n.get("height")
                if h is None:
                    rep.unknown("D10", fname, nid, "height")
                elif h < rules["touch_target_min_height"]:
                    rep.violate("D10", fname, nid, f"높이 {h}")

            if "D11" in active and role == "input":
                strokes = n.get("strokes") or []
                if n.get("state", "rest") == "focus":
                    ring = str(rules["input"]["focus_ring"]).split()  # 예: "1px #141414"
                    want_w, want_c = int(ring[0].rstrip("px")), norm_color(ring[1])
                    ok = (len(strokes) == 1 and strokes[0].get("weight") == want_w
                          and norm_color(strokes[0].get("color", "")) == want_c)
                    if not ok:
                        rep.violate("D11", fname, nid, f"포커스 링이 {rules['input']['focus_ring']}가 아님")
                elif strokes:
                    rep.violate("D11", fname, nid, "기본 상태에 테두리")

        if "D03" in active and accent_nodes > rules["accent"]["max_per_frame"]:
            rep.violate("D03", fname, None, f"accent 사용 요소 {accent_nodes}개")

    if not comp:
        check_v1(frames, rules, mode, rep)
        check_v2(frames, rules, mode, rep)
        check_badges(frames, rules, rep)
    return rep


def _variants(frames, base):
    return [f for f in frames if base_name(f.get("name", "")) == base]


def _missing_state_frames(frames, base, suffixes, mode, rule, rep):
    # 안 표시(#A)는 떼고 비교한다: screen/my-assets/register#A@seller → screen/my-assets/register@seller
    present = {re.sub(r"#[^@]*", "", f["name"]) for f in frames}
    for suf in suffixes:
        if base + suf not in present:
            msg = f"상태 프레임 {base + suf} 없음"
            if mode == "final":
                rep.violate(rule, base, None, msg)
            else:
                rep.unknown(rule, base, None, base + suf)


def check_v1(frames, rules, mode, rep):
    base = "screen/my-assets/register"
    regs = _variants(frames, base)
    if not regs:
        if mode == "final":
            rep.violate("V1", base, None, "자산 등록 프레임 없음")
        return
    default = rules["violations"]["V1"]["default_option"]
    for f in regs:
        nodes = f.get("nodes", []) or []
        names = {n.get("name") for n in nodes}
        if "visibility-selector" not in names:
            rep.violate("V1", f["name"], None, "visibility-selector 없음")
        selected = [n["name"] for n in nodes if str(n.get("name", "")).startswith("option/") and n.get("selected")]
        if selected != [default]:
            rep.violate("V1", f["name"], None, f"기본 선택 {selected}, 기대 [{default}]")
        if f["name"].endswith("@non-seller") and "option/sale-request" in names:
            rep.violate("V1", f["name"], None, "seller가 아닌 상태에 option/sale-request 노출")
    _missing_state_frames(frames, base, rules["figma"]["state_suffixes"]["V1"], mode, "V1", rep)


def check_v2(frames, rules, mode, rep):
    base = "screen/my-assets/sale-request"
    frs = _variants(frames, base)
    if not frs:
        if mode == "final":
            rep.violate("V2", base, None, "판매 신청 프레임 없음")
        return
    phrases = rules["violations"]["V2"]["required_phrases"]
    for f in frs:
        nodes = f.get("nodes", []) or []
        text = " ".join(str(n.get("text", "")) for n in nodes)
        for p in phrases:
            if p not in text:
                rep.violate("V2", f["name"], None, f"금지 항목 문구 '{p}' 없음")
        if not any(str(n.get("name", "")).startswith("confirm-checkbox") for n in nodes):
            rep.violate("V2", f["name"], None, "confirm-checkbox 없음")
        if f["name"].endswith("@unchecked"):
            subs = [n for n in nodes if str(n.get("name", "")).startswith("submit-button")]
            if not subs:
                rep.violate("V2", f["name"], None, "submit-button 없음")
            elif any(n.get("variant") != "disabled" for n in subs):
                rep.violate("V2", f["name"], None, "체크 전 submit-button이 disabled가 아님")
    _missing_state_frames(frames, base, rules["figma"]["state_suffixes"]["V2"], mode, "V2", rep)


def check_badges(frames, rules, rep):
    spec_all = rules["status_badges"]
    for f in frames:
        for n in f.get("nodes", []) or []:
            if not str(n.get("name", "")).startswith("status-badge"):
                continue
            fname, nid = f["name"], n.get("id") or n.get("name")
            label = n.get("text")
            if not label:
                rep.violate("badge", fname, nid, "텍스트 라벨 없음")
                continue
            spec = spec_all.get(label)
            if spec is None:
                rep.violate("badge", fname, nid, f"정의되지 않은 상태 '{label}'")
                continue
            fills = [norm_color(c) for c in (n.get("fills") or [])]
            strokes = n.get("strokes") or []
            if "fill" in spec:
                if fills != [norm_color(spec["fill"])]:
                    rep.violate("badge", fname, nid, f"{label} 채움 {fills}")
            elif fills:
                rep.violate("badge", fname, nid, f"{label}에 채움 있음 {fills}")
            if "stroke" in spec:
                if len(strokes) != 1 or norm_color(strokes[0].get("color", "")) != norm_color(spec["stroke"]):
                    rep.violate("badge", fname, nid, f"{label} 외곽선 불일치")
                else:
                    want = spec.get("stroke_style", "solid")
                    if strokes[0].get("style", "solid") != want:
                        rep.violate("badge", fname, nid, f"{label} 외곽선 스타일 {strokes[0].get('style')}")
            elif strokes:
                rep.violate("badge", fname, nid, f"{label}에 외곽선 있음")
            if norm_color(n.get("textColor", "")) != norm_color(spec["text"]):
                rep.violate("badge", fname, nid, f'{label} 글자색 {n.get("textColor")}')
            if (n.get("icon") or None) != spec.get("icon"):
                rep.violate("badge", fname, nid, f'{label} 아이콘 {n.get("icon")}')
            f_ = n.get("font") or {}
            if f_ and (f_.get("size") != 12 or f_.get("weight") != 600):
                rep.violate("badge", fname, nid, "배지 글자는 12px/600이어야 함")


# ---------- 마크다운 게이트 ----------
def parse_sections(text):
    sec, cur = {}, None
    for line in text.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            cur = m.group(1)
            sec[cur] = []
        elif cur is not None:
            sec[cur].append(line)
    return sec


def ref_ids(out):
    t = read_text(out / "research/s1-references.md") or ""
    return set(re.findall(r"^\s*-\s+(R-\d+)\s*\|", t, flags=re.M))


def active_screens(out, rules):
    """대상 화면: output/run/state.json 의 input.screens, 없으면 rules.json 기본(3개)."""
    allowed = rules["gates"]["screens"]
    st = read_json(out / "run/state.json")
    screens = (st or {}).get("input", {}).get("screens") or allowed
    return [s for s in screens if s in allowed] or allowed


def variants_per_screen(out):
    """화면마다 만들 시안 수: output/run/state.json 의 input.variants. 없으면 1 (안 구분 없음)"""
    st = read_json(out / "run/state.json")
    try:
        return max(1, int((st or {}).get("input", {}).get("variants") or 1))
    except (TypeError, ValueError):
        return 1


def gate_G1(out, rules):
    g, gs = rules["gates"]["G1"], active_screens(out, rules)
    t = read_text(out / "research/s1-references.md")
    if t is None:
        return ["output/research/s1-references.md 없음"]
    msgs, sec, ids = [], parse_sections(t), []
    comp = [l for l in sec.get("경쟁사", []) if re.match(r"^\s*-\s+\S", l)]
    if len(comp) < g["competitors_min"]:
        msgs.append(f'경쟁사 {len(comp)}개 (최소 {g["competitors_min"]})')
    for screen in gs:
        refs = [l for l in sec.get(screen, []) if re.match(r"^\s*-\s+R-\d+\s*\|", l)]
        if len(refs) < g["refs_per_screen_min"]:
            msgs.append(f'{screen} 레퍼런스 {len(refs)}개 (최소 {g["refs_per_screen_min"]})')
        for l in refs:
            rid = re.match(r"^\s*-\s+(R-\d+)", l).group(1)
            ids.append(rid)
            if not re.search(r"https?://", l):
                msgs.append(f"{rid}에 URL 없음")
    if len(ids) != len(set(ids)):
        msgs.append("레퍼런스 ID 중복")
    return msgs


def gate_G2(out, rules):
    g, gs = rules["gates"]["G2"], active_screens(out, rules)
    t = read_text(out / "research/s2-analysis.md")
    if t is None:
        return ["output/research/s2-analysis.md 없음"]
    known, msgs, per = ref_ids(out), [], {s: 0 for s in gs}
    points = [l for l in t.splitlines() if re.match(r"^\s*-\s+P-\d+\s*\|", l)]
    for l in points:
        parts = [p.strip() for p in l.split("|")]
        pid = re.match(r"^\s*-\s+(P-\d+)", l).group(1)
        if parts[1] in per:
            per[parts[1]] += 1
        else:
            msgs.append(f"{pid}: 알 수 없는 화면 '{parts[1]}'")
        cited = re.findall(r"R-\d+", parts[-1]) if "근거" in parts[-1] else []
        if not cited:
            msgs.append(f"{pid}: 근거 레퍼런스 없음")
        for r in cited:
            if r not in known:
                msgs.append(f"{pid}: 근거 {r}가 s1에 없음")
    need = min(g["points_min"], g["points_per_screen_min"] * len(gs))
    if len(points) < need:
        msgs.append(f'반영 포인트 {len(points)}개 (최소 {need})')
    for s, c in per.items():
        if c < g["points_per_screen_min"]:
            msgs.append(f'{s} 반영 포인트 {c}개 (최소 {g["points_per_screen_min"]})')
    return msgs


def gate_G3(out, rules):
    g, gs = rules["gates"]["G3"], active_screens(out, rules)
    t = read_text(out / "spec/s3-screen-spec.md")
    if t is None:
        return ["output/spec/s3-screen-spec.md 없음"]
    msgs, sec = [], parse_sections(t)
    for s in gs:
        if s not in sec:
            msgs.append(f"화면 섹션 '{s}' 없음")
            continue
        lines = [l.strip() for l in sec[s]]
        for sub in g["required_subsections"]:
            if f"### {sub}" not in lines:
                msgs.append(f"{s}: '### {sub}' 없음")
    body = "\n".join(sec.get("내 자산", []))
    for w in (g["my_assets_required"] if "내 자산" in gs else []):
        if w not in body:
            msgs.append(f"내 자산: '{w}' 명시 없음 (V1·V2 요구)")
    for i, line in enumerate(t.splitlines(), 1):
        for term in g["mvp_excluded_terms"]:
            if term in line and g["exclusion_marker"] not in line:
                msgs.append(f"{i}행: MVP 제외 표현 '{term}'")
    return msgs


def _load_dump(out, name, msgs):
    d = read_json(out / f"verdict/dump/{name}.json")
    if d is None:
        msgs.append(f"output/verdict/dump/{name}.json 없음")
    return d


def gate_G4(out, rules):
    msgs = []
    d = _load_dump(out, "s4", msgs)
    if d is None:
        return msgs, None
    g = rules["gates"]["G4"]
    fmin = min(g["frames_min"], len(active_screens(out, rules)))
    frames = select_frames(d, rules, "key", page="S4 Keyscreens")
    bases = {base_name(f["name"]) for f in frames}
    if not fmin <= len(bases) <= g["frames_max"]:
        msgs.append(f'키스크린 {len(bases)}개 (허용 {fmin}~{g["frames_max"]})')
    nvar = variants_per_screen(out)
    if nvar > 1:
        vmin, vmax = g["variants_min"], min(g["variants_max"], nvar)
        for b in sorted(bases):
            tags = {variant_of(f["name"]) for f in frames if base_name(f["name"]) == b}
            if "" in tags:
                msgs.append(f"{b}: 안 표시(#A 등) 없는 프레임이 있음")
            n = len(tags - {""})
            if not vmin <= n <= vmax:
                msgs.append(f"{b}: 시안 {n}안 (허용 {vmin}~{vmax}안)")
    rep = check_dump(d, rules, "key", page="S4 Keyscreens")
    msgs += rep.messages()
    return msgs, rep


def _ids_in(text, pattern):
    ids = []
    for m in re.finditer(pattern, text or "", flags=re.M):
        ids += [x.strip() for x in m.group(1).split(",") if x.strip()]
    return set(ids)


def gate_G5(out, rules):
    s4 = read_text(out / "design/s4-keyscreens.md")
    s5 = read_text(out / "run/s5-approval.md")
    if s5 is None:
        return ["output/run/s5-approval.md 없음 (사람 승인 전)"]
    if s4 is None:
        return ["output/design/s4-keyscreens.md 없음"]
    s4_ids = _ids_in(s4, r"^\s*-\s*frame:\s*(\S+)")
    ok_ids = _ids_in(s5, r"확정 프레임 ID:\s*(.+)")
    if not ok_ids:
        return ["확정 프레임 ID 없음"]
    extra = ok_ids - s4_ids
    if extra:
        return [f"S4에 없는 프레임 ID: {sorted(extra)}"]
    if variants_per_screen(out) <= 1:
        return []
    # 안 방식: 화면마다 안 하나만 확정. S4 문서의 '- frame: <ID> | <이름>' 에서 이름을 찾는다
    names = {}
    for m in re.finditer(r"^\s*-\s*frame:\s*(\S+)\s*\|\s*(.+?)\s*$", s4, flags=re.M):
        names[m.group(1)] = m.group(2)
    chosen, msgs = {}, []
    for i in sorted(ok_ids):
        nm = names.get(i, "")
        chosen.setdefault(base_name(nm), set()).add(variant_of(nm))
    for b, tags in sorted(chosen.items()):
        if "" in tags or len(tags) != 1:
            msgs.append(f"{b}: 확정한 안이 하나가 아님 {sorted(tags)} (화면마다 안 하나만 확정)")
    screens = rules["gates"]["screen_frames"]
    for sc in active_screens(out, rules):
        if screens.get(sc) not in chosen:
            msgs.append(f"{sc}: 확정한 안 없음")
    return msgs


def gate_G6(out, rules):
    msgs = []
    d = _load_dump(out, "s6", msgs)
    if d is None:
        return msgs, None
    rep = check_dump(d, rules, "components")
    msgs += rep.messages(COMPONENT_RULES)
    frames = select_frames(d, rules, "components")
    names = {f.get("name", "") for f in frames} | {n.get("name", "") for f in frames for n in f.get("nodes", []) or []}
    for c in rules["gates"]["G6"]["components"]:
        if not any(nm == c or nm.startswith(c + "/") or nm.startswith(c) for nm in names):
            msgs.append(f"컴포넌트 '{c}' 없음")
    v = d.get("variables")
    if not v:
        msgs.append("variables 없음 (변수 값을 검사할 수 없음)")
    else:
        colors = {norm_color(c) for c in rules["colors"]}
        rad = rules["radius"]
        radii = {rad[k] for k in ("button", "badge", "toggle", "tab", "input", "faq_row", "card")} | set(rad["media"])
        steps = set(rules["spacing"]["steps"])
        for c in v.get("colors", []):
            if norm_color(c) not in colors:
                msgs.append(f"변수 색 {c}이 rules.json에 없음")
        for r in v.get("radius", []):
            if r not in radii:
                msgs.append(f"변수 반경 {r}이 rules.json에 없음")
        for s in v.get("spacing", []):
            if s not in steps:
                msgs.append(f"변수 스페이싱 {s}이 rules.json에 없음")
    return msgs, rep


def gate_G7(out, rules):
    msgs = []
    d = _load_dump(out, "s7", msgs)
    if d is None:
        return msgs, None
    frames = select_frames(d, rules, "final", page="S7 Screens")
    have = {base_name(f["name"]) for f in frames}
    required = [rules["gates"]["screen_frames"][s] for s in active_screens(out, rules)]
    for s in required:
        if s not in have:
            msgs.append(f"완성본 프레임 {s} 없음")
    rep = check_dump(d, rules, "final", page="S7 Screens")
    msgs += rep.messages({"badge"})
    return msgs, rep


def gate_G8(out, rules):
    msgs = []
    d = _load_dump(out, "s7", msgs)
    if d is None:
        return msgs, None
    rep = check_dump(d, rules, "final", page="S7 Screens")
    msgs += rep.messages()
    return msgs, rep


def run_gate(gate, out, rules):
    g = gate.upper()
    rep = None
    if g in ("G1", "G2", "G3", "G5"):
        msgs = {"G1": gate_G1, "G2": gate_G2, "G3": gate_G3, "G5": gate_G5}[g](out, rules)
    elif g in ("G4", "G6", "G7", "G8"):
        msgs, rep = {"G4": gate_G4, "G6": gate_G6, "G7": gate_G7, "G8": gate_G8}[g](out, rules)
    else:
        raise SystemExit(f"알 수 없는 게이트 {gate}")
    result = {"gate": g, "passed": not msgs, "messages": msgs,
              "violations": rep.violations if rep else [],
              "unverifiable": rep.unverifiable if rep else []}
    vdir = out / "verdict"
    vdir.mkdir(parents=True, exist_ok=True)
    (vdir / f"gate-{g}.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    if g == "G8" and rep is not None:
        report = {"passed": not msgs, "counts": rep.counts(),
                  "violations": rep.violations, "unverifiable": rep.unverifiable}
        (vdir / "s8-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check")
    c.add_argument("dump")
    c.add_argument("--mode", default="final", choices=["key", "final", "components"])
    c.add_argument("--page")
    c.add_argument("--rules")
    c.add_argument("--out")
    g = sub.add_parser("gate")
    g.add_argument("gate")
    g.add_argument("--output", default=str(ROOT / "output"))
    g.add_argument("--rules")
    a = ap.parse_args()

    rules = load_rules(a.rules)
    if a.cmd == "check":
        rep = check_dump(read_json(a.dump), rules, a.mode, a.page)
        result = {"passed": not rep.violations, "counts": rep.counts(),
                  "violations": rep.violations, "unverifiable": rep.unverifiable}
        if a.out:
            Path(a.out).parent.mkdir(parents=True, exist_ok=True)
            Path(a.out).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        sys.exit(0 if result["passed"] else 1)
    result = run_gate(a.gate, Path(a.output), rules)
    print(json.dumps({k: result[k] for k in ("gate", "passed", "messages")}, ensure_ascii=False, indent=2))
    sys.exit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
