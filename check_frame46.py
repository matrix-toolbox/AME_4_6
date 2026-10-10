"""Run with: python3 check_frame46.py

All algebra and areas use integers; no numerical tolerance is involved.
The checks establish finite certificates used by the proofs in FRAME46.tex.
The controlled chain is product_r Tg[i_r,j_r,k_r,l_r] times
(-1)**sum_r([k_r=0]*[i_(r+1)=2]); its normalized state divides this by 6**n.
The four-copy invariant uses A:(01)(23), B:(02)(13), C:id, D:(03)(12).
Its numerator J_n has denominator 6**(8*n).  See check_recurrence below.
"""

from collections import Counter, defaultdict
from itertools import combinations, product
from time import perf_counter
from seed46 import (TABLE, B1, DIAGONALS, ROTATIONS, add, mul, seed, rotate,
                    geomagic, atoms, masks, nested_mask)


def check(condition, message):
    if not condition:
        raise AssertionError(message)  # Also runs when Python is invoked with -O.


def two_unitary(T, d, scale=4):
    """Values encode scale*T.  Check three real Gram matrices exactly."""
    for order in ((0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 2, 1)):
        columns = defaultdict(list)
        for t, value in T.items():
            row = d*t[order[0]] + t[order[1]]
            col = d*t[order[2]] + t[order[3]]
            columns[col].append((row, value))
        gram = {}
        for column in columns.values():
            for (r, x), (s, y) in product(column, repeat=2):
                gram[r, s] = add(gram.get((r, s), (0, 0)), mul(x, y))
        for r in range(d*d):
            gram[r, r] = add(gram.get((r, r), (0, 0)), (-scale*scale, 0))
        check(all(x == (0, 0) for x in gram.values()), f"Gram failed: d={d}, {order}")


def check_seeds():
    T, G = seed(), geomagic()
    check(Counter(T.values()) == {(4, 0): 12, (0, 2): 34, (0, -2): 14}, "Seed values")
    check(len(G) == 152, "Geomagic support")
    check(Counter(mul(q, q) for q in G.values()) == {(8, 0): 24, (4, 0): 64, (2, 0): 64},
          "Geomagic coefficient squares")
    two_unitary(T, 6)
    two_unitary(G, 6)
    back = G
    for axis, start, block in reversed(ROTATIONS):
        back = rotate(back, axis, start, tuple(zip(*block)))
    check(back == T, "Inverse local rotations")
    check(G[0, 4, 0, 4] == (-2, 0), "Worked coefficient Tg[0,4,0,4]=-1/2")
    print("PASS: T has 60 entries; Tg has 152; all three cuts and inverse rotations are exact.")
    return T, G


def check_table(G):
    area = defaultdict(int)  # Units of 1/16; these equal |Tg|^2.
    check(len(TABLE) == len({(r[0], r[1]) for r in TABLE}) == 32, "Table records")
    check(sum(1+(r[4] is not None) for r in TABLE) == 48, "Weighted transversals")
    for k, m, tau, s1, s2, den in TABLE:
        check(sorted(tau) == list("012345"), "Matching permutation")
        for diagonal in DIAGONALS:
            check(sum(int(tau[i]) == diagonal[i] for i in range(6)) == 1, "Diagonal")
        for sigma in (s1, s2):
            if sigma is not None:
                check(sorted(sigma) == list("012345"), "Colour permutation")
                for i in range(6):
                    area[i, int(tau[i]), k, int(sigma[i])] += 16//den
    check(dict(area) == {t: mul(q, q)[0] for t, q in G.items()}, "All Table I areas")
    for k, word in enumerate(B1):
        check(Counter(map(int, word)) == {r[1]: 2 for r in TABLE if r[0] == k}, "B1")
    for axes in combinations(range(4), 2):
        marginal = Counter()
        for t, weight in area.items():
            marginal[tuple(t[a] for a in axes)] += weight
        check(len(marginal) == 36 and set(marginal.values()) == {16}, "Area marginal")
    print("PASS: 32 Table I records, 48 weighted transversals, all 152 coefficient areas.")
    return area


def d2_images(cells):
    """Four reflections, each translated to have minimum x=y=0."""
    images = []
    for sx, sy in product((1, -1), repeat=2):
        moved = [(sx*x, sy*y) for x, y in cells]
        x0, y0 = min(x for x, y in moved), min(y for x, y in moved)
        images.append(tuple(sorted((x-x0, y-y0) for x, y in moved)))
    return images


