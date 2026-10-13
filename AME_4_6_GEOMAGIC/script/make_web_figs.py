"""Pictures AME46_geomagic_a01..a03.png.

Notation as in the paper "Geomagic Square Representation of a Real AME(4,6) State":
T is the sparse tensor of Eqs. (1)-(2), T^g = (O_A x O_B x O_C x I_6) T with
O_A = H + I_4, O_B = H + H + I_2, O_C = I_4 + HX (Eq. (5)), and the pieces follow
Table I and Eq. (B1) with the canonical equal split of Appendix B: every thin triangle
covers 1/8 of the outer edge in sectors 0-3 and 1/16 in sectors 4 and 5.

Color l is shown twice, by its fill color and by its own texture; a minus sign is a
black dot just outside the rim, one per thin triangle.

  a01  the full geomagic square with row, column and diagonal assemblies
  a02  cell (0, 4) enlarged, with the color l written next to each group of triangles
  a03  sector 0 of the top row assembling one full sector

Run: python make_web_figs.py [output_folder]  (default: the folder above scripts/)
Uses ame46.py and the drawing helpers of make_figures.py.  Color 5 is hatched in white on a dark
fill, which needs a hatch color of its own: matplotlib >= 3.10 takes hatchcolor= per patch, while
older versions draw the hatch in the edge color, so there the hatch is laid over as a second patch.
"""
import math
import os
import sys
from fractions import Fraction

import numpy as np
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle

import ame46 as am
import make_figures as mf
from make_figures import vertex, fan

OUT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.dirname(am.HERE)
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({'font.family': 'DejaVu Sans', 'hatch.linewidth': 0.7})
COL, INK, GRAY, DIAG_COLORS = mf.COLORS, mf.INK, mf.GRAY, mf.DIAG_COLORS
TEX = ['', '-----', '|||||', '.....', '\\\\\\\\\\', 'xxx']
HCOL = [INK, INK, INK, INK, INK, 'white']

try:  # matplotlib >= 3.10 takes the hatch color per patch
    Polygon([(0, 0), (1, 0), (0, 1)], hatchcolor='k')
    _HATCHCOLOR_KW = True
except AttributeError:  # older versions draw the hatch in the edge color
    _HATCHCOLOR_KW = False


def add_hatched(ax, cls, *args, l, **kw):
    """Add cls(*args, **kw) filled with color l and hatched with texture TEX[l] in color HCOL[l].

    Without hatchcolor= the hatch would take the edge color, so the patch is split into the
    three passes matplotlib makes internally: fill, then hatch in HCOL[l], then the outline
    (lw=0 suppresses an outline without affecting the hatch).
    """
    if _HATCHCOLOR_KW:
        ax.add_patch(cls(*args, fc=COL[l], hatch=TEX[l] or None, hatchcolor=HCOL[l], **kw))
        return
    if not TEX[l]:
        ax.add_patch(cls(*args, fc=COL[l], **kw))
        return
    bare = {k: v for k, v in kw.items() if k not in ('ec', 'lw')}
    ax.add_patch(cls(*args, fc=COL[l], ec='none', lw=0, **bare))
    ax.add_patch(cls(*args, fc='none', ec=HCOL[l], lw=0, hatch=TEX[l], **bare))
    ax.add_patch(cls(*args, fc='none', **kw))

LS_MAIN, LS_ANTI = (0, (5, 2)), (0, (1, 1.6))
SECTOR_SLOT, DIAG_MAIN, DIAG_ANTI = am.SECTOR_SLOT, am.DIAG_MAIN, am.DIAG_ANTI
ROW_ORDER, COL_ORDER = am.ROW_ORDER, am.COL_ORDER

FR = am.colored_fragments(fans=am.canonical_fans())
TG = am.to_float(*am.geomagic_tensor_exact())


def rim(c, k, t, S):
    return c + S * mf.boundary_point(SECTOR_SLOT[k] + float(t))


def draw_frag(ax, c, f, S, lw=0.2, dot=1.6, out=1.09):
    """Thin triangle f; if negative, a minus dot of size `dot` (pt) at radius `out` (circumradius units)."""
    i, j, k, l, t0, t1 = f
    add_hatched(ax, Polygon, fan(c, k, t0, t1, S), l=l, closed=True, ec=INK, lw=lw, zorder=2)
    if TG[i, j, k, l] < 0:
        p = rim(c, k, (t0 + t1) / 2, S * out)
        ax.plot(p[0], p[1], 'o', ms=dot, mfc='black', mec='none', zorder=5)


def hexagon(ax, c, S, lw=0.8):
    ax.add_patch(Polygon([c + S * vertex(m) for m in range(6)], closed=True, fill=False, ec=INK, lw=lw, zorder=4))
    for m in range(6):
        p = c + S * vertex(m)
        ax.plot([c[0], p[0]], [c[1], p[1]], color=GRAY, lw=0.3, zorder=1)


