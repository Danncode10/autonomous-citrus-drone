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

W = 453.54  # design width in pt; layout() re-sets it to fit, the SVG is always scaled to 16 cm
PHYS_W_CM = 16.0
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

BW = 90       # block width
GAP_AB = 98   # gap between columns A and B (wider: holds the 4-line arrow 3 label)
GAP_BC = 76   # gap between columns B and C
XA = 14
XB = XA + BW + GAP_AB
XC = XB + BW + GAP_BC
Y1 = 27       # top of row 1

BLOCKS = {
    1: dict(col=XA, row=1, title=["Hydroponic Tower", "+ Tower Unit"],
            body=["Tower frame with lettuce, empty pots, and ArUco markers", SEP,
                  "Tower Unit: ESP32 + GPS module + e-paper QR display + Generate button"]),
    2: dict(col=XB, row=1, title=["Farmer", "(Smartphone)"],
            body=["scans the QR code (tower ID, GPS coordinates, checksum), "
                  "registers the tower, requests a scan"]),
    3: dict(col=XC, row=1, shape="cylinder", title=["Database", "(Supabase)"],
            body=["Stores towers, locations, scan missions, and results"]),
    4: dict(col=XA, row=2, title=["Drone"],
            body=["Flight controller: SpeedyBee F405 Mini (ArduPilot) + GPS/compass", SEP,
                  "Raspberry Pi Zero 2 W + Pi Camera V2: records backup, streams video, "
                  "visual alignment (QR + ArUco)"]),
    5: dict(col=XB, row=2, title=["Ground Laptop"],
            body=["Live YOLOv8 detection (tower frame, lettuce, empty pot)", DOWN,
                  "Slot matching by face, level, position", DOWN, "Slot availability", SEP,
                  "Local offline cache", "Local dashboard: start scan, Live Scan, Sync Center"]),
    6: dict(col=XC, row=2, title=["Web Dashboard", "(Next.js)"],
            body=["Tower map, per-pot results, scan history"]),
}

MARGIN = 9         # min clearance (pt) between any arrow label and a block edge (= 12 px at 96 dpi)
LABEL_W = GAP_BC - 2 * MARGIN  # max label width in the B-C gap
LABEL_W_AB = GAP_AB - 2 * MARGIN  # max label width in the A-B gap
CLEAR = 7.5        # label offset from an arrow that carries a number circle


def body_height(lines):
    return sum(7 if ln == SEP else 9 if ln == DOWN else BODY_PT * LINE for ln in lines)


def cyl(b):
    return 7 if b.get("shape") == "cylinder" else 0


def content_height(b):
    return len(b["title"]) * TITLE_PT * LINE + 3 + body_height(b["lines"])


