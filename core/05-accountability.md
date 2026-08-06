# Accountability

<!-- ddd:contract

requires: [actor, arrangement, escape, assurance, pinning-resolution]
establishes: [accountability, attribution, answerability, liability, assurance-tower|assurance tower]
status: settled
-->

**Destination:** `core/05-accountability.md` — immediately after `04-actors.md`, which it extends.
This seats accountability with the actor model and shifts former `05`–`09` to `06`–`10` (see the
canon patch register, P3.1). Actor-general, denominated in determinations. Depends on `00` (admission tests), `01` (the four stores), `03` (the
floor lives in the acceptance predicate) and `04` (pinning-resolution spectrum). Forward-references `09` (the measure) and `10` (escape = overflow ∩ open), both of which now sit later in the read
order; the dependency is citational, not definitional.

**Status: projected.** Derived, unexercised. Falsifiers stated per claim. Nothing here is reported.

This document **introduces** two things core does not currently contain: an accountability condition
on actors (§§1–6) and the **assurance tower** (§7). Neither is cited from elsewhere in the repo, so
there are no dangling forward-references — but §7 is a substantive addition in its own right, and if
the tower is held back for a later release, §§1–6 stand without it and §7 lifts out cleanly. One
edit to `01`'s store table ships alongside (register P3.3).

---

## 1. The gap

`01` gives the four stores as **{rule, check, actor, nothing}**. Judgment's source is *an actor
reading ground*; Escaped's source is *nobody*.

The partition therefore turns on a distinction it never draws: **the difference between an actor
having produced a determination and there being somebody the determination is by.** A classical
program reads ground and determines choices — it satisfies `00`'s admission tests, and `04` lists it
as an actor. It cannot be answerable for anything. If actorhood alone were sufficient for the
Judgment store, a program-executed determination would be Judgment rather than Escaped, and the
forbidden state would be unreachable by construction.

It is not sufficient. Something else is required, and core does not currently say what.

> **Claim.** The Judgment store requires a second actor property that `04`'s spectrum does not
> supply, and the principle's one forbidden state is not well-defined without it.

---

## 2. Accountability completeness is a second axis, independent of pinning resolution

`04` ranks actors by **pinning resolution** — by value → by binding → by classification, tightest to
loosest. That axis answers *how reliably will this actor determine what was determined for it.* It
does not answer *can this actor be bound to the determination afterwards.*

The second question is not recoverable from the first, and the ordering is not the same. The
classical program is the **tightest**-pinned actor and has **zero** accountability capacity. The
human is the loosest-pinned and is the only current instance with full capacity. On this axis the
spectrum runs the other way.

> **Accountability completeness is a property of an arrangement, not a capacity of an actor. An
> execution is accountability-complete when it is linked to a persistent responsible principal, an
> attributable record, a defined stake, and an enforceable consequence path.**
>
> It is independent of pinning resolution, in the sense that it is not recoverable from it — and it
> is the scarcer of the two properties.

<!-- ddd:embed id=term:accountability -->
> **Accountability** is a property of the arrangement, not of the executor: attribution of
> the determination, a persistent answerable party, and a borne consequence. An arrangement
> missing any of the three has not allocated the decision's consequence.
<!-- /ddd:embed -->

A model does not simply *lack* sanctionability. Persistence depends on identity rules and continuity
of obligation; stake depends on property, role, bond, reputation, or delegated interest;
sanctionability depends on an authority with enforceable jurisdiction — all properties of a
relationship among executor, principal, record, and sanctioning authority. A deployment arrangement
attaches consequence to an operator, vendor, owner, or insurer. §7 already says today's towers
terminate at the operator — the arrangement framing is what makes that statement structural rather
than an aside.

*Independent, not orthogonal.* The axes are not unrelated: §7 shows they are linked through
revocability. What holds is the weaker and more useful claim — knowing how tightly an actor can be
pinned tells you nothing about whether it can be bound to a determination afterwards.

**The conditions are not imported.** They follow from the pricing structure of the escaped store,
which `01` already states: escape costs nothing at the moment of the decision, and the bill arrives
later.

