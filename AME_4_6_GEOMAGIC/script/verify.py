"""Verify the finite tensor construction, two-unitarity and the geometric data of the paper.

All checks marked [exact] use integer or rational arithmetic only.
Run: python verify.py
"""
import itertools
import math
import sys
from fractions import Fraction

import numpy as np

import ame46 as am

failures = []


def check(label, ok, detail=''):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f"  ({detail})" if detail else ''))
    if not ok:
        failures.append(label)


s2 = math.sqrt(2)

print('Sec. II: construction of the sparse tensor T, Eqs. (1)-(2)')
R, H, d = am.sparse_tensor_exact()
T = am.to_float(R, H, d)
nz = np.abs(T) > 1e-12
check('60 nonzero entries', nz.sum() == 60, f'{nz.sum()}')
check('12 entries 1, 34 entries +1/sqrt2, 14 entries -1/sqrt2',
      (np.isclose(T, 1).sum(), np.isclose(T, 1 / s2).sum(), np.isclose(T, -1 / s2).sum()) == (12, 34, 14))
check('sum of squares = 36 [exact]', int((R * R + 2 * H * H).sum()) == 36 * d * d)
U = am.flatten(T, 'U (AB|CD)')
check('worked example x=3, pair AD: U[22,27],U[22,33],U[23,27],U[23,33] = 0, 1/sqrt2, 1/sqrt2, 0',
      np.allclose([U[22, 27], U[22, 33], U[23, 27], U[23, 33]], [0, 1 / s2, 1 / s2, 0]))

print('Sec. III: two-unitarity')
for cut, (a, b) in am.exact_two_unitarity(R, H, d).items():
    check(f'{cut} orthogonal [exact certificate]', (a, b) == (0, 0))

table = am.load_pair_table()
PAIRQ = {p: table[p] for p in table}
odd = am.odd_permutations()
R1 = [(i, j) for i in range(4) for j in range(4) if i != j]
DIAG = [(x, x) for x in range(4)]
NN = [(4, 4), (4, 5), (5, 4), (5, 5)]
MIX = [p for x in range(4) for p in [(x, 4), (x, 5), (4, x), (5, x)]]


def blockdiag(*Ms):
    n = sum(M.shape[0] for M in Ms)
    out = np.zeros((n, n))
    r = 0
    for M in Ms:
        k = M.shape[0]
        out[r:r + k, r:r + k] = M
        r += k
    return out


def blocks(row_pair, col_pair, K):
    Mrow = np.array([PAIRQ[row_pair[0]][x].T.ravel() if row_pair[1] else PAIRQ[row_pair[0]][x].ravel()
                     for x in range(4)]) / s2
    Mcol = np.array([PAIRQ[col_pair][x].ravel() for x in range(4)]).T / s2
    Ks = [np.block([[f(x) for f in r] for r in K]) / s2 for x in range(4)]
    return blockdiag(np.eye(12), Mrow, Mcol, *Ks)


def q(p, tr=False):
    return (lambda x: PAIRQ[p][x].T) if tr else (lambda x: PAIRQ[p][x])


specs = {'U (AB|CD)': (('AB', False), 'CD', [[q('AC'), q('AD')], [q('BC'), q('BD')]]),
         'UR (AC|BD)': (('AC', False), 'BD', [[q('AB'), q('AD', True)], [q('BC'), q('CD')]]),
         'UG (AD|CB)': (('AD', True), 'BC', [[q('AC', True), q('AB', True)], [q('CD'), q('BD')]])}
for cut, (rp, cp, K) in specs.items():
    M = am.flatten(T, cut)
    Tp = T.transpose(am.CUTS[cut])
    partner = {r: next((k, l) for k in range(4) for l in range(4) if np.isclose(Tp[r[0], r[1], k, l], 1)) for r in R1}
    rows = R1 + DIAG + NN + MIX
    cols = [partner[r] for r in R1] + NN + DIAG + MIX
    P = M[np.ix_([6 * a + b for a, b in rows], [6 * a + b for a, b in cols])]
    check(f'{cut} = I_12 + M + M + K_0..K_3 after reordering', np.allclose(P, blocks(rp, cp, K)))

print('Sec. IV: geomagic representative T^g, Eq. (5)')
Rg, Hg, dg = am.geomagic_tensor_exact()
Tg = am.to_float(Rg, Hg, dg)
check('T^g = (O_A x O_B x O_C x I) T  agrees with floating-point construction',
      np.allclose(Tg, np.einsum('ai,bj,ck,ijkl->abcl',
                                (am.O_A[0] + s2 * am.O_A[1]) / 2, (am.O_B[0] + s2 * am.O_B[1]) / 2,
                                (am.O_C[0] + s2 * am.O_C[1]) / 2, T)))
