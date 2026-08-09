#!/usr/bin/env python3
"""
measure-mdl-demo.py — Per-act cost register over the date-validation task.

Demonstrates the per-act cost layer on the conserved demand identity
H(V) = I(V;E) + H(V|E): the locus-of-supply split (standing artifact vs
contemporaneous event), the degeneracy of information-linear standing cost,
and the residual floor.

Findings extracted:
  1. DEGENERACY — pricing standing supply as captured information I(V;E)
     makes every inter-encoding density exactly 1.000 (conservation forces
     dI = -dR), so no distinction can be priced ahead of another.
  2. SEPARATION — pricing standing supply as mechanism description length
     L(E) separates the distinctions: bits captured per unit of description
     differ per feature, so an ordering exists.
  3. RESIDUAL FLOOR — H(V|E) reaches zero only at the full-verdict encoding;
     under any partial mechanism the per-act occasioned side is bounded
     below by a non-zero floor.

Volume-denominated quantities (act volume N, crossover volumes N*) are
outside this repository's charter (DDD-dec-09) and are not computed here.

Status: reports an identity consequence (DDD-cost-02) and exercises a
projected rate-split (DDD-cost-03). Coefficients stipulated, not measured.

Task (identical to measure-toy.py figures): (M, D), M in 1..4, D in 1..31,
uniform ground, verdict VALID iff D <= days(M), days = {31, 28, 31, 30}.
"""

import itertools
import math

# ---------------------------------------------------------------- task setup
DAYS = {1: 31, 2: 28, 3: 31, 4: 30}
POINTS = [(m, d) for m in range(1, 5) for d in range(1, 32)]
N_PTS = len(POINTS)  # 124
VERDICT = {(m, d): d <= DAYS[m] for (m, d) in POINTS}


def h_binary_counts(n_true, n_total):
    """Entropy in bits of a binary verdict over n_total equiprobable points,
    returned as total bits (H * n_total)."""
    if n_total == 0 or n_true == 0 or n_true == n_total:
        return 0.0
    p = n_true / n_total
    h = -(p * math.log2(p) + (1 - p) * math.log2(1 - p))
    return h * n_total


def total_H_V():
    n_valid = sum(VERDICT.values())
    return h_binary_counts(n_valid, N_PTS)


def residual_bits(features):
    """H(V|E) * n for the encoding E = the given tuple of feature functions.
    E partitions the input space by the joint feature value; residual is the
    verdict entropy summed within cells."""
    cells = {}
    for pt in POINTS:
        key = tuple(f(pt) for f in features)
        cells.setdefault(key, []).append(pt)
    return sum(
        h_binary_counts(sum(VERDICT[p] for p in pts), len(pts))
        for pts in cells.values()
    )


# ------------------------------------------------------------ feature lattice
# Atomic distinctions available to an encoding, from cheapest to the full
# verdict. Each is something an actor could pre-compute about the input.
FEATURES = {
    "d<=28":   lambda pt: pt[1] <= 28,          # the weak-model feature
    "is-feb":  lambda pt: pt[0] == 2,           # the mid-model addition
    "d<=30":   lambda pt: pt[1] <= 30,          # separates day-31 cases
    "is-apr":  lambda pt: pt[0] == 4,           # resolves the last cell
}

H_V = total_H_V()

encodings = []
names = list(FEATURES)
for r in range(len(names) + 1):
    for combo in itertools.combinations(names, r):
        feats = [FEATURES[k] for k in combo]
        res = residual_bits(feats)
        encodings.append({
            "label": "+".join(combo) if combo else "(none)",
            "k": r,
            "I": H_V - res,     # I(V;E)*n — standing bits
            "R": res,           # H(V|E)*n — occasioned bits per act
        })

# Keep, per achievable residual level, the cheapest-standing encoding
# (the efficient frontier: no point paying more standing for the same residual)
best = {}
for e in encodings:
    key = round(e["R"], 6)
    if key not in best or e["I"] < best[key]["I"]:
        best[key] = e
frontier = sorted(best.values(), key=lambda e: -e["R"])

print(f"Task: date validation, n = {N_PTS}, H(V)*n = {H_V:.3f} bits\n")
print("Efficient frontier of encodings (cheapest standing cost per residual):")
print(f"{'encoding':<28}{'I(V;E)*n':>10}{'H(V|E)*n':>10}{'sum':>10}")
for e in frontier:
    print(f"{e['label']:<28}{e['I']:>10.3f}{e['R']:>10.3f}{e['I']+e['R']:>10.3f}")

# ------------------------- densities under model 1 (information pricing)
# Between adjacent frontier encodings: bits of residual removed per standing
# bit added. Conservation (dI = -dR) forces every entry to 1.000.
print("\nInter-encoding densities under information pricing (model 1):")
print("bits of residual removed per standing bit added, adjacent frontier steps:")
for a, b in zip(frontier, frontier[1:]):
    dI, dR = b["I"] - a["I"], a["R"] - b["R"]
    if dI > 1e-9:
        print(f"  {a['label']:<24} -> {b['label']:<24} density {dR/dI:.3f}")

# -------------------------------------------------- FINDING: the degeneracy
print("""
FINDING (model 1 is degenerate, and the identity is why):
Pricing standing cost as I(V;E) makes dI = dR exactly — conservation forces
density 1.000 everywhere, so no distinction can be priced ahead of another.
A cost model linear in captured information cannot separate the distinctions.
The non-trivial pricing takes the standing side as DESCRIPTION LENGTH of the
mechanism, L(E) — which is not a conserved quantity — while entropy governs
only the occasioned side. That is precisely MDL's L(model) + L(data|model),
read as per-act rates.""")

# ------------------- separation under model 2 (description-length pricing)
# Description-length proxy: one unit per atomic feature (each feature is one
# comparison — a threshold or an equality test — of roughly equal length).
GAMMA = 3.0  # bits per feature (stipulated proxy)
print("Separation under description-length pricing (gamma = 3 bits/feature):")
print("greedy order — bits of residual captured per unit of description:")
chosen, remaining = [], set(names)
while remaining:
    base_R = residual_bits([FEATURES[k] for k in chosen])
    gains = {f: base_R - residual_bits([FEATURES[k] for k in chosen + [f]])
             for f in remaining}
    pick = max(gains, key=gains.get)
    print(f"  + {pick:<8} captures {gains[pick]:>7.3f} bits"
          f"   {gains[pick] / GAMMA:>6.3f} bits per description bit")
    chosen.append(pick); remaining.discard(pick)

print("\nResidual floor check: H(V|E) = 0 requires I(V;E) = H(V) "
      f"({H_V:.3f} bits) — no partial encoding reaches zero residual.")
print("\nStatus: coefficients stipulated. This exercises the projected "
      "rate-split;\nit does not test the correspondence. Volume-denominated "
      "quantities are\noutside this repository's charter (DDD-dec-09).")