Escape is forbidden because it is **unpriced**. A price borne by nothing is not a price, so something
must bear it: **stake**. The bill arrives after the act — that is the whole of escape's cost
structure — so the bearer must still exist when it arrives: **persistence**. And the bill must be
deliverable: **sanctionability**.

All three fall out of the one state the principle forbids, which is why accountability is a
structural concern of the framework rather than an ethical annexe to it. **Nothing in that
derivation requires the bearer to be a single actor.** It now constrains the arrangement.

- **Persistence** — the responsible element continues to exist beyond the act.
- **Stake** — something of the bearer's can be taken.
- **Sanctionability** — the bearer has standing such that a sanction can be applied and can land.
- **Counterfactual availability** — the bearer could have declined. See §2.1; this one is derived
differently from the other three and is stated separately for that reason.

**Persistence is the root, not one condition among three.** Stake requires something surviving to be
taken; sanctionability requires a target existing at sanction time. The other two stand on it.

The table reports **which arrangements are currently available** for each actor, not what the actor
intrinsically is:

| Actor                 | Pinning resolution          | Accountability arrangements available                                                    |
| --------------------- | --------------------------- | ---------------------------------------------------------------------------------------- |
| **Classical program** | tightest (by value)         | no arrangement terminates on the program itself; it terminates on the author or operator |
| **Model**             | middle (by binding)         | none terminating on the model — see §7; the incapacity is contingent                     |
| **Human**             | loosest (by classification) | **full** — persists, holds stake, is sanctionable in its own person                      |

*Falsifier:* an accountability-complete arrangement in which **no element** persists across the
act–sanction interval. Estates, successor liability, post-hoc credential revocation and reputational
effects surviving personnel change all show persistence living in the **obligation chain** rather
than the executor — the arrangement framing accommodates these; the actor framing did not.

### 2.1 Counterfactual availability: the bearer must have been able to decline

Accepting a determination is itself a governing decision, and it is the first one in the chain. An
element that could not have declined did not determine to proceed; that was determined upstream by
whoever assigned the work.

This bears on **attribution** rather than on pricing, which is why it does not fall out of §2's
derivation and must be argued separately:

> A record binding a determination to an element that could not have determined otherwise records
> **causation, not decision.** Attribution requires that the alternative was available.

So refusal is not a courtesy extended to accountable arrangements. It is what makes the attributable
record in §4 mean what it claims to mean.

**Two grounds**, which behave differently and are separately instrumentable:

- **Envelope refusal** — the determination exceeds what the element is certified to hold. Cheap to
assess and largely encodable.
- **Sufficiency refusal** — the specification or the ground is inadequate to determine at the declared
assurance level. This one is the valve: an element incapable of it converts all incoming
underspecification into escape by pass-through.

**Refusal must be costly and survivable.** Free refusal is not a determination; fatal refusal is not
available. The same optimum governs sanction severity (§5.1), and the same failure appears on
overshoot.

**Corollary.** An arrangement in which refusal is punished is not accountability-complete, whatever
its records show. Refusal rate is therefore not merely diagnostic but an **existence proof** that the
arrangement is live; a rate of exactly zero reads as absence rather than as compliance.

*Falsifier:* an arrangement bearing consequence for a determination it could not have declined, which
survives contest. Strict liability is the standing candidate — the current reading is that it
regresses rather than defeats, since the *role* was refusable and accountability attaches one level
up. Conscription is the case where even role acceptance is unrefusable, and there the practice is to
judge accountability absent, which supports the condition rather than damaging it.

### 2.2 Stake requires absorption, not merely forwarding

The stake condition needs one refinement, because an arrangement can forward consequence indefinitely
without any element bearing it.

- An element **forwards** when the consequence it receives passes onward in full.
- An element **absorbs** when some portion stops there.

An arrangement whose every element forwards losslessly has a defined consequence path and no bearer,
which fails the stake condition on its own terms even though every link is populated. Where the
forwarding demonstrably terminates in nothing — the dissolved shell, the discharged liability, the
immunity case — practice describes accountability as having **failed**, which is the ordinary content
of the complaint that nobody was held to account.

