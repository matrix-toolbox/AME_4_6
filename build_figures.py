#!/usr/bin/env python3
"""Build exact, responsive SVG figures for AME46_FRACTAL.html.

Run from any directory: python3 build_figures.py
Python standard library only. Place the unchanged, verified seed46.py beside
this file. For development, the original sibling FRAME46 package is also
accepted as a source. Every occupied region is calculated from integer masks.
No image tracing, random sampling, or artistic approximation is used.

Most palettes distinguish puzzle pieces or panels only. The atom-recipe figure
is the exception: it explicitly displays the quantum colour l and seed sign.
The sign-control figure displays the EXTRA conditional minus only.
"""

from collections import Counter, defaultdict
from colorsys import hls_to_rgb
from html import escape
from itertools import groupby, product
from math import log, sqrt
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE
if not (HERE / "seed46.py").exists():
    sys.path.insert(0, str(ROOT.parent / "FRAME46"))
from seed46 import atoms, geomagic, masks, nested_mask

OUT = ROOT
INK, MUTED, LINE, EMPTY = "#243b43", "#52666e", "#aab9bf", "#f5f7f8"
TEAL, GOLD = "#267c82", "#d69627"
PAL = ("#4477aa", "#ee6677", "#228833", "#ccbb44", "#66ccee", "#aa3377")
QCOL = ("#0072b2", "#e69f00", "#009e73", "#cc79a7", "#56b4e9", "#d55e00")
ROW = (0, 2, 4, 5, 3, 1)
COL = (2, 4, 0, 1, 5, 3)
BASE = masks()
META = []


def n(v):
    return f"{v:.6f}".rstrip("0").rstrip(".") if isinstance(v, float) else str(v)


class SVG:
    def __init__(self, w, h, title, desc):
        self.w, self.h, self.title, self.desc = w, h, title, desc
        self.parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',
            f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>',
            '<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9" fill="#52666e"/></marker>',
            '<pattern id="extra-minus" width="7" height="7" patternUnits="userSpaceOnUse"><rect width="7" height="7" fill="#d69627"/><path d="M-1,1L1,-1M0,7L7,0M6,8L8,6" stroke="#714a0d" stroke-width=".8"/></pattern></defs>',
            f'<rect width="{w}" height="{h}" fill="#fff"/>',
            '<g font-family="Arial, Helvetica, sans-serif" fill="#243b43">']

    def text(self, x, y, text, size=18, anchor="start", fill=INK, weight=None):
        wt = f' font-weight="{weight}"' if weight else ""
        self.parts.append(f'<text x="{n(x)}" y="{n(y)}" font-size="{size}" text-anchor="{anchor}" fill="{fill}"{wt}>{escape(str(text))}</text>')

    def rect(self, x, y, w, h, fill="none", stroke=None, sw=1, **attrs):
        at = "".join(f' {k.replace("_", "-")}="{escape(str(v))}"' for k, v in attrs.items())
        st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
        self.parts.append(f'<rect x="{n(x)}" y="{n(y)}" width="{n(w)}" height="{n(h)}" fill="{fill}"{st}{at}/>')

    def line(self, x1, y1, x2, y2, color=MUTED, sw=1, arrow=False, dashed=False):
        attr = (' marker-end="url(#arrow)"' if arrow else "") + (' stroke-dasharray="5 4"' if dashed else "")
        self.parts.append(f'<line x1="{n(x1)}" y1="{n(y1)}" x2="{n(x2)}" y2="{n(y2)}" stroke="{color}" stroke-width="{sw}"{attr}/>')

    def frame(self, x, y, w, h, fill=EMPTY):
        self.rect(x, y, w, h, fill, LINE, .8)

    def cells(self, x, y, w, h, cells, W=24, H=4, color=TEAL, opacity=None):
        # Exact horizontal runs. All path coordinates remain integers.
        paths = []
        for yy, row in groupby(sorted(cells, key=lambda p: (p[1], p[0])), key=lambda p: p[1]):
            xs = [p[0] for p in row]
            for _, run in groupby(enumerate(xs), key=lambda p: p[1]-p[0]):
                xx = [p[1] for p in run]
                length = xx[-1] + 1 - xx[0]
                paths.append(f'M{xx[0]} {yy}h{length}v1h-{length}z')
        op = f' opacity="{opacity}"' if opacity is not None else ""
        self.parts.append(f'<g transform="translate({n(x)} {n(y+h)}) scale({n(w/W)} {n(-h/H)})"><path d="{"".join(paths)}" fill="{color}"{op}/></g>')

    def save(self, filename, palette, notes, facts):
        self.parts += ["</g></svg>"]
        (OUT / filename).write_text("\n".join(self.parts), encoding="utf-8")
        META.append(dict(file=filename, title=self.title, description=self.desc,
                         palette=palette, caption_notes=notes, exact_facts=facts))


