"""Figure 1. Conceptual Framework of the Autonomous Hydroponic Tower Monitoring System.

Re-runnable generator. One layout model is written to three outputs:
  conceptual-framework.svg     vector figure (Caladea embedded, Cambria preferred when installed)
  conceptual-framework.drawio  editable draw.io copy of the same layout
  conceptual-framework.png     300 dpi raster, 16 cm wide (rendered with headless Google Chrome)

Usage:  python3 build_figure.py [--no-png]
Needs: Pillow, ImageMagick (`magick`), Google Chrome (PNG only).
Units are typographic points (1 pt = 1/72 in); the canvas is 16 cm wide.
Style: white background, black plus one gray accent, serif font, no caption inside the image.
Caladea (fonts/) is an open-licence font with the same metrics as Cambria, so text fits either way.
"""
import argparse
import base64
import os
import subprocess
import sys
from xml.sax.saxutils import escape

from PIL import ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "fonts")
NAME = "conceptual-framework"

BLACK = "#000000"
GRAY = "#7F7F7F"  # the single gray accent: network zones, separators, zone labels
FONT_STACK = "Cambria, Caladea, Georgia, 'Times New Roman', serif"

W = 453.54  # 16 cm
TITLE_PT = 9.5
BODY_PT = 9.0
LABEL_PT = 9.0
SMALL_PT = 8.5
LINE = 1.16  # line height factor
CIRCLE_R = 5.6

# ---------------------------------------------------------------- font metrics
_FONTS = {}


def text_w(s, size, bold=False):
    key = (bold, size)
    if key not in _FONTS:
        f = "Caladea-Bold.ttf" if bold else "Caladea-Regular.ttf"
        _FONTS[key] = ImageFont.truetype(os.path.join(FONT_DIR, f), int(size * 100))
    return _FONTS[key].getlength(s) / 100.0


def wrap(text, size, maxw):
    lines, cur = [], ""
    for word in text.split():
        t = (cur + " " + word).strip()
        if cur and text_w(t, size) > maxw:
            lines.append(cur)
            cur = word
        else:
            cur = t
    return lines + [cur]


# ---------------------------------------------------------------- content
SEP = "---"   # thin gray rule inside a block
DOWN = "v"    # small internal arrow inside a block

BW = 98       # block width
GAP = 68      # horizontal gap between blocks (holds the arrow labels)
XA, XB, XC = 16, 16 + BW + GAP, 16 + 2 * (BW + GAP)
Y1 = 27       # top of row 1
ROW_GAP = 62

BLOCKS = {
    1: dict(col=XA, row=1, title=["Hydroponic Tower", "+ Tower Unit"],
            body=["Tower frame with lettuce, empty pots, and ArUco markers", SEP,
                  "Tower Unit: ESP32 + GPS module + e-paper QR display + Generate button"]),
    2: dict(col=XB, row=1, title=["Farmer + Web", "Application"],
            body=["Smartphone scans the QR code (tower ID, GPS coordinates, checksum) "
                  "to register the tower and request a scan"]),
    3: dict(col=XC, row=1, shape="cylinder", title=["Database", "(Supabase)"],
            body=["Stores towers, locations, scan missions, and results"]),
    4: dict(col=XA, row=2, title=["Drone"],
            body=["Flight controller: SpeedyBee F405 Mini (ArduPilot) + GPS/compass", SEP,
                  "Raspberry Pi Zero 2 W + Pi Camera V2: records backup, streams video, "
                  "visual alignment (QR + ArUco)"]),
    5: dict(col=XB, row=2, title=["Ground Laptop"],
            body=["Live YOLOv8 detection (tower frame, lettuce, empty pot)", DOWN,
                  "Slot matching by face, level, position", DOWN, "Slot availability", SEP,
                  "Local offline cache"]),
    6: dict(col=XC, row=2, title=["Web Dashboard"],
            body=["Tower map, per-pot results, scan history, upload (Sync Center)"]),
}

LABEL_W = GAP - 3  # max width of a label that sits in a gap between blocks
CLEAR = 7.5        # label offset from an arrow that carries a number circle


def body_height(lines):
    return sum(7 if ln == SEP else 9 if ln == DOWN else BODY_PT * LINE for ln in lines)


def cyl(b):
    return 7 if b.get("shape") == "cylinder" else 0


def content_height(b):
    return len(b["title"]) * TITLE_PT * LINE + 3 + body_height(b["lines"])


