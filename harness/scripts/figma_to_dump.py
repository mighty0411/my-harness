#!/usr/bin/env python3
"""Figma 읽기 결과(get_metadata XML + get_design_context 코드)를 dump JSON으로 변환한다.
변환은 규칙 기반이라 사람이나 LLM이 손으로 옮기다 생기는 오류가 없다. 결과는 stdout으로 나간다.

stdin 형식 (텍스트 묶음, 프레임을 여러 개 이어 붙일 수 있음)
  ### PAGE <페이지 이름>
  ### FRAME <프레임 ID> [+root]
  ### META
  <get_metadata XML>
  ### META            (선택, 여러 번 가능) variant 노드를 개별로 읽은 get_metadata. 같은 ID 의 자식을 대신한다
  <get_metadata XML>
  ### CODE
  <get_design_context 가 돌려준 React+Tailwind 코드>
  ### VARS            (선택) get_variable_defs 가 돌려준 JSON
  <JSON>

사용법
  figma_to_dump.py < bundle.txt | save_dump.py s7
  figma_to_dump.py --summary < bundle.txt        # 프레임·노드 수와 경고만 출력

규칙 (원본: rules.json figma)
  - 노드 이름 끝의 [selected] [disabled] [focus] 는 상태 표기다: 이름에서 떼어 내고 selected / variant / state 필드로 옮긴다
  - status-badge 는 안의 첫 TEXT 를 text·textColor·font 로 접어 넣고, 자식 icon/check|alert|close 로 icon 을 정한다
  - 굵기는 폰트 스타일 이름(Pretendard:SemiBold 등)에서 rules.json font.weight_styles 로 계산한다
  - Tailwind 는 값이 0이면 클래스를 생략하므로, 생략된 반경·자간·패딩은 0으로 본다
  - 변수에 묶인 값은 var(--이름,기본값) 으로 나온다: 기본값(변수의 현재 값)을 읽는다 (예: rounded-[var(--radius\\/badge,9999px)] → 9999)
  - 컴포넌트 인스턴스는 <StatusBadge className="..."/> 로 나와 data-node-id 가 없다: 메타데이터의 인스턴스 이름(status-badge)과
    태그 이름(StatusBadge → status-badge)을 짝지어 문서 순서대로 스타일을 준다
  - variant 세트 프레임의 코드는 삼항식이라 읽을 수 없다: variant 자식 노드를 개별로 읽어 ### CODE 에 이어 붙인다 (r7 Figma 덤프)
  - 세트의 get_metadata 는 variant 자식(option/* 등)을 보여 주지 않는다: variant 별 get_metadata 를 ### META 로 더 붙이면 세트 안의 같은 ID 를 대신한다
  - 글자 색·폰트 패밀리·굵기·크기는 CSS 처럼 부모에서 자식 글자로 상속된다: 글자 노드에 없으면 가장 가까운 조상 값을 쓴다
  - 인스턴스 안쪽 노드(코드의 data-node-id="I26:234;23:55")는 get_metadata 에 나오지 않는다: 코드에만 있는 I 노드를 덤프에 넣는다.
    이름은 data-name(없으면 글자는 text), 부모는 코드의 태그 중첩으로 정하고, 글자 상속과 배경(bg)도 그 부모를 따른다
  - 화면 좌우 패딩(frame.padding): 루트에 좌우 패딩이 없고 이름이 content-area 인 노드가 있으면 그 노드의 좌우 패딩을 쓴다 (전체 폭 status-bar·header 때문에 여백이 content-area 에만 있는 구조)
  - 함수 컴포넌트로 나온 인스턴스(<ActionArea className=.../>): 안쪽 노드가 컴포넌트 정의의 ID(64:181)로만 나와 I 노드가 아니다.
    정의 안에 변형 분기(=== · && · id={… ? …})가 없는 함수만, 그 안의 노드를 메타의 같은 이름 인스턴스(action-area) 아래에
    I<인스턴스ID>;<정의ID> 로 넣는다. 한 프레임에 여러 변형을 섞어 쓴 함수(분기 있음)는 넣지 않는다 (그 안쪽은 검사되지 않는다)
  - +root: 프레임 루트 자체도 노드로 검사한다 (컴포넌트 루트의 배경·반경). 화면 프레임에는 쓰지 않는다
"""
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RULES = json.loads((ROOT / "harness" / "rules.json").read_text(encoding="utf-8"))
WEIGHTS = RULES["font"]["weight_styles"]
ICONS = RULES["figma"]["icon_nodes"]
TAGS = set(RULES["figma"]["state_tags"])
NAMED = {"white": "#ffffff", "black": "#000000"}
INHERIT = ("textColor", "family", "style", "weight", "size")
NAMED_RADIUS = {"sm": 2, "md": 6, "lg": 8, "xl": 12, "2xl": 16, "3xl": 24}