def d4_images(cells):
    """Eight square-grid isometries, normalized by translation as above."""
    return d2_images(cells) + d2_images([(y, x) for x, y in cells])


def check_geometry(area):
    A, P = atoms(), masks()
    grid = {(c, v) for c in range(24) for v in range(4)}
    check(len(A) == 96 and {(a[0], a[1]) for a in A} == grid, "96 rectangle atoms")
    check(len(P) == 36 and {len(p) for p in P.values()} == {16}, "36 masks")
    reconstructed, colours = Counter(), [Counter() for _ in range(6)]
    for c, v, k, m, tau, sigma in A:
        for i in range(6):
            j, colour = int(tau[i]), int(sigma[i])
            reconstructed[i, j, k, colour] += 1
            colours[colour][c, v] += 1
    check(reconstructed == area, "Rectangle areas agree with Table I")
    lines = [[(i, j) for j in range(6)] for i in range(6)]
    lines += [[(i, j) for i in range(6)] for j in range(6)]
    lines += [[(i, diagonal[i]) for i in range(6)] for diagonal in DIAGONALS]
    covers = colours + [Counter(t for p in line for t in P[p]) for line in lines]
    check(all(set(c) == grid and set(c.values()) == {1} for c in covers), "All tilings")
    check(len({image for p in P.values() for image in d2_images(p)}) == 144, "D2 images")
    print("PASS: 96 atoms; 36 masks; 144 distinct normalized D2 images; 14 line tilings.")
    print("PASS: all six colours cover the rectangle exactly once.")
    return P


def check_square_base(P):
    # S(x,y)=(x/sqrt(6),y): each old cell is six unit cells of a 24x24 grid.
    images = {image for cells in P.values()
              for image in d4_images({(c, 6*v+t) for c, v in cells for t in range(6)})}
    check(len(images) == 288, "Square-normalized base D4 images")
    print("PASS: 36 square-normalized base masks have 288 distinct D4 images.")


def check_level_two(P):
    classes, square_classes = set(), set()
    for p, q in product(P, repeat=2):
        cells, W, H = nested_mask((p, q), P)
        check((W, H, len(cells)) == (96, 96, 256), "Level-two grid and atom count")
        classes.add(min(d2_images(cells)))
        images = d4_images(cells)  # The square-normalized level-two grid is isotropic.
        check(len(set(images)) == 8, "Level-two square mask has eight distinct D4 images")
        square_classes.add(min(images))
    check(len(classes) == 1296, "Level-two congruence classes")
    print("PASS: all 1296 level-two masks are distinct under translations and D2.")
    check(len(square_classes) == 1296, "Square-normalized level-two D4 classes")
    print("PASS: 1296 square-normalized level-two masks have 10,368 distinct D4 images.")


def check_controlled(T):
    # These controls commute with OA (mixes 0,1) and OC (mixes 4,5).
    for axis, start, block in ROTATIONS:
        check(not (axis == 0 and 2 in (start, start+1)), "A=2 control commutation")
        check(not (axis == 2 and 0 in (start, start+1)), "C=0 control commutation")
    W = {}
    for outer, inner in product(T, repeat=2):
        address = tuple(6*a+b for a, b in zip(outer, inner))
        sign = -1 if outer[2] == 0 and inner[0] == 2 else 1
        a, b = mul(T[outer], T[inner])
        W[address] = sign*a, sign*b  # 16*W, since each factor encodes 4*T.
    check(len(W) == 3600, "Controlled support")
    two_unitary(W, 36, scale=16)
    print("PASS: controlled AME(4,36), 3600 sparse entries, all three cuts exact.")


