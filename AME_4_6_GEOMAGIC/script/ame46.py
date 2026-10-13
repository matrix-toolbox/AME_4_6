"""Sparse real AME(4,6) state and its geomagic representative.

conventions (as in the paper)
-----------------------------
* T[i,j,k,l], indices 0..5, subsystems A,B,C,D; the state is T/6
* U[6i+j, 6k+l] = T[i,j,k,l]
  UR[6i+k, 6j+l] = T[i,j,k,l]
  UG[6i+l, 6k+j] = T[i,j,k,l]
* exact arithmetic: a real tensor with entries in Q(sqrt2) is stored as integers
  (R, H, d) with T = (R + sqrt2 * H) / d
"""
import csv
import itertools
import math
import os
from fractions import Fraction

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data')

PAULI = {
    'I': np.array([[1, 0], [0, 1]]),
    'X': np.array([[0, 1], [1, 0]]),
    'Z': np.array([[1, 0], [0, -1]]),
    'iY': np.array([[0, 1], [-1, 0]]),
}
PARTY = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
CUTS = {'U (AB|CD)': (0, 1, 2, 3), 'UR (AC|BD)': (0, 2, 1, 3), 'UG (AD|CB)': (0, 3, 2, 1)}


def signed_pauli(name):
    sign = -1 if name.startswith('-') else 1
    return sign * PAULI[name.lstrip('-')]


def load_pair_table(path=os.path.join(DATA, 'pair_table.csv')):
    """Eq. (2): pair ab -> list of the four signed 2x2 matrices Xi^{ab}_x, x = 0..3."""
    table = {}
    with open(path) as f:
        rows = [r for r in f if not r.startswith('#')]
    for row in csv.DictReader(rows):
        table[row['pair']] = [signed_pauli(row[f'x{x}']) for x in range(4)]
    return table


def odd_permutations():
    return [q for q in itertools.permutations(range(4))
            if sum(q[a] > q[b] for a in range(4) for b in range(a + 1, 4)) % 2 == 1]


def sparse_tensor_exact(table=None):
    """The 60-term tensor T of Eqs. (1)-(2) as (R, H, d): units R=2, Bell entries H=Xi_uv, d=2."""
    table = table or load_pair_table()
    R = np.zeros((6,) * 4, dtype=np.int64)
    H = np.zeros((6,) * 4, dtype=np.int64)
    for q in odd_permutations():
        R[q] = 2
    for pair, Qs in table.items():
        a, b = PARTY[pair[0]], PARTY[pair[1]]
        c, d = [p for p in range(4) if p not in (a, b)]
        for x, Q in enumerate(Qs):
            for u, v in itertools.product(range(2), repeat=2):
                q = [0] * 4
                q[a] = q[b] = x
                q[c], q[d] = 4 + u, 4 + v
                H[tuple(q)] = Q[u, v]
    return R, H, 2


def to_float(R, H, d):
    return (R + math.sqrt(2) * H) / d


def flatten(T, cut):
    return T.transpose(CUTS[cut]).reshape(36, 36)


def exact_two_unitarity(R, H, d):
    """For every cut M = (R + sqrt2 H)/d check  R R^T + 2 H H^T = d^2 I  and  R H^T + H R^T = 0."""
    out = {}
    for cut in CUTS:
        MR, MH = flatten(R, cut), flatten(H, cut)
        a = MR @ MR.T + 2 * MH @ MH.T - d * d * np.eye(36, dtype=np.int64)
        b = MR @ MH.T + MH @ MR.T
        out[cut] = (int(np.count_nonzero(a)), int(np.count_nonzero(b)))
    return out


def apply_local_exact(T, O, party):
    """Apply a local matrix O = (Ro + sqrt2 Ho)/do to index `party` of T = (R, H, d)."""
    (R, H, d), (Ro, Ho, do) = T, O

    def act(M, A):
        return np.moveaxis(np.tensordot(M, A, axes=([1], [party])), 0, party)

    R2 = act(Ro, R) + 2 * act(Ho, H)
    H2 = act(Ro, H) + act(Ho, R)
    d2 = do * d
    g = math.gcd(d2, math.gcd(*map(int, np.abs(np.concatenate([R2.ravel(), H2.ravel()])))))
    return R2 // g, H2 // g, d2 // g


def local_exact(blocks):
    """Block-diagonal 6x6 local matrix. blocks: list of 'I1' (1x1 identity), 'H' or 'HX'."""
    Ro, Ho = np.zeros((6, 6), dtype=np.int64), np.zeros((6, 6), dtype=np.int64)
    r = 0
    for b in blocks:
        if b == 'I1':
            Ro[r, r] = 2
            r += 1
        else:
            Ho[r:r + 2, r:r + 2] = {'H': [[1, 1], [1, -1]], 'HX': [[1, 1], [-1, 1]]}[b]
            r += 2
    return Ro, Ho, 2


O_A = local_exact(['H', 'I1', 'I1', 'I1', 'I1'])
O_B = local_exact(['H', 'H', 'I1', 'I1'])
O_C = local_exact(['I1', 'I1', 'I1', 'I1', 'HX'])