TAG_RE = re.compile(r"""<(\w+)((?:\s+[\w:.-]+(?:=(?:"[^"]*"|'[^']*'|\{\{[^{}]*\}\}|\{[^{}]*\}))?)*)\s*(/?)>""")
ATTR_RE = re.compile(r"""([\w:.-]+)(?:=(?:"([^"]*)"|'([^']*)'|\{\{([^{}]*)\}\}|\{([^{}]*)\}))?""")


def hex_norm(c):
    c = c.lower()
    if re.fullmatch(r"#[0-9a-f]{3}", c):
        c = "#" + "".join(ch * 2 for ch in c[1:])
    return c


def px(tok, prefix):
    """prefix-[12px] 또는 prefix-3 (=12px) 에서 숫자를 뽑는다."""
    m = re.fullmatch(prefix + r"-\[(-?\d+(?:\.\d+)?)px\]", tok)
    if m:
        return float(m.group(1)) if "." in m.group(1) else int(m.group(1))
    m = re.fullmatch(prefix + r"-(\d+(?:\.\d+)?)", tok)
    if m:
        v = float(m.group(1)) * 4
        return int(v) if v == int(v) else v
    return None


def strip_var(s):
    """var(--이름,기본값) 을 기본값으로 바꾼다. 기본값이 없거나 괄호가 안 닫히면 그대로 둔다."""
    out, i = [], 0
    while True:
        j = s.find("var(--", i)
        if j < 0:
            out.append(s[i:])
            return "".join(out)
        out.append(s[i:j])
        depth, k, comma = 0, j + 3, None
        while k < len(s):
            ch = s[k]
            if ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
                if depth == 0:
                    break
            elif ch == "," and depth == 1 and comma is None:
                comma = k
            k += 1
        if k >= len(s) or comma is None:
            out.append(s[j:k + 1])
        else:
            out.append(strip_var(s[comma + 1:k]))
        i = k + 1