def layout():
    """Wrap block text, size rows, and place every block, arrow, label and zone."""
    g = {}
    for b in BLOCKS.values():
        b["lines"] = [p for para in b["body"]
                      for p in ([para] if para in (SEP, DOWN) else wrap(para, BODY_PT, BW - 10))]
    row_h = {r: max(content_height(b) + 14 + 2 * cyl(b) for b in BLOCKS.values() if b["row"] == r)
             for r in (1, 2)}
    lh = LABEL_PT * LINE

    def nlines(text):
        return len(wrap(text, LABEL_PT, LABEL_W))

    # bottom row, Drone <-> Ground Laptop: three arrows stacked with their labels (3, 5, 5 dashed)
    t3, t5, t5b = ("mission (tower GPS, face A first)", "live video + telemetry over local Wi-Fi",
                   "backup recording after landing (gap filling)")
    d5 = 10 + CLEAR + nlines(t3) * lh + 4 + nlines(t5) * lh + CLEAR
    d5b = d5 + CLEAR + nlines(t5b) * lh + 3
    row_h[2] = max(row_h[2], d5b + 9)
    y2 = Y1 + row_h[1] + ROW_GAP
    for b in BLOCKS.values():
        b["x"], b["w"] = b["col"], BW
        b["y"] = Y1 if b["row"] == 1 else y2
        b["h"] = row_h[b["row"]]

    x1, y1, w1, h1 = (BLOCKS[1][k] for k in "xywh")
    x2, _, w2, _ = (BLOCKS[2][k] for k in "xywh")
    x3, _, w3, _ = (BLOCKS[3][k] for k in "xywh")
    x4, y4, w4, h4 = (BLOCKS[4][k] for k in "xywh")
    x5, y5, w5, _ = (BLOCKS[5][k] for k in "xywh")
    x6, y6, w6, _ = (BLOCKS[6][k] for k in "xywh")
    r1m, r1b = y1 + h1 / 2, y1 + h1
    ab, bc = (x1 + w1 + x2) / 2, (x2 + w2 + x3) / 2
    a3y, a5y, a5by = y4 + 10, y4 + d5, y4 + d5b
    a6x, a7x = bc - 14, bc + 12       # ⑥ and ⑦ vertical runs in the B-C gap
    lane = r1b + 20                   # ⑦ return lane under block 2

    # arrows: id -> (points, dashed)
    g["arrows"] = {
        "a1g": ([(x2, r1m - 13), (x1 + w1, r1m - 13)], False),
        "a1q": ([(x1 + w1, r1m + 13), (x2, r1m + 13)], False),
        "a2": ([(x2 + w2, r1m - 13), (x3, r1m - 13)], False),
        "a3": ([(x5, a3y), (x4 + w4, a3y)], False),
        "a4": ([(x4 + 18, y4), (x1 + 18, r1b)], False),
        "a5": ([(x4 + w4, a5y), (x5, a5y)], False),
        "a5b": ([(x4 + w4, a5by), (x5, a5by)], True),
        "a6": ([(x5 + w5, y5 + 12), (a6x, y5 + 12), (a6x, r1b - 12), (x3, r1b - 12)], True),
        "a7": ([(x3 + w3 - 18, r1b), (x6 + w6 - 18, y6)], False),
        "a7b": ([(x6, y6 + 24), (a7x, y6 + 24), (a7x, lane), (x2 + w2 - 20, lane), (x2 + w2 - 20, r1b)], False),
    }
    g["hops"] = {"a7b": (a6x, lane)}

    def stack(lines, top=None, bottom=None):
        n = len(lines)
        return top if top is not None else bottom - n * lh

    lab = []  # (lines, x, y_top, anchor, number-or-None)

    def gap_label(text, cx, top=None, bottom=None):
        lines = wrap(text, LABEL_PT, LABEL_W)
        lab.append((lines, cx, stack(lines, top, bottom), "middle", None))

    gap_label("press Generate", ab, bottom=r1m - 13 - 3)
    gap_label("QR with tower ID + location", ab, top=r1m + 13 + 3)
    gap_label("register tower / request scan", bc, bottom=r1m - 13 - CLEAR)
    gap_label(t3, ab, top=a3y + CLEAR)
    gap_label(t5, ab, bottom=a5y - CLEAR)
    gap_label(t5b, ab, top=a5y + CLEAR)
    lab.append((["GPS approach → YOLO tower", "detection → QR/ArUco alignment",
                 "→ full-tower scan, face by face,", "bottom to top"],
                x1 + 32, r1b + 8, "start", 4))
    lab.append((["upload when internet", "is available"], a6x - 5, lane + 7, "end", 6))
    lab.append((["updated lettuce and", "empty pot counts", "per tower"], x6 + w6 - 24, r1b + 8, "end", 7))
    g["labels"] = lab

    # number circles that sit on an arrow
    g["circles"] = [(1, ab, r1m), (2, bc, r1m - 13), (3, ab, a3y), (5, ab, a5y)]

    # network zones (gray dotted); block 2 straddles the shared border
    pad = 7
    yt, yb = Y1 - pad - 12, y2 + row_h[2] + pad
    xl, xr = x1 - pad - 3, x3 + w3 + pad + 3
    midb = x2 + w2 / 2
    step = r1m + 24
    g["zones"] = [
        [(xl, yt), (midb - 2, yt), (midb - 2, step), (bc - 2, step), (bc - 2, yb), (xl, yb)],
        [(midb + 2, yt), (xr, yt), (xr, yb), (bc + 2, yb), (bc + 2, step + 4), (midb + 2, step + 4)],
    ]
    g["zone_labels"] = [("Offline (local Wi-Fi)", xl + 6, yt + 3, "start"),
                        ("Online (internet)", xr - 6, yt + 3, "end")]
    g["legend_y"] = yb + 13
    g["H"] = yb + 22
    return g