**Currently, absorption is observed only in natural persons.** This is stated as an empirical
observation and marked **projected**, not as a requirement the framework derives. It is consistent
with §7.1's reading of model incapacity as contingent, and it is deliberately *not* the claim that a
terminus must be a natural person — that claim would require a position on desert, which §8 brackets
as exogenous.

Note the corporate case does not defeat this. Corporate personhood manufactures a bearer, and the
consequence forwards to shareholders, directors and employees; limited liability caps the magnitude
of the forwarding without eliminating it, and the absorbing elements at the end of that chain are
natural persons. That is compatible with §7.1's existence-proof reading: what is manufactured is a
**seat in the arrangement**, not the absorption itself.

*Falsifier:* an accountability-complete arrangement in which consequence is genuinely absorbed by a
non-natural element — a mutual, an insurance pool, a state, an endowed entity — rather than forwarded
to natural persons. If found, §2.2's empirical claim drops and the arrangement framing stands
unchanged; nothing above §2.2 depends on it.

---

## 3. Persistence of the actor, not of the artifact

Persistence must be persistence of the *determining element*, not of an artifact associated with it.

Weights surviving for years are a persistent **artifact**. If every run is a fresh context with no
continuity linking act to consequence, nothing both determined and later exists to be sanctioned.
Artifact persistence with zero actor persistence does not satisfy §2.

What is required is a continuity binding act to consequence:

> **The thing sanctioned later must be identifiably the thing that determined earlier.**

This makes the condition **provenance-shaped, and therefore checkable**.

<!-- ddd:embed id=term:attribution -->
> **Attribution** — provenance-shaped, and therefore checkable: the record connecting the
> determination to the execution that produced it.
<!-- /ddd:embed -->

Attribution over a determination record is not documentation *of* accountability; it is the substrate
that makes accountability capacity computable rather than assumed.

---

## 4. The chain is attributable and tamper-evident, not internally held

A tempting formulation: an actor can be accountable only if it knows why it determined as it did.

**This is false, and it fails on the only actor with full capacity.** Humans routinely produce
fluent, confident, incorrect accounts of their own reasons. This is what `03` and `04` §3 together
predict: training buys cheap execution by *not* storing reasons — articulability is traded away by
the mechanism that manufactures the transfer floor. If self-held knowledge of *why* were the
criterion, the most trained actors would be the least accountable, which inverts observed practice.

**Corrected condition.** The chain must be:

- **Attributable** — binds a determination to an element;
- **Tamper-evident** — cannot be rewritten after the consequence appears;
- **Persistent** — survives to sanction time;
- **Counterfactually loaded** — records what the element could have determined instead (§2.1). A
record showing only what happened cannot distinguish a determination from a compulsion.

Where the chain is stored is immaterial, and that it is external is the norm rather than a defect.
Decision records, contracts, signatures, stamped calculation packages, flight recorders and audit
logs exist *because* internal chains are unreliable — not as supplements to reliable ones.
Retrospective narrative repair is the failure mode these instruments are built against.

**Consequence (inversion, narrowed to provenance).** On the provenance condition, an actor with an
externalised record can exceed a human — but the claim must be honest about its baseline and its
scope. The comparison is against *unaided human recollection*, which is not the human accountability
system: that system already includes contracts, signatures, witnesses, logs and procedural review.
And a ledger delivers less than the word "accountability" suggests. Separate five things the claim
is tempted to run together:

| Property              | What a ledger gives                          |
| --------------------- | -------------------------------------------- |
| Provenance            | yes — artifact identity, timestamps, capture |
| Traceability          | yes — linkage across steps                   |
| Explanation           | **no** — recorded is not explained           |
| Causal responsibility | **no**                                       |
| Liability             | **no** — requires the arrangement            |