def parse_classes(cls):
    # className={className || '...'} 처럼 클래스 목록을 감싼 따옴표만 떼고, font-["Pretendard:Bold"] 안의 따옴표는 둔다
    cls = re.sub(r"""(^|\s)['"]""", r"\1", cls)
    cls = re.sub(r"""['"](\s|$)""", r"\1", cls)
    cls = strip_var(cls)
    out = {"fills": [], "gradient": False, "effects": [], "padding": {}}
    border = {"present": False, "weight": 1, "color": None, "style": "solid"}
    for tok in cls.split():
        m = re.fullmatch(r"bg-\[(#[0-9a-fA-F]{3,8})\]", tok)
        if m:
            out["fills"].append(hex_norm(m.group(1)))
            continue
        m = re.fullmatch(r"bg-\[(white|black)\]", tok)
        if m:
            out["fills"].append(NAMED[m.group(1)])
            continue
        m = re.fullmatch(r"bg-\[(rgba?\([^)]*\))\]", tok)
        if m:
            out["fills"].append(m.group(1).replace("_", "").lower())
            continue
        if tok in ("bg-white", "bg-black"):
            out["fills"].append(NAMED[tok[3:]])
            continue
        if tok.startswith(("bg-gradient", "bg-linear", "bg-radial", "bg-conic")):
            out["gradient"] = True
            continue
        # 테두리
        if tok == "border":
            border["present"] = True
            continue
        if tok in ("border-solid", "border-dashed", "border-dotted"):
            border["style"] = tok[7:]
            continue
        m = re.fullmatch(r"border-\[(?:color:)?(#[0-9a-fA-F]{3,8})\]", tok)
        if m:
            border["present"], border["color"] = True, hex_norm(m.group(1))
            continue
        m = re.fullmatch(r"border-\[(?:color:)?(white|black)\]", tok)
        if m:
            border["present"], border["color"] = True, NAMED[m.group(1)]
            continue
        if tok in ("border-white", "border-black"):
            border["present"], border["color"] = True, NAMED[tok[7:]]
            continue
        m = re.fullmatch(r"border-\[(\d+(?:\.\d+)?)px\]", tok) or re.fullmatch(r"border-(\d+)", tok)
        if m:  # 테두리 굵기: border-2 는 2px (간격처럼 4배 하지 않는다)
            v = float(m.group(1))
            border["present"], border["weight"] = True, (int(v) if v == int(v) else v)
            continue
        # 반경
        if tok == "rounded-full":
            out["radius"] = 9999
        elif tok == "rounded-none":
            out["radius"] = 0
        elif tok == "rounded":
            out["radius"] = 4
        else:
            m = re.fullmatch(r"rounded-\[(\d+(?:\.\d+)?)px\]", tok)
            if m:
                out["radius"] = float(m.group(1)) if "." in m.group(1) else int(m.group(1))
            elif re.fullmatch(r"rounded-(sm|md|lg|xl|2xl|3xl)", tok):
                out["radius"] = NAMED_RADIUS[tok[8:]]
        # 폰트
        m = re.fullmatch(r"""font-\[['"]([^:'"]+):([^'"]+)['"]\]""", tok)
        if m:
            style = m.group(2).replace("_", "").replace(" ", "")
            out["family"], out["style"] = m.group(1).replace("_", " "), style
            out["weight"] = WEIGHTS.get(style)
            continue
        m = re.fullmatch(r"text-\[(\d+(?:\.\d+)?)px\]", tok)
        if m:
            out["size"] = float(m.group(1)) if "." in m.group(1) else int(m.group(1))
            continue
        m = re.fullmatch(r"text-\[(?:color:)?(#[0-9a-fA-F]{3,8})\]", tok)
        if m:
            out["textColor"] = hex_norm(m.group(1))
            continue
        m = re.fullmatch(r"text-\[(?:color:)?(white|black)\]", tok)
        if m:
            out["textColor"] = NAMED[m.group(1)]
            continue
        if tok in ("text-white", "text-black"):
            out["textColor"] = NAMED[tok[5:]]
            continue
        m = re.fullmatch(r"tracking-\[(-?\d+(?:\.\d+)?)(px|em)\]", tok)
        if m:
            v = float(m.group(1))
            out["tracking"] = (v, m.group(2))
            continue
        if tok in ("uppercase", "lowercase", "capitalize"):
            out["textCase"] = {"uppercase": "UPPER", "lowercase": "LOWER", "capitalize": "TITLE"}[tok]
            continue
        # 패딩·간격
        for key, sides in (("px", ("left", "right")), ("py", ("top", "bottom")), ("pl", ("left",)),
                           ("pr", ("right",)), ("pt", ("top",)), ("pb", ("bottom",)),
                           ("p", ("left", "right", "top", "bottom"))):
            v = px(tok, key)
            if v is not None:
                for s in sides:
                    out["padding"][s] = v
                break
        else:
            v = px(tok, "gap")
            if v is not None:
                out["gap"] = v
                continue
            # shadow-…, shadow-[…], drop-shadow-[0px_4px_8px_rgba(…)] 모두 그림자로 읽는다 (shadow-none·drop-shadow-none 제외)
            if (tok.startswith("shadow") or tok.startswith("drop-shadow")) and not tok.endswith("-none"):
                out["effects"].append({"type": "INNER_SHADOW" if "inset" in tok else "DROP_SHADOW"})
                continue
            for k, dim in (("w", "width"), ("h", "height")):
                v = px(tok, k)
                if v is not None:
                    out[dim] = v
            v = px(tok, "size")
            if v is not None:
                out["width"] = out["height"] = v
    if border["present"]:
        out["stroke"] = {"color": border["color"], "weight": border["weight"], "style": border["style"]}
    return out