def coverage(collection, W, H):
    counter = Counter(p for cells in collection for p in cells)
    assert len(counter) == W * H and set(counter.values()) == {1}
    assert all(0 <= x < W and 0 <= y < H for x, y in counter)


def assemble(svg, x, y, w, h, line, palette=PAL, W=24, H=4, data=BASE):
    svg.frame(x, y, w, h)
    for index, key in enumerate(line):
        svg.cells(x, y, w, h, data[key], W, H, palette[index % len(palette)])
    svg.rect(x, y, w, h, stroke=LINE, sw=.8)


def seed_atlas():
    svg = SVG(1060, 680, "The complete order-6 geomagic array",
              "All 36 base pieces, in the row and column orders for which the two displayed diagonals tile the target. Each pale rectangle shows the same full target R. The occupied cells form one piece. Colours identify column positions only.")
    svg.text(28, 34, "The 36 base pieces", 25, weight="bold")
    svg.text(28, 63, "Each piece keeps its components in fixed positions inside the same rectangle.", 17, fill=MUTED)
    left, top, pw, ph, gx, gy = 87, 119, 145, 145/sqrt(6), 14, 26
    for c, j in enumerate(COL):
        svg.text(left+c*(pw+gx)+pw/2, 104, f"j = {j}", 17, "middle", MUTED)
    for r, i in enumerate(ROW):
        y = top+r*(ph+gy)
        svg.text(67, y+ph/2+6, f"i = {i}", 17, "end", MUTED)
        for c, j in enumerate(COL):
            x = left+c*(pw+gx)
            svg.frame(x, y, pw, ph)
            svg.cells(x, y, pw, ph, BASE[i, j], color=PAL[c])
    svg.text(28, 653, "16 occupied cells per piece • 96 equal cells in the target • area fraction 1/6", 17, fill=MUTED)
    svg.save("seed_atlas.svg", "Decorative: colour identifies the displayed column, not a quantum label.",
             "The pale frames indicate a common target. They are not part of a puzzle piece. This is the full base array, with 36 pieces. Disconnected components keep their relative positions.",
             dict(pieces=36, cells_per_piece=16, target_cells=96, row_order=ROW, column_order=COL))


def all_lines():
    svg = SVG(1100, 1030, "All fourteen base geomagic assemblies",
              "The six rows, six columns, and two designated diagonals each cover every one of the 96 target cells exactly once. The colour index restarts in each panel and distinguishes its six contributing pieces.")
    svg.text(28, 34, "Every complete line fills the target", 25, weight="bold")
    svg.text(28, 62, "Superposition uses the pieces in their original coordinates. Nothing is slid or rotated.", 17, fill=MUTED)
    pw, ph, gap = 318, 318/sqrt(6), 39
    rows = [(f"Row i = {i}", [(i, j) for j in COL]) for i in ROW]
    cols = [(f"Column j = {j}", [(i, j) for i in ROW]) for j in COL]
    diags = [("Main displayed diagonal", list(zip(ROW, COL))),
             ("Other displayed diagonal", list(zip(ROW, reversed(COL))))]
    for basey, heading, entries in [(100, "All six rows", rows), (470, "All six columns", cols), (840, "Both diagonals", diags)]:
        svg.text(28, basey, heading, 20, weight="bold")
        for index, (title, keys) in enumerate(entries):
            row, col = divmod(index, 3)
            x, y = 28+col*(pw+gap), basey+39+row*171
            svg.text(x, y-11, title, 16, fill=MUTED)
            coverage([BASE[key] for key in keys], 24, 4)
            assemble(svg, x, y, pw, ph, keys)
    svg.text(748, 919, "Each panel:", 17)
    svg.text(748, 947, "6 pieces · 96 cells", 17, fill=MUTED)
    svg.text(748, 975, "exactly one layer everywhere", 17, fill=MUTED)
    svg.save("seed_all_lines.svg", "Decorative: six contributor colours restart in every assembly.",
             "All 14 complete lines tile R without gaps or overlapping interiors. Overlaying all 36 pieces instead covers R six times, because it overlays six complete rows.",
             dict(verified_lines=14, multiplicity_per_line=1, all_array_multiplicity=6))