def check(g):
    problems = []
    for n, b in BLOCKS.items():
        for ln in b["title"]:
            if text_w(ln, TITLE_PT, True) > b["w"] - 8:
                problems.append(f"block {n} title too wide: {ln!r}")
    for lines, x, y, anchor, num in g["labels"]:
        for ln in lines:
            if anchor == "middle" and text_w(ln, LABEL_PT) > LABEL_W:
                problems.append(f"gap label too wide: {ln!r}")
    return problems


# ---------------------------------------------------------------- SVG writer
def f2(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


def svg_text(lines, x, y_top, size, anchor="middle", bold=False, italic=False, fill=BLACK):
    out = []
    extra = (' font-weight="bold"' if bold else "") + (' font-style="italic"' if italic else "")
    for i, ln in enumerate(lines):
        base = y_top + i * size * LINE + size * 0.86
        out.append(f'<text x="{f2(x)}" y="{f2(base)}" font-size="{size}" text-anchor="{anchor}"'
                   f'{extra} fill="{fill}">{escape(ln)}</text>')
    return out


def path_d(pts, hop=None):
    d = f"M{f2(pts[0][0])},{f2(pts[0][1])}"
    for (ax, ay), (bx, by) in zip(pts, pts[1:]):
        if hop and ay == by == hop[1] and min(ax, bx) < hop[0] < max(ax, bx):
            r, s = 3.2, (1 if bx > ax else -1)
            d += (f" L{f2(hop[0] - s * r)},{f2(ay)} A{r},{r} 0 0 {1 if s > 0 else 0} "
                  f"{f2(hop[0] + s * r)},{f2(ay)}")
        d += f" L{f2(bx)},{f2(by)}"
    return d


def block_svg(n, b):
    x, y, w, h = b["x"], b["y"], b["w"], b["h"]
    cx, c = x + w / 2, cyl(b)
    out = []
    if c:
        ry = 6
        out.append(f'<path d="M{f2(x)},{f2(y + ry)} A{w / 2},{ry} 0 0 1 {f2(x + w)},{f2(y + ry)} '
                   f'V{f2(y + h - ry)} A{w / 2},{ry} 0 0 1 {f2(x)},{f2(y + h - ry)} Z" '
                   f'fill="#FFFFFF" stroke="{BLACK}" stroke-width="0.9"/>')
        out.append(f'<path d="M{f2(x)},{f2(y + ry)} A{w / 2},{ry} 0 0 0 {f2(x + w)},{f2(y + ry)}" '
                   f'fill="none" stroke="{BLACK}" stroke-width="0.9"/>')
    else:
        out.append(f'<rect x="{f2(x)}" y="{f2(y)}" width="{w}" height="{f2(h)}" rx="7" ry="7" '
                   f'fill="#FFFFFF" stroke="{BLACK}" stroke-width="0.9"/>')
    # title + body block centred vertically in the box
    yy = y + c + (h - 2 * c - content_height(b)) / 2
    out += svg_text(b["title"], cx, yy, TITLE_PT, bold=True)
    yy += len(b["title"]) * TITLE_PT * LINE + 3
    for ln in b["lines"]:
        if ln == SEP:
            out.append(f'<line x1="{f2(x + 14)}" y1="{f2(yy + 3.5)}" x2="{f2(x + w - 14)}" y2="{f2(yy + 3.5)}" '
                       f'stroke="{GRAY}" stroke-width="0.6"/>')
            yy += 7
        elif ln == DOWN:
            out.append(f'<line x1="{f2(cx)}" y1="{f2(yy + 1)}" x2="{f2(cx)}" y2="{f2(yy + 7)}" '
                       f'stroke="{BLACK}" stroke-width="0.7" marker-end="url(#mini)"/>')
            yy += 9
        else:
            out += svg_text([ln], cx, yy, BODY_PT)
            yy += BODY_PT * LINE
    return out


def circle_svg(n, cx, cy):
    return [f'<circle cx="{f2(cx)}" cy="{f2(cy)}" r="{CIRCLE_R}" fill="{BLACK}"/>',
            f'<text x="{f2(cx)}" y="{f2(cy + 2.75)}" font-size="7.8" font-weight="bold" '
            f'text-anchor="middle" fill="#FFFFFF">{n}</text>']


def label_circle_x(lines, x, anchor):
    if anchor == "start":
        return x - CIRCLE_R - 2.5
    return x - max(text_w(l, LABEL_PT) for l in lines) - CIRCLE_R - 2.5


def build_svg(g):
    H = g["H"]
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="16cm" height="{H / 72 * 2.54:.2f}cm" '
         f'viewBox="0 0 {f2(W)} {f2(H)}" font-family="{FONT_STACK}">',
         '<title>Conceptual Framework of the Autonomous Hydroponic Tower Monitoring System</title>']
    faces = []
    for f, wgt in (("Caladea-Regular.ttf", "normal"), ("Caladea-Bold.ttf", "bold")):
        with open(os.path.join(FONT_DIR, f), "rb") as fh:
            data = base64.b64encode(fh.read()).decode()
        faces.append(f"@font-face{{font-family:'Caladea';font-weight:{wgt};"
                     f"src:url(data:font/ttf;base64,{data}) format('truetype');}}")
    o.append("<style>" + "".join(faces) + "</style>")
    o.append('<defs>'
             '<marker id="arr" viewBox="0 0 10 10" refX="9.5" refY="5" markerWidth="6.5" markerHeight="6.5" '
             f'markerUnits="userSpaceOnUse" orient="auto"><path d="M0,0.8 L10,5 L0,9.2 z" fill="{BLACK}"/></marker>'
             '<marker id="mini" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="4" markerHeight="4" '
             f'markerUnits="userSpaceOnUse" orient="auto"><path d="M0,0.5 L10,5 L0,9.5 z" fill="{BLACK}"/></marker>'
             '</defs>')
    o.append(f'<rect x="0" y="0" width="{f2(W)}" height="{f2(H)}" fill="#FFFFFF"/>')
    for poly in g["zones"]:
        pts = " ".join(f"{f2(a)},{f2(b)}" for a, b in poly)
        o.append(f'<polygon points="{pts}" fill="none" stroke="{GRAY}" stroke-width="0.8" '
                 f'stroke-dasharray="0.8 2.2" stroke-linecap="round" stroke-linejoin="round"/>')
    for txt, x, y, anchor in g["zone_labels"]:
        o += svg_text([txt], x, y, SMALL_PT, anchor=anchor, italic=True, fill=GRAY)
    for aid, (pts, dashed) in g["arrows"].items():
        dash = ' stroke-dasharray="3.2 2.2"' if dashed else ""
        o.append(f'<path d="{path_d(pts, g["hops"].get(aid))}" fill="none" stroke="{BLACK}" '
                 f'stroke-width="0.8"{dash} stroke-linejoin="round" marker-end="url(#arr)"/>')
    for n, b in BLOCKS.items():
        o += block_svg(n, b)
    for n, cx, cy in g["circles"]:
        o += circle_svg(n, cx, cy)
    for lines, x, y, anchor, num in g["labels"]:
        if num is not None:
            o += circle_svg(num, label_circle_x(lines, x, anchor), y + LABEL_PT * 0.55)
        o += svg_text(lines, x, y, LABEL_PT, anchor=anchor)
    # legend
    lx, ly = g["zones"][0][0][0], g["legend_y"]
    o += svg_text(["Legend:"], lx, ly - 4.5, SMALL_PT, anchor="start", bold=True)
    lx += text_w("Legend:", SMALL_PT, True) + 8
    for kind, txt in (("solid", "live flow"), ("dash", "deferred transfer (after landing / when online)"),
                      ("dot", "network zone")):
        stroke = GRAY if kind == "dot" else BLACK
        dash = {"solid": "", "dash": ' stroke-dasharray="3.2 2.2"',
                "dot": ' stroke-dasharray="0.8 2.2" stroke-linecap="round"'}[kind]
        mk = "" if kind == "dot" else ' marker-end="url(#arr)"'
        o.append(f'<line x1="{f2(lx)}" y1="{f2(ly)}" x2="{f2(lx + 22)}" y2="{f2(ly)}" stroke="{stroke}" '
                 f'stroke-width="0.8"{dash}{mk}/>')
        lx += 26
        o += svg_text([txt], lx, ly - 4.5, SMALL_PT, anchor="start")
        lx += text_w(txt, SMALL_PT) + 12
    o += circle_svg("n", lx + CIRCLE_R, ly)
    o += svg_text(["step order"], lx + 2 * CIRCLE_R + 3, ly - 4.5, SMALL_PT, anchor="start")
    o.append("</svg>")
    return "\n".join(o)