def compute_F(T):
    """Recompute the eight-factor contraction using sparse bit-mask joins.

    Four ket addresses determine four bra addresses via the copy permutations.
    Given t0,t1,t2, intersect four restrictions to find possible t3 addresses.
    State order is 00,10,01,11; F rows are C=0 parities and columns A=2 parities.
    """
    support = sorted(T)
    values = {t: 2 if q == (4, 0) else q[1]//2 for t, q in T.items()}
    by_value = [defaultdict(int) for _ in range(4)]
    for number, t in enumerate(support):
        for axis, value in enumerate(t):
            by_value[axis][value] |= 1 << number
    completions = [defaultdict(int) for _ in range(4)]
    for t in support:
        for axis in range(4):
            completions[axis][t[:axis]+t[axis+1:]] |= by_value[axis][t[axis]]
    scaled, histogram = [[0]*4 for _ in range(4)], Counter()
    for t0, t1, t2 in product(support, repeat=3):
        a0, b0, c0, d0 = t0
        a1, b1, c1, d1 = t1
        a2, b2, c2, d2 = t2
        choices = (completions[3].get((a1, b2, c0), 0)
                   & completions[1].get((a0, c1, d2), 0)
                   & completions[0].get((b0, c2, d1), 0)
                   & completions[2].get((a2, b1, d0), 0))
        while choices:
            bit = choices & -choices
            choices ^= bit
            t3 = support[bit.bit_length()-1]
            a3, b3, c3, d3 = t3
            bra = ((a1, b2, c0, d3), (a0, b3, c1, d2),
                   (a3, b0, c2, d1), (a2, b1, c3, d0))
            factors = [values[t] for t in (t0, t1, t2, t3, *bra)]
            halves = sum(abs(x) == 1 for x in factors)
            check(halves % 2 == 0, "Unexpected radical in invariant term")
            sign = (-1)**sum(x < 0 for x in factors)
            control = int((c0 == 0) != (c1 == 0)) + 2*int((c2 == 0) != (c3 == 0))
            target = int((a0 == 2) != (a1 == 2)) + 2*int((a2 == 2) != (a3 == 2))
            scaled[control][target] += sign * (1 << ((8-halves)//2))
            histogram[halves] += 1  # All terms accumulated in units of 1/16.
    check(histogram == {0: 36, 6: 640, 8: 1728}, "2404 invariant assignments")
    check(all(x % 16 == 0 for row in scaled for x in row), "Integral matrix F")
    F = tuple(tuple(x//16 for x in row) for row in scaled)
    check(F == ((44, -3, -3, 10), (-3, 8, 1, 0), (-3, 1, 8, 0), (10, 0, 0, 2)), "F")
    print("PASS: F recomputed exactly from 2404 nonzero eight-factor assignments:")
    for row in F:
        print("     ", row)
    return F


def mv(M, v):
    return tuple(sum(a*b for a, b in zip(row, v)) for row in M)


def check_recurrence(F):
    H = [[(-1)**bin(s & e).count('1') for e in range(4)] for s in range(4)]
    M = [[sum(F[i][e]*H[e][j] for e in range(4)) for j in range(4)] for i in range(4)]
    reduced = ((48, 68, 60), (6, -6, -12), (12, 16, 12))
    # Checking coefficients of these linear identities proves them for all a,b,c.
    for a, b, c in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
        ap, bp, cp = mv(reduced, (a, b, c))
        check(mv(M, (a, b, b, c)) == (ap, bp, bp, cp), "Recurrence reduction")
        check(bp == 6*(a-b-2*c), "Nonnegative b inside the cone")
        check(ap-bp-2*cp == 18*a+42*b+48*c, "Invariant cone")
        check(72*(a+2*b+c)-(ap+2*bp+cp) == 72*b+24*c, "Strict comparison")
    v = mv(F, (1, 1, 1, 1))
    check(v == (48, 6, 6, 12), "Initial invariant vector")
    sequence = []
    for n in range(1, 9):
        a, b, other_b, c = v
        check(b == other_b and a >= b+2*c and b >= 0 and c > 0, "Cone positivity")
        J = sum(v)
        check(J > 0 and (n == 1 or J < 72**n), "Chain and plain power differ")
        sequence.append(J)
        v = mv(M, v)
    check(sequence[:2] == [72, 4464], "First invariant values")
    print("PASS: J_(n+1) recurrence and all-depth cone/comparison identities.")
    print("      J_1,...,J_8 =", sequence)
    print("      J_n/6^(8n) differs from 72^n/6^(8n) for every n >= 2.")


def main():
    started = perf_counter()
    T, G = check_seeds()
    area = check_table(G)
    P = check_geometry(area)
    check_square_base(P)
    check_controlled(T)
    check_recurrence(compute_F(T))
    check_level_two(P)
    print(f"All exact checks passed in {perf_counter()-started:.3f} seconds.")


if __name__ == "__main__":
    main()
