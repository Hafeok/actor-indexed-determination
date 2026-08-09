#!/usr/bin/env python3
"""
measure-mdl-demo.py — Act-indexed cost model over the date-validation task.

Demonstrates the two-part MDL correspondence as a *cost* model layered on the
conserved demand identity H(V) = I(V;E) + H(V|E).

Cost model (coefficients STIPULATED, not measured — see status note):
    C(E, N) = alpha * I(V;E)*n   [standing: paid once into the encoding]
            + beta  * N * H(V|E)*n  [occasioned: paid per act, N acts]

Predictions extracted:
  1. Optimal encoding richness is monotone in N (amortisation tendency —
     shared with any fixed+marginal model).
  2. Distinctions flip from occasioned to standing at computable crossover
     volumes, ordered by information density  I gained / (residual removed)
     — the MARGINAL CONDITION specific to the MDL form.
  3. Residual H(V|E) reaches zero only at the full-verdict encoding, whose
     standing cost equals H(V) — the RESIDUAL FLOOR under any partial model.

Status: exercises a projected claim. Computable + non-degenerate only.
Does not and cannot confirm the correspondence (coefficients stipulated).

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

# ------------------------------------------------- optimal encoding vs volume
# Stipulated coefficients: alpha = beta = 1 (one cost unit per bit).
# C(E, N) = I + N * (R / n)   — residual expressed per act.
print("\nOptimal encoding as act volume N varies (alpha = beta = 1):")
print(f"{'N':>8}  optimal encoding            standing   per-act residual")
prev = None
for exp in range(0, 15):
    N = 2 ** exp
    opt = min(frontier, key=lambda e: e["I"] + N * (e["R"] / N_PTS))
    if opt["label"] != prev:
        print(f"{N:>8}  {opt['label']:<26}{opt['I']:>9.3f}   {opt['R']/N_PTS:>8.4f} bits/act")
        prev = opt["label"]

# Exact crossover volumes between adjacent frontier encodings:
# flip when I2 - I1 = N * (R1 - R2)/n  =>  N* = n * (I2 - I1) / (R1 - R2)
print("\nCrossover volumes (marginal condition — the MDL-specific prediction):")
print("A distinction becomes worth standing supply at N* = n*ΔI/ΔR:")
for a, b in zip(frontier, frontier[1:]):
    dI, dR = b["I"] - a["I"], a["R"] - b["R"]
    if dR > 1e-9:
        n_star = N_PTS * dI / dR
        density = dR / dI if dI > 1e-9 else float("inf")
        print(f"  {a['label']:<24} -> {b['label']:<24} N* = {n_star:>8.1f}"
              f"   (density {density:.3f} bits residual removed per standing bit)")

# -------------------------------------------------- FINDING: the degeneracy
print("""
FINDING (model 1 is degenerate, and the identity is why):
Pricing standing cost as I(V;E) makes dI = dR exactly — conservation forces
density 1.000 everywhere, so every crossover is N* = n*(alpha/beta) and the
whole frontier flips at once. A cost model linear in captured information
cannot produce a graded build-out. The non-trivial MDL form prices the
standing side as DESCRIPTION LENGTH of the mechanism, L(E) — which is not
a conserved quantity — while entropy governs only the occasioned side.
That is precisely MDL's L(model) + L(data|model).""")

# ----------------------------------- cost model 2: L(E) + N * H(V|E) per act
# Description-length proxy: one unit per atomic feature (each feature is one
# comparison — a threshold or an equality test — of roughly equal length).
print("Cost model 2:  C(E, N) = gamma*L(E) + N * H(V|E)/n,  L(E) = #features,"
      "\ngamma = 3 bits per feature (stipulated proxy):")
GAMMA = 3.0
print(f"\n{'N':>8}  optimal encoding            L(E)   per-act residual")
prev = None
for exp in range(0, 15):
    N = 2 ** exp
    opt = min(encodings, key=lambda e: GAMMA * e["k"] + N * (e["R"] / N_PTS))
    if opt["label"] != prev:
        print(f"{N:>8}  {opt['label']:<26}{opt['k']:>4}   {opt['R']/N_PTS:>8.4f} bits/act")
        prev = opt["label"]

# Greedy build-out order: which distinction earns its description length first
print("\nBuild-out order under model 2 (bits captured per unit description):")
chosen, remaining = [], set(names)
while remaining:
    base_R = residual_bits([FEATURES[k] for k in chosen])
    gains = {f: base_R - residual_bits([FEATURES[k] for k in chosen + [f]])
             for f in remaining}
    pick = max(gains, key=gains.get)
    n_star = N_PTS * GAMMA / gains[pick] if gains[pick] > 1e-9 else float("inf")
    print(f"  + {pick:<8} captures {gains[pick]:>7.3f} bits"
          f"   worth standing at N* ≈ {n_star:>8.1f}")
    chosen.append(pick); remaining.discard(pick)

print("\nResidual floor check: H(V|E) = 0 requires I(V;E) = H(V) "
      f"({H_V:.3f} bits) — no partial encoding reaches zero residual.")
print("\nStatus: coefficients stipulated. This exercises the projected cost "
      "model;\nit does not test the correspondence. The empirical falsifiers "
      "are the\ncrossover-curve shape and the non-zero occasioned floor.")