# ---------------------------------------------------------------- draw.io writer
S = 2.0  # draw.io units per pt


def build_drawio(g):
    cells, counter = [], [0]

    def nid():
        counter[0] += 1
        return f"c{counter[0]}"

    def attr(v):
        return escape(v, {'"': "&quot;"})

    def pt(p, role=""):
        return f'<mxPoint x="{f2(p[0] * S)}" y="{f2(p[1] * S)}"{f" as={chr(34)}{role}{chr(34)}" if role else ""}/>'

    def polyline(pts, style, cid=None):
        mids = "".join(pt(p) for p in pts[1:-1])
        cells.append(f'<mxCell id="{cid or nid()}" style="{style}" edge="1" parent="1">'
                     f'<mxGeometry relative="1" as="geometry">{pt(pts[0], "sourcePoint")}{pt(pts[-1], "targetPoint")}'
                     + (f'<Array as="points">{mids}</Array>' if mids else "") + "</mxGeometry></mxCell>")

    def text(value, x, y, w, h, style):
        cells.append(f'<mxCell id="{nid()}" value="{attr(value)}" style="text;html=1;strokeColor=none;'
                     f'fillColor=none;fontFamily=Cambria;spacing=0;{style}" vertex="1" parent="1">'
                     f'<mxGeometry x="{f2(x)}" y="{f2(y)}" width="{f2(w)}" height="{f2(h)}" as="geometry"/></mxCell>')

    def circle(n, cx, cy):
        r = CIRCLE_R * S
        cells.append(f'<mxCell id="{nid()}" value="{n}" style="ellipse;whiteSpace=wrap;html=1;fillColor=#000000;'
                     'strokeColor=none;fontColor=#FFFFFF;fontStyle=1;fontSize=15;fontFamily=Cambria;" vertex="1" '
                     f'parent="1"><mxGeometry x="{f2(cx * S - r)}" y="{f2(cy * S - r)}" width="{f2(2 * r)}" '
                     f'height="{f2(2 * r)}" as="geometry"/></mxCell>')

    for poly, (txt, x, y, anchor) in zip(g["zones"], g["zone_labels"]):
        polyline(poly + [poly[0]], f"endArrow=none;html=1;dashed=1;dashPattern=1 3;strokeColor={GRAY};"
                                   "strokeWidth=1.5;rounded=0;")
        tw = text_w(txt, SMALL_PT) * S + 10
        text(txt, x * S if anchor == "start" else x * S - tw, y * S, tw, SMALL_PT * LINE * S,
             f"fontColor={GRAY};fontStyle=2;fontSize={int(SMALL_PT * S)};"
             f"align={'left' if anchor == 'start' else 'right'};verticalAlign=top;")
    for aid, (pts, dashed) in g["arrows"].items():
        polyline(pts, "endArrow=block;endFill=1;endSize=6;html=1;rounded=0;strokeColor=#000000;strokeWidth=1.6;"
                      + ("dashed=1;dashPattern=6 4;" if dashed else "")
                      + ("jumpStyle=arc;jumpSize=8;" if aid in g["hops"] else ""), cid=aid)
    for n, b in BLOCKS.items():
        body = []
        for ln in b["lines"]:
            body.append('<hr style="border:none;border-top:1px solid #7F7F7F;margin:3px 18px;">' if ln == SEP
                        else "↓<br>" if ln == DOWN else escape(ln) + "<br>")
        html = ("<b>" + "<br>".join(escape(t) for t in b["title"]) + "</b><br>"
                f'<span style="font-size:{int(BODY_PT * S)}px">' + "".join(body) + "</span>")
        shape = ("shape=cylinder3;boundedLbl=1;backgroundOutline=1;size=12;" if cyl(b)
                 else "rounded=1;arcSize=12;")
        cells.append(f'<mxCell id="b{n}" value="{attr(html)}" style="{shape}whiteSpace=wrap;html=1;'
                     'fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.6;fontFamily=Cambria;fontColor=#000000;'
                     f'fontSize={int(TITLE_PT * S)};verticalAlign=middle;" vertex="1" parent="1">'
                     f'<mxGeometry x="{f2(b["x"] * S)}" y="{f2(b["y"] * S)}" width="{f2(b["w"] * S)}" '
                     f'height="{f2(b["h"] * S)}" as="geometry"/></mxCell>')
    for n, cx, cy in g["circles"]:
        circle(n, cx, cy)
    for lines, x, y, anchor, num in g["labels"]:
        tw = max(text_w(l, LABEL_PT) for l in lines) * S + 8
        th = len(lines) * LABEL_PT * LINE * S + 4
        lx = {"middle": x * S - tw / 2, "start": x * S - 4, "end": x * S - tw + 4}[anchor]
        align = {"middle": "center", "start": "left", "end": "right"}[anchor]
        text("<br>".join(escape(l) for l in lines), lx, y * S - 2, tw, th,
             f"fontColor=#000000;fontSize={int(LABEL_PT * S)};align={align};verticalAlign=top;")
        if num is not None:
            circle(num, label_circle_x(lines, x, anchor), y + LABEL_PT * 0.55)
    return ('<mxfile host="build_figure.py"><diagram id="fig1" name="Figure 1 - Conceptual Framework">'
            '<mxGraphModel dx="1000" dy="800" grid="0" gridSize="10" guides="1" tooltips="1" connect="1" '
            f'arrows="1" fold="1" page="1" pageScale="1" pageWidth="{int(W * S)}" pageHeight="{int(g["H"] * S)}" '
            'background="#FFFFFF" math="0" shadow="0"><root><mxCell id="0"/><mxCell id="1" parent="0"/>'
            + "".join(cells) + "</root></mxGraphModel></diagram></mxfile>\n")