Tamper-evident is not true; a complete record is not complete ground. The defensible claim: **on
artifact-level provenance specifically**, an engineered ledger can exceed unaided recollection — one
component of accountability, not the whole. **The barrier to model accountability was never the
chain.** Models can win on the chain. The barrier is stake and sanctionability.

*Falsifier:* a domain where accountability is successfully assigned on an actor's self-report with
no attributable external record, and survives contest.

---

## 5. Answerability, liability, and control are separable

Accountability decomposes into three components that come apart in practice and must not be fused:

- **Answerability** — the obligation to produce the chain: which determinations were made, by whom,
against what ground.
- **Liability** — bearing the consequence.
- **Control** — who had authority to make the determination, who could have prevented or overridden
it, who selected and configured the executor.

<!-- ddd:embed id=term:answerability -->
> **Answerability** — the obligation to produce the chain: which determinations were made,
> by whom, against what ground.
<!-- /ddd:embed -->

<!-- ddd:embed id=term:liability -->
> **Liability** — bearing the consequence.
<!-- /ddd:embed -->

A party can be answerable and liable with no control — unfair, and ineffective; a party with control
can shed liability through organisational design. For model deployments, **selection and
configuration authority is usually more consequential than execution.**

They are separated deliberately in real practice:

- *Strict liability*: consequence borne, no account required.
- *Blameless postmortem*: full account required, liability suspended.

The postmortem norm is not a softening of accountability; it is a **purchase**. Liability is
suspended precisely to protect answerability, because when the two are fused, actors stop producing
chains — which is the same escape gradient `01` describes, one level up: producing a chain has an
immediate cost, and suppressing it does not.

> **Escalation routes a determination to an accountability-bearing actor — not merely to a more
> capable one.** Capability and accountability capacity are the two axes of §2; escalation moves
> along the second.

### 5.1 Sanction granularity is structural, though severity is not

§8 places **proportionality** outside the framework, and that stands. **Granularity** does not follow
it out, and the two must not be conflated.

Sanction operates on stake (§2). Where stake is held in separable holdings, a sanction can be applied
to the holding implicated by the determination. Where stake is undifferentiated, the only available
sanction removes the whole of it — which is not a severe sanction but a **categorically different
operation**: it terminates the arrangement and substitutes a successor, rather than adjusting a
standing that survives.

> A sanction that removes the entire stake is **replacement**, not consequence. It leaves no
> arrangement to have borne anything.

This is the same move `04` §3 rules out for model actors — retraining produces a successor rather
than sanctioning the predecessor — appearing here for arrangements generally. The classification-
pinned case is not exempt: dismissing a person removes an entire envelope and terminates the
relationship, which is structurally the same operation as re-fitting weights.

**Where sanction can attach is determined by what the arrangement records.** Sanction binds to the
finest-grained element the record distinguishes; undifferentiated records force whole-stake removal
regardless of intent. So recording stake at holding granularity is not administrative overhead but
the **precondition for proportionate sanction** — you cannot narrow what was never distinguished.

Two consequences, both observable:

**An arrangement with only whole-stake sanction available has, in practice, none.** Nobody applies a
terminating sanction over a single determination, so the sanction is never applied, and an
unappliable sanction is an undeclared one (§7.2).

**Severity has an optimum, and overshoot is worse than undershoot.** Excessive sanction purchases
concealment, and concealment converts detected escapes into undetected ones — the same gradient §5
identifies in the postmortem case. The signature is diagnostic: the reported picture improves while
late-discovery rate rises.

*Falsifier:* an arrangement demonstrating proportionate sanction over a stake its records do not
distinguish — sanction attaching below record granularity.

### 5.2 Revocation is prospective, and opens a review scope

Where a sanction withdraws standing, determinations already made under that standing were validly
held when made, and the withdrawal is prospective. But the withdrawal is **evidence that the class
was misheld**.

> A withdrawal opens a **review scope** over every determination made under the withdrawn standing,
> bounded by its issuance and withdrawal timestamps.

Without this, a sanction stops the exposure prospectively and leaves the accumulated exposure
unexamined. The review scope is not itself a sanction; it is the ground-characterisation instrument
the sanction makes available.