for cut, (a, b) in am.exact_two_unitarity(Rg, Hg, dg).items():
    check(f'T^g {cut} orthogonal [exact certificate]', (a, b) == (0, 0))
check('152 nonzero coefficients', (np.abs(Tg) > 1e-12).sum() == 152)
for mag, pos, neg in ((1 / s2, 18, 6), (0.5, 38, 26), (1 / (2 * s2), 36, 28)):
    m = np.isclose(np.abs(Tg), mag)
    check(f'|T^g| = {mag:.4f}: {pos} positive, {neg} negative', ((m & (Tg > 0)).sum(), (m & (Tg < 0)).sum()) == (pos, neg))
check('every coefficient is rational or a rational multiple of sqrt2 [exact]', not np.any(Rg * Hg))
W = [[[[Fraction(int(Rg[i, j, k, l]) ** 2 + 2 * int(Hg[i, j, k, l]) ** 2, dg * dg)
        for l in range(6)] for k in range(6)] for j in range(6)] for i in range(6)]
one = Fraction(1)
check('rows: sum_{j,l} T^2 = 1 for all i,k [exact]',
      all(sum(W[i][j][k][l] for j in range(6) for l in range(6)) == one for i in range(6) for k in range(6)))
check('columns: sum_{i,l} T^2 = 1 for all j,k [exact]',
      all(sum(W[i][j][k][l] for i in range(6) for l in range(6)) == one for j in range(6) for k in range(6)))
for name, D in (('main', am.DIAG_MAIN), ('other', am.DIAG_ANTI)):
    check(f'{name} diagonal j = {D}: sum_{{i,l}} T^2 = 1 for all k [exact]',
          all(sum(W[i][D[i]][k][l] for i in range(6) for l in range(6)) == one for k in range(6)))
check('colors: sum_{i,j} T^2 = 1 for all k,l [exact]',
      all(sum(W[i][j][k][l] for i in range(6) for j in range(6)) == one for k in range(6) for l in range(6)))
check('displayed orders put the cells (i,D(i)) and (i,D\'(i)) on the two main diagonals',
      all(am.COL_ORDER[n] == am.DIAG_MAIN[am.ROW_ORDER[n]] and am.COL_ORDER[5 - n] == am.DIAG_ANTI[am.ROW_ORDER[n]]
          for n in range(6)))

print('Sec. IV and App. B: Table I, Eq. (B1), thin triangles and tilings')
trans, fans = am.load_transversals(), am.load_fans()
check('48 colored transversals in 32 matchings', (sum(len(v[1]) for v in trans.values()), len(trans)) == (48, 32))
check('weights are 1/4 and 1/16', {v[2] for v in trans.values()} == {Fraction(1, 4), Fraction(1, 16)})
perm = lambda w: sorted(w) == list(range(6))
check('all tau and sigma are permutations', all(perm(p) and all(perm(z) for z in zs) for p, zs, w in trans.values()))
check('every tau meets each diagonal exactly once',
      all(sum(p[i] == am.DIAG_MAIN[i] for i in range(6)) == 1 and sum(p[i] == am.DIAG_ANTI[i] for i in range(6)) == 1
          for p, zs, w in trans.values()))
acc = {}
for (k, m), (p, zs, w) in trans.items():
    for z in zs:
        for i in range(6):
            acc[(i, p[i], k, z[i])] = acc.get((i, p[i], k, z[i]), 0) + w
check('transversal weights reproduce (T^g)^2 exactly [exact]',
      all(acc.get((i, j, k, l), 0) == W[i][j][k][l] for i, j, k, l in itertools.product(range(6), repeat=4)))
check('64 thin triangles, endpoints with denominator 8000',
      sum(len(w) for w, e in fans.values()) == 64 and all(8000 % x.denominator == 0 for w, e in fans.values() for x in e))
check('endpoints strictly increasing in every sector', all(all(a < b for a, b in zip(e, e[1:])) for w, e in fans.values()))
check('interval lengths of each matching = (number of color words) x weight [exact]',
      all(sum(e[n + 1] - e[n] for n, mm in enumerate(w) if mm == m) == len(trans[(k, m)][1]) * trans[(k, m)][2]
          for k, (w, e) in fans.items() for m in set(w)))
frags = am.colored_fragments(trans, fans)
check('80 colored subintervals (480 fragments)', len(frags) == 480, f'{len(frags)} fragments')
geo = {}
for (i, j, k, l, t0, t1) in frags:
    geo[(i, j, k, l)] = geo.get((i, j, k, l), 0) + (t1 - t0)
