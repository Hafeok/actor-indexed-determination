# The Floor Mechanism

<!-- ddd:contract

requires: [floor, closure, verdict, verdict-entropy, escape, judgment, demand]
establishes: [capacity, overflow, escape-mechanism|overflow ∩ open, p-err|p_err]
status: settled
-->

Completes `core/03` (the floor is in the acceptance
predicate) by supplying the *mechanism*: how, and exactly when, demand escapes. Depends on the
measure (`core/09`), the matched-pair invariant (`core/06`), and the closure principle (an actor's own prior output is not ground). Reproduction: `assets/floor-mechanism.py` and `assets/perr-rate-distortion.py`.

**Status.** The mechanism is derived and demonstrated on toys (hard and soft capacity). The
identification of the two escape conditions is a modelling claim; both were exercised computationally
and reproduce a field observation (a code-generation task that "passed validation but failed
inspection"). The soft-capacity section **corrects an earlier over-prediction** (a context
"U-curve"), which is noted where it occurs — the corrected result is stronger. The error model
`p_err` is **derived** from rate-distortion theory (§4.1), not assumed; substituting it changes the
numbers and **no structural claim**.

---

## 1. What `core/03` left open

`core/03` located the floor: it lives in the **acceptance predicate**, non-zero exactly where the
predicate does not close. And `core/09` measured demand in bits and split it into encoded
(`I(verdict;X)`) and everything-else (`H(verdict|X)`). But "everything else" fuses **judgment** and
**escape** — the chain rule cleaves "encoded" from "the rest," not "carried" from "shed."

This document cuts that seam. It answers: of the residual `H(verdict|X)`, what does the actor carry
as judgment, and what escapes — and why.

---

## 2. Two capacities, in series

An actor resolving residual demand faces two bounds, and they fail differently:

- **Hold capacity `C_hold`** — the bits of ground it can have in context at once. The substrate it
  reads.
- **Resolve capacity `C_resolve`** — the bits it can actually process into output given what it
  holds. The work done over the held ground.

Effective capacity is `min(C_hold, C_resolve)`, but the two produce different escapes:

<!-- ddd:embed id=term:capacity -->
> An actor's **capacity** is two-fold: **hold capacity** — the bits of ground it can have in
> context at once — and **resolve capacity** — the bits it can jointly resolve.
<!-- /ddd:embed -->

<!-- ddd:embed id=term:overflow -->
> **Hold-overflow** — the decision's governing ground does not fit. **Resolve-overflow** —
> the ground fits and is held, but the bits that must be *jointly resolved* exceed resolve
> capacity.
<!-- /ddd:embed -->

- **Hold-overflow** — the decision's governing ground does not fit; the actor decides against a
  *partial view*. This is **encodable away**: pre-resolve some ground into the constraint (raise
  `I(verdict;X)`) and the residual that must be held shrinks until it fits. RAG is this move. Not
  floor.
- **Resolve-overflow** — the ground fits and is held, but the bits that must be *jointly resolved*
  exceed `C_resolve`, so the actor sheds. This is the harder one, and the candidate for floor.

---

## 3. The floor is an intersection (hard-capacity result)

Model the actor with a hard resolve bound: it resolves `C_resolve` bits correctly per run; anything
beyond is shed and resolved at chance. Split the task's decisions into two classes:

- **Closing (verified):** the actor holds a verifier. A shed error is *caught* and retried.
- **Open (unverified):** the actor holds no verifier. A shed error *survives* as escape.

Computed (`assets/floor-mechanism.py` and `assets/perr-rate-distortion.py`, `n_closing = n_open = 20`, each decision 1 bit):

| `C_resolve` | overflow | escape (open) | retries (closing) |
|---|---|---|---|
| 40 | 0 | 0.000 | 0.000 |
| 30 | 10 | 2.49 | 2.51 |
| 24 | 16 | 3.99 | 4.03 |
| 16 | 24 | 5.99 | 6.03 |
| 0 | 40 | 9.97 | 10.02 |

And with **every** decision verified (`n_open = 0`), escape is **0 at every capacity**, even
`C_resolve = 0` — overflow becomes pure retry cost.

The result:

<!-- ddd:embed id=term:escape-mechanism -->
> **Capacity-generated escape — the escape an actor produces from residual it has taken up —
> requires two conditions, both necessary:**
>
> **(1) Overflow** — demand exceeds resolve capacity.
> **(2) Open** — no verifier the actor holds.
>
> Overflow alone (closing predicate) → **retries, not escape.** Recoverable. Not floor.
> Open alone (within capacity) → **carried by judgment**, where an accountable supplier is
> named. Not floor. Where none is named, it is escape by another route (`05` §7) — outside
> this mechanism, not excluded by it.
> **Overflow AND open** → **escape. This is the floor.**
>
> **Sufficient for escape, never necessary.** A governing decision that never entered an
> actor's residual escapes without overflowing anything: escape is supplied-by-nobody
> (`term:escape`), and capacity shortfall is one generator of it.
<!-- /ddd:embed -->

With a formula, in bits:

> **floor = (chance error rate) × max(0, demand − C_resolve) × (open fraction)**

Three prior results unify here: `core/03`'s "floor is in the predicate" is condition (2); `core/06`'s
matched-pair invariant is *why* verification removes floor (it converts escape into retry — the check
is the thing that catches the shed error); and `core/09`'s bits are the unit throughout.

**The worked instance.** `core/00` §6.1's immune floor is this intersection, with the two conjuncts
satisfied for different reasons: overflow because the antigen space exceeds the genome, and openness
because the organism has no verdict function over that space.

---

## 4. The soft-capacity bound, and a corrected prediction

Real overflow is not a cliff. Error rate rises *smoothly* with load, giving:

<!-- ddd:embed id=term:p-err -->
> `p_err` is **derived** from rate-distortion theory, not assumed — the error rate rises
> *smoothly* with load.
<!-- /ddd:embed -->

> **escape = (open residual) × p_err(load)**

### 4.1 `p_err` is derived, not assumed

An earlier version of this document *assumed* a logistic for `p_err`. It is instead **derived**, and
the derivation is the right one: *"what happens when you push more bits through a channel than its
capacity"* is exactly the question **rate-distortion theory** answers.

Treat resolve capacity as a channel of `C` bits per run carrying `n` binary decisions, so the
available rate is `r = C/n` bits per decision. For a Bernoulli(½) source under Hamming distortion,
the rate-distortion function is `R(D) = 1 − H_b(D)`. Inverting at the available rate:

> **p_err = H_b⁻¹(1 − r)**, where `r = C_resolve / n` and `H_b` is binary entropy.

This is a **theorem, not a fitted curve** — it is the information-theoretic *lower bound* on
per-decision error when capacity is `r` bits per decision. **No actor can do better.** Its limits are
exactly right, and were not tuned to be:

| `r = C/n` | `p_err` (derived) | meaning |
|---|---|---|
| ≥ 1.00 | **0.0000** | capacity ≥ demand → **no forced error** |
| 0.90 | 0.0130 | slight overflow, slight forced error |
| 0.60 | 0.0794 | |
| 0.40 | 0.1461 | |
| 0.20 | 0.2430 | |
| → 0 | **0.5000** | no capacity → **pure chance** (recovers the hard-case coin flip) |

The hard-capacity model (§3) is the limiting case: it assumed chance (0.5) on shed decisions, which
is exactly `p_err` at `r → 0`. **The two regimes are one model at different rates.**

### 4.2 A prediction retracted — and the structure that survived

An earlier version predicted a context "U-curve" (an optimal context size beyond which more context
hurts). The toy does **not** robustly show a U. The corrected result is a design rule rather than an
optimum, and — importantly — **it is unchanged when the assumed logistic is replaced by the derived
bound.** Substituting `p_err = H_b⁻¹(1 − r)` changes every number and **not one structural claim**:

- **Adding raw ground is monotonic harm past capacity.** Raw ground raises `n` (more to process) while
  the open residual stays flat, so `r` falls, `p_err` rises, escape rises. *There is no optimal amount
  of raw ground; more is worse.*

| raw ground added | effective `n` | `r` | `p_err` | escape |
|---|---|---|---|---|
| 0 | 40 | 0.750 | 0.042 | 1.67 |
| 20 | 60 | 0.500 | 0.110 | 4.40 |
| 40 | 80 | 0.375 | 0.156 | 6.25 |
| 60 | 100 | 0.300 | 0.189 | 7.57 |

- **Adding encoded decisions helps on both axes.** At a *fixed* context budget, converting raw ground
  into encoded decisions cuts the open residual *and* raises `r`. Escape falls to zero.

| encoded (fixed budget 50) | residual | `r` | `p_err` | escape |
|---|---|---|---|---|
| 0 | 40 | 0.333 | 0.174 | 6.96 |
| 20 | 20 | 0.429 | 0.135 | 2.70 |
| 40 | 0 | 0.600 | — | **0.00** |

> **The lever is not context *size*. It is the *encode fraction* — how much of the window is
> pre-resolved decisions versus raw ground.** "More context" fails because people add raw ground;
> "better context" works because it adds encoded decisions. **Same window size, opposite outcome.**

This is exactly the fix observed in the field: a code-generation task that produced gibberish under a
large raw context was repaired not by shrinking the window or adding capacity, but by **replacing raw
ground with encoded decisions** in the same window — lowering residual and raising the per-decision
rate at once.

**And the hard result is untouched by any of this.** Rate-distortion sets the *error rate* on shed
decisions; whether a shed error **escapes** or becomes a **retry** depends on the *verifier*, which is
orthogonal to `p_err`. The intersection structure (§3) does not depend on the error model at all.

---

## 5. The skill-floor corollary

A **skill** — any invokable capability that says what it does but ships no per-invocation check — is
**specification without verification**: an encoded constraint with no mechanical partner (`core/06`).
It satisfies condition (2) by construction, so the moment condition (1) is met (a loaded context), it
sits in the escape intersection and fails *silently*.

Its reliability is therefore not authored in — it is `1 − (overflow × openness)`, and it degrades
under load. That an unverified skill cannot be trusted to work as intended is the correct verdict,
mechanically: an unverified skill is protected from overflow-escape by nothing.

---

## 6. Hallucination is surfaced escape

The mechanism delivers a hallucination taxonomy as a corollary — and it is a *causal decomposition*,
derived from the store model, not a catalogue from observation.

> **Hallucination is what the escaped store looks like when the escaped decision surfaces as output:
> output decoupled from the true ground — confident, fluent, and unconstrained by what is actually
> the case.**

Escape that surfaces as output has exactly three sources, because there are exactly three ways a
decision can be made without correct ground:

| Cause | The ground is… | Mechanism | The fix |
|---|---|---|---|
| **Missing** | **absent** — not in the window | the ground was never supplied; hold-overflow where the window is full, plain non-supply where it is not | **add** ground (retrieval) |
| **Poisoned** | **false** — present but wrong | a cached belief / own prior output consumed as ground (`closure-principle`) | **re-verify** ground against source of truth |
| **Overflowed** | **correct but unresolved** — present, right, but exceeds `C_resolve` | resolve-overflow; the actor sheds and coin-flips | **encode** ground (raise encode fraction) — do *not* add |

Absent, false, or unresolved. That is the complete partition, because those are the only ways the
governing ground of a decision can fail to constrain it.

**Why lumping them is dangerous.** The three share one surface — decoupled output — and demand
*opposite* remedies:

- For **missing**, more context helps.
- For **poisoned**, more context is neutral-to-harmful (you may add more poison).
- For **overflowed**, more context is **actively harmful** — it is the *cause*.

This is why *"just give the model more context"* sometimes cures hallucination and sometimes worsens
it, with no apparent rule. The rule is: **it depends which of the three you face, and adding raw
context only helps one.** Overflow is the one that *inverts* the usual advice.

**Register.** Keep the claim mechanical. The precise statement is *output decouples from ground under
one of three ground-failures*; the intuition "the model is hallucinating / deluded" is a fine pump and
a poor formalism — it imports intentionality the mechanism does not need. Say what escapes and why.

**Relation to the intelligence result (`core/07`).** The overflow cause concentrates in **open**
decisions — the closing ones are caught (retried) or benchmarked (visible). So a benchmark, being a
closing predicate, measures exactly the region where overflow-hallucination is *invisible*. Two
actors at identical load can look identical on the benchmark and diverge wildly in deployment. *Passed
validation, failed inspection* is this, observed.

---

## 7. What is now closed, and what remains

**Closed.** The judgment/escape seam that `core/09` left fused. Capacity-generated escape is the
intersection of overflow and open (hard case) / `open_residual × p_err` with `p_err = H_b⁻¹(1 − C/n)`
(soft case, **derived** from rate-distortion, §4.1). The floor is the escape that both exceeds
capacity *and* has no verifier — *the demand you can neither resolve nor catch.* This is `core/03`'s
"predicate doesn't close" given a mechanism and a unit.

**What this section does not close.** The intersection is sufficient for escape and is not necessary
for it. It describes what an actor sheds from residual it has taken up; a governing decision that no
supplier took up at all is escaped without overflowing anything, and canon diagnoses exactly that in
`05` §7, `05` §8, `06`'s unanticipated situation at an encoded seam, and `10` §9's claim layer. The
scope correction is recorded in `DDD-dec-15`; the general category remains `term:escape`'s —
supplied by nobody, for any reason.

**Remains.** `C_resolve` and `C_hold` are treated as **given constants**. Deriving them from actor
architecture (parameters, context length, attention) is open — and is an **empirical calibration
problem, not a proof**: construct tasks of known bit-demand, find where error rate departs from zero,
and that value *is* `C_resolve` for that actor. Nobody has published such a measurement; it would be a
novel empirical contribution and it needs a rig, not more theory.

The toys are demonstrations, not certification — an outside reviewer should check the identification,
as with `core/09`.

**Not open — a boundary.** Measuring demand on **open** predicates is sometimes listed as an
outstanding debt. It is not. `core/09` measures demand as verdict *entropy*, which requires a verdict
function; an open predicate is precisely one that lacks it. Asking to measure demand there is asking
for entropy without a random variable. **This is the framework's stated limit, not an unpaid debt**,
and it coincides exactly with the floor: measurement and closure have the same domain (`core/09` §7).

---

## 8. The one line

> **Demand an actor has taken up escapes where two conditions meet: it exceeds what the actor can
> resolve, *and* it has no verifier to catch what is shed. That intersection is the floor. Everything
> else it took up is either caught (a retry) or carried (judgment) — and demand it never took up
> escapes without meeting either condition. Hallucination is escape surfacing as output — from ground
> that is absent, false, or unresolved — and only the first is helped by more context.**