def atom_recipe():
    svg = SVG(1130, 690, "From placement words to labelled atoms",
              "The 24 by 4 grid is split into six sectors. The top panel prints the matching index m in every atom. The lower panel selects the 16 atoms of piece i=0,j=2, and prints the quantum colour l together with the actual coefficient sign in each occupied atom.")
    svg.text(28, 34, "What one rectangular atom records", 25, weight="bold")
    svg.text(28, 64, "Read sectors left to right, starting at the bottom row. Use m to select a Table I record.", 17, fill=MUTED)
    x, y, w, h = 46, 132, 1038, 173
    cw, ch = w/24, h/4
    svg.frame(x, y, w, h, "#fff")
    for c, v, k, m, tau, sigma in atoms():
        xx, yy = x+c*cw, y+(3-v)*ch
        svg.rect(xx, yy, cw, ch, QCOL[k], "#fff", .8, opacity=.17)
        svg.text(xx+cw/2, yy+ch/2+7, m, 21, "middle")
    for k in range(6):
        svg.text(x+(4*k+2)*cw, y-15, f"sector k = {k}", 17, "middle")
        if k:
            svg.line(x+4*k*cw, y, x+4*k*cw, y+h, INK, 1.6)
    svg.text(28, 350, "Select i = 0 and j = 2: keep exactly those atoms whose matching satisfies τ(0) = 2.", 18)
    svg.text(28, 380, "Each printed entry is ±l: the sign comes from Tᵍ, and l = σ(0).", 17, fill=MUTED)
    yy = 430
    svg.frame(x, yy, w, h)
    Tg = geomagic()
    selected = []
    counts = Counter()
    for c, v, k, m, tau, sigma in atoms():
        if int(tau[0]) != 2:
            continue
        ell = int(sigma[0])
        a, b = Tg[0, 2, k, ell]
        sign = "−" if a+b*sqrt(2) < 0 else "+"
        xx, yyy = x+c*cw, yy+(3-v)*ch
        svg.rect(xx, yyy, cw, ch, QCOL[ell], "#fff", .8, opacity=.82)
        svg.text(xx+cw/2, yyy+ch/2+7, f"{sign}{ell}", 19, "middle", "#111")
        selected.append((c, v))
        counts[k, ell] += 1
    assert frozenset(selected) == BASE[0, 2] and len(selected) == 16
    for k in range(6):
        svg.text(x+(4*k+2)*cw, yy-15, f"k = {k}", 17, "middle", MUTED)
        if k:
            svg.line(x+4*k*cw, yy, x+4*k*cw, yy+h, LINE, 1)
    svg.text(28, 645, "Each atom has area fraction 1/96. Add all fragments with the same (i,j,k,l) before taking a square root.", 17, fill=MUTED)
    svg.save("atom_recipe.svg", "Top: pale colour marks sector k. Bottom: colour and printed digit mark quantum l. The printed ± is the actual seed sign.",
             "The first four eight-character placement words are expanded by repeating every character twice. Here the displayed grid is read from bottom to top, so the earliest row is at the bottom. Fragment areas must be aggregated before decoding a coefficient.",
             dict(piece=[0, 2], selected_cells=16, coefficient_fragment_counts={f"{k},{l}": v for (k,l),v in sorted(counts.items())}))


def coefficient_bridge():
    pair, k, ell = (0, 4), 0, 4
    selected = frozenset((a,b) for a,b,kk,m,tau,sigma in atoms()
                         if kk == k and int(tau[pair[0]]) == pair[1]
                         and int(sigma[pair[0]]) == ell)
    assert selected == frozenset(((0,0),(1,0),(2,3),(3,3)))
    assert geomagic()[0,4,0,4] == (-2,0)
    svg = SVG(960, 520, "The coefficient Tᵍ[0,4,0,4] in a rectangular piece",
              "The piece with i=0,j=4 has 16 atoms. Four highlighted gold atoms, at (0,0), (1,0), (2,3), (3,3), carry sector k=0, colour l=4 and a minus sign. Their total area fraction is four over ninety-six, or one over twenty-four, and they encode Tᵍ[0,4,0,4]=minus one half.")
    svg.text(28, 34, "Piece (i,j) = (0,4)", 24, weight="bold")
    svg.text(28, 62, "Gold: k = 0, l = 4, sign −. The other occupied atoms are pale.", 18, fill=MUTED)
    x, y, w = 29, 111, 902
    h = w/sqrt(6)
    svg.frame(x, y, w, h)
    svg.cells(x, y, w, h, BASE[pair], color="#cedce1")
    svg.cells(x, y, w, h, selected, color=GOLD)
    for sec in range(6):
        svg.text(x+w*(sec+.5)/6, y-15, f"k = {sec}", 18, "middle", MUTED)
        if sec:
            svg.line(x+w*sec/6, y, x+w*sec/6, y+h, LINE, 1.1, dashed=True)
    for a,b in selected:
        svg.text(x+(a+.5)*w/24, y+(3.5-b)*h/4+7, "−4", 21, "middle", "#38270b")
    svg.text(28, 507, "4 atoms → area fraction 4/96 = 1/24 → Tᵍ₀₄₀₄ = −1/2 → normalized amplitude ψ₀₄₀₄ = −1/12", 17, fill=MUTED)
    svg.save("coefficient_bridge.svg", "Gold identifies one specified quantum coefficient. Its printed −4 means sign minus and quantum colour l=4. Pale occupied cells belong to other coefficients.",
             "This is the rectangular encoding of the same signed area data used by the hexagonal picture. The four highlighted fragments must be combined before decoding. Coordinates count columns from the left and rows from the bottom.",
             dict(piece=[0,4], k=0, l=4, highlighted_atoms=sorted(selected), highlighted_count=4,
                  area_fraction="1/24", matrix_coefficient="-1/2", normalized_state_amplitude="-1/12"))