check('drawn fragment areas equal (T^g)^2 for every (i,j,k,l) [exact]',
      all(geo.get(key, 0) == W[key[0]][key[1]][key[2]][key[3]] for key in itertools.product(range(6), repeat=4)))
check('every fragment sits on a nonzero coefficient (sign defined)',
      all(abs(Tg[i, j, k, l]) > 1e-12 for (i, j, k, l, t0, t1) in frags))
by_iv = {}
for f in frags:
    by_iv.setdefault((f[2], f[4], f[5]), []).append(f)
lines = [('row', lambda f, a=a: f[0] == a) for a in range(6)] + [('col', lambda f, b=b: f[1] == b) for b in range(6)] + \
        [('diag', lambda f: f[1] == am.DIAG_MAIN[f[0]]), ('anti', lambda f: f[1] == am.DIAG_ANTI[f[0]])]
check('on every subinterval each of the 14 lines has exactly one cell (lines tile the hexagon)',
      all(sum(1 for f in fl if sel(f)) == 1 for fl in by_iv.values() for _, sel in lines))
check('on every subinterval the six cells carry six different colors',
      all(sorted(f[3] for f in fl) == list(range(6)) for fl in by_iv.values()))

print('Sec. IV and App. B: pieces, non-congruence and perimeters')
bounds = {}
for i, j in itertools.product(range(6), repeat=2):
    lobes = am.piece_lobes(frags, i, j)
    assert sum(b - a for a, b in lobes) == 1
    bounds[(i, j)] = am.perimeter_bounds(lobes)
check('every piece has the area of one sector [exact]', True)
iv = sorted(bounds.values())
gaps = [b[0] - a[1] for a, b in zip(iv, iv[1:])]
check('36 perimeter intervals pairwise disjoint [exact]', min(gaps) > 0, f'smallest gap {float(min(gaps)):.6f}')
check('smallest separation > 0.00485', min(gaps) > Fraction(485, 100000))
print('  perimeters (lower bounds, rows i, columns j in natural order):')
for i in range(6):
    print('   ', ' '.join(f'{float(bounds[(i, j)][0]):10.6f}' for j in range(6)))
SCALE = 16000
PERIOD = 6 * SCALE


def placement_classes(ends):
    """Number of congruence classes of the 36 pieces for every placement (sector k -> slot)."""
    runs = {(i, j): {k: [(int(ends[k][n] * SCALE), int(ends[k][n + 1] * SCALE))
                          for n, m in enumerate(fans[k][0]) if trans[(k, m)][0][i] == j] for k in range(6)}
            for i, j in itertools.product(range(6), repeat=2)}

    def merge(iv):
        iv = sorted((a % PERIOD, a % PERIOD + b - a) for a, b in iv)
        out = []
        for a, b in iv:
            if out and a <= out[-1][1]:
                out[-1] = (out[-1][0], max(out[-1][1], b))
            else:
                out.append((a, b))
        if len(out) > 1 and out[-1][1] >= out[0][0] + PERIOD:
            a, b = out.pop()
            out[0] = (a, out[0][1] + PERIOD)
        return tuple(out)

    def canon(S):
        return min(merge([(sg * (a if sg > 0 else b) + r * SCALE, sg * (b if sg > 0 else a) + r * SCALE)
                          for a, b in S]) for r in range(6) for sg in (1, -1))

    counts = []
    for slot in itertools.permutations(range(6)):
        pieces = [merge([(slot[k] * SCALE + a, slot[k] * SCALE + b) for k in range(6) for a, b in runs[c][k]])
                  for c in runs]
        counts.append(len({canon(S) for S in pieces}))
    return counts


canonical_ends = {}
for k, (word, e) in fans.items():
    L = [Fraction(0)]
    for m in word:
        L.append(L[-1] + len(trans[(k, m)][1]) * trans[(k, m)][2] / 2)
    canonical_ends[k] = L
for name, ends in (('canonical', canonical_ends), ('illustrated', {k: e for k, (w, e) in fans.items()})):
    counts = placement_classes(ends)
    check(f'all 720 sector placements give 36 pairwise non-congruent pieces ({name} split) [exact]',
          min(counts) == 36, f'{len(counts)} placements')
check('the twelve pieces of the sparse T with an entry 1 are single full sectors (congruent)',
      all(sum(np.isclose(T[i, j], 1).ravel()) == 1 for i, j in R1) and len(R1) == 12)

print()
if failures:
    print(f'{len(failures)} check(s) FAILED:', *failures, sep='\n  ')
    sys.exit(1)
print('all checks passed!')
