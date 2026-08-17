# An Information-Theoretic Account of Determination Demand

<!-- ddd:contract

requires: [closure, acceptance-predicate, demand, conservation, seam, store, actor, act, determinable, determinate]
establishes: [verdict|verdict function, verdict-entropy|verdict entropy, chain-rule-identification, seam-information|I(V;S), act-individuation|act individuation, outcome]
status: settled
-->

**A formal note.** Reproduction scripts in `core/assets/measure-*.py`.

**Claims.** The propositions of this note are landed as claim nodes under `core/claims/`
(`DDD-measure-*`); canon authority for each is its claim file, and this document is their
exposition (canon authority lives in the claim files; see `core/claims/README.md`). The mapping:

| Section | Proposition | Claim |
|---|---|---|
| §1 | Demand is a measure, not a count | `DDD-measure-09` |
| §1 | Demand is verdict entropy (the identification) | `DDD-measure-01` |
| §2 | Conservation is the chain rule | `DDD-measure-02` |
| §2–§3 | Seam demand is `I(V;S)` | `DDD-measure-03` |
| §4 | *"A better decomposition destroys demand"* — retired | `DDD-measure-08` |
| §5 | You cannot decompose your way out (`H(V\|S)=0 ⟺ I(V;S)=H(V)`) | `DDD-measure-10` |
| §5 | Maturation asymptote `H(V) − I(V;S_encoded)` | `DDD-measure-13` |
| §5, §6.2 | Predictive claims (`I(V;S)` cost, `I(V;E)` performance) | `DDD-measure-07` |
| §6.2 | Store allocation actor-relative, total actor-invariant | `DDD-measure-04` |
| §6.3 | Identification survives an estimated channel (tractability, not measurement) | `DDD-measure-05` |
| §7 | The measure exists iff the predicate closes; vanishes at the floor | `DDD-measure-06` |
| §7, §9 | The measure prices the verdict, not the search | `DDD-measure-11` |
| §9 | Demand is relative to the ground distribution | `DDD-measure-12` |
| §2.1 | Admissibility: the engineering reading holds for admissible `X` only | `DDD-measure-15` |
| §9 | The chain rule iterates; the conditional term is an internal seam | `DDD-measure-14` |
| §7a | Outcome and verdict: the determinate's two registers | `DDD-frame-14` |