def palette36():
    hues = (.49, .60, .76, .94, .075, .30)
    return ["#"+"".join(f"{round(255*c):02x}" for c in hls_to_rgb(hues[a], .32+.062*b, .64)) for a in range(6) for b in range(6)]


def row36():
    svg = SVG(1200, 800, "One complete depth-two row and its exact assembly",
              "The 36 panels on the left list one row I=(0,0) of the order-36 array. Their column addresses are J=(j1,j2). The large square is their exact superposition. All 9216 cells are covered once, with 256 cells contributed by each piece.")
    svg.text(28, 35, "A larger puzzle: 36 pieces fill one square", 25, weight="bold")
    svg.text(28, 65, "At depth 2 the complete geomagic array has 36 × 36 pieces. Below is just one of its rows.", 17, fill=MUTED)
    colors, pieces, keys = palette36(), {}, []
    left, top, side, step = 64, 149, 82, 96
    for b, j2 in enumerate(COL):
        svg.text(left+b*step+side/2, top-17, f"{j2}", 17, "middle", MUTED)
    svg.text(left+3*step-side/2, 105, "column address J = (j₁,j₂)", 17, "middle")
    svg.text(30, 131, "j₁ / j₂", 15, "middle", MUTED)
    for a, j1 in enumerate(COL):
        svg.text(left-20, top+a*step+side/2+5, str(j1), 17, "middle", MUTED)
        for b, j2 in enumerate(COL):
            cells, W, H = nested_mask(((0, j1), (0, j2)), BASE)
            assert len(cells) == 256 and (W, H) == (96, 96)
            key = (j1, j2)
            keys.append(key)
            pieces[key] = cells
            x, y = left+b*step, top+a*step
            svg.frame(x, y, side, side)
            svg.cells(x, y, side, side, cells, W, H, colors[6*a+b])
    coverage(pieces.values(), 96, 96)
    svg.line(652, 390, 695, 390, sw=2, arrow=True)
    assemble(svg, 730, 177, 418, 418, keys, colors, 96, 96, pieces)
    svg.text(939, 637, "96 × 96 cells", 21, "middle")
    svg.text(939, 668, "each covered exactly once", 17, "middle", MUTED)
    svg.text(939, 714, "Each piece occupies 1/36 of the target.", 17, "middle", MUTED)
    svg.text(28, 774, "Colours identify the 36 contributing pieces. A 6 × 6 contact sheet of this row is not the full order-36 array.", 17, fill=MUTED)
    svg.save("row36_assembly.svg", "Decorative: 36 colours identify the 36 contributors in one depth-two row.",
             "The 6×6 contact sheet is one complete row of a 36×36 geomagic array, not that array itself. Square coordinates are a common affine normalization of the rectangular construction.",
             dict(depth=2, row_address=[0, 0], row_pieces=36, array_order=36, full_array_pieces=1296, grid=[96, 96], cells_per_piece=256, verified_multiplicity=1))


