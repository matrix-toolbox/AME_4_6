#!/usr/bin/env python3
"""Export the exact FRAME46 seed and rectangle labels for the browser.

Use only the Python standard library.  Put seed46.py beside this script, then
run ``python3 export_data46.py`` from the companion page directory.
Alternatively pass ``--seed-dir PATH``.  No floating-point arithmetic is used
to build or check coefficients, areas, signs, or the matching data.
"""

import argparse
from collections import Counter
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
import json
from pathlib import Path


def rational(value):
    value = Fraction(value)
    return {"num": value.numerator, "den": value.denominator}


def require(condition, description):
    if not condition:
        raise AssertionError(description)


def load_seed(directory):
    path = directory / "seed46.py"
    spec = spec_from_file_location("frame46_export_seed", path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_data(seed_module):
    S = seed_module
    G = S.geomagic()
    all_atoms = S.atoms()
    masks = S.masks()
    addresses = sorted(G)
    entry_ids = {address: n for n, address in enumerate(addresses)}
    entries = []
    for address in addresses:
        a, b = G[address]
        require((a == 0) != (b == 0), "Every geometric coefficient is one signed radical")
        square_numerator, radical_part = S.mul((a, b), (a, b))
        require(radical_part == 0, "Every squared coefficient is rational")
        square = Fraction(square_numerator, 16)
        sign = 1 if a + b > 0 else -1  # Exactly one of a and b is nonzero.
        i, j, k, l = address
        entries.append({
            "id": entry_ids[address], "i": i, "j": j, "k": k, "l": l,
            "ring": [a, b], "sign": sign, "square": rational(square),
            "fragmentCount": square_numerator, "atomIds": [],
            "pictureArea": rational(square / 6),
            "stateProbability": rational(square / 36),
        })

    pieces = [{"id": 6*i+j, "i": i, "j": j, "atomIds": [], "cells": [],
               "placements": [], "entryIds": []}
              for i, j in product(range(6), repeat=2)]
    atoms = []
    for atom_id, (a, b, k, matching, tau_word, sigma_word) in enumerate(all_atoms):
        tau = [int(x) for x in tau_word]
        sigma = [int(x) for x in sigma_word]
        placements = []
        for i in range(6):
            j, l = tau[i], sigma[i]
            entry_id = entry_ids[i, j, k, l]
            sign = entries[entry_id]["sign"]
            placement = {"i": i, "j": j, "l": l, "sign": sign, "entryId": entry_id}
            placements.append(placement)
            entries[entry_id]["atomIds"].append(atom_id)
            piece = pieces[6*i+j]
            piece["atomIds"].append(atom_id)
            piece["cells"].append([a, b])
            piece["placements"].append({"atomId": atom_id, "k": k, "l": l,
                                        "sign": sign, "entryId": entry_id})
            piece["entryIds"].append(entry_id)
        atoms.append({"id": atom_id, "a": a, "b": b, "k": k,
                      "matching": matching, "tau": tau, "sigma": sigma,
                      "placements": placements})
    for piece in pieces:
        piece["entryIds"] = sorted(set(piece["entryIds"]))

    rows, columns = [0, 2, 4, 5, 3, 1], [2, 4, 0, 1, 5, 3]
    diagonals = [list(x) for x in S.DIAGONALS]
    require([columns.index(diagonals[0][i]) for i in rows] == list(range(6)),
            "First chosen transversal is the display main diagonal")
    require([columns.index(diagonals[1][i]) for i in rows] == list(reversed(range(6))),
            "Second chosen transversal is the display anti-diagonal")
    table = []
    for k, matching, tau, sigma1, sigma2, denominator in S.TABLE:
        table.append({"k": k, "matching": matching, "tau": [int(x) for x in tau],
                      "tauWord": tau,
                      "sigmaWords": [x for x in (sigma1, sigma2) if x is not None],
                      "sigmas": [[int(y) for y in x] for x in (sigma1, sigma2) if x is not None],
                      "weight": {"num": 1, "den": denominator}})

    require(len(entries) == 152 and len(atoms) == 96 and len(pieces) == 36,
            "Dataset cardinalities")
    for entry in entries:
        require(len(entry["atomIds"]) == entry["fragmentCount"],
                "Summing equal-area atoms reproduces every signed coefficient magnitude")
    for piece in pieces:
        require(len(piece["atomIds"]) == 16, "Each piece has 16 atoms")
        require(set(map(tuple, piece["cells"])) == set(masks[piece["i"], piece["j"]]),
                "Browser mask agrees with the reference mask")
        probability = sum(Fraction(entries[e]["stateProbability"]["num"],
                                   entries[e]["stateProbability"]["den"])
                          for e in piece["entryIds"])
        require(probability == Fraction(1, 36), "Every matrix row has unit norm")
    all_cells = {(a, b) for a in range(24) for b in range(4)}
    lines = [[(i, j) for j in range(6)] for i in range(6)]
    lines += [[(i, j) for i in range(6)] for j in range(6)]
    lines += [[(i, d[i]) for i in range(6)] for d in diagonals]
    for line in lines:
        counts = Counter(cell for i, j in line for cell in masks[i, j])
        require(set(counts) == all_cells and set(counts.values()) == {1},
                "All 14 geomagic lines tile the rectangle once")
    for l in range(6):
        counts = Counter((atom["a"], atom["b"]) for atom in atoms
                         for p in atom["placements"] if p["l"] == l)
        require(set(counts) == all_cells and set(counts.values()) == {1},
                "Each of the six quantum colours covers the target once")

    examples = {
        "positive": {"entryId": entry_ids[0, 2, 0, 2], "address": [0, 2, 0, 2],
                     "matrixTex": "1/2", "stateTex": "1/12"},
        "negative": {"entryId": entry_ids[0, 4, 0, 4], "address": [0, 4, 0, 4],
                     "matrixTex": "-1/2", "stateTex": "-1/12"},
        "radical": {"entryId": entry_ids[2, 0, 0, 3], "address": [2, 0, 0, 3],
                    "matrixTex": "1/\\sqrt{2}", "stateTex": "1/(6\\sqrt{2})"},
        "controlledDepthTwo": {
            "I": [0, 2], "J": [2, 0], "K": [0, 0], "L": [2, 3],
            "outerEntryId": entry_ids[0, 2, 0, 2],
            "innerEntryId": entry_ids[2, 0, 0, 3],
            "flatAddress": [2, 12, 0, 15], "dimension": 36,
            "fragmentCount": 32, "targetAtomCount": 9216,
            "pictureArea": {"num": 1, "den": 288},
            "matrixSquare": {"num": 1, "den": 8},
            "stateProbability": {"num": 1, "den": 10368},
            "productSign": 1, "controlFactor": -1, "controlledSign": -1,
            "productMatrixTex": "1/(2\\sqrt{2})",
            "controlledMatrixTex": "-1/(2\\sqrt{2})",
            "controlledStateTex": "-1/(72\\sqrt{2})",
        },
    }
    outer, inner = G[0, 2, 0, 2], G[2, 0, 0, 3]
    product_ring = S.mul(outer, inner)
    require(product_ring == (0, 4), "Two-level worked example: numerator over 16")
    require(entries[entry_ids[0, 2, 0, 2]]["fragmentCount"]
            * entries[entry_ids[2, 0, 0, 3]]["fragmentCount"] == 32,
            "Two-level worked example uses 32 equal-area fragments")
    sign_counts = Counter(entry["sign"] for entry in entries)
    square_counts = Counter((entry["square"]["num"], entry["square"]["den"])
                            for entry in entries)
    return {
        "schemaVersion": 1,
        "metadata": {
            "title": "Exact geometric AME(4,6) seed and recursive rectangle data",
            "source": "seed46.py: geomagic(), atoms(), masks(), TABLE, B1",
            "tensorSymbol": "T^g", "tensorScale": 4,
            "ringConvention": "Tg[i,j,k,l] = (ring[0] + ring[1]*sqrt(2))/4",
            "stateConvention": "psi[i,j,k,l] = Tg[i,j,k,l]/6",
            "coordinateConvention": "a increases right; b increases upwards; atoms() order gives atom ids",
            "baseDimension": 6, "gridColumns": 24, "gridRows": 4,
            "atomCount": 96, "atomsPerPiece": 16, "pieceCount": 36,
            "nonzeroTensorEntries": 152, "positiveEntries": sign_counts[1],
            "negativeEntries": sign_counts[-1],
            "squareHistogram": [{"num": n, "den": d, "count": c}
                                for (n, d), c in sorted(square_counts.items())],
            "rectangleWidthTex": "\\sqrt{6}", "rectangleHeight": 1,
            "atomAreaFraction": {"num": 1, "den": 96},
            "pieceAreaFraction": {"num": 1, "den": 6},
            "oneStepContractionTex": "1/\\sqrt{96}",
            "hausdorffDimensionTex": "\\log(256)/\\log(96)",
            "checks": ["Exact signed seed coefficients", "All 152 reconstructed areas",
                       "All 36 masks", "14 geomagic line tilings", "Six colour coverings",
                       "Display diagonal permutations", "Worked depth-two sign and area"],
        },
        "display": {"rows": rows, "columns": columns, "diagonals": diagonals},
        "words": list(S.B1),
        "expandedWords": ["".join(x*2 for x in word) if k < 4 else word
                          for k, word in enumerate(S.B1)],
        "table": table, "entries": entries, "atoms": atoms, "pieces": pieces,
        "examples": examples,
    }


def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed-dir", type=Path, default=here,
                        help="Directory containing the unchanged seed46.py")
    parser.add_argument("--output", type=Path, default=here / "ame46_data.js")
    args = parser.parse_args()
    data = build_data(load_seed(args.seed_dir))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(data, ensure_ascii=True, separators=(",", ":"))
    args.output.write_text(
        "/* Generated by export_data46.py from the exact seed46.py.\n"
        "   Do not hand-edit numerical data. Coordinates count rows bottom-up. */\n"
        "(function (root) {\n  'use strict';\n  root.AME46_DATA = " + payload + ";\n"
        "})(typeof window !== 'undefined' ? window : globalThis);\n",
        encoding="utf-8")
    print(f"PASS: exported {len(data['entries'])} exact tensor entries, "
          f"{len(data['atoms'])} atoms, and {len(data['pieces'])} masks.")
    print("PASS: reconstructed every area and sign; checked all 14 line tilings and six colour coverings.")
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