# ---------------------------------------------------------------- PNG via Chrome
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def render_png(svg_path, png_path, H, dpi=300):
    css_w, css_h = W * 96 / 72, H * 96 / 72
    html = os.path.join(os.path.dirname(png_path), ".render.html")
    with open(html, "w") as fh:
        fh.write('<!doctype html><html><body style="margin:0;background:#fff">'
                 f'<img src="{os.path.basename(svg_path)}" style="display:block;width:{css_w}px;height:{css_h}px">'
                 '</body></html>')
    raw = png_path + ".raw.png"
    try:
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        f"--force-device-scale-factor={dpi / 96}",
                        f"--window-size={int(round(css_w))},{int(round(css_h)) + 1}",
                        f"--screenshot={raw}", "file://" + html], check=True, capture_output=True)
        px_w, px_h = round(W / 72 * dpi), round(H / 72 * dpi)
        subprocess.run(["magick", raw, "-crop", f"{px_w}x{px_h}+0+0", "+repage", "-background", "white",
                        "-alpha", "remove", "-units", "PixelsPerInch", "-density", str(dpi), png_path], check=True)
    finally:
        for f in (raw, html):
            if os.path.exists(f):
                os.remove(f)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-png", action="store_true")
    args = ap.parse_args()
    geo = layout()
    for p in check(geo):
        print("WARN:", p, file=sys.stderr)
    svg = os.path.join(HERE, NAME + ".svg")
    with open(svg, "w") as fh:
        fh.write(build_svg(geo))
    with open(os.path.join(HERE, NAME + ".drawio"), "w") as fh:
        fh.write(build_drawio(geo))
    if not args.no_png:
        render_png(svg, os.path.join(HERE, NAME + ".png"), geo["H"])
    print(f"canvas {W / 72 * 2.54:.1f} x {geo['H'] / 72 * 2.54:.1f} cm")