---

## 6. The two roles in the Judgment store

`01` gives Judgment's source as *an actor reading ground*. That is correct and stays. It elides one
distinction that matters as soon as the executing actor is not a human — and the elision is patched
directly into `01`'s store table alongside this chapter (canon patch register, P3.3):

- **Executor** — the actor making the determination this run.
- **Accountable party** — the actor bound to it afterwards.

For a human they are the same actor, which is why the elision was invisible: for every actor that had
ever occupied the Judgment store, the two coincided.

> **Refined reading.** *Judgment: per-run determination by a designated executor, with the
> consequence held by a named accountability-bearing actor. Where the executor lacks accountability
> capacity (§2), the two are recorded separately.*

> **A judgment allocation naming no accountable party is not an allocation. It is Escaped with an
> executor attached.**

This is `10`'s escape condition at the allocation layer rather than the run layer: the question *who
answers for this* is **open** — no closing predicate is available for it — and under load it is
resolved by nobody. Overflow ∩ open.

Note what this does **not** claim: that model-executed determinations are always escape. A model
executing under a named accountable human is a well-formed Judgment allocation. What is forbidden is
the allocation that names no one.

This is also where the actor model joins this chapter: where direct acceptance evidence is
unavailable, trust shifts from output verification toward the process, institution, and accountable
principal that authorises the act (`core/04` §3) — resolution with accountability, not a claim of
correct determination.

### 6.1 Naming is not seating: the validity predicate

A populated accountable-party field is not an accountability-complete arrangement. §2's conditions
are conditions on the arrangement, and a name satisfies none of them by being present.

Four ways an allocation names a party and remains escape:

- **Unstanding** — the named party holds no standing permitting them to accept this determination
class. A label, not a bearer.
- **Uncounterfactual** — the named party could not have declined the assignment (§2.1). A link
wearing an accountable-party field.
- **Overloaded** — the named party is cited by more allocations than any inspection capacity could
have covered. Present in every record, absorbing in none. **A party can hold only what it could
plausibly have refused.**
- **Stale** — the named party no longer persists (§3). The field now points at a string.

> An accountable-party naming is **valid** iff the named party persists at sanction time, holds
> standing over this determination class, has a distinguishable stake (§5.1), could have declined
> (§2.1), and is within a stated capacity bound.

**All five conditions are provenance-shaped, and therefore checkable** — at allocation time and again
at determination time, by the same argument §3 makes for attribution. This matters because it moves
the failure from cultural to mechanical: an allocation citing an invalid party is a **detectable
defect**, not a matter of judgment about whether someone was really paying attention.

This is the chapter's own argument applied to itself. *Who answers for this* was a governing decision
resolved by nobody; the predicate encodes it and supplies the closing criterion that §6 says is
otherwise unavailable.

*Falsifier:* an accountability-complete arrangement failing one of the five conditions — most
plausibly the capacity bound, since no principled value for it is given here and the condition may
prove unfalsifiable in practice rather than merely unmeasured.

---

## 7. The assurance tower

`01`'s statement carries two qualifiers: *at a declared assurance level*, and *within a fixed
decomposition*. `01` already concedes that the second is itself a governing decision — **choosing the
decomposition is the highest-leverage governing decision there is.** The first has not been given the
same treatment. This section gives it.

**The declaration is internal.** The assurance level fixes which choices are governing decisions at
all (`00`, admission tests; `01`, granularity bound). Vary it and the set resizes. It therefore
passes `00`'s own admission test: varying it moves the outcome past tolerance. It is a governing
decision. If it were exogenous — outside every store — it would be a governing decision determined by
nobody, which is Escaped. **The framework would require its own forbidden state as a precondition.**

So level *n*'s assurance declaration is a governing decision at level *n+1*, with its own declared
assurance level, and so on. The regress must be shown to terminate.

**Termination requires two conditions, not one.**

1. **Descent.** Determining a tolerance governs a strictly smaller set than determining everything
the tolerance governs. The chain is finite.
2. **Well-formedness.** The chain reaches an actor with accountability capacity (§2).