def stationary_portraits():
    selected = ((0, 1), (4, 4), (5, 3))
    svg = SVG(1090, 1200, "Three stationary words at three finite depths",
              "Each row repeatedly chooses one fixed base piece, producing its depth-one, depth-two and depth-three approximations in square coordinates. These nine portraits are selected members of different arrays, not one tiling line. Fine detail is exact and remains visible on zooming the SVG.")
    svg.text(28, 35, "Repeat a piece: a self-similar portrait emerges", 25, weight="bold")
    svg.text(28, 65, "Read across a row. The address is (i,j), then (i,j)(i,j), then (i,j)(i,j)(i,j).", 17, fill=MUTED)
    side, xs = 290, (77, 413, 749)
    for d, x in enumerate(xs, 1):
        svg.text(x+side/2, 105, f"depth {d} · {16**d:,} cells", 18, "middle")
    for row, pair in enumerate(selected):
        y = 162+row*337
        svg.text(28, y-21, f"(i,j) = {pair}", 19, weight="bold")
        for dep, x in enumerate(xs, 1):
            cells, W, H = nested_mask((pair,)*dep, BASE)
            assert len(cells) == 16**dep
            svg.frame(x, y, side, side)
            svg.cells(x, y, side, side, cells, W, H, (TEAL, "#af7130", "#73548f")[row])
    svg.text(28, 1172, "These are finite, positive-area approximations. Their infinite attractors have zero area. These selected limits do not tile the square.", 16, fill=MUTED)
    svg.save("stationary_portraits.svg", "Decorative: one colour identifies each stationary address. No quantum labels or signs are shown.",
             "Square normalization is self-affine for one original step. Grouping two steps gives similarities. The selected stationary portraits are not a complete geomagic line or array. Open or zoom the SVG to inspect all exact depth-three cells.",
             dict(addresses=selected, depths=[1, 2, 3], cells_per_depth=[16, 256, 4096], grids=[[24,4],[96,96],[2304,384]]))


def detail4():
    pair = (0, 1)
    cells, W, H = nested_mask((pair,)*4, BASE)
    assert len(cells) == 65536 and (W, H) == (9216, 9216)
    svg = SVG(1000, 1070, "A depth-four stationary portrait, with every cell retained",
              "Exact square-normalized depth-four approximation for the repeated address (0,1). Its 65536 cells lie in a 9216 by 9216 grid and occupy area fraction 1/1296. This is one finite piece, not a complete target or an image of all quantum coefficients.")
    svg.text(28, 35, "One address, four repetitions", 25, weight="bold")
    svg.text(28, 66, "(i,j) = (0,1) at every level · 65,536 occupied cells · exact vector detail", 17, fill=MUTED)
    svg.frame(45, 100, 910, 910, "#fff")
    svg.cells(45, 100, 910, 910, cells, W, H, "#165d72")
    svg.text(28, 1046, "Zoom this figure to inspect the small cells. The pale area belongs to the target, not to this piece.", 17, fill=MUTED)
    svg.save("stationary_depth4.svg", "Decorative: a single blue colour shows occupied cells only.",
             "This sparse exact vector portrait is most useful at full size or under zoom. It is not an assembled puzzle, and labels and signs needed to recover a quantum state are omitted.",
             dict(address=[0, 1], depth=4, cells=65536, grid=[9216, 9216], area_fraction="1/1296"))


def stationary_gallery():
    svg = SVG(1200, 1440, "All thirty-six stationary depth-two portraits",
              "Every panel repeats its own base label (i,j) twice, showing P at depth two with I=(i,i) and J=(j,j) in square coordinates. Each of the 36 portraits contains exactly 256 cells in a 96 by 96 target grid. The row and column order is the base display order, but these selected depth-two portraits are not a complete order-36 geomagic array or one of its tiling lines.")
    svg.text(28, 36, "All 36 stationary addresses", 28, weight="bold")
    svg.text(28, 69, "Repeat each label twice: I = (i,i), J = (j,j). Every portrait has 256 cells in its own 96 × 96 target.", 20, fill=MUTED)
    left, top, side, sx, sy = 88, 148, 164, 182, 209
    for col, j in enumerate(COL):
        svg.text(left+col*sx+side/2, top-22, f"j = {j}", 22, "middle", MUTED)
    for row, i in enumerate(ROW):
        y = top+row*sy
        svg.text(left-20, y+side/2+7, f"i = {i}", 21, "end", MUTED)
        for col, j in enumerate(COL):
            cells, W, H = nested_mask(((i,j),(i,j)), BASE)
            assert len(cells) == 256 and (W,H) == (96,96)
            x = left+col*sx
            svg.frame(x, y, side, side)
            svg.cells(x, y, side, side, cells, W, H, PAL[col])
    svg.text(28, 1391, "These portraits share the same limiting dimension, but they are selected pieces rather than a complete tiling line.", 19, fill=MUTED)
    svg.text(28, 1422, "Colours identify display columns only. The sector words, quantum-colour words and signs are not displayed.", 19, fill=MUTED)
    svg.save("stationary_gallery.svg", "Decorative: colour identifies the display column only, not a quantum label.",
             "Each panel is P^(2)_((i,i),(j,j)). The base display order is retained to label all 36 stationary choices, but it does not make this selection the order-36 array or a complete tiling line. Each full square frame is a separate target. Only its coloured cells belong to the piece.",
             dict(portraits=36, depth=2, cells_per_portrait=256, grid=[96,96], row_order=ROW, column_order=COL,
                  addresses="I=(i,i), J=(j,j)", view_box=[1200,1440], minimum_label_size=19))


