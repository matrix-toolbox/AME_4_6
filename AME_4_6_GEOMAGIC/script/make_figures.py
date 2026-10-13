"""Draw the figures of the paper "Geomagic Square Representation of a Real AME(4,6) State" from the exact data.

  RAME46_G.{pdf,svg,png}                      -->  Fig. 1: genuine geomagic square of T^g (illustrated split)
  RAME46_matrix.{pdf,svg,png}                 -->  Fig. 2: the matrix U as a square 36x36 grid
  RAME46_matrix_table.tex                     -->  the same matrix as a LaTeX table
  AME46_GEOMAGIC_SILHOUETTES.{pdf,svg,png}    -->  36 pieces without colors (supplementary)

Run: python make_figures.py [output_folder] (default: the folder above scripts/)
"""
import math
import os
import sys

import numpy as np
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import patheffects
from matplotlib.patches import Polygon, Rectangle

import ame46 as am

OUT = os.path.abspath(sys.argv[1]) if __name__ == '__main__' and len(sys.argv) > 1 else os.path.dirname(am.HERE)
plt.rcParams.update({'font.family': 'DejaVu Sans', 'hatch.linewidth': 0.45, 'svg.fonttype': 'none'})

COLORS = ['#ff6666', '#65d8e8', '#dc6eeb', '#69d879', '#f0de5c', '#6867ef']
INK, GRAY = '#263442', '#9aa5b1'
DIAG_COLORS = ('#6d48ad', '#188b86')


def matrix_table():
    T = am.to_float(*am.sparse_tensor_exact())
    U = am.flatten(T, 'U (AB|CD)')
    lab = [f'{i}{j}' for i in range(6) for j in range(6)]

    def sym(v):
        if np.isclose(v, 1):
            return r'$\mathbf{1}$'
        if np.isclose(v, 1 / math.sqrt(2)):
            return '$+$'
        if np.isclose(v, -1 / math.sqrt(2)):
            return '$-$'
        return r'$\cdot$'

    lines = [r'\begin{tabular}{c|' + '|'.join(['c' * 6] * 6) + '}', ' & ' + ' & '.join(lab) + r'\\\hline']
    for r in range(36):
        end = r'\\\hline' if r % 6 == 5 and r < 35 else r'\\'
        lines.append(lab[r] + ' & ' + ' & '.join(sym(U[r, c]) for c in range(36)) + end)
    lines.append(r'\end{tabular}')
    with open(os.path.join(OUT, 'RAME46_matrix_table.tex'), 'w') as f:
        f.write('\n'.join(lines) + '\n')


def matrix_figure():
    """Fig. 2 of the paper: the 36x36 matrix U as a square grid with 6x6 blocks.

    Entries: black '1' for 1, red '+' and blue '-' for +-1/sqrt2, gray dot for 0. Row ij and column kl carry the
    block digit i (k) and the digit j (l) within the block, i.e. U[6i+j, 6k+l] = T[i,j,k,l].
    The figure is drawn at its final size, one REVTeX column (246 pt) wide, so that font sizes
    are the printed ones; include it with width=\\columnwidth.
    """
    T = am.to_float(*am.sparse_tensor_exact())
    U = am.flatten(T, 'U (AB|CD)')
    n = 36
    left, top, edge = 2.05, 2.0, 0.12
    cell = 246.0 / (n + left + edge)
    OPTICAL = {'1': (0.073, -0.190), '+': (0.010, 0.000), '-': (0.010, 0.008)}
    PLUS, MINUS = '#d0021b', '#1550c8'
    with plt.rc_context({'mathtext.fontset': 'cm'}):
        fig = plt.figure(figsize=(246.0 / 72.27, (n + top + edge) * cell / 72.27))
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_xlim(-left, n + edge)
        ax.set_ylim(-n - edge, top)
        ax.set_aspect('equal')
        ax.axis('off')
        for m in range(n + 1):
            heavy = m % 6 == 0
            kw = dict(color=INK if heavy else '#c3cad2', lw=0.7 if heavy else 0.25, zorder=2 if heavy else 1)
            ax.plot([0, n], [-m, -m], solid_capstyle='projecting', **kw)
            ax.plot([m, m], [0, -n], solid_capstyle='projecting', **kw)
        zeros = []
        for r in range(n):
            for c in range(n):
                v = U[r, c]
                if np.isclose(v, 1):
                    s, (dx, dy), col = r'$\mathbf{1}$', OPTICAL['1'], 'black'
                elif np.isclose(v, 1 / math.sqrt(2)):
                    s, (dx, dy), col = r'$+$', OPTICAL['+'], PLUS
                elif np.isclose(v, -1 / math.sqrt(2)):
                    s, (dx, dy), col = r'$-$', OPTICAL['-'], MINUS
                else:
                    zeros.append((c + 0.5, -r - 0.5))
                    continue
                t = ax.text(c + 0.5 + dx, -r - 0.5 + dy, s, ha='center', va='center', fontsize=6.3, color=col)
                if s != r'$\mathbf{1}$':
                    t.set_path_effects([patheffects.withStroke(linewidth=0.25, foreground=col)])
        ax.scatter(*zip(*zeros), s=0.9 ** 2, marker='o', color=GRAY, linewidths=0, zorder=3)
        for b in range(6):
            ax.text(-1.45, -6 * b - 3, f'${b}$', ha='center', va='center', fontsize=7.5, color=INK)
            ax.text(6 * b + 3, 1.45, f'${b}$', ha='center', va='center', fontsize=7.5, color=INK)
        for m in range(n):
            ax.text(-0.42, -m - 0.5, f'${m % 6}$', ha='center', va='center', fontsize=5.6, color=INK)
            ax.text(m + 0.5, 0.5, f'${m % 6}$', ha='center', va='center', fontsize=5.6, color=INK)
        for ext in ('pdf', 'svg', 'png'):
            fig.savefig(os.path.join(OUT, f'RAME46_matrix.{ext}'), dpi=600)
        plt.close(fig)