def layout():
    """Wrap block text, size rows, and place every block, arrow, label, badge and zone."""
    g = {}
    lh = LABEL_PT * LINE
    for b in BLOCKS.values():
        b["lines"] = [p for para in b["body"]
                      for p in ([para] if para in (SEP, DOWN) else wrap(para, BODY_PT, BW - 8))]
    row_h = {r: max(content_height(b) + 14 + 2 * cyl(b) for b in BLOCKS.values() if b["row"] == r)
             for r in (1, 2)}

    def wl(text, width=LABEL_W):
        return wrap(text, LABEL_PT, width)

    def wab(text):
        return wrap(text, LABEL_PT, LABEL_W_AB)

    t_gen, t_qr = "press Generate", "QR with tower ID + location"
    t_reg = "register tower / request scan"
    t_mis = ["mission and guidance", "(tower GPS, face A", "first, turn-to-tower", "commands)"]
    t_vid, t_bak = "live video + telemetry over local Wi-Fi", "backup recording after landing (gap filling)"
    t_fly = ("GPS approach \u2192 YOLO tower detection \u2192 QR/ArUco alignment \u2192 "
             "full-tower scan, face by face, bottom to top")
    t_sync = ["download tower list", "and scan requests /", "upload results (when", "internet is available)"]
    t_dash = "updated lettuce and empty pot counts per tower"
    t_view = "view results"

    # bottom row, Drone <-> Ground Laptop: three arrows stacked with their labels (3, 5, 5 dashed)
    d3 = 10
    d5 = d3 + MARGIN + len(t_mis) * lh + 4 + len(wab(t_vid)) * lh + MARGIN
    d5b = d5 + MARGIN + len(wab(t_bak)) * lh + MARGIN
    row_h[2] = max(row_h[2], d5b + 12)

    # band between the rows: holds label 4, the return lane of 7 and label 6
    lane_off = 38
    ROW_GAP = lane_off + 7 + len(t_sync) * lh + MARGIN
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
    a3y, a5y, a5by = y4 + d3, y4 + d5, y4 + d5b
    up, lo = r1m - 13, r1m + 13        # the two parallel arrows between blocks 1 and 2 (and 2 -> 3)
    a6x, a7x = bc - 14, bc + 16        # vertical runs of arrows 6 and 7 in the B-C gap
    a7in = x2 + w2 - 16                # where arrow 7 (return) enters the Farmer block
    a4x = x1 + 18
    lane = r1b + lane_off              # return lane of arrow 7 under the Farmer block
    a7dx = x3 + w3 - 18                # arrow 7 (database -> dashboard)

    g["arrows"] = {
        "a1g": ([(x2, up), (x1 + w1, up)], False, False),
        "a1q": ([(x1 + w1, lo), (x2, lo)], False, False),
        "a2": ([(x2 + w2, up), (x3, up)], False, False),
        "a3": ([(x5, a3y), (x4 + w4, a3y)], False, False),
        "a4": ([(a4x, y4), (a4x, r1b)], False, False),
        "a5": ([(x4 + w4, a5y), (x5, a5y)], False, False),
        "a5b": ([(x4 + w4, a5by), (x5, a5by)], True, False),
        "a6": ([(x5 + w5, y5 + 12), (a6x, y5 + 12), (a6x, r1b - 12), (x3, r1b - 12)], True, True),
        "a7": ([(a7dx, r1b), (a7dx, y6)], False, False),
        "a7b": ([(x6, y6 + 24), (a7x, y6 + 24), (a7x, lane), (a7in, lane), (a7in, r1b)], False, False),
    }
    g["hops"] = {"a7b": (a6x, lane)}

    lab, circles = [], []

    def gap_label(text, cx, top=None, bottom=None, ab_gap=False):
        lines = text if isinstance(text, list) else (wab(text) if ab_gap else wl(text))
        y = top if top is not None else bottom - len(lines) * lh
        lab.append((lines, cx, y, "middle", None))

    # horizontal arrows: label above/below, badge on the line
    gap_label(t_gen, ab, bottom=up - MARGIN + 1.5, ab_gap=True)
    gap_label(t_qr, ab, top=lo + MARGIN - 1.5, ab_gap=True)
    gap_label(t_reg, bc, bottom=up - MARGIN + 1.5)
    gap_label(t_mis, ab, top=a3y + MARGIN - 1.5)
    gap_label(t_vid, ab, bottom=a5y - MARGIN + 1.5, ab_gap=True)
    gap_label(t_bak, ab, top=a5y + MARGIN - 1.5, ab_gap=True)
    circles += [("1a", ab, up), ("1b", ab, lo), (2, bc, up), (3, ab, a3y), ("5a", ab, a5y), ("5b", ab, a5by)]

    # vertical arrows: badge on the line, label beside it, vertically centred on the badge
    mid4 = (y4 + r1b) / 2
    l4 = wl(t_fly, 124)
    lab.append((l4, a4x + CIRCLE_R + 5, mid4 - len(l4) * lh / 2, "start", None))
    circles.append((4, a4x, mid4))

    mid6 = lane + 7 + len(t_sync) * lh / 2
    lab.append((t_sync, a6x - CIRCLE_R - 4, mid6 - len(t_sync) * lh / 2, "end", None))
    circles.append((6, a6x, mid6))

    mid7 = (r1b + y6) / 2
    l7 = wl(t_dash, 76)
    lab.append((l7, a7dx - hw("7a") - 4, mid7 - len(l7) * lh / 2, "end", None))
    circles.append(("7a", a7dx, mid7))

    mid7b = (r1b + lane) / 2 + 3
    l7b = wl(t_view)
    lab.append((l7b, a7in - hw("7b") - 4, mid7b - len(l7b) * lh / 2, "end", None))
    circles.append(("7b", a7in, mid7b))
    g["labels"], g["circles"] = lab, circles

    # network zones: one continuous dotted outline each. The Farmer block straddles the boundary,
    # so both outlines run behind it (blocks are drawn on top of the zones).
    global W
    pad = 7
    yt, yb = Y1 - pad - 12, y2 + row_h[2] + pad
    xl, xr = x1 - 10, x3 + w3 + 10
    W = xr + xl                        # equal outer margins
    xm = x2 + w2 / 2
    xo = a6x + 10
    ys = r1b + 5
    g["zones"] = [
        [(xl, yt), (xm - 3, yt), (xm - 3, ys), (xo, ys), (xo, yb), (xl, yb)],
        [(xm + 3, yt), (xr, yt), (xr, yb), (xo + 5, yb), (xo + 5, ys + 5), (xm + 3, ys + 5)],
    ]
    g["zone_labels"] = [("Offline (local Wi-Fi)", xl + 6, yt + 3, "start"),
                        ("Online (internet)", xr - 6, yt + 3, "end")]
    g["legend_y"] = yb + 13
    g["H"] = yb + 22 + 12              # two legend rows
    return g