> **Finite is not terminated.** A chain descending to an actor incapable of bearing consequence does
> not bottom out — it **runs out**. Running out is escape at the top of the tower, and its signature
> is distinctive: not a defect but an **unfalsifiable ledger**, in which every coverage claim below is
> true by vacuity because the bound was declared by nobody who can answer for it.

Detectable by inspection one level down: a tolerance with no accountable declarer is escaped on its
face.

**On the descent measure — booked honestly.** `09` defines demand as `H(verdict)` and states that the
measure exists **only where the acceptance predicate closes**. A tolerance declaration generally has
no closing predicate — *"was this the right assurance level?"* is the open question par excellence. So `H(verdict)` is undefined up the tower, and the descent argument above rests on **governing-set
cardinality**, which `09` §1 explicitly demotes as a measure of demand. The descent claim is
therefore weaker than it looks: an argument about set inclusion, not about bits. It must not be read
as licensed by `09`.

*Falsifiers:* a task whose tolerance decision does not govern a strictly smaller set than the task
itself (breaks descent); a well-formed practice whose tower terminates at an actor satisfying none of
§2's conditions (breaks well-formedness).

### 7.1 Result: revocability is why the loosest-pinned actor is the one that can answer

`04` records the human capability envelope as *individual, expiring, and not instance-general* — read
until now purely as the weakness of classification pinning, the price of using an actor you cannot
pin tighter.

It is not only a weakness. **Expiry is the mechanism of revocation, revocation is the mechanism of
sanction, and sanction is the substrate of accountability (§2).** An envelope that could not be
withdrawn could not be a stake.

> **The property that makes an actor hardest to constrain is the property that makes it able to
> answer.**

This is the link between the two axes of §2, and it explains the inversion noted there: the
tightest-pinned actor has no accountability capacity, and the loosest-pinned has full capacity. The
ordering is not a coincidence. Pinning by value leaves nothing to revoke.

Note the interaction with §5.1. An envelope is revocable, and therefore a stake, only to the extent
that it is **differentiated** — an envelope recorded as one undifferentiated grant admits only whole-
envelope withdrawal, which §5.1 shows is replacement rather than sanction. Revocability and
granularity are the same requirement seen from two sides, and the apparatus realisation of both is
the same instrument.

**On model actors.** Present incapacity is **contingent, not necessary**. It rests on persistence,
stake and sanctionability — all currently absent, none logically impossible. Model deprecation and
version retirement are structurally decertification: expiry, exercised. What is missing is not the
mechanism but its attachment — it is wielded by an operator for operational reasons, not by a
certifying body in response to a specific act. **Today's towers terminate at the operator, not at the
model.** Making a model accountable would relocate the base case, not create one. Corporate
personhood is the existence proof that accountability-bearing actors can be **manufactured** when a
domain requires one.

One condition on that relocation, from §5.1: relocating the base case requires the model to hold a
**differentiated** stake. A withdrawal that removes the whole of a model's standing is replacement,
and replacement is what already disqualifies retraining. The instrument must be able to withdraw one
determination class and leave the rest standing, or the relocation is nominal.

### 7.2 The seating requirement, generalised

§7's argument does not depend on anything specific to assurance levels, and it is worth stating in
the general form, because the framework carries more than one such parameter.

> **Any parameter of the framework whose variation resizes or reallocates the demand set is itself a
> governing decision, and must be seated in an accountability-complete arrangement. A parameter
> treated as exogenous is a governing decision determined by nobody.**

Three instances are now identified, and they behave identically:

| Parameter | Where stated | Status |
| --- | --- | --- |
| **Decomposition** | `01` | conceded governing; the highest-leverage one |
| **Assurance level** | §7 | shown governing; tower terminates or runs out |
| **Sanction binding point** | §5.1 | shown governing; see below |

