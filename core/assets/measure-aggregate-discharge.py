"""
Aggregate discharge for "Specification Demand Is Verdict Entropy."

Per-act demand is H(V). Over N acts the question is what the acts sum to, and
the answer depends on whether the draws are independent:

    H(V_1 ... V_N) <= N*H(V),  with equality iff the draws are independent.

That is Shannon's — subadditivity of joint entropy — and this script computes
both sides exactly on the date task of measure-toy.py, so the gap can be read
rather than asserted. The gap N*H(V) - H(V_1...V_N) is the aggregate demand a
correlated stream does NOT face, and it is the seam of measure-toy.py's
decomposition A, harvested once per act instead of paid once per act.

The correlation model, stated so that it is a model and not a fudge: a batch of
N acts shares one MONTH, drawn uniformly once; each act's day is then drawn
uniformly from 1..31. Verdicts are conditionally independent given the month, so
the joint entropy is exact in closed form. Canon licenses the framing directly
(term:act-individuation: "batch boundaries are verdict boundaries").

The i.i.d. control redraws the month at every act. It must return exactly
N*H(V) — the equality limb of the inequality, demonstrated rather than stated.

Task, denomination (bits x n) and ground distribution as in measure-toy.py;
entropies are exact (exhaustive, log-space), nothing is sampled.
Exercises DDD-frame-16 (discharge is act-indexed) as worked arithmetic.

Run: python3 measure-aggregate-discharge.py
"""
from math import log2, lgamma, log

LOG2E = 1.0 / log(2.0)

# Task: validate (M, D). VALID iff D <= days_in_month(M). Uniform ground.
days = {1: 31, 2: 28, 3: 31, 4: 30}
points = [(m, d) for m in days for d in range(1, 32)]
verdict = {(m, d): (d <= days[m]) for (m, d) in points}
n = len(points)
months = sorted(days)


def Hb(p):
    """Binary Shannon entropy in bits."""
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -(p * log2(p) + (1 - p) * log2(1 - p))


# ---------------------------------------------------------------- per-act base
p_valid = sum(1 for q in points if verdict[q]) / n           # P(VALID)
p_month = {m: days[m] / 31 for m in months}                  # P(VALID | M = m)
P_M = 1.0 / len(months)                                      # months uniform

H_V = Hb(p_valid)                                            # H(V), per act
H_VgM = sum(P_M * Hb(p_month[m]) for m in months)            # H(V|M), per act
I_VM = H_V - H_VgM                                           # I(V;M), per act
H_M = log2(len(months))                                      # H(M) = 2 bits

print(f"n={n}  valid={sum(1 for q in points if verdict[q])}  "
      f"months uniform, days uniform within month\n")
print("Per-act, and the same quantities at the paper's display scale (x n):\n")
print(f"  H(V)     = {H_V:.6f} bits/act    x n = {H_V * n:7.3f}")
print(f"  H(V|M)   = {H_VgM:.6f} bits/act    x n = {H_VgM * n:7.3f}")
print(f"  I(V;M)   = {I_VM:.6f} bits/act    x n = {I_VM * n:7.3f}")
print(f"  H(M)     = {H_M:.6f} bits  (paid once per batch, never per act)\n")

# The x n column must be measure-toy.py's decomposition A, unchanged.
assert abs(H_V * n - 25.493) < 5e-4
assert abs(H_VgM * n - 20.593) < 5e-4
assert abs(I_VM * n - 4.901) < 5e-4
print("  -> 25.493 / 20.593 / 4.901: measure-toy.py's decomposition A exactly.")
print("     Nothing new is introduced here; the seam is the one already worked.\n")


# ------------------------------------------------------- exact joint entropies
def log2C(N, k):
    """log2 of the binomial coefficient, via lgamma (stable for large N)."""
    return (lgamma(N + 1) - lgamma(k + 1) - lgamma(N - k + 1)) * LOG2E