def ifs_step():
    pair = (0, 1)
    atom = (8, 1)
    inner = BASE[pair]
    leaves, W, H = nested_mask((pair, pair), BASE)
    group = frozenset((4*atom[0]+v, 24*(atom[1]+1)-1-c) for c, v in inner)
    assert len(group) == 16 and group <= leaves
    svg = SVG(1110, 790, "How the quarter-turn substitution works",
              "The selected base mask is replaced inside each of its 16 atoms by a clockwise rotated, uniformly shrunken copy of itself. A highlighted atom is enlarged below. All 16 descendants in that block are shown in their exact relative positions. The rectangle aspect ratio is square root of six throughout.")
    svg.text(28, 34, "One rule at every occupied atom", 25, weight="bold")
    svg.text(28, 64, "Shrink by 1/√96, rotate clockwise by 90°, and put the copy into the selected atom.", 17, fill=MUTED)
    ph = 164
    pw = ph*sqrt(6)
    x1, x2, y = 42, 654, 145
    svg.text(x1+pw/2, 123, "One piece: 16 atoms", 20, "middle")
    svg.text(x2+pw/2, 123, "Replace every atom: 256 cells", 20, "middle")
    svg.frame(x1, y, pw, ph)
    svg.cells(x1, y, pw, ph, inner, color=TEAL)
    svg.frame(x2, y, pw, ph)
    svg.cells(x2, y, pw, ph, leaves, W, H, TEAL)
    svg.cells(x2, y, pw, ph, group, W, H, GOLD)
    svg.line(489, 225, 606, 225, sw=2, arrow=True)
    svg.text(548, 198, "same rule", 17, "middle", MUTED)
    for xx in (x1, x2):
        bx, by = xx+atom[0]*pw/24, y+(3-atom[1])*ph/4
        svg.rect(bx, by, pw/24, ph/4, stroke="#754f18", sw=2.2)
    svg.text(28, 374, "Inside the highlighted atom", 21, weight="bold")
    svg.text(28, 404, "A quarter-turn changes the wide rectangle into the tall atom. No stretching occurs in the physical rectangle.", 17, fill=MUTED)
    zx, zy, zw, zh = 108, 451, 105, 105*sqrt(6)
    svg.frame(zx, zy, zw, zh)
    # The highlighted block occupies four fine columns and 24 fine rows.
    local = frozenset((x-4*atom[0], yy-24*atom[1]) for x, yy in group)
    assert all(0 <= x < 4 and 0 <= yy < 24 for x, yy in local)
    svg.cells(zx, zy, zw, zh, local, 4, 24, GOLD)
    svg.line(269, 582, 370, 582, sw=2, arrow=True)
    svg.text(424, 492, "16 occupied descendants", 21)
    svg.text(424, 529, "Each copy has the original rectangle’s shape.", 18, fill=MUTED)
    svg.text(424, 565, "Each length is multiplied by 1/√96.", 18, fill=MUTED)
    svg.text(424, 601, "Each area is multiplied by 1/96.", 18, fill=MUTED)
    svg.text(424, 653, "16 retained copies give area fraction 16/96 = 1/6.", 18)
    svg.text(28, 761, "This geometric rule uses the same atom data as the seed. The coloured zoom is an enlargement, not an additional piece.", 16, fill=MUTED)
    svg.save("ifs_step.svg", "Decorative: teal is occupied geometry. Gold identifies one atom and its descendants.",
             "The selected stationary address is (0,1), and the enlarged outer atom is (a,b)=(8,1). All copies are Euclidean similarities in the physical rectangle R. The golden block contains precisely 16 depth-two leaves.",
             dict(address=[0,1], highlighted_atom=atom, base_cells=16, depth_two_cells=256, highlighted_leaves=16, contraction="1/sqrt(96)"))