def rect_gap(a, b):
    dx = max(b[0] - a[2], a[0] - b[2], 0)
    dy = max(b[1] - a[3], a[1] - b[3], 0)
    return (dx * dx + dy * dy) ** 0.5


def seg_hits_rect(p, q, r, inflate=1.0):
    """Axis-aligned segment p-q against rectangle r=(x0,y0,x1,y1) grown by `inflate`."""
    x0, y0, x1, y1 = r[0] - inflate, r[1] - inflate, r[2] + inflate, r[3] + inflate
    sx0, sx1 = sorted((p[0], q[0]))
    sy0, sy1 = sorted((p[1], q[1]))
    return sx1 >= x0 and sx0 <= x1 and sy1 >= y0 and sy0 <= y1


def dist_to_seg(pt, p, q):
    (x, y), (ax, ay), (bx, by) = pt, p, q
    dx, dy = bx - ax, by - ay
    t = 0 if dx == dy == 0 else max(0, min(1, ((x - ax) * dx + (y - ay) * dy) / (dx * dx + dy * dy)))
    return ((x - ax - t * dx) ** 2 + (y - ay - t * dy) ** 2) ** 0.5


def check(g):
    """Returns a list of problems and prints the four checks the figure is held to."""
    problems = []
    lh = LABEL_PT * LINE
    for n, b in BLOCKS.items():
        for ln in b["title"]:
            if text_w(ln, TITLE_PT, True) > b["w"] - 8:
                problems.append(f"block {n} title too wide: {ln!r}")
    boxes = {n: (b["x"], b["y"], b["x"] + b["w"], b["y"] + b["h"]) for n, b in BLOCKS.items()}
    badges = [(n, (cx - hw(n), cy - CIRCLE_R, cx + hw(n), cy + CIRCLE_R)) for n, cx, cy in g["circles"]]
    lbls = []
    for lines, x, y, anchor, num in g["labels"]:
        w = max(text_w(l, LABEL_PT) for l in lines)
        x0 = {"middle": x - w / 2, "start": x, "end": x - w}[anchor]
        lbls.append((lines[0], (x0, y, x0 + w, y + len(lines) * lh)))
    # (a) labels vs block edges, other labels, badges
    worst = 1e9
    for name, bb in lbls:
        for n, box in boxes.items():
            gap = rect_gap(bb, box)
            worst = min(worst, gap)
            if gap < MARGIN - 0.01:
                problems.append(f"(a) label {name!r} is {gap:.1f} pt from block {n} (need {MARGIN})")
        for n, bd in badges:
            if rect_gap(bb, bd) < 1.5:
                problems.append(f"(a) label {name!r} touches badge {n}")
    for i, (na, ba) in enumerate(lbls):
        for nb, bb in lbls[i + 1:]:
            if rect_gap(ba, bb) < 2:
                problems.append(f"(a) labels {na!r} and {nb!r} touch")
    # (b) arrows vs label text
    for aid, (pts, dashed, both) in g["arrows"].items():
        for name, bb in lbls:
            for p, q in zip(pts, pts[1:]):
                if seg_hits_rect(p, q, bb):
                    problems.append(f"(b) arrow {aid} crosses label {name!r}")
    # (c) every badge sits on an arrow line
    worst_on = 0
    for n, cx, cy in g["circles"]:
        d = min(dist_to_seg((cx, cy), p, q) for pts, _, _ in g["arrows"].values() for p, q in zip(pts, pts[1:]))
        worst_on = max(worst_on, d)
        if d > 0.01:
            problems.append(f"(c) badge {n} is {d:.2f} pt off its arrow line")
    # (d) readability at the printed width
    scale = PHYS_W_CM / 2.54 * 72 / W
    smallest = min(LABEL_PT, BODY_PT, SMALL_PT, 7.8) * scale
    print(f"(a) closest label-to-block gap {worst:.1f} pt = {worst * scale * 96 / 72 / scale:.1f} px at 96 dpi (design units)")
    print(f"(c) worst badge offset from its arrow line: {worst_on:.3f} pt")
    print(f"(d) print scale {scale:.3f}: labels {LABEL_PT * scale:.2f} pt, block text {BODY_PT * scale:.2f} pt, "
          f"legend {SMALL_PT * scale:.2f} pt, badge digits {7.8 * scale:.2f} pt (smallest {smallest:.2f} pt)")
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
    half = hw(n)
    shape = (f'<circle cx="{f2(cx)}" cy="{f2(cy)}" r="{CIRCLE_R}" fill="{BLACK}"/>' if half == CIRCLE_R else
             f'<rect x="{f2(cx - half)}" y="{f2(cy - CIRCLE_R)}" width="{f2(2 * half)}" height="{f2(2 * CIRCLE_R)}" '
             f'rx="{CIRCLE_R}" ry="{CIRCLE_R}" fill="{BLACK}"/>')
    return [shape, f'<text x="{f2(cx)}" y="{f2(cy + 2.75)}" font-size="7.8" font-weight="bold" '
                   f'text-anchor="middle" fill="#FFFFFF">{n}</text>']


