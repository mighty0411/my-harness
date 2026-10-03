#!/usr/bin/env python3
"""테스트 픽스처 생성: pass.json 1개 + 규칙별 위반 덤프 15개를 fixtures/에 만든다."""
import copy
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent / "fixtures"
PAGE = "S7 Screens"
_counter = [0]


def nid():
    _counter[0] += 1
    return f"9:{_counter[0]}"


def text(name, txt, size=28, weight=700, color="#141414", bg="#ffffff"):
    return {"id": nid(), "name": name, "type": "TEXT", "text": txt, "textColor": color, "bg": bg,
            "font": {"family": "Pretendard", "weight": weight, "size": size},
            "letterSpacing": 0, "textCase": "ORIGINAL"}


def frame(name, nodes):
    return {"id": nid(), "name": name, "page": PAGE, "width": 390, "height": 844,
            "padding": {"left": 16, "right": 16}, "nodes": nodes}


def button(name="button/primary", variant=None):
    n = {"id": nid(), "name": name, "type": "FRAME", "fills": ["#141414"], "cornerRadius": 8,
         "height": 48, "interactive": True, "padding": {"left": 16, "right": 16, "top": 0, "bottom": 0}}
    if variant:
        n["variant"] = variant
    return n


def badge(label, fills, strokes, color, icon=None):
    return {"id": nid(), "name": "status-badge", "type": "FRAME", "text": label, "fills": fills,
            "strokes": strokes, "textColor": color, "cornerRadius": 9999, "icon": icon,
            "font": {"family": "Pretendard", "weight": 600, "size": 12}}


def build_pass():
    home = frame("screen/home", [
        text("heading", "홈"),
        button(),
        {"id": nid(), "name": "card/content", "type": "FRAME", "fills": ["#ffffff"],
         "strokes": [{"color": "#f0f0f0", "weight": 1, "style": "solid"}], "cornerRadius": 24, "itemSpacing": 8},
        {"id": nid(), "name": "text-input", "type": "FRAME", "fills": ["#f0f0f0"], "strokes": [],
         "cornerRadius": 8, "height": 48, "interactive": True, "state": "rest"},
        badge("작성 중", ["#ffffff"], [{"color": "#e0e0e0", "weight": 1, "style": "dashed"}], "#707070", "✎"),
        badge("승인됨", ["#141414"], [], "#ffffff", "✓"),
    ])
    skills = frame("screen/skills", [
        text("heading", "스킬 라이브러리"),
        {"id": nid(), "name": "skill-card/item", "type": "FRAME", "fills": ["#ffffff"], "cornerRadius": 24},
        {"id": nid(), "name": "tab-bar", "type": "FRAME", "fills": ["#f3f3f3"], "cornerRadius": 9999, "height": 56},
    ])

    def opts(with_sale):
        o = [{"id": nid(), "name": "visibility-selector", "type": "FRAME", "fills": ["#f3f3f3"]},
             {"id": nid(), "name": "option/private", "selected": True},
             {"id": nid(), "name": "option/member-only", "selected": False}]
        if with_sale:
            o.append({"id": nid(), "name": "option/sale-request", "selected": False})
        return o

    reg_s = frame("screen/my-assets/register@seller", [text("heading", "자산 등록")] + opts(True))
    reg_n = frame("screen/my-assets/register@non-seller", [text("heading", "자산 등록")] + opts(False))

    def sale(variant):
        return [text("heading", "판매 신청"),
                text("notice", "개인정보, 고객정보, 회사기밀, 타인 저작물은 판매 자산에 포함할 수 없어요", 13, 400),
                {"id": nid(), "name": "confirm-checkbox", "type": "FRAME"},
                button("submit-button", variant)]

    sale_u = frame("screen/my-assets/sale-request@unchecked", sale("disabled"))
    sale_c = frame("screen/my-assets/sale-request@checked", sale("enabled"))
    return {"frames": [home, skills, reg_s, reg_n, sale_u, sale_c]}


def get_frame(d, name):
    return next(f for f in d["frames"] if f["name"] == name)


def get_node(d, fname, nname):
    return next(n for n in get_frame(d, fname)["nodes"] if n.get("name") == nname)


def mutations():
    def d01(d): get_frame(d, "screen/home")["width"] = 360
    def d02(d): get_node(d, "screen/home", "card/content")["fills"] = ["#ff0000"]
    def d03(d):
        for _ in range(3):
            get_frame(d, "screen/home")["nodes"].append({"id": nid(), "name": "accent-dot", "fills": ["#0066ff"]})
    def d04(d): get_node(d, "screen/home", "button/primary")["cornerRadius"] = 9999  # 버튼 반경은 8, 알약은 위반
    def d05(d): get_node(d, "screen/home", "card/content")["effects"] = [{"type": "DROP_SHADOW"}]
    def d06(d): get_frame(d, "screen/home")["nodes"].append({"id": nid(), "name": "decor", "gradient": True})
    def d07(d): get_node(d, "screen/home", "heading")["font"]["weight"] = 500
    def d08(d): get_node(d, "screen/home", "heading")["letterSpacing"] = 2
    def d09(d): get_node(d, "screen/home", "card/content")["itemSpacing"] = 10
    def d10(d): get_node(d, "screen/home", "button/primary")["height"] = 36
    def d11(d): get_node(d, "screen/home", "text-input")["strokes"] = [{"color": "#e0e0e0", "weight": 1, "style": "solid"}]
    def d12(d):
        get_frame(d, "screen/home")["nodes"].append(text("muted", "보조 문구", 13, 400, "#707070", "#f3f3f3"))
    def v1(d):
        f = "screen/my-assets/register@seller"
        get_node(d, f, "option/private")["selected"] = False
        get_node(d, f, "option/member-only")["selected"] = True
    def v2(d):
        for f in ("screen/my-assets/sale-request@unchecked", "screen/my-assets/sale-request@checked"):
            fr = get_frame(d, f)
            fr["nodes"] = [n for n in fr["nodes"] if n.get("name") != "confirm-checkbox"]
    def bad(d):
        n = next(n for n in get_frame(d, "screen/home")["nodes"] if n.get("text") == "승인됨")
        n["icon"] = None
    return {"D01": d01, "D02": d02, "D03": d03, "D04": d04, "D05": d05, "D06": d06, "D07": d07,
            "D08": d08, "D09": d09, "D10": d10, "D11": d11, "D12": d12, "V1": v1, "V2": v2, "badge": bad}


def main():
    OUT.mkdir(exist_ok=True)
    base = build_pass()
    (OUT / "pass.json").write_text(json.dumps(base, ensure_ascii=False, indent=1), encoding="utf-8")
    for rule, fn in mutations().items():
        d = copy.deepcopy(base)
        fn(d)
        (OUT / f"fail-{rule}.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"픽스처 {1 + len(mutations())}개 생성: {OUT}")


if __name__ == "__main__":
    main()