def legend(ax, x0, y0, sw, gap, fs, rows=1, dot=4.0):
    per = 6 if rows == 1 else 3
    for l in range(6):
        x = x0 + (l % per) * gap; y = y0 - (l // per) * 0.9
        add_hatched(ax, Rectangle, (x, y - 0.28), sw, 0.56, l=l, ec=INK, lw=0.6)
        ax.text(x + sw + 0.12, y, str(l), ha='left', va='center', fontsize=fs, color=INK)
    x = x0 + (6 if rows == 1 else 3) * gap + 0.1; y = y0 if rows == 1 else y0 - 0.45
    ax.plot(x + sw / 2, y, 'o', ms=dot, mfc='black', mec='none')
    ax.text(x + sw + 0.15, y, 'dot at rim = minus', ha='left', va='center', fontsize=fs, color=INK)


def full_square():
    dx, dy, gap = 2.3, 2.15, 0.55
    pr = {i: n for n, i in enumerate(ROW_ORDER)}; pc = {j: n for n, j in enumerate(COL_ORDER)}
    fig, ax = plt.subplots(figsize=(8.6, 9.9)); ax.set_aspect('equal'); ax.axis('off')
    for i in range(6):
        for j in range(6):
            c = np.array([pc[j] * dx, -pr[i] * dy])
            for f in FR:
                if (f[0], f[1]) == (i, j): draw_frag(ax, c, f, 1.0)
            hexagon(ax, c, 1.0)
            for D, col, ls in ((DIAG_MAIN, DIAG_COLORS[0], LS_MAIN), (DIAG_ANTI, DIAG_COLORS[1], LS_ANTI)):
                if D[i] == j:
                    w, h = 0.97 * dx, 0.97 * dy
                    ax.add_patch(Rectangle(c - [w / 2, h / 2], w, h, fill=False, ec=col, lw=1.1, ls=ls, zorder=6))
    for n, i in enumerate(ROW_ORDER):
        ax.text(-dx / 2 - 0.35, -n * dy, str(i), ha='right', va='center', fontsize=11, fontweight='bold', color=INK)
    for n, j in enumerate(COL_ORDER):
        ax.text(n * dx, dy / 2 + 0.05, str(j), ha='center', va='bottom', fontsize=11, fontweight='bold', color=INK)
    ax.text(-dx / 2 - 0.35, dy / 2 + 0.05, r'$i\ \backslash\ j$', ha='right', va='bottom', fontsize=10, color=INK)
    xr, yc = 6 * dx + gap, -(6 * dy + gap)
    for n, i in enumerate(ROW_ORDER):
        c = np.array([xr, -n * dy])
        for f in FR:
            if f[0] == i: draw_frag(ax, c, f, 1.0)
        hexagon(ax, c, 1.0)
    for n, j in enumerate(COL_ORDER):
        c = np.array([n * dx, yc])
        for f in FR:
            if f[1] == j: draw_frag(ax, c, f, 1.0)
        hexagon(ax, c, 1.0)
    ax.plot([6 * dx - dx / 2 + gap / 2] * 2, [dy / 2, yc - dy / 2], color=INK, lw=1.2)
    ax.plot([-dx / 2, xr + dx / 2], [-(6 * dy - dy / 2 + gap / 2)] * 2, color=INK, lw=1.2)
    ax.text(xr, dy / 2 + 0.05, 'rows', ha='center', va='bottom', fontsize=9, color=INK)
    ax.text(-dx / 2 - 0.35, yc, 'columns', ha='right', va='center', fontsize=9, color=INK)
    c = np.array([xr, yc]); hexagon(ax, c, 1.0)
    for k in range(6):
        p = c + 0.58 * (vertex(SECTOR_SLOT[k]) + vertex(SECTOR_SLOT[k] + 1)) / 2 / math.cos(math.radians(30))
        ax.text(p[0], p[1], str(k), ha='center', va='center', fontsize=8, color=INK)
    ax.text(xr, yc - dy / 2 - 0.05, 'sector $k$', ha='center', va='top', fontsize=9, color=INK)
    yd = yc - dy - gap
    for x0, D, col, name, ls in ((1.5 * dx, DIAG_MAIN, DIAG_COLORS[0], 'main diagonal', LS_MAIN),
                                 (4.15 * dx, DIAG_ANTI, DIAG_COLORS[1], 'other diagonal', LS_ANTI)):
        c = np.array([x0, yd])
        for f in FR:
            if f[1] == D[f[0]]: draw_frag(ax, c, f, 1.0)
        hexagon(ax, c, 1.0)
        ax.plot([x0 + 1.2, x0 + 1.95], [yd, yd], color=col, lw=1.4, ls=ls)
        ax.text(x0 + 2.1, yd, name, ha='left', va='center', fontsize=9, color=col)
    yl = yd - 1.75
    ax.text(-dx / 2, yl + 0.45, 'color $l$', ha='left', va='bottom', fontsize=9, color=INK)
    legend(ax, -dx / 2, yl, sw=0.6, gap=1.35, fs=9, dot=2.6)
    ax.set_xlim(-dx / 2 - 1.3, xr + dx / 2 + 0.1); ax.set_ylim(yl - 0.5, dy / 2 + 0.6)
    fig.savefig(os.path.join(OUT, 'AME46_geomagic_a01.png'), dpi=300, bbox_inches='tight', pad_inches=0.03)
    plt.close(fig)


def example_cell(i=0, j=4):
    fig, ax = plt.subplots(figsize=(6.0, 6.6)); ax.set_aspect('equal'); ax.axis('off')
    c = np.zeros(2); S = 2.0
    cell = sorted([f for f in FR if (f[0], f[1]) == (i, j)], key=lambda f: (SECTOR_SLOT[f[2]], f[4]))
    for f in cell: draw_frag(ax, c, f, S, lw=0.4, dot=5.0, out=1.05)
    hexagon(ax, c, S, lw=1.3)
    s0 = SECTOR_SLOT[0]
    ax.add_patch(Polygon([c, c + S * vertex(s0), c + S * vertex(s0 + 1)], closed=True, fill=False, ec=INK, lw=2.6, zorder=7))
    runs = []
    for f in cell:
        if runs and runs[-1][0] == f[2] and runs[-1][1] == f[3] and runs[-1][3] == f[4]: runs[-1][3] = f[5]
        else: runs.append([f[2], f[3], f[4], f[5]])
    last = None
    for k, l, a, b in runs:
        tau = SECTOR_SLOT[k] + float(a + b) / 2
        far = last is not None and abs(tau - last[0]) < 0.12 and not last[1]
        q = rim(c, k, (a + b) / 2, S * (1.29 if far else 1.16))
        ax.text(q[0], q[1], str(l), ha='center', va='center', fontsize=12, fontweight='bold', color=INK)
        last = (tau, far)
    for k in range(6):
        s = SECTOR_SLOT[k]; mid = (vertex(s) + vertex(s + 1)) / 2
        ax.text(*(c + S * 0.42 * mid), f'k={k}', ha='center', va='center', fontsize=9, color='#5b6874',
                bbox=dict(boxstyle='round,pad=0.15', fc='white', ec='none', alpha=0.85), zorder=8)
    legend(ax, -2.45, -2.75, sw=0.42, gap=1.0, fs=10, rows=2, dot=5.0)
    ax.set_xlim(-2.75, 2.75); ax.set_ylim(-4.0, 2.6)
    fig.savefig(os.path.join(OUT, 'AME46_geomagic_a02.png'), dpi=200, bbox_inches='tight', pad_inches=0.05)
    plt.close(fig)


def row_strip():
    fig, ax = plt.subplots(figsize=(11, 2.5)); ax.set_aspect('equal'); ax.axis('off')
    d, S = 2.75, 1.0
    row = [f for f in FR if f[0] == 0 and f[2] == 0]
    for n, j in enumerate(COL_ORDER):
        c = np.array([n * d, 0.0])
        for f in row:
            if f[1] == j: draw_frag(ax, c, f, S, dot=2.2)
        hexagon(ax, c, S, lw=0.9)
        ax.text(c[0], -1.12, f'$(0,{j})$', ha='center', va='top', fontsize=12, color=INK)
        if n < 5: ax.text(c[0] + d / 2, 0, '+', ha='center', va='center', fontsize=16, color=INK)
    c = np.array([6 * d + 0.25, 0.0])
    ax.text(c[0] - d / 2 - 0.15, 0, '=', ha='center', va='center', fontsize=18, color=INK)
    for f in row: draw_frag(ax, c, f, S, dot=2.2)
    hexagon(ax, c, S, lw=1.4)
    ax.text(c[0], -1.12, 'row 0', ha='center', va='top', fontsize=12, color=INK)
    ax.set_xlim(-1.2, c[0] + 1.2); ax.set_ylim(-1.55, 1.1)
    fig.savefig(os.path.join(OUT, 'AME46_geomagic_a03.png'), dpi=200, bbox_inches='tight', pad_inches=0.05)
    plt.close(fig)


if __name__ == '__main__':
    A = np.zeros((6,) * 4)
    for i, j, k, l, t0, t1 in FR:
        A[i, j, k, l] += float(t1 - t0)
    assert np.allclose(A, TG ** 2), 'areas do not reproduce T^g'
    widths = {f[5] - f[4] for f in FR}
    assert widths <= {Fraction(1, 8), Fraction(1, 16)}, widths
    full_square(); example_cell(); row_strip()
    print('pictures written to', os.path.normpath(OUT), '; fragment widths', sorted(widths))