def vertex(m):
    a = math.radians(60 * m)
    return np.array([math.cos(a), math.sin(a)])


def boundary_point(tau):
    """Point of the unit hexagon at boundary parameter tau = slot + t."""
    m = math.floor(tau)
    t = tau - m
    return (1 - t) * vertex(m % 6) + t * vertex((m + 1) % 6)


def fan(center, k, t0, t1, scale=1.0):
    s = am.SECTOR_SLOT[k]
    pts = [np.zeros(2), boundary_point(s + float(t0)), boundary_point(s + float(t1))]
    return [center + scale * p for p in pts]


def hexagon(ax, c, scale=1.0, sectors=True, lw=0.7):
    ax.add_patch(Polygon([c + scale * vertex(m) for m in range(6)], closed=True, fill=False, ec=INK, lw=lw, zorder=3))
    if sectors:
        for m in range(6):
            p = c + scale * vertex(m)
            ax.plot([c[0], p[0]], [c[1], p[1]], color=GRAY, lw=0.3, zorder=1)


def draw_fragments(ax, c, frags, signs, scale=1.0):
    for (i, j, k, l, t0, t1) in frags:
        neg = signs[(i, j, k, l)] < 0
        ax.add_patch(Polygon(fan(c, k, t0, t1, scale), closed=True, fc=COLORS[l], ec=INK, lw=0.12,
                             hatch='//////' if neg else None, zorder=2))