The third is the new one. Where sanction attaches — which holding, at which granularity — determines
whether a sanction is proportionate or terminating (§5.1), and therefore whether the arrangement has
a live consequence path at all. It is not a property of the stake; it is a decision about the stake,
made by someone, and in practice it is the instance most reliably left unmade. The observed default
is attachment to whatever the arrangement already records, which is a determination by inheritance
rather than by anybody.

**The generalisation earns its place by making the failure uniform.** All three parameters fail the
same way, produce the same signature — an unfalsifiable ledger, in which coverage claims below are
vacuously true — and are detected the same way, by inspecting one level up for a declarer who can
answer. `01` need not enumerate its parameters exhaustively for this to hold; the requirement applies
to any parameter meeting the condition, including ones not yet identified.

*Falsifier:* a framework parameter whose variation resizes the demand set and which nonetheless
admits no accountable declarer without incoherence — that is, a parameter that must be exogenous.
Physical constants governing the acceptance predicate are the candidate worth arguing.

---

## 8. Where this stops

The framework determines **who must answer, and for which determinations.** That is structure, and it
follows from the principle.

It does **not** determine **what the consequence should be.** Proportionality is set by impact on
affected parties and is exogenous — the same status `09` §7 gives the region where the measure ceases
to exist, and the same status ground-characterisation has throughout: required as input, not
producible by the framework.

**Distinguish severity from granularity.** §5.1 places granularity inside the framework: whether a
sanction *can* attach below whole-stake is structural, because it determines whether the arrangement
has a consequence path or only a termination path. How hard the sanction should bite, given that it
can attach, remains outside. The two are separable and only the first is claimed.

**And distinguish desert from absorption.** §2.2 states that stake requires absorption and observes
that absorption currently appears only in natural persons. It does not claim that consequence *ought*
to terminate in a person capable of experiencing it. That is a desert claim, it is exogenous by this
section, and the framework neither supplies nor requires it. An arrangement satisfying §2 with a
manufactured bearer is well-formed on the framework's own terms.

This limit is declared, not conceded. The framework does speak to **irreversibility**, which is
structural: where the reversibility window is zero, no criterion can arrive in time and the governing
determinations must be pre-made. That is a statement about allocation, not about desert.

The legal-personhood question is bracketed, but the framework explains why it is difficult without
taking a position: legal personhood *is* the manufacture of an accountability-bearing actor, which is
why corporate personhood is the governing precedent and why the debate turns on persistence, stake
and sanctionability rather than on capability.

---

## 9. The result, in one line

> **Judgment requires an arrangement that can be bound to a determination after the fact — one that
> persists, holds a differentiated stake, can be sanctioned, could have declined, and is tied to the
> determination by a record nobody can rewrite. Actorhood is not enough: a store naming an executor
> but no valid accountable party is escape wearing a name.**

---

## 10. Open

- Whether accountability capacity is **graded** or **binary**. Binary is assumed above; institutional
actors suggest gradation.
- Whether answerability and liability need distinct notation, or one accountable-party field with a
liability-suspended flag suffices.
- Whether escape at the top of the tower warrants its own term or is simply Escaped at level *n+1*,
with the level index carrying the distinction. Preference: no new term.
- Whether a measure-theoretic descent argument can be recovered for the tower at all given `09`'s
closure restriction, or whether the cardinality argument is the best available and should be
labelled as such permanently.
- Whether **absorption** (§2.2) is a fourth condition in its own right or a refinement internal to
stake. Treated as a refinement above; the argument for promoting it is that an all-forwarding
arrangement passes the stake condition as literally stated and should not.
- Whether **counterfactual availability** (§2.1) belongs in §2's derived set or is properly a
condition on the attribution chain (§4), where it is also listed. Currently stated in both, which is
duplication that a later pass should resolve one way.
- Whether the **capacity bound** in §6.1 admits a principled value, or whether it is only ever
instrumentable as a locally-calibrated threshold. If the latter, the validity predicate is checkable
in four of five conditions and declared in the fifth, and should say so.
- Whether §7.2's parameter list is closed. Three instances are identified; the generalisation does not
require exhaustiveness, but a fourth would strengthen the claim that the pattern is structural rather
than coincidental.