Where this prose and a claim disagree, the claim governs and the prose is the bug
(flagged in the claim's `notes:`, not silently harmonised).

**Status.** The central identity is a theorem (Shannon, 1948). The **claim** of this note is not
the theorem — it is the *identification* of the framework's informal quantities with exact
information-theoretic ones. That identification is a modelling claim, it is falsifiable, and on the
worked example it holds without leftover or contradiction. **Scope: the closing-predicate region
only.** The note is explicit about where the measure ceases to exist, which is exactly the floor.

**What this pays off.** The counting-procedure debt booked in `meta/lineage-and-limits.md` — *"until
a counting procedure for governing decisions exists and is shown invariant across two architectures,
conservation is an accounting identity, not a measured invariant."* This note supplies the
procedure, for closing predicates, and shows the invariance is a theorem rather than an observation.

---

## 1. The move: demand is not a count

The counting procedure kept failing because it tried to measure an extensive quantity with a
cardinality. Decisions resist counting for a concrete reason: a decision closing over a large ground
carries more demand than one over a small ground, and decomposition *creates* decisions (the seam).
Count and demand come apart.

So demand is not a count. It is a **measure**. And the measure is **Shannon information**.

<!-- ddd:embed id=term:verdict -->
> **Definition (determination demand).** *(In the engineering projection this same quantity is
> denominated in the vocabulary of the domain and called* **specification demand** *; the measure
> below is identical either way.)* For a task whose acceptance predicate **closes** for the
> arrangement (`term:closure`; *decidable* is the formal special case, not the requirement),
> the predicate evaluates outcomes, and the **task class** supplies one correct output per
> input point. The **verdict** is that induced assignment — the correct output over each point
> of the input space. Let `P` be the distribution over inputs (the *ground distribution*). The
> **determination demand** of the task is the Shannon entropy of the verdict:
>
> **D = H(verdict)**, measured in **bits**.
>
> Where the task class supplies no such assignment, the predicate still evaluates outcomes and
> there is no verdict to have entropy about — which is the boundary `09` §7 draws.
<!-- /ddd:embed -->

Demand is the information required to specify the correct answer over the ground the task faces. Not
how many decisions — *how much distinction*.

**The unit of account.** Every quantity in this note is **per-act** (`00` §1). `H(verdict)` is the
demand of one act, and the identities below split per-act demand. The earlier statements carried an
unexposed assumption: act volume was fixed at one. Exposing it revises nothing — volume is a
parameter demand never sees; it prices supply, not the task, and belongs to the cost register, not
to the conserved identity. The act's individuation is filed here because this is where the
predicate's measure exists (§7):

<!-- ddd:embed id=term:act-individuation -->
> **Act individuation** — one act = one verdict of the acceptance predicate at the declared
> boundary, where the predicate's measure exists; batch boundaries are verdict boundaries.
> The individuation inherits the predicate's discipline and adds no free parameter.
<!-- /ddd:embed -->

The boundary clause is load-bearing for composition: **acts nest as actors nest.** An inner
check with its own verdict individuates an inner act; the declared boundary's verdict
individuates the outer act, one act regardless of how many inner verdicts fire inside it
(`06`, composition at one act). Retry economics stays synchronic as an expectation over the
outer act; learning from rejections *across* acts persists between acts and is outside this
repository's charter (`DDD-dec-09`).

The individuation also extends in time: **a claim is an act with a deferred verdict** — one
claim = one act, individuated by the verdict of its declared predicate at the declared
boundary; the verdict event arrives at the declared horizon, and the act is in flight until it
does. Nothing new is added — deferral moves only the verdict's time. *(Claim `DDD-frame-12`,
projected; the deferred-verdict machinery is operable only with the ledger layer, outside this
repository's charter.)*

---

## 2. The identity: conservation is the chain rule

Let `S` be a **decomposition** — any variable that splits the task into sub-tasks (handle each value
of `S` separately). The chain rule of entropy gives, with no approximation:

> **H(verdict) = H(verdict | S) + I(verdict ; S)**

Read through the framework's vocabulary:

| Information quantity | Framework quantity | Meaning |
|---|---|---|
| **H(verdict)** | total demand `D` | the task's distinction demand — **fixed by the task** |
| **H(verdict \| S)** | runtime demand of the parts | what the sub-actors must still resolve *given the split* |
| **I(verdict ; S)** | **seam demand `\|S\|`** | what the *decomposition choice* absorbed |

So the framework's asserted seam identity

> `|D_comp| = |D_single| + |S|`

is **derived**, not posited: it is the chain rule, with `|S| = I(verdict ; S)`. The seam demand is
the **mutual information between the decomposition and the answer.**

<!-- ddd:embed id=term:seam-information -->
> **I(verdict ; S)** is **seam demand** — what the *decomposition choice* absorbed.
<!-- /ddd:embed -->

<!-- ddd:embed id=term:chain-rule-identification -->
> The **chain-rule identification**: conditioning the verdict on any variable `X` splits
> total demand, exactly, into what `X` encoded — `I(verdict; X)` — and what remains —
> `H(verdict | X)`. The theorem is Shannon's; the identification is the framework's claim.
<!-- /ddd:embed -->

**This is what "conservation within a fixed decomposition" means, made exact.** Fix `S`, and
`H(verdict|S) + I(verdict;S)` is *forced* to equal `H(verdict)`. Moving work between the split and
the parts is a zero-sum transfer. Conservation is not an empirical regularity; it is an algebraic
identity — once you accept the identification in §1.

### 2.1 Which conditioning variables the engineering reading applies to

The arithmetic above holds for **any** `X` whatever. The engineering reading does not, and the
condition that restricts it is the encoded store's own definition read as a restriction on
conditioning variables (`term:encoded`, `term:act`):

> **Admissibility.** A conditioning variable `X` is **admissible** where it is computable from
> ground available at the act, and from what the arrangement has standing before it, and not from
> the verdict itself. It must be computable by something that has not been handed the answer.

The condition does real work. Choosing `X = verdict` gives `I(V;X) = H(V)` and `H(V|X) = 0` — the
whole of the demand absorbed, tautologically — and without the restriction §5's *you cannot
decompose your way out of the work* would be nearly vacuous. `X = V` is inadmissible because the
verdict is not ground available before the verdict.

What admissibility does **not** exclude is a mechanism that *computes* the verdict from admissible
ground. §6.2's program does exactly that and reaches `H(V|E) = 0` legitimately. **The difference is
between building the answer and being handed it** — the work is not escaped, it is relocated to the
standing side and paid there (`core/10` §1). *(Claim `DDD-measure-15`, projected.)*

Two further things `I(V;X)` does not establish, recorded so the reading is not taken wider than it
is: mutual information is symmetric and observational, so it claims neither that anyone constructed
`X` nor that information flowed causally from `X` to the verdict. Where this document calls `I(V;X)`
*encoded* or *pre-paid*, the word is its name under the identification of §1, never a property of
mutual information.

---

## 3. Worked example (fully computed)

Task: validate a two-field date `(M, D)`, `M ∈ {1,2,3,4}`, `D ∈ {1,…,31}`, uniform inputs.
Verdict: `VALID ⟺ D ≤ days(M)`, with `days = {Jan 31, Feb 28, Mar 31, Apr 30}`.
`n = 124` points; 120 valid, 4 invalid.

**Total demand:** `H(verdict) × n = 25.493 bits`.

Two decompositions, each computed exactly:

| Decomposition `S` | groups | runtime `H(V\|S)·n` | seam `I(V;S)·n` | sum |
|---|---|---|---|---|
| **A** — split by month | 4 | 20.593 | 4.901 | **25.493** |
| **B** — split by day (`≤28` vs `≥29`) | 2 | 11.020 | 14.474 | **25.493** |

Both sum to the whole, exactly. (Verified to machine precision: residual `−0.0000`.)

---

## 4. What the example corrects in the framework

Decomposition B's *parts* are much cheaper than A's (11.0 vs 20.6 bits). The earlier framework
language would call B "a better decomposition that destroys demand." **The computation shows this is
wrong.** B did not destroy demand; it moved *more* demand into the seam — `I(verdict;S)` rose from
4.9 to 14.5 bits. B's split (knowing the valid/invalid boundary lives at day 29) is a
**high-information choice**: it absorbs more, so the parts are easier. The total is invariant.

> **Correction to the canon.** "A better decomposition destroys demand" → **"A better decomposition
> pre-pays more demand into the seam, buying cheaper parts. The total is invariant."** The
> destruction was always an artifact of not counting the seam.

This also sharpens the encoded store's role (`core/01`): the seam `I(verdict;S)` is *encoded*
demand — paid once, into the decomposition, and inherited by every run. B is "better" only because
someone already knew where the boundary was. That knowledge is not free; it is the mutual
information, pre-paid.

---

## 5. What it predicts (not just postdicts)

The identity is not merely descriptive. For a fixed task, ranging over all decompositions `S`:

- **A hard frontier.** `H(verdict|S)` is minimised exactly when `I(verdict;S)` is maximised, and
  the sum is constant. **You cannot make the parts easier without a higher-information seam.** This
  is a quantitative tradeoff curve, testable against any concrete task.
- **You cannot decompose your way out of the work.** `H(verdict|S) = 0` requires
  `I(verdict;S) = H(verdict)` — the decomposition already contains the *entire* answer. The only way
  to make the parts trivial is to put all the demand in the seam. This is the exact, quantitative
  form of the framework's claim that demand is conserved, not escapable.
- **The maturation/funnel asymptote** (`core/08`) is `H(verdict) − I(verdict;S_encoded)`: as you
  harvest more of the answer into the encoded decomposition, runtime demand falls toward the
  residual the encoding hasn't captured — never below what the *open* part of the predicate leaves
  undetermined.

---

## 6. One theorem, three conditioning variables

The decomposition result (§2) is one instance of something more general. The chain rule holds for
**any** variable `X` you condition the verdict on:

> **H(verdict) = I(verdict ; X) + H(verdict | X)**
>
> total demand = what `X` encoded + what is left to resolve given `X`

The framework's separately-stated claims turn out to be this one identity with three different
choices of `X`. Each was verified computationally.

### 6.1 X = a decomposition → seam demand

Covered in §2–§3. `I(verdict; S)` is the seam; `H(verdict|S)` is the runtime demand of the parts.
This *derives* the asserted `|D_comp| = |D_single| + |S|`.

### 6.2 X = an actor's encoding → store allocation (the actor model, unified)

Let `E` be **what an actor can encode before acting** — the actor's pinning resolution made concrete
as a variable it can compute about the input. Then:

> **H(verdict) = I(verdict ; E) + H(verdict | E)**
> total demand = **encoded by this actor** + **left to this actor's judgment**

Computed on the date task (`H(verdict) = 25.493` bits), for three actors of increasing encode
capacity:

| Actor | what it can encode | encoded `I(V;E)` | judged `H(V\|E)` | sum |
|---|---|---|---|---|
| **Program** (pins by value) | the exact verdict | 25.493 | 0.000 | **25.493** |
| **Weak model** | coarse proxy (`D ≤ 28`) | 14.474 | 11.020 | **25.493** |
| **Mid model** | `D ≤ 28` + "is it February?" | 20.964 | 4.529 | **25.493** |

**The total is actor-invariant; the allocation is actor-relative.** This is the precise, provable
form of the unification of conservation with the actor model — and it corrects a tempting overclaim:

> **Demand is NOT "constant *by* actor" (each actor with its own conserved quantity — that would be
> mere relabelled difficulty). Demand is "constant *across* actors, *allocated by* actor."** The same
> `H(verdict)` faces every actor; the actor sets only how it splits between encoded and judgment.

`H(verdict)` never mentions the actor. It is a property of the verdict function and the ground
distribution — the task. That is exactly why it is "fixed by the task, never by the system."

### 6.3 X = what is supplied before the act → the encode/verify split

Retrieval-augmented generation motivates this instance; it is not what is simulated, and the
instance is named for what is. The structure is the framework's **encode/verify split**: part of
what an act needs is supplied to it in advance, and the rest is left to whatever acts. With `R` =
what is supplied:

> **H(answer) = I(answer ; R) + H(answer | R)**
> total demand = **encoded by retrieval** + **left to the model's judgment**

The generating model is **stipulated, not learned**, and contains neither documents nor a model: `A`
is drawn at each act from a fixed eight-outcome prior with population entropy `H(A) = 2.6126` bits,
and `R` is a single categorical symbol carrying no document identity. The information quantities are
*estimated empirically from 40,000 samples* per row:

| retrieval (hit / distractor) | encoded `I(A;R)` | judged `H(A\|R)` | sum |
|---|---|---|---|
| 0.00 / 0.00 | 0.000 | 2.609 | **2.61** |
| 0.30 / 0.20 | 0.458 | 2.154 | **2.61** |
| 0.50 / 0.30 | 0.791 | 1.812 | **2.60** |
| 0.70 / 0.20 | 1.365 | 1.251 | **2.62** |
| 0.90 / 0.05 | 2.136 | 0.474 | **2.61** |
| 1.00 / 0.00 | 2.612 | 0.000 | **2.61** |

`H(answer) ≈ 2.61` bits throughout. **Better supply moves demand from judgment to encoded;
distractors push it back.**

**What this instance tests, and what it cannot.** `I(A;R)` is computed as `H(A) − H(A|R)`, so the
sum column is exact by construction and tests nothing; presenting it as a check would be the
arithmetic-as-evidence error this document exists to avoid. What the run does test is whether a
plug-in estimator recovers the conditional entropy of a channel it is not given in closed form. It
does: against the analytic joint, the mean estimate over 200 replicates is within 0.002 bits at
every setting, and a single 40,000-sample run carries a standard deviation of up to 0.010 bits. The
totals differ between rows because each re-estimates `H(A)` from its own fresh sample — estimator
noise, nothing else; over 200 replicates at `N = 40,000` the plug-in `H(A)` has mean 2.6117 bits and
standard deviation 0.0049, and every total above falls inside its central 95% range `[2.601, 2.621]`
around the population value 2.6126.

So this is **a tractability result, not a measurement of conservation**: it shows the quantities are
estimable from samples at a useful accuracy, which is the condition any deployed system presents.
The answer is generated independently of what is supplied, by construction, which makes the run
closer to construction than to measurement — and `H(A|R)` remains the ideal-observer residual, so an
actor that cannot exploit everything `R` carries faces more than the table shows, never less
(`DDD-measure-05`).

### 6.4 What this unifies

Three of the framework's claims that read as independent —

- the **seam identity** (`core/06`),
- the **actor-relative store allocation** (`core/04`),
- the **encode/verify split**,

— are **one theorem seen three ways**: the chain rule of entropy, conditioned on a decomposition, an
actor's encoding, or a retrieval policy. Different `X`, same `I(verdict;X) + H(verdict|X) =
H(verdict)`.

**One caveat, now paid down.** In all three, *escape* is folded into `H(verdict|X)` together with
*judgment* — the identity separates "encoded" from "everything else," not "judged" from "escaped."
Splitting those two required a model of actor **capacity**, and `core/11-the-floor-mechanism.md`
supplies it: hold and resolve capacity in bits, effective capacity `min(C_hold, C_resolve)`, the two
overflow modes, and the intersection result — overflow ∩ open is the mechanism of
**capacity-generated** escape, sufficient for escape and never necessary for it (`DDD-dec-15`) —
with a formula in bits, plus a soft-capacity bound derived from rate-distortion theory. The point at
which `H(verdict|X)` exceeds effective capacity is where demand an actor has taken up begins to
escape — derived and demonstrated, not conjectured (`core/11` §§2–4). The supply is partial: demand
no actor took up escapes without overflowing anything, and is not split by this model.

---

## 7. Where the measure stops — and why that is the right boundary

**This account works only where the acceptance predicate closes**, and it is essential to say so.

Shannon entropy of the verdict requires the verdict function to be *defined*. Where the acceptance
predicate does not close (`core/03`), there is no verdict function — no ground truth to have entropy
about — so `H(verdict)` is **undefined** and the measure does not exist.

This is not a gap to be patched. It is the **same boundary** the floor result already draws:

> **The information-theoretic measure of demand exists if and only if the acceptance predicate is
> closed for the arrangement over ground it can inspect. It vanishes exactly at the floor.**

Which is the elegant, and honest, consequence: we have measured demand precisely on the region where
the framework says the floor is zero, and the measure *itself* goes silent precisely where the floor
becomes non-zero. Measurement and closure have the same domain. The floor remains unmeasured —
correctly, because it is where measurement fails.

So the claim is bounded: **conservation of determination demand is a theorem for closing
predicates.** For open predicates it remains what it was — a principle, an accounting discipline, not
a measured invariant. The note does not extend the framework's reach; it *proves* the part that was
already inside the decidable region, and marks the boundary sharply.

**A second silence, inside the boundary.** Even where it exists, `H(verdict)` prices the
**verdict**, not the **search**: it is the information required to *specify* the correct answer over
the ground the task faces, and it says nothing about the cost of *computing* one. Two tasks with
identical verdict entropy can differ unboundedly in generation cost — a lookup table and a SAT
instance over the same input space carry the same `H(verdict)`, and one is answered by indexing
while the other is NP-hard to solve. Closure decides whether the floor is zero and whether the
measure exists; generation cost is a second, independent variable the measure does not see
(`core/03` §2, `core/04` §2). The two quantities are separated deliberately and must not be re-fused through
the measure.

### The operational form: two questions

The boundary gives the framework its operational form, and the form survives the measure's
silence. **For an act, every decision governing it must be supplied from one of the four
stores** — and the operational demand is two questions with different domains:

- **The governance question** — *is every governing decision in a declared store, none
  escaped?* Binary per decision, count-free, and **total in domain**: well-formed on open
  predicates, exactly where the measure does not exist. Three suppliers, one sink; the goal
  is a dry sink.
- **The cost question** — *how much is in each store?* Denominated in bits, and **partial in
  domain**: it exists only where the predicate closes (§7 above).

The governance question therefore ranges strictly wider than the measure — the reason the
framework is not merely applied information theory, and the reason it governs claims, mission
statements, and architecture where `H(verdict)` is undefined. *(Claim `DDD-frame-11`,
projected.)*

### 7a. Outcome and verdict: the determinate's two registers

The boundary sharpens once the determinate (`core/00` §4a) is in hand. Discharge always produces
a determinate — the act completes, and some way of occupying the determinable obtains whether or
not anything governed it. What varies with governance is not whether a determinate lands but
**which registers it lands in**:

<!-- ddd:embed id=term:outcome -->
> The **outcome** — the determinate as it lands in the world, produced at every completed
> act. The **verdict** is the same determinate as assessed by a declared predicate,
> produced only where governance has declared one. The world renders outcomes, never
> verdicts; governance is the conversion of outcomes into verdicts.
<!-- /ddd:embed -->

§7 already draws this line without naming it: where the task class supplies no assignment, "the
predicate still evaluates outcomes and there is no verdict to have entropy about." The register
pair names it, and one consequence carries the weight: **every diachronic instrument runs on
verdicts.** Maturation is the compound over repetition, and the compound harvests through a
mechanical check on what was harvested — a check's product is a predicate-assessed determinate,
a verdict. An outcome no predicate assesses never enters the return channel; ungoverned
discharge is invisible to learning, in principle and not merely in practice.

The state space follows: **outcome-only** (ungoverned) · **verdict-pending** (governed, open —
the claim layer's deferred verdict, `DDD-frame-12`) · **verdict-rendered** (governed, closed or
matured). Replay over recorded ground can retro-judge outcomes into verdicts once a predicate is
declared — honestly only under retro-filing's two fields (`DDD-ground-04`). And the two silences
of §7 survive beneath the registers: an outcome is convertible where a verdict function can be
declared; floor residual has none in any tense. *(Claim `DDD-frame-14`, projected.)*

Two consequences, booked:

- **Conservation retires a practice class.** Reduction is impossible; relocation is the whole
  game. "Simplify away the decisions" is not a goal — the only games are **placement** and
  **escape-prevention**.
- **The measure's job is to exist, not to be computed.** Its existence on the closing region
  is what makes conservation a theorem, escape a defined category, and the cost proxies
  honest. Practice runs count-free on the audit and proxy-priced — money, hours, tokens — on
  the optimisation, never on live entropy. Necessary for the warrant, unnecessary for the
  operation.

---

## 8. Related work

**Shannon (1948).** The chain rule, the unit, and the source-coding interpretation used below are his.
This note contributes no mathematics. It contributes an identification, and the identification is
falsifiable where the mathematics is not (§9).

**Ashby (1956).** Requisite variety is the rigorous ancestor: a fixed quantity of variety must be
absorbed by whatever regulates, and the quantity is stated in bits. The framework's conservation
principle is Ashby's shape, and this note is the point at which it recovers Ashby's unit — on the
region where a verdict function exists. That the arrival is late is a comment on the engineering
literature, not on Ashby.

**Kolmogorov complexity and MDL.** The obvious neighbour, and the obvious objection: if demand is the
information required to specify the verdict, why is it not the length of the shortest description —
Kolmogorov complexity (Li and Vitányi 2008), or its statistical descendant, minimum description length
(Rissanen 1978; Grünwald 2007)?

Three answers, in increasing order of strength.

First, computability and relativity. Kolmogorov complexity is uncomputable and distribution-free.
Demand as defined here is computable and deployment-relative: the same validator faces different demand
under different input distributions, and §9 argues that this relativity is a correction rather than a
concession. A distribution-free quantity cannot express it.

Second, the objects differ. MDL is computable — that is its purpose — but it prices the description of
a hypothesis against data. It is model-selection machinery. Verdict entropy prices the distinctions a
task requires of whatever resolves it. The two reconcile rather than compete: by the source-coding
theorem, `H(V)` is the expected length of an optimal description of the verdict under the ground
distribution. The measure proposed here is therefore itself a description-length quantity — the
distribution-relative expectation, which is the form a deployed system faces.

Third, and decisive for this note: the chain rule is exact for entropy and is not exact for
description length. Conservation here is the identity `I(V;X) + H(V|X) = H(V)`, holding with no error
term for every conditioning variable (§6). The Kolmogorov analogue — symmetry of information — holds
only to logarithmic precision (Zvonkin and Levin 1970). A conserved quantity that leaks
logarithmically under decomposition is an approximation, not an identity, and §§4–6 rest on the
identity being forced. Entropy is not a convenient choice among complexity measures. It is the measure
under which conservation is a theorem, and the objection, followed to its end, becomes an argument for
the identification.

**Information bottleneck.** The closest formal machinery (Tishby, Pereira and Bialek 1999). The
bottleneck optimises a trade-off between compression and relevance over exactly the quantities used
here. This note optimises nothing: the total is fixed, and the identity holds for every `X`, optimal or
not. The point of contact is §5's prediction — over the decompositions of a fixed task, parts are
minimised exactly when the seam is maximised — which is a bottleneck-shaped frontier for a concrete
engineering object. Where the bottleneck asks for the best `T`, this note asks what any `S` must pay.

**Actor uncertainty as difficulty.** A recent line estimates task difficulty from a model's own output
entropy — predictive entropy over responses (Malinin and Gales 2020), or the entropy of plausibility
scores over candidate answers in subsequent LLM-difficulty work. These are actor-side quantities: the
residual uncertainty of one arrangement, `H(V|E)` in §6.2's terms, and they vary by actor exactly as
the framework requires — which is why they measure difficulty-for-an-actor and not demand. Verdict
entropy never mentions the actor. §6.2 states the relation exactly: actor uncertainty is what remains
of demand after that actor's encoding.

**Psychometrics.** The Rasch tradition separates person ability from item difficulty as a modelling
requirement (Rasch 1960), and entropy-based construct specification equations have been used within it
to explain memory-test difficulty. The separability is an ancestor of §6.2's result — total fixed by
the task, split relative to the actor — reached from measurement theory rather than information
theory.

**Rate–distortion.** Adjacent rather than overlapping. The framework derives its soft-capacity bound
from it (`core/11` §4), and that bound supplies the escape/judgment split that §6.4 records. The
supply is partial: the mechanism is sufficient for escape and not necessary for it (`core/11` §7).

**Brooks (1987).** "No Silver Bullet" claims an essential complexity fixed by the problem. `H(V)` gives
that claim an exact form and a boundary: fixed by the task, the tolerance, and the ground distribution
— and never by the actor — where the predicate closes, and only there.

### References

- **Ashby, W. R.** (1956). *An Introduction to Cybernetics.* Chapman & Hall, London.
- **Brooks, F. P.** (1987). "No Silver Bullet: Essence and Accidents of Software Engineering."
  *IEEE Computer* 20(4), 10–19.
- **Grünwald, P. D.** (2007). *The Minimum Description Length Principle.* MIT Press.
- **Li, M., and P. Vitányi** (2008). *An Introduction to Kolmogorov Complexity and Its Applications*,
  3rd ed. Springer.
- **Malinin, A., and M. Gales** (2020). "Uncertainty Estimation in Autoregressive Structured
  Prediction." arXiv:2002.07650; published ICLR 2021.
- **Rasch, G.** (1960). *Probabilistic Models for Some Intelligence and Attainment Tests.*
  Danmarks Pædagogiske Institut, Copenhagen.
- **Rissanen, J.** (1978). "Modeling by Shortest Data Description." *Automatica* 14(5), 465–471.
- **Shannon, C. E.** (1948). "A Mathematical Theory of Communication." *Bell System Technical Journal*
  27, 379–423 and 623–656.
- **Tishby, N., F. C. Pereira and W. Bialek** (1999). "The Information Bottleneck Method."
  *Proceedings of the 37th Allerton Conference on Communication, Control and Computing*, 368–377.
- **Zvonkin, A. K., and L. A. Levin** (1970). "The Complexity of Finite Objects and the Development of
  the Concepts of Information and Randomness by Means of the Theory of Algorithms."
  *Russian Mathematical Surveys* 25(6), 83–124.

---

## 9. Caveats, booked

Three, none fatal, all required in any write-up:

1. **The theorem is Shannon's; the claim is the mapping.** The chain rule is 1948. What is asserted
   here is the *identification* of demand with verdict-entropy, seam with mutual information,
   decomposition with conditioning. That identification is falsifiable and was vindicated on the
   example — but it must be claimed as a modelling result, never as a mathematical discovery.

2. **Demand is relative to the ground distribution.** `H(verdict)` depends on `P(input)`; the
   example used uniform. So *"fixed by the task"* must be stated as *"fixed by the task, the
   tolerance, and the ground distribution."* This is arguably more correct — the same validator
   faces different demand in different deployment environments — but it is an added parameter, not a
   free lunch.

3. **Five instances is credibility, not certification.** The identity is general (it is the chain
   rule), and it has now been exercised on five conditioning variables — decomposition, actor
   encoding, what is supplied before the act (empirically, with distractors), a decomposition
   applied *twice*, and a decomposition under varied ground — all on closing-predicate tasks. That
   is real triangulation, not a single toy. Two of the three cases this caveat previously named as
   owed are now worked: **chained seams** (`core/assets/measure-chained-seams.py`, claim
   `DDD-measure-14` — both chain orders re-split the seam and leave the parts residual invariant)
   and **non-uniform ground** (`core/assets/measure-nonuniform-ground.py`, claim `DDD-measure-12` —
   the identity holds exactly under three ground distributions while the demand itself moves by a
   factor of six). **Multi-actor compositions remain owed**, and the debt is not reduced by the
   chained-seam instance: there the conditioning variables are sub-decompositions of one task, and
   the composition case conditions on *actor encodings*. Same arithmetic, distinct instance,
   unworked. An information theorist should still certify the framing. The theorem is exact;
   *identifying* the real conditioning variable for a deployed system is estimation with error
   bars.

---

## 10. The result, in one line

> **For a task whose acceptance predicate closes, determination demand is the Shannon entropy of the
> verdict. Conditioning on any variable `X` splits it, by the chain rule, into what `X` encoded
> (`I(verdict;X)`) and what remains (`H(verdict|X)`), which always sum to the whole. Three of the
> framework's claims are this one identity: `X` a *decomposition* gives the seam; `X` an *actor's
> encoding* gives the store allocation (total actor-invariant, split actor-relative); `X` a
> *retrieval policy* gives RAG. Conservation of determination demand is the chain rule of entropy —
> where the predicate closes, and only there.**

---

## Reproduce

Three self-contained scripts regenerate every figure in this note:

- `assets/measure-toy.py` — §3, decomposition (the seam).
- `assets/measure-actor-allocation.py` — §6.2, three actors, one invariant total.
- `assets/measure-rag.py` — §6.3, messy empirical retrieval with distractors.