def parse_bundle(text):
    page, frames, cur, mode, vars_lines = None, [], None, None, []
    for line in text.splitlines():
        m = re.match(r"^###\s+(PAGE|FRAME|META|CODE|VARS)\b\s*(.*)$", line)
        if m:
            kind, arg = m.group(1), m.group(2).strip()
            if kind == "PAGE":
                page, mode = arg, None
            elif kind == "FRAME":
                if not page:
                    sys.exit("### PAGE 가 ### FRAME 보다 먼저 있어야 합니다")
                parts = arg.split()
                cur = {"page": page, "id": parts[0] if parts else "", "root": "+root" in parts[1:], "meta": [], "code": []}
                frames.append(cur)
                mode = None
            elif kind == "VARS":
                mode = "vars"
            else:
                if cur is None:
                    sys.exit("### FRAME 없이 META/CODE 가 나왔습니다")
                mode = kind.lower()
                if mode == "meta":
                    cur["meta"].append([])
            continue
        if mode == "vars":
            vars_lines.append(line)
        elif cur is not None and mode == "meta":
            cur["meta"][-1].append(line)
        elif cur is not None and mode:
            cur[mode].append(line)
    return frames, "\n".join(vars_lines).strip()


def parse_meta(meta_text):
    s = meta_text.strip()
    i, j = s.find("<"), s.rfind(">")
    if i < 0 or j < 0:
        sys.exit("META 에서 XML 을 찾지 못했습니다")
    return ET.fromstring(s[i:j + 1])


def kebab(tag):
    return re.sub(r"(?<!^)(?=[A-Z])", "-", tag).lower()


CLOSE_RE = re.compile(r"</(\w+)\s*>")


def parse_code(code_text):
    """returns (노드 ID별 스타일, 컴포넌트 이름별 인스턴스 스타일 목록)
    스타일에는 tag, name(data-name), parent(태그 중첩상 가장 가까운 data-node-id 조상), order 도 담는다"""
    styles, comps = {}, {}
    starts = [(m.start(), m.group(1), m.group(0).startswith("export")) for m in
              re.finditer(r"^(?:export default )?function (\w+)\(", code_text, re.M)]
    blocks = []
    for bi, (st_pos, bname, is_default) in enumerate(starts):
        end = starts[bi + 1][0] if bi + 1 < len(starts) else len(code_text)
        body = code_text[st_pos:end]
        if not is_default:
            blocks.append((st_pos, end, bname, bool(re.search(r"===|&&|id=\{[^}]*\?", body))))
    events = [(m.start(), "open", m) for m in TAG_RE.finditer(code_text)]
    events += [(m.start(), "close", m) for m in CLOSE_RE.finditer(code_text)]
    stack = []  # (tag, nid or None)
    for _pos, kind, m in sorted(events, key=lambda e: e[0]):
        if kind == "close":
            for k in range(len(stack) - 1, -1, -1):
                if stack[k][0] == m.group(1):
                    del stack[k:]
                    break
            continue
        tag, attrs = m.group(1), m.group(2)
        a = {}
        for am in ATTR_RE.finditer(attrs):
            a[am.group(1)] = next((g for g in am.groups()[1:] if g is not None), "")
        nid = a.get("data-node-id")
        if not m.group(3):
            stack.append((tag, nid))
        if not nid:
            if tag[0].isupper() and a.get("className"):
                comps.setdefault(kebab(tag), []).append(parse_classes(a["className"]))
            continue
        st = parse_classes(a.get("className", a.get("class", "")))
        st["tag"], st["name"], st["order"] = tag, a.get("data-name", ""), len(styles)
        for b_start, b_end, b_name, b_mixed in blocks:
            if b_start <= _pos < b_end:
                st["func"], st["func_mixed"] = b_name, b_mixed
                break
        st["parent"] = next((n for t, n in reversed(stack[:-1] if not m.group(3) else stack) if n), None)
        if tag in ("p", "span", "h1", "h2", "h3", "h4", "h5", "h6"):
            end = code_text.find("<", m.end())
            st["text"] = code_text[m.end(): end if end >= 0 else None].strip()
        styles[nid] = st
    return styles, comps