def geomagic_figure(frags, Tg):
    """Fig. 1 of the paper: the genuine geomagic square of T^g with its row, column and diagonal assemblies."""
    signs = {(i, j, k, l): Tg[i, j, k, l] for i, j, k, l in np.ndindex(6, 6, 6, 6)}
    dx, dy, gap = 2.3, 2.15, 0.55
    pos_col = {j: n for n, j in enumerate(am.COL_ORDER)}
    pos_row = {i: n for n, i in enumerate(am.ROW_ORDER)}
    center = lambda n_row, n_col: np.array([n_col * dx, -n_row * dy])
    fig, ax = plt.subplots(figsize=(8.6, 9.9))
    ax.set_aspect('equal')
    ax.axis('off')
    for i in range(6):
        for j in range(6):
            c = center(pos_row[i], pos_col[j])
            draw_fragments(ax, c, [f for f in frags if (f[0], f[1]) == (i, j)], signs)
            hexagon(ax, c)
            for D, col in ((am.DIAG_MAIN, DIAG_COLORS[0]), (am.DIAG_ANTI, DIAG_COLORS[1])):
                if D[i] == j:
                    w, h = 0.97 * dx, 0.97 * dy
                    ax.add_patch(Rectangle(c - [w / 2, h / 2], w, h, fill=False, ec=col, lw=0.9,
                                           ls=(0, (3, 1.6)), zorder=4))
    for n, i in enumerate(am.ROW_ORDER):
        ax.text(-dx / 2 - 0.35, -n * dy, str(i), ha='right', va='center', fontsize=11, fontweight='bold', color=INK)
    for n, j in enumerate(am.COL_ORDER):
        ax.text(n * dx, dy / 2 + 0.05, str(j), ha='center', va='bottom', fontsize=11, fontweight='bold', color=INK)
    ax.text(-dx / 2 - 0.35, dy / 2 + 0.05, r'$i\ \backslash\ j$', ha='right', va='bottom', fontsize=10, color=INK)
    xr, yc = 6 * dx - dx / 2 + gap + dx / 2, -(6 * dy - dy / 2 + gap + dy / 2)
    for n, i in enumerate(am.ROW_ORDER):
        c = np.array([xr, -n * dy])
        draw_fragments(ax, c, [f for f in frags if f[0] == i], signs)
        hexagon(ax, c)
    for n, j in enumerate(am.COL_ORDER):
        c = np.array([n * dx, yc])
        draw_fragments(ax, c, [f for f in frags if f[1] == j], signs)
        hexagon(ax, c)
    ax.plot([6 * dx - dx / 2 + gap / 2] * 2, [dy / 2, yc - dy / 2], color=INK, lw=1.2)
    ax.plot([-dx / 2, xr + dx / 2], [-(6 * dy - dy / 2 + gap / 2)] * 2, color=INK, lw=1.2)
    ax.text(xr, dy / 2 + 0.05, 'rows', ha='center', va='bottom', fontsize=9, color=INK)
    ax.text(-dx / 2 - 0.35, yc, 'columns', ha='right', va='center', fontsize=9, color=INK)
    c = np.array([xr, yc])
    hexagon(ax, c)
    for k in range(6):
        p = c + 0.58 * (vertex(am.SECTOR_SLOT[k]) + vertex(am.SECTOR_SLOT[k] + 1)) / 2 / math.cos(math.radians(30))
        ax.text(p[0], p[1], str(k), ha='center', va='center', fontsize=8, color=INK)
    ax.text(xr, yc - dy / 2 - 0.05, 'sector $k$', ha='center', va='top', fontsize=9, color=INK)
    yd = yc - dy - gap
    for x0, D, col, name in ((1.5 * dx, am.DIAG_MAIN, DIAG_COLORS[0], 'main diagonal'),
                             (3.9 * dx, am.DIAG_ANTI, DIAG_COLORS[1], 'other diagonal')):
        c = np.array([x0, yd])
        draw_fragments(ax, c, [f for f in frags if f[1] == D[f[0]]], signs)
        hexagon(ax, c)
        ax.text(x0 + 1.2, yd, name, ha='left', va='center', fontsize=9, color=col)
    yl = yd - 1.75
    for l in range(6):
        x0 = -dx / 2 + l * 1.35
        ax.add_patch(Rectangle((x0, yl - 0.18), 0.55, 0.36, fc=COLORS[l], ec=INK, lw=0.5))
        ax.text(x0 + 0.7, yl, str(l), ha='left', va='center', fontsize=9, color=INK)
    x0 = -dx / 2 + 6 * 1.35 + 0.3
    ax.add_patch(Rectangle((x0, yl - 0.18), 0.55, 0.36, fc='white', ec=INK, lw=0.5, hatch='//////'))
    ax.text(x0 + 0.7, yl, 'negative coefficient', ha='left', va='center', fontsize=9, color=INK)
    ax.text(-dx / 2, yl + 0.45, 'color $l$', ha='left', va='bottom', fontsize=9, color=INK)
    ax.set_xlim(-dx / 2 - 1.3, xr + dx / 2 + 0.1)
    ax.set_ylim(yl - 0.5, dy / 2 + 0.6)
    for ext in ('pdf', 'svg', 'png'):
        fig.savefig(os.path.join(OUT, f'RAME46_G.{ext}'), bbox_inches='tight', pad_inches=0.03, dpi=300)
    plt.close(fig)


def lobe_polygon(c, a, b, scale=1.0):
    taus = [float(a)] + [m for m in range(math.ceil(float(a)), math.floor(float(b)) + 1) if a < m < b] + [float(b)]
    return [c] + [c + scale * boundary_point(t) for t in taus]


def silhouettes_figure(frags):
    """The 36 pieces without colors (supplementary figure)."""
    d = 2.45
    fig, ax = plt.subplots(figsize=(7.2, 7.6))
    ax.set_aspect('equal')
    ax.axis('off')
    for n_row, i in enumerate(am.ROW_ORDER):
        for n_col, j in enumerate(am.COL_ORDER):
            c = np.array([n_col * d, -n_row * d])
            for a, b in am.piece_lobes(frags, i, j):
                ax.add_patch(Polygon(lobe_polygon(c, a, b), closed=True, fc=INK, ec=INK, lw=0.15))
            ax.text(c[0], c[1] - 1.08, f'$({i},{j})$', ha='center', va='top', fontsize=9, color=INK)
    ax.set_xlim(-1.25, 5 * d + 1.25)
    ax.set_ylim(-5 * d - 1.5, 1.1)
    for ext in ('pdf', 'svg', 'png'):
        fig.savefig(os.path.join(OUT, f'AME46_GEOMAGIC_SILHOUETTES.{ext}'), bbox_inches='tight', pad_inches=0.03, dpi=300)
    plt.close(fig)


if __name__ == '__main__':
    frags = am.colored_fragments()
    Tg = am.to_float(*am.geomagic_tensor_exact())
    os.makedirs(OUT, exist_ok=True)
    matrix_table()
    matrix_figure()
    geomagic_figure(frags, Tg)
    silhouettes_figure(frags)
    print('figures written to', OUT)