def hw(n):
    """Half width of a badge: a circle for one character, a pill for two."""
    t = str(n)
    return CIRCLE_R if len(t) == 1 else (text_w(t, 7.8, True) + 7) / 2


def label_circle_x(lines, x, anchor):
    if anchor == "start":
        return x - CIRCLE_R - 2.5
    return x - max(text_w(l, LABEL_PT) for l in lines) - CIRCLE_R - 2.5


def build_svg(g):
    H = g["H"]
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{PHYS_W_CM}cm" height="{H * PHYS_W_CM / W:.2f}cm" '
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
             f'markerUnits="userSpaceOnUse" orient="auto-start-reverse"><path d="M0,0.8 L10,5 L0,9.2 z" fill="{BLACK}"/></marker>'
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
    for aid, (pts, dashed, both) in g["arrows"].items():
        dash = ' stroke-dasharray="3.2 2.2"' if dashed else ""
        start = ' marker-start="url(#arr)"' if both else ""
        o.append(f'<path d="{path_d(pts, g["hops"].get(aid))}" fill="none" stroke="{BLACK}" '
                 f'stroke-width="0.8"{dash} stroke-linejoin="round"{start} marker-end="url(#arr)"/>')
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
        lx += text_w(txt, SMALL_PT) + 14
    lx = g["zones"][0][0][0] + text_w("Legend:", SMALL_PT, True) + 8   # second row, aligned under the items
    ly += 13
    o += circle_svg("n", lx + CIRCLE_R, ly)
    o += svg_text(["step order (a, b = parts of the same step)"], lx + 2 * CIRCLE_R + 6, ly - 4.5, SMALL_PT,
                  anchor="start")
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
        r, half = CIRCLE_R * S, hw(n) * S
        shape = "ellipse" if half == r else "rounded=1;arcSize=50"
        cells.append(f'<mxCell id="{nid()}" value="{n}" style="{shape};whiteSpace=wrap;html=1;fillColor=#000000;'
                     'strokeColor=none;fontColor=#FFFFFF;fontStyle=1;fontSize=15;fontFamily=Cambria;spacing=0;" '
                     f'vertex="1" parent="1"><mxGeometry x="{f2(cx * S - half)}" y="{f2(cy * S - r)}" '
                     f'width="{f2(2 * half)}" height="{f2(2 * r)}" as="geometry"/></mxCell>')

    for poly, (txt, x, y, anchor) in zip(g["zones"], g["zone_labels"]):
        polyline(poly + [poly[0]], f"endArrow=none;html=1;dashed=1;dashPattern=1 3;strokeColor={GRAY};"
                                   "strokeWidth=1.5;rounded=0;")
        tw = text_w(txt, SMALL_PT) * S + 10
        text(txt, x * S if anchor == "start" else x * S - tw, y * S, tw, SMALL_PT * LINE * S,
             f"fontColor={GRAY};fontStyle=2;fontSize={int(SMALL_PT * S)};"
             f"align={'left' if anchor == 'start' else 'right'};verticalAlign=top;")
    for aid, (pts, dashed, both) in g["arrows"].items():
        polyline(pts, "endArrow=block;endFill=1;endSize=6;html=1;rounded=0;strokeColor=#000000;strokeWidth=1.6;"
                      + ("startArrow=block;startFill=1;startSize=6;" if both else "")
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
    css_w = PHYS_W_CM / 2.54 * 96
    css_h = css_w * H / W
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
        px_w = round(PHYS_W_CM / 2.54 * dpi)
        px_h = round(px_w * H / W)
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
    print(f"canvas {PHYS_W_CM:.1f} x {geo['H'] * PHYS_W_CM / W:.1f} cm (design {W:.0f} x {geo['H']:.0f} pt)")