def square_bridge():
    svg = SVG(1080, 625, "The same tiling in rectangle and square coordinates",
              "Six pieces from base row i=0 tile the physical rectangle. Applying one common horizontal rescaling maps them to a tiling of the unit square with identical relative areas. The six square-normalized pieces are displayed separately below.")
    svg.text(28, 35, "A square target works too", 25, weight="bold")
    svg.text(28, 66, "Apply the same horizontal rescaling to every piece and to the target.", 17, fill=MUTED)
    line = [(0, j) for j in COL]
    y, h = 135, 183
    w = h*sqrt(6)
    svg.text(35+w/2, y-20, "Rectangle R", 20, "middle")
    svg.text(927, y-20, "Unit square", 20, "middle")
    assemble(svg, 35, y, w, h, line)
    assemble(svg, 835, y, h, h, line)
    svg.text(653, 198, "S(x,y) = (x/√6,y)", 20, "middle")
    svg.line(545, 230, 771, 230, sw=2, arrow=True)
    svg.text(653, 267, "same relative areas", 17, "middle", MUTED)
    svg.text(28, 366, "The six corresponding pieces in square coordinates", 20)
    for ind, key in enumerate(line):
        x = 47+ind*172
        svg.frame(x, 398, 130, 130)
        svg.cells(x, 398, 130, 130, BASE[key], color=PAL[ind])
        svg.text(x+65, 555, f"j = {key[1]}", 17, "middle", MUTED)
    svg.text(28, 599, "In square coordinates one step is self-affine. Two steps together form a similarity with ratio 1/96.", 17, fill=MUTED)
    svg.save("square_bridge.svg", "Decorative: six contributor colours identify the corresponding pieces on both sides.",
             "The common affine rescaling preserves areas as fractions of the target and preserves exact coverage. Noncongruence after square normalization is a separate property, verified by the supplied exact checks. It does not follow from arbitrary affine maps in general.",
             dict(row=0, pieces=6, square_map="S(x,y)=(x/sqrt(6),y)", grouped_contraction="1/96"))


