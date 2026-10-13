"""Export the tensors and matrices in plain-text form.

  data/T60_nonzero.csv           -->  60 nonzero entries of the sparse tensor T
  data/Tg152_nonzero.csv         -->  152 nonzero entries of the geomagic representative T^g
  data/U60.csv, data/Ug152.csv   -->  36x36 matrices U[6i+j, 6k+l] (floating point, 17 digits)
  data/perimeters.csv            -->  exact rational perimeter bounds of the 36 pieces

Run: python make_data.py
"""
import csv
import itertools
import math
import os

import numpy as np

import ame46 as am

NAMES = {1.0: '1', 1 / math.sqrt(2): '1/sqrt(2)', 0.5: '1/2', 1 / (2 * math.sqrt(2)): '1/(2*sqrt(2))'}


def exact_name(v):
    for mag, name in NAMES.items():
        if math.isclose(abs(v), mag):
            return ('-' if v < 0 else '') + name
    raise ValueError(v)


def export_tensor(T, path, title):
    with open(path, 'w', newline='') as f:
        f.write(f'# {title}; state = T/6; U[6i+j,6k+l] = T[i,j,k,l]\n')
        w = csv.writer(f)
        w.writerow(['i', 'j', 'k', 'l', 'value', 'value_float'])
        for idx in itertools.product(range(6), repeat=4):
            if abs(T[idx]) > 1e-12:
                w.writerow([*idx, exact_name(T[idx]), repr(float(T[idx]))])


if __name__ == '__main__':
    T = am.to_float(*am.sparse_tensor_exact())
    Tg = am.to_float(*am.geomagic_tensor_exact())
    export_tensor(T, os.path.join(am.DATA, 'T60_nonzero.csv'), 'sparse real AME(4,6) tensor T (60 nonzero entries)')
    export_tensor(Tg, os.path.join(am.DATA, 'Tg152_nonzero.csv'),
                  'geomagic representative T^g = (O_A x O_B x O_C x I) T (152 nonzero entries)')
    np.savetxt(os.path.join(am.DATA, 'U60.csv'), am.flatten(T, 'U (AB|CD)'), delimiter=',', fmt='%.17g')
    np.savetxt(os.path.join(am.DATA, 'Ug152.csv'), am.flatten(Tg, 'U (AB|CD)'), delimiter=',', fmt='%.17g')
    frags = am.colored_fragments()
    with open(os.path.join(am.DATA, 'perimeters.csv'), 'w', newline='') as f:
        f.write('# perimeter P_ij of piece (i,j) for unit circumradius: lower <= P_ij < upper (exact rationals)\n')
        w = csv.writer(f)
        w.writerow(['i', 'j', 'lower', 'upper', 'lower_float'])
        for i, j in itertools.product(range(6), repeat=2):
            lo, hi = am.perimeter_bounds(am.piece_lobes(frags, i, j))
            w.writerow([i, j, str(lo), str(hi), f'{float(lo):.9f}'])
    print('data written to', am.DATA)