def binom_pmf(k, N, p):
    """P(k successes in N Bernoulli(p) trials). Exact at p = 0 and p = 1."""
    if p >= 1.0:
        return 1.0 if k == N else 0.0
    if p <= 0.0:
        return 1.0 if k == 0 else 0.0
    return 2.0 ** (log2C(N, k) + k * log2(p) + (N - k) * log2(1 - p))


def joint_entropy(N, shared_month):
    """
    H(V_1...V_N) in bits, exactly.

    Verdict sequences are exchangeable in both models, so a sequence's
    probability depends only on its count k of VALIDs. With P_k the probability
    of the COUNT and C(N,k) sequences carrying it, each sequence has probability
    q_k = P_k / C(N,k), and H = -sum_k P_k * log2(q_k).
    """
    total = 0.0
    for k in range(N + 1):
        if shared_month:
            P_k = sum(P_M * binom_pmf(k, N, p_month[m]) for m in months)
        else:
            P_k = binom_pmf(k, N, p_valid)
        if P_k > 0.0:
            total -= P_k * (log2(P_k) - log2C(N, k))
    return total


print("Aggregate over N acts. 'batch' shares one month; 'i.i.d.' redraws it "
      "every act.\n")
header = (f"{'N':>5} {'N*H(V)':>11} {'H(V1..VN)':>11} {'gap':>10} "
          f"{'gap/act':>9} {'per-act':>9} | i.i.d. control")
print(header)
print("-" * (len(header) + 16))
rows = {}

for N in (1, 10, 100, 1000):
    independent = N * H_V
    batch = joint_entropy(N, shared_month=True)
    control = joint_entropy(N, shared_month=False)
    gap = independent - batch

    # The inequality, and its equality limb under the control.
    assert batch <= independent + 1e-9, "subadditivity violated"
    assert abs(control - independent) < 1e-9, "i.i.d. draws must give N*H(V)"
    # The gap is the seam harvested: gap = N*I(V;M) - I(V1..VN;M), and the
    # subtracted term is a mutual information with M, so it never exceeds H(M).
    harvested = N * I_VM - gap
    assert -1e-9 <= harvested <= H_M + 1e-9, "I(V1..VN;M) outside [0, H(M)]"

    gap = gap if abs(gap) > 1e-12 else 0.0          # -0.0000 reads as a result
    rows[N] = (independent, batch, gap)
    print(f"{N:>5} {independent:>11.4f} {batch:>11.4f} {gap:>10.4f} "
          f"{gap / N:>9.5f} {batch / N:>9.6f} | {control:.6f}")

print(f"""
Three things are exact here, and none is an assumption.

The gap is exactly zero at N = 1 -- a batch of one is not correlated -- and the
i.i.d. control returns N*H(V) at every N. That is the equality limb of the
inequality: equality iff independent, computed rather than stated.

The per-act aggregate H(V1..VN)/N falls from H(V) = {H_V:.6f} toward
H(V|M) = {H_VgM:.6f}. The shared month costs H(M) = {H_M:.3f} bits ONCE for the
whole batch, so its share per act vanishes as N grows, and what every act still
faces is the residual the month does not settle. Paid once, inherited by each
act: the asymmetry is O(1) against O(N), in figures.

The gap is the seam, harvested. It equals N*I(V;M) - I(V1..VN;M), and the
subtracted term is bounded by H(M) = {H_M:.3f} bits for every N, so the gap grows
at I(V;M) = {I_VM:.6f} bits per act less a one-off of at most two bits. At
N = 1000, {rows[1000][2]:.4f} of the batch's {1000 * I_VM:.4f} bits of seam are harvested
({100 * rows[1000][2] / (1000 * I_VM):.1f}%); the {1000 * I_VM - rows[1000][2]:.4f} bits withheld are that one-off, and it
does not grow.

What none of this establishes: that correlated verdicts ARE cacheable work. The
inequality is Shannon's and holds for every joint distribution; the reading of
its gap as amortisable engineering effort is a modelling claim, and it is
untested. See the note's section 6.6.""")