def controlled_sign():
    outer, inner = (0, 2), (2, 0)
    groups = {(a,b): frozenset((4*a+y, 24*(b+1)-1-x) for x,y in BASE[inner]) for a,b in BASE[outer]}
    all_cells, W, H = nested_mask((outer, inner), BASE)
    flipped = frozenset().union(*(cells for (a,b),cells in groups.items() if a//4 == 0))
    assert all_cells == frozenset().union(*groups.values())
    assert len(all_cells) == 256 and len(flipped) == 64
    svg = SVG(1090, 640, "A controlled sign changes the state while leaving the geometry fixed",
              "Two copies of the depth-two piece I=(0,2),J=(2,0) are displayed at identical coordinates. On the right, exactly 64 of its 256 leaves acquire the extra factor minus one because the outer sector k1 is zero and the inner row digit i2 is two. Gold displays only the extra sign, not the original coefficient signs.")
    svg.text(28, 35, "Same geometry, a different sign rule", 25, weight="bold")
    svg.text(28, 65, "Example: I = (0,2), J = (2,0). Toggle a sign when k₁ = 0 and i₂ = 2.", 17, fill=MUTED)
    ph, pw, yy = 180, 180*sqrt(6), 140
    for side, x in enumerate((36, 610)):
        svg.text(x+pw/2, 118, "Product geometry" if side == 0 else "Add the controlled minus", 20, "middle")
        svg.frame(x, yy, pw, ph)
        svg.cells(x, yy, pw, ph, all_cells, W, H, TEAL)
        if side:
            svg.cells(x, yy, pw, ph, flipped, W, H, GOLD)
        svg.line(x+pw/6, yy, x+pw/6, yy+ph, LINE, 1.2, dashed=True)
        svg.text(x+pw/12, yy+ph+28, "k₁ = 0", 17, "middle", MUTED)
    svg.text(28, 394, "The extra factor is −1 on 64 leaves and +1 on the other 192.", 20)
    svg.text(28, 428, "An extra minus toggles the ordinary product sign. It need not make the final coefficient negative.", 17, fill=MUTED)
    block = (0,2)
    detail = groups[block]
    local = frozenset((x-4*block[0], y-24*block[1]) for x,y in detail)
    svg.frame(57, 474, 44, 108)
    svg.cells(57, 474, 44, 108, local, 4, 24, GOLD)
    svg.text(130, 505, "One affected outer atom contains 16 descendants.", 18)
    svg.text(130, 538, "Four affected outer atoms give 4 × 16 = 64 sign toggles.", 18, fill=MUTED)
    svg.text(130, 572, "All occupied positions and all area magnitudes are unchanged.", 18, fill=MUTED)
    svg.text(28, 619, "Gold shows the additional control factor only. The original seed signs and quantum colour labels are not displayed here.", 16, fill=MUTED)
    svg.save("controlled_sign.svg", "Decorative geometry plus extra-control marker: gold means multiplication by −1 in addition to the seed product sign.",
             "The two panels have exactly the same 256 occupied cells. The prescribed one-index control changes the AME state while preserving the geometry. This illustration alone does not certify AME. That requires the controlled-unitarity argument and exact seed.",
             dict(I=[0,2], J=[2,0], leaves=256, extra_minus_leaves=64, control="[k1=0][i2=2]"))


def refine_mask(cells, t):
    return frozenset((t*x+u,t*y+v) for x,y in cells for u,v in product(range(t), repeat=2))


def refined_depth(cells, t, depth):
    base = refine_mask(cells, t)
    result, W, H = frozenset({(0,0)}), 1, 1
    for _ in range(depth):
        result = frozenset((a*H+y, (b+1)*W-1-x) for a,b in base for x,y in result)
        W, H = 24*t*H, 4*t*W
    return result, W, H


def refinement():
    pair = (0,1)
    svg = SVG(1110, 970, "The dimension depends on the chosen geometric encoding",
              "The same base piece is subdivided into t by t smaller atoms, with t equal to one, two and three. In each column the top row shows the identical base shape, and the bottom row shows the exact second iteration of its refined substitution rule. The associated similarity dimensions differ although the aggregate state coefficients do not.")
    svg.text(28, 35, "One state, several fractal geometries", 25, weight="bold")
    svg.text(28, 65, "Subdivide every atom into t × t labelled subatoms before applying the replacement rule.", 17, fill=MUTED)
    xs, side = (59, 415, 771), 280
    for t, x in enumerate(xs, 1):
        svg.text(x+side/2, 107, f"t = {t}", 21, "middle", weight="bold")
        base = refine_mask(BASE[pair], t)
        svg.frame(x, 139, side, side)
        svg.cells(x, 139, side, side, base, 24*t, 4*t, TEAL)
        svg.text(x+side/2, 451, f"{16*t*t} retained subatoms", 17, "middle", MUTED)
        cells, W, H = refined_depth(BASE[pair], t, 2)
        assert len(cells) == (16*t*t)**2 and len(cells)*36 == W*H
        svg.frame(x, 510, side, side)
        svg.cells(x, 510, side, side, cells, W, H, TEAL)
        dimension = log(16*t*t)/log(t*sqrt(96))
        svg.text(x+side/2, 825, f"s = {dimension:.6f}…", 21, "middle")
        svg.text(x+side/2, 854, f"{len(cells):,} cells at depth 2", 16, "middle", MUTED)
    svg.text(28, 900, "Top row: identical base pieces. Bottom row: different recursive geometries, each with area fraction 1/36.", 17)
    svg.text(28, 934, "All refined subatoms inherit the same labels and signs. Hausdorff dimension is an encoding choice, not a quantum-state invariant.", 16, fill=MUTED)
    svg.save("dimension_refinement.svg", "Decorative: teal shows occupied geometry. No quantum labels or signs are displayed.",
             "For t×t refinement, s_t = log(16t²)/log(t√96). The first-level shapes and the decoded aggregate amplitudes are unchanged. At deeper levels the shape changes. This figure compares exact depth-two stationary approximations.",
             dict(address=pair, refinements=[1,2,3], dimension=[log(16*t*t)/log(t*sqrt(96)) for t in (1,2,3)], depth=2, area_fraction="1/36"))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    assert len(BASE) == 36 and {len(p) for p in BASE.values()} == {16}
    for i in range(6):
        coverage([BASE[i,j] for j in range(6)], 24, 4)
    for j in range(6):
        coverage([BASE[i,j] for i in range(6)], 24, 4)
    for line in (list(zip(ROW,COL)), list(zip(ROW,reversed(COL)))):
        coverage([BASE[key] for key in line], 24, 4)
    for make in (seed_atlas, all_lines, atom_recipe, coefficient_bridge, row36, stationary_portraits,
                 detail4, stationary_gallery, ifs_step, square_bridge, controlled_sign, refinement):
        make()
    (OUT / "figure_manifest.json").write_text(json.dumps(META, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    print(f"Built {len(META)} exact SVG figures in {OUT}")
    print("Verified all 14 base tilings, the complete depth-two row, controlled-sign counts, and every rendered cell count.")
    for item in META:
        path = OUT / item['file']
        print(f"{item['file']}: {path.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