def split_name(name):
    m = re.fullmatch(r"(.*?)((?:\[[a-z-]+\])+)", name)
    if not m:
        return name, []
    return m.group(1), re.findall(r"\[([a-z-]+)\]", m.group(2))


def to_num(v):
    return int(v) if isinstance(v, float) and v == int(v) else v


def build_node(el, st, parent_fill, warnings):
    base, tags = split_name(el.get("name", ""))
    is_text = el.tag == "text"
    n = {"id": el.get("id"), "name": base, "type": "TEXT" if is_text else "FRAME"}
    for k in ("width", "height"):
        v = el.get(k)
        if v is not None:
            n[k] = to_num(float(v))
    fills = list(st.get("fills", []))
    if not is_text:
        n["fills"] = fills
        n["cornerRadius"] = st.get("radius", 0)
        n["strokes"] = [st["stroke"]] if st.get("stroke") else []
        if st.get("stroke") and not st["stroke"]["color"]:
            warnings.append(f"{el.get('id')} {base}: 테두리 색을 읽지 못함")
        if st.get("padding"):
            n["padding"] = st["padding"]
        if st.get("gap") is not None:
            n["itemSpacing"] = st["gap"]
        if st.get("gradient"):
            n["gradient"] = True
    n["effects"] = st.get("effects", [])
    if is_text:
        n["text"] = st.get("text", "")
        if st.get("textColor"):
            n["textColor"] = st["textColor"]
        if st.get("family"):
            n["font"] = {"family": st["family"], "weight": st.get("weight"), "size": st.get("size")}
        tr = st.get("tracking")
        if tr is None:
            n["letterSpacing"] = 0
        else:
            n["letterSpacing"] = to_num(round(tr[0] * (st.get("size") or 0), 4)) if tr[1] == "em" else to_num(tr[0])
        n["textCase"] = st.get("textCase", "ORIGINAL")
        if parent_fill:
            n["bg"] = parent_fill
    for t in tags:
        if t not in TAGS:
            warnings.append(f"{el.get('id')} {base}: 알 수 없는 상태 표기 [{t}]")
    if base.startswith("option/"):
        n["selected"] = "selected" in tags
    if base.startswith(("submit-button", "button")):
        n["variant"] = "disabled" if "disabled" in tags else "enabled"
    if "focus" in tags:
        n["state"] = "focus"
    return n


