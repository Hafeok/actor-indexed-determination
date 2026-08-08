# Cost

<!-- ddd:contract

requires: [act, actor, demand, judgment, escape, acceptance-predicate, closure|closes|closing, verdict]
establishes: [cost-register|cost register, standing-cost|standing cost, occasioned-cost|occasioned cost, act-volume|act volume]
status: settled
-->

**A cost note.** Reproduction script in `core/assets/measure-mdl-demo.py`. Empirical basis filed in
`meta/mdl-cost-manufacturing-assessment-2026-08-08.md`.

**Claims.** The propositions of this note are landed as claim nodes under `core/claims/`
(`DDD-cost-*`); canon authority for each is its claim file, and this document is their exposition.
The mapping:

| Section | Proposition | Claim | Status |
|---|---|---|---|
| §1 | Bits are per-act on both sides; the asymmetry is locus of supply | `DDD-cost-01` | projected |
| §3 | Degeneracy: standing cost linear in `I(V;E)` gives a flat tradeoff | `DDD-cost-02` | reported (arithmetic) |
| §3 | A graded build-out requires standing cost priced as description length | `DDD-cost-02` | reported (arithmetic) |
| §4 | MDL correspondence: cost = `L(mechanism)` + N·`H(V\|E)` | `DDD-cost-03` | projected |
| §5 | The `09` §6.2 actor rows are optimal encodings at three act-volume regimes | `DDD-cost-04` | projected |
| §6 | Capacity = bits suppliable per act; escape = residual exceeding capacity | `DDD-cost-05` | projected, named next result |

Where this prose and a claim disagree, the claim governs and the prose is the bug.

**Status.** `09` states a conserved quantity; this note states what is optimised. The registers stay
separate deliberately: cost is **not** conserved — `L(mechanism)` has no conservation identity, and
act volume is a parameter demand never sees. Nothing here amends the demand identity; everything
here is layered on it.

---

## 1. The register split: demand is conserved, cost is not

The demand identity (`09` §2) is per-act on both sides:

> **H(verdict) = I(verdict;E) + H(verdict|E)** — per act, every term.

The two sides denominate in the same unit — bits of one act's verdict — and differ only in **locus
of supply**. `I(V;E)` is supplied by a **standing artifact**: a mechanism built before any act,
paid for once, present for every act thereafter. `H(V|E)` is supplied by a **contemporaneous
event**: an actor's judgment spent at the act, again at the next act, amortising never.

<a name="cost-register"></a>That difference in locus is what a **cost register** prices and the
demand register cannot see. Write **standing cost** for the price of building and holding the
artifact, and **occasioned cost** for the price of the per-act event. Then for **act volume** `N` —
the number of acts the arrangement will face, a quantity no demand identity mentions —

> **C(E, N) = α · standing + β · N · occasioned**

with the demand identity fixing, for every candidate encoding `E`, how much of the verdict each
side must supply. Demand says what must be supplied; cost says what supplying it that way is worth
across `N` acts. *(Claim `DDD-cost-01`, projected; falsifier: a case where the two sides of the
identity denominate differently.)*

---

## 2. Cost model 1: standing cost as captured information

The obvious first model prices the standing side by what the encoding captures: standing =
`I(V;E)`. It is wrong, and the way it is wrong is the load-bearing result of this note.

---

## 3. The degeneracy — and what a graded build-out requires

Under model 1, conservation forces the tradeoff flat. For any two encodings, ΔI = −ΔR exactly —
the identity permits nothing else — so every distinction removes precisely as many occasioned bits
as it adds standing bits. Every crossover then sits at the same volume,

> **N\* = n · (α/β)**, identically, for every step of the frontier,

and the whole frontier flips at once: below N\* supply nothing standing, above it supply
everything. **A cost model linear in captured information cannot produce a graded build-out.**
This is an identity consequence, not an observation — *reported as arithmetic*, exercised end to
end by `measure-mdl-demo.py` (all densities 1.000, all crossovers at N\* = 124 on the date task).
*(Claim `DDD-cost-02`.)*

The consequence runs forward: **a graded build-out requires standing cost priced as mechanism
description length, not captured information.** `L(mechanism)` is not a conserved quantity, so it
can differ per distinction, so crossovers can spread — which is exactly what the demand register,
where everything is forced to sum to `H(V)`, is structurally unable to express. Also reported as
arithmetic, per the degeneracy.

---

## 4. The MDL correspondence

The non-degenerate form prices the standing side as description length and the occasioned side by
entropy:

> **cost = L(mechanism) + N · H(verdict|E)** — MDL's `L(model) + L(data|model)`, with the model
> the mechanism the arrangement stands up, and the data the residual verdicts its actor must
> supply per act.

Entropy prices the occasioned side; description length prices the standing side. The
correspondence is a modelling claim, **projected**, and its discriminating predictions are two:

1. **The marginal condition.** Distinctions flip from occasioned to standing at computable
   crossover volumes `N* = n · ΔL/ΔR`, ordered by information density — residual removed per unit
   of mechanism description. Falsifier (a): within-task cost-vs-volume data whose crossover-curve
   shape contradicts the marginal condition.
2. **The occasioned floor.** Under any finite mechanism the residual `H(V|E)` reaches zero only
   when the acceptance predicate closes and the mechanism carries the whole verdict; short of
   that, per-act occasioned cost asymptotes to a non-zero floor. Falsifier (b): occasioned per-act
   cost driven to zero at high volume under a partial mechanism.

**Empirical basis, filed and graded** (`meta/mdl-cost-manufacturing-assessment-2026-08-08.md`):
the public manufacturing data is abundantly consistent with the generic two-part form but was
never collected to discriminate the MDL form. The experience-curve meta-analyses are structurally
floor-free — pure power laws, a floor term never tested — so the strongest datasets are silent on
prediction 2; within-part moulding cost-vs-volume data is the accessible discriminating test; and
no prior MDL-to-manufacturing-cost application was found. The correspondence is therefore
projected on basis, not reported. *(Claim `DDD-cost-03`.)*

---

## 5. The actor table as optimal encodings

`09` §6.2's actor table — program, weak model, mid model, one invariant total, three allocations —
re-reads under the cost model as **the optimal encodings at three act-volume regimes**: the
encoding worth standing up depends on `N`, and the rows are the frontier points a cost-minimising
arrangement selects as volume grows. Projected; falsifier: an optimal build-out ordering that
contradicts observed actor orderings. *(Claim `DDD-cost-04`.)*

---

## 6. Capacity and escape, named

The cost register gives capacity its per-act denomination: **capacity is the bits an actor can
supply per act; escape is the residual exceeding it.** Where `H(V|E)` — the occasioned side — is
greater than what the actor can supply at the act, the excess is supplied by nobody, and the
demand escapes. Projected and **named as the next result**: the model that earns it lands with the
floor-mechanism work (`11`), where hold and resolve capacity already have their bits. *(Claim
`DDD-cost-05`.)*

---

## 7. Reproduce

One self-contained script regenerates every figure in this note:

- `assets/measure-mdl-demo.py` — the frontier, the degeneracy (§3), the graded build-out under
  description-length pricing, and the residual-floor check (§4), on the `09` §3 date task.

Coefficients are stipulated, not measured. The script exercises the projected cost model; it does
not and cannot confirm the correspondence.