def geomagic_tensor_exact():
    """T^g = (O_A x O_B x O_C x I_6) T of Eq. (5) as (R, H, d)."""
    T = sparse_tensor_exact()
    T = apply_local_exact(T, O_A, 0)
    T = apply_local_exact(T, O_B, 1)
    T = apply_local_exact(T, O_C, 2)
    return T


SECTOR_SLOT = (0, 1, 4, 5, 2, 3)
DIAG_MAIN = (2, 3, 4, 5, 0, 1)
DIAG_ANTI = (3, 2, 5, 4, 1, 0)
ROW_ORDER = (0, 2, 4, 5, 3, 1)
COL_ORDER = (2, 4, 0, 1, 5, 3)


def _rows(path):
    with open(path) as f:
        return list(csv.DictReader([r for r in f if not r.startswith('#')]))


def load_transversals(path=os.path.join(DATA, 'transversals.csv')):
    """Table I: (k, m) -> (tau, [sigma_1, (sigma_2)], weight w per color word)."""
    out = {}
    for r in _rows(path):
        s1 = r['sigma_1'] if 'sigma_1' in r else r['sigma1']
        s2 = r['sigma_2'] if 'sigma_2' in r else r['sigma2']
        sig = [[int(c) for c in s1]] + ([[int(c) for c in s2]] if s2 != '-' else [])
        out[(int(r['sector']), int(r['matching']))] = ([int(c) for c in r['tau']], sig, Fraction(r['weight']))
    return out


def load_fans(path=os.path.join(DATA, 'fans.csv')):
    """k -> (Eq. (B1) word, endpoints of the illustrated split) with endpoints = [0, e1/8000, ..., 1] as Fractions."""
    out = {}
    for r in _rows(path):
        ends = [Fraction(int(e), 8000) for e in r['endpoints_times_8000'].split(';')]
        out[int(r['sector'])] = ([int(c) for c in r['word']], [Fraction(0)] + ends + [Fraction(1)])
    return out


def canonical_fans(trans=None, fans=None):
    """The canonical equal split of Appendix B: each occurrence of a matching with q color words
    has length q w / 2, i.e. 1/8 in sectors 0-3 and 1/16 in sectors 4 and 5."""
    trans = trans or load_transversals()
    fans = fans or load_fans()
    out = {}
    for k, (word, _) in fans.items():
        ends = [Fraction(0)]
        for m in word:
            ends.append(ends[-1] + len(trans[(k, m)][1]) * trans[(k, m)][2] / 2)
        out[k] = (word, ends)
    return out


def colored_fragments(trans=None, fans=None):
    """All drawn fragments: (i, j, k, l, t0, t1) with exact t0 < t1 on the outer edge of sector k.

    Along the edge of sector k the intervals are occupied by matchings in the order of the
    Eq. (B1) word.  A matching m (permutation tau) puts the interval into the six cells (i, tau(i)).
    If it has one color word sigma, cell (i, tau(i)) gets color sigma(i).  If it has two color words,
    each receives total length w: the intervals of m are traversed in order and colored by sigma_1
    until its length w is used up, and by sigma_2 afterwards.  Default: the illustrated split of Fig. 1.
    """
    trans = trans or load_transversals()
    fans = fans or load_fans()
    frags = []
    for k, (word, ends) in fans.items():
        state = {}
        for n, m in enumerate(word):
            tau, sig, w = trans[(k, m)]
            ci, left = state.get(m, (0, w if len(sig) > 1 else None))
            a, b = ends[n], ends[n + 1]
            while a < b:
                step = b - a if left is None else min(b - a, left)
                for i in range(6):
                    frags.append((i, tau[i], k, sig[ci][i], a, a + step))
                a += step
                if left is not None:
                    left -= step
                    if left == 0 and ci + 1 < len(sig):
                        ci, left = ci + 1, w
            state[m] = (ci, left)
    return frags


def piece_lobes(frags, i, j):
    """Merged boundary intervals of piece (i,j) in tau = slot + t in [0,6), circularly merged."""
    iv = sorted((SECTOR_SLOT[k] + t0, SECTOR_SLOT[k] + t1)
                for (a, b, k, l, t0, t1) in frags if (a, b) == (i, j))
    merged = []
    for lo, hi in iv:
        if merged and lo <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], hi)
        else:
            merged.append([lo, hi])
    if len(merged) > 1 and merged[0][0] == 0 and merged[-1][1] == 6:
        first = merged.pop(0)
        merged[-1][1] = 6 + first[1]
    return [tuple(x) for x in merged]


def radius_sq(tau):
    """Squared distance from the center to the boundary point at tau (unit circumradius)."""
    t = tau - math.floor(tau)
    return t * t - t + 1


def perimeter_bounds(lobes, digits=12):
    """Exact rational bounds of the perimeter: outer length + radii, sqrt by integer isqrt."""
    scale = 10 ** digits
    lo = hi = sum(Fraction(b - a) for a, b in lobes)
    for a, b in lobes:
        for tau in (a, b):
            q = Fraction(radius_sq(Fraction(tau)))
            n = math.isqrt(int(q * scale * scale))
            if Fraction(n * n, scale * scale) == q:
                lo += Fraction(n, scale)
                hi += Fraction(n, scale)
            else:
                lo += Fraction(n, scale)
                hi += Fraction(n + 1, scale)
    return lo, hi