def convert_frame(fr, warnings):
    root = parse_meta("\n".join(fr["meta"][0]))
    for extra in fr["meta"][1:]:  # variant 별 메타: 세트 안의 같은 ID 를 대신한다
        e = parse_meta("\n".join(extra))
        for parent in root.iter():
            kids = list(parent)
            for i, k in enumerate(kids):
                if k.get("id") == e.get("id"):
                    parent.remove(k)
                    parent.insert(i, e)
    styles, comps = parse_code("\n".join(fr["code"]))
    nodes = []
    root_st = styles.get(root.get("id"), {})
    pad = root_st.get("padding", {})
    if not (pad.get("left") or pad.get("right")):
        # 상태 표시줄·헤더처럼 전체 폭 영역이 있는 화면은 좌우 여백이 루트가 아니라 content-area 에 있다
        ca = next((e for e in root.iter() if split_name(e.get("name", ""))[0] == "content-area"), None)
        cp = styles.get(ca.get("id"), {}).get("padding", {}) if ca is not None else {}
        if cp.get("left") or cp.get("right"):
            pad = cp
    frame = {"id": root.get("id"), "name": root.get("name", ""), "page": fr["page"],
             "width": to_num(float(root.get("width", 0))), "height": to_num(float(root.get("height", 0))),
             "padding": {"left": pad.get("left", 0), "right": pad.get("right", 0)}, "nodes": nodes}
    if root.get("id") not in styles:
        warnings.append(f'프레임 {root.get("id")}: CODE 에서 스타일을 찾지 못함')

    def walk(el, parent_fill, parent_gradient, inh):
        for child in el:
            st = styles.get(child.get("id"))
            if st is None and child.tag == "instance":
                queue = comps.get(split_name(child.get("name", ""))[0])
                if queue:
                    st = queue.pop(0)
            if st is None:
                warnings.append(f'{child.get("id")} {child.get("name")}: CODE 에 없음 (크기·이름만 기록)')
                st = {}
            child_inh = {**inh, **{k: st[k] for k in INHERIT if k in st}}
            eff = {**{k: v for k, v in inh.items() if k not in st}, **st} if child.tag == "text" else st
            node = build_node(child, eff, None if parent_gradient else parent_fill, warnings)
            nodes.append(node)
            own = st.get("fills", [])
            next_fill = own[0] if own else parent_fill
            walk(child, next_fill, parent_gradient or (st.get("gradient") and not own), child_inh)
            if node["name"].startswith("status-badge"):
                fold_badge(node, child, nodes)

    def fold_badge(node, el, all_nodes):
        by_id = {n["id"]: n for n in all_nodes}
        icon, label = None, None
        for d in el.iter():
            if d is el:
                continue
            nm = split_name(d.get("name", ""))[0]
            if nm in ICONS and icon is None:
                icon = ICONS[nm]
            if d.tag == "text" and label is None and nm not in ICONS:
                label = by_id.get(d.get("id"))
        if label:
            node["text"] = label.get("text", "")
            for k in ("textColor", "font"):
                if k in label:
                    node[k] = label[k]
        node["icon"] = icon

    if fr.get("root") and root.get("id") in styles:
        nodes.append(build_node(root, root_st, None, warnings))
    seen = {e.get("id") for e in root.iter()}

    def chain(nid):
        out, guard = [], 0
        while nid and nid in styles and guard < 50:
            out.append(styles[nid])
            nid, guard = styles[nid].get("parent"), guard + 1
        return out

    def ancestors(nid):
        out, guard = [], 0
        nid = styles.get(nid, {}).get("parent")
        while nid and guard < 50:
            out.append(nid)
            nid, guard = styles.get(nid, {}).get("parent"), guard + 1
        return out

    for nid, st in sorted(styles.items(), key=lambda kv: kv[1].get("order", 0)):
        if nid in seen or not nid.startswith("I"):
            continue  # 메타에 있거나, 컴포넌트 정의 안의 노드는 건너뛴다
        is_text = st.get("tag") in ("p", "span", "h1", "h2", "h3", "h4", "h5", "h6")
        anc = chain(st.get("parent"))
        eff = dict(st)
        if is_text:
            for a_st in anc:
                for k in INHERIT:
                    if k in a_st and k not in eff:
                        eff[k] = a_st[k]
        el = ET.Element("text" if is_text else "frame", {"id": nid, "name": st.get("name") or ("text" if is_text else "")})
        for k in ("width", "height"):
            if k in st:
                el.set(k, str(st[k]))
        bg = next((a_st["fills"][0] for a_st in anc if a_st.get("fills")), None)
        nodes.append(build_node(el, eff, None if any(a_st.get("gradient") and not a_st.get("fills") for a_st in anc) else bg, warnings))
    top_fill = root_st.get("fills", [None])[0] if root_st.get("fills") else None
    walk(root, top_fill, bool(root_st.get("gradient") and not root_st.get("fills")),
         {k: root_st[k] for k in INHERIT if k in root_st})
    def local_chain(nid):
        out, guard = [], 0
        nid = styles.get(nid, {}).get("parent")
        while nid and guard < 50:
            out.append(styles[nid])
            nid, guard = styles.get(nid, {}).get("parent"), guard + 1
        return out

    for inst in [e for e in root.iter() if e.tag == "instance"]:
        base = split_name(inst.get("name", ""))[0]
        iid = inst.get("id")
        if any(k.startswith(f"I{iid};") for k in styles):
            continue  # 안쪽이 이미 I 노드로 나와 있다
        fn_nodes = [(nid, st) for nid, st in styles.items()
                    if st.get("func") and kebab(st["func"]) == base and not st.get("func_mixed")]
        for nid, st in sorted(fn_nodes, key=lambda kv: kv[1].get("order", 0)):
            is_text = st.get("tag") in ("p", "span", "h1", "h2", "h3", "h4", "h5", "h6")
            anc = local_chain(nid)
            eff = dict(st)
            if is_text:
                for a_st in anc:
                    for k in INHERIT:
                        if k in a_st and k not in eff:
                            eff[k] = a_st[k]
            el = ET.Element("text" if is_text else "frame", {"id": f"I{iid};{nid}", "name": st.get("name") or ("text" if is_text else "")})
            for k in ("width", "height"):
                if k in st:
                    el.set(k, str(st[k]))
            bg = next((a_st["fills"][0] for a_st in anc if a_st.get("fills")), None)
            nodes.append(build_node(el, eff, bg, warnings))
    orphans = {n["id"]: n for n in nodes if n["id"] not in seen}
    for bnode in nodes:  # 안쪽 글자가 I 노드인 status-badge (메타 인스턴스이거나 I 노드 자신) 도 글자·아이콘을 접어 넣는다
        bid = bnode["id"]
        if not bnode["name"].startswith("status-badge") or bnode.get("text"):
            continue
        desc = [x for x in orphans if x != bid and bid in ancestors(x)]
        if not desc:
            continue
        icon = next((ICONS[split_name(styles[x].get("name", ""))[0]] for x in desc
                     if split_name(styles[x].get("name", ""))[0] in ICONS), None)
        lab = next((orphans[x] for x in desc if orphans[x]["type"] == "TEXT"
                    and split_name(styles[x].get("name", ""))[0] not in ICONS), None)
        if lab:
            bnode["text"] = lab.get("text", "")
            for k in ("textColor", "font"):
                if k in lab:
                    bnode[k] = lab[k]
        bnode["icon"] = icon
    return frame


