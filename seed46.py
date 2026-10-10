"""Exact seed and rectangle data for FRAME46; Python standard library only.

Tensors are sparse dictionaries indexed by (i,j,k,l).  A value (a,b)
means 4*T[i,j,k,l] = a + b*sqrt(2).  Thus the normalized AME state is T/6.
Table I and B1 are transcribed from the supplied manuscript, version 6.
Rectangle coordinates (c,v) have 24 columns and 4 rows, counted bottom-up.
The pieces may be disconnected; their components keep fixed positions.
"""

from collections import Counter
from itertools import permutations, product


def add(p, q):
    return p[0] + q[0], p[1] + q[1]


def mul(p, q):
    """Multiply the numerators a+b*sqrt(2), with no implicit rescaling."""
    return p[0]*q[0] + 2*p[1]*q[1], p[0]*q[1] + p[1]*q[0]


H = ((1, 1), (1, -1))                 # Numerators; divide by sqrt(2).
R = ((1, 1), (-1, 1))
ROTATIONS = ((0, 0, H), (1, 0, H), (1, 2, H), (2, 4, R))


def seed():
    """Construct the 60 nonzero entries of T from the signed-Pauli recipe."""
    I, X = ((1, 0), (0, 1)), ((0, 1), (1, 0))
    Z, J = ((1, 0), (0, -1)), ((0, 1), (-1, 0))  # J=iY=ZX.
    minus = lambda M: tuple(tuple(-x for x in row) for row in M)
    table = {"AB": (Z, J, I, X), "AC": (minus(Z), minus(I), X, minus(J)),
             "AD": (J, I, minus(Z), X), "BC": (X, Z, I, J),
             "BD": (I, Z, minus(J), X), "CD": (I, X, Z, minus(J))}
    T = {}
    for pair, blocks in table.items():
        named = ["ABCD".index(letter) for letter in pair]
        other = [axis for axis in range(4) if axis not in named]
        for level, block in enumerate(blocks):
            for u, v in product(range(2), repeat=2):
                if block[u][v]:
                    t = [0]*4
                    t[named[0]] = t[named[1]] = level
                    t[other[0]], t[other[1]] = 4+u, 4+v
                    T[tuple(t)] = (0, 2*block[u][v])
    for t in permutations(range(4)):
        if sum(t[a] > t[b] for a in range(4) for b in range(a+1, 4)) % 2:
            T[t] = (4, 0)
    return T


def rotate(T, axis, start, block):
    """Apply block/sqrt(2) on the selected pair of levels of one party."""
    result = {}
    for t, value in T.items():
        if t[axis] not in (start, start+1):
            result[t] = add(result.get(t, (0, 0)), value)
            continue
        a, b = value
        if a % 2:
            raise ArithmeticError("This rotation needs a finer integer scale")
        for row in range(2):
            sign = block[row][t[axis]-start]
            address = list(t)
            address[axis] = start+row
            address = tuple(address)
            term = sign*b, sign*(a//2)  # (a+b*sqrt(2))/sqrt(2).
            result[address] = add(result.get(address, (0, 0)), term)
    return {t: value for t, value in result.items() if value != (0, 0)}


def geomagic(T=None):
    """Return Tg=(OA tensor OB tensor OC tensor I)T at the same scale."""
    T = seed() if T is None else T
    for axis, start, block in ROTATIONS:
        T = rotate(T, axis, start, block)
    return T


# Table I: sector k, matching m, tau, sigma1, sigma2 (or None), denominator.
# Every sigma word has weight 1/denominator.  Leading zeroes are significant.
TABLE = (
    (0, 0, '251340', '253104', None, 4),
    (0, 1, '341205', '243150', None, 4),
    (0, 2, '430215', '423150', None, 4),
    (0, 3, '520341', '523104', None, 4),
    (1, 0, '253014', '350241', None, 4),
    (1, 1, '342051', '340215', None, 4),
    (1, 2, '432150', '430215', None, 4),
    (1, 3, '523104', '530241', None, 4),
    (2, 0, '035142', '314025', None, 4),
    (2, 1, '124035', '315042', None, 4),
    (2, 2, '215043', '134025', None, 4),
    (2, 3, '304125', '135042', None, 4),
    (3, 0, '031452', '201534', None, 4),
    (3, 1, '120534', '201453', None, 4),
    (3, 2, '210453', '021534', None, 4),
    (3, 3, '301524', '021453', None, 4),
    (4, 0, '142530', '415320', '504321', 16),
    (4, 1, '145203', '412503', '502413', 16),
    (4, 2, '152403', '415302', '504312', 16),
    (4, 3, '154320', '402531', '512430', 16),
    (4, 4, '403512', '054312', '145302', 16),
    (4, 5, '405231', '042531', '152430', 16),
    (4, 6, '503421', '054321', '145320', 16),
    (4, 7, '504312', '052413', '142503', 16),
    (5, 0, '042513', '415302', '504312', 16),
    (5, 1, '045231', '412530', '502431', 16),
    (5, 2, '052431', '415320', '504321', 16),
    (5, 3, '054312', '402513', '512403', 16),
    (5, 4, '413520', '054321', '145320', 16),
    (5, 5, '415203', '042513', '152403', 16),
    (5, 6, '513402', '054312', '145302', 16),
    (5, 7, '514320', '052431', '142530', 16),
)
B1 = ('23310102', '21303021', '32113020', '11302230',
      '7632321056014475', '6013617402535724')
DIAGONALS = ((2, 3, 4, 5, 0, 1), (3, 2, 5, 4, 1, 0))


def atoms():
    """Return 96 tuples (column,row,sector,matching,tau,sigma)."""
    table = {(k, m): (tau, s1, s2) for k, m, tau, s1, s2, den in TABLE}
    result = []
    for k, word in enumerate(B1):
        word = ''.join(digit*2 for digit in word) if k < 4 else word
        seen = Counter()
        for t, digit in enumerate(word):
            m = int(digit)
            tau, s1, s2 = table[k, m]
            sigma = s1 if s2 is None or seen[m] == 0 else s2
            result.append((4*k+t % 4, t//4, k, m, tau, sigma))
            seen[m] += 1
    return result


def masks():
    """Return the 36 pieces as {(i,j): frozenset[(column,row)]}."""
    pieces = {(i, j): set() for i, j in product(range(6), repeat=2)}
    for c, v, k, m, tau, sigma in atoms():
        for i in range(6):
            pieces[i, int(tau[i])].add((c, v))
    return {p: frozenset(cells) for p, cells in pieces.items()}


def nested_mask(word, pieces=None):
    """Return (occupied cells,width,height) for an outer-to-inner cell word.

    In R=[0,sqrt(6)] x [0,1], the clockwise map for atom (c,v) is
    (x,y) -> (c*sqrt(6)/24+y/(4*sqrt(6)), (v+1)/4-x/(4*sqrt(6))).
    Its contraction ratio is 1/sqrt(96).  Only 16**len(word) cells are stored.
    """
    pieces = masks() if pieces is None else pieces
    cells, W, H = frozenset({(0, 0)}), 1, 1
    for p in reversed(tuple(word)):
        cells = frozenset((c*H+y, (v+1)*W-1-x)
                          for c, v in pieces[p] for x, y in cells)
        W, H = 24*H, 4*W
    return cells, W, H