def parse_vars(raw):
    if not raw:
        return None
    data = json.loads(raw)
    out = {"colors": [], "radius": [], "spacing": []}
    for name, val in data.items():
        sval = str(val).strip()
        if re.fullmatch(r"#[0-9a-fA-F]{3,8}", sval):
            out["colors"].append(hex_norm(sval))
            continue
        m = re.fullmatch(r"(-?\d+(?:\.\d+)?)(?:px)?", sval)
        if m:
            num = to_num(float(m.group(1)))
            lname = name.lower()
            if "radius" in lname or "round" in lname:
                out["radius"].append(num)
            elif any(k in lname for k in ("space", "spacing", "gap", "padding")):
                out["spacing"].append(num)
    return out


def main():
    text = sys.stdin.read()
    frames, vars_raw = parse_bundle(text)
    if not frames:
        sys.exit("### FRAME 이 없습니다")
    warnings = []
    dump = {"frames": [convert_frame(f, warnings) for f in frames]}
    v = parse_vars(vars_raw)
    if v is not None:
        dump["variables"] = v
    for w in warnings:
        print("경고:", w, file=sys.stderr)
    if "--summary" in sys.argv:
        for f in dump["frames"]:
            print(f'{f["page"]} / {f["name"]}: 노드 {len(f["nodes"])}개')
        print(f"경고 {len(warnings)}건")
        return
    print(json.dumps(dump, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
