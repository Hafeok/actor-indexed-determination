# Delivery

<!-- ddd:contract

requires: [store, mechanical, judgment, escape, assurance, act, maturation, verdict, outcome, determinate]
establishes: [delivery, undelivered, presumed-discharge|presumed discharge]
status: draft
-->

**Read `00` through `12` first.** This document is deliberately minimal: it establishes the
delivery vocabulary and points at the claims and the evidence; the corpus test that earned it
(2026-08-14) carries the weight. The claims are `DDD-ground-01` through `DDD-ground-03` for the
applicability side, `DDD-delivery-01` through `DDD-delivery-03` here, and `DDD-frame-17` and
`DDD-frame-16` for the discharge section (§4); their files govern, and this prose is exposition.

**Status: draft, pending ratification** — filed from the vocabulary-and-delivery session
(2026-08-15), scoped to what the corpus evidenced.

## 1. The axis

Supply says who resolves a governing decision and when. It does not say whether the resolution
**reaches** the act it governs. Delivery is that axis.

<!-- ddd:embed id=term:delivery -->
> **Delivery** is how authored governance reaches an act: **mechanical** — the act triggers
> retrieval, without judgment — or **judgment-mediated** — it reaches the act only if an actor
> recalls it. Delivery is a property of a decision **at an act-site**, never of the decision
> alone: the same decision can be mechanically delivered at one act-site and judgment-mediated at
> another, and a path from a decision to an act is only as mechanical as its weakest edge.
<!-- /ddd:embed -->

Delivery sits beside standing supply rather than replacing it: standing supply says when the
demand was paid; delivery says whether the payment arrives. They come apart, and that they come
apart is the finding (`DDD-delivery-01` — filing is not encoding: store allocation cannot be read
off artefacts, because an artefact records the authoring, not the arrival).

The trigger, not the index, is what distinguishes the values: if the act triggers retrieval,
delivery is mechanical; if someone must decide to look, delivery is judgment-mediated, whatever
machinery then runs. The corpus's no-unwrap row shows one criterion carrying both values at two
act-sites — act-triggered in CI, actor-triggered locally.

## 2. The failure

<!-- ddd:embed id=term:undelivered -->
> **Undelivered** — filed, adequate, and never reached the act. No source supplied the governing
> decision at the act, so it was determined by nobody: escape, with a distinguishing feature —
> **the ledger shows coverage.** Escape that presents as governance.
<!-- /ddd:embed -->

Undelivered adds no condition to escape and widens nothing: escape is supplied-by-nobody for any
reason (`term:escape`), and delivery failure is one more generator of it, alongside capacity
shortfall and no-applicable-filed-source (`DDD-delivery-02`, joining the instances recorded in
the escape reconciliation). What earns it a name is the presentation: every other escape leaves
the register empty at the point of failure; this one leaves it full.

## 3. The record property

<!-- ddd:embed id=term:presumed-discharge -->
> **Presumed discharge** — a gate's *pass* meaning never-reached: the artefact recording the
> skip is identical to the artefact recording the pass. Named as a property of the record, not
> of an actor's omission, so it stays mechanisable — a discharge ref can be asked whether it
> distinguishes applied-and-satisfied from never-reached.
<!-- /ddd:embed -->

On the source side an act's outcome is at least available to argue from; on the assurance side
the only evidence is the check saying it is fine. That asymmetry is why the compounding claim
(`DDD-delivery-03`) predicts that mechanising checks matters more than mechanising retrieval:
an unretrieved decision and an unretrieved check over the same act are correlated failures —
same actor, same budget, same position — and correlation is exactly what a gate exists not to
have.

## 4. Discharge — how demand meets the act

Delivery is how authored governance reaches an act. Discharge is what happens at the act
regardless: the act completes, a determinate obtains — an outcome always, a verdict only where a
predicate is declared (`core/09` §7a) — and the act's determination demand is thereby met by
*something*.

**Discharge exhaustiveness** (`DDD-frame-17`). At every completed act in a task's scope, each
outcome-relevant alternative is discharged in exactly one of three ways. **Fixed** — the
arrangement's standing configuration together with the ground at the act determines the
resolution. **Resolved** — it does not, and something within the arrangement's control determines
it at the act. **Drawn** — it does not, and what determines it lies outside the arrangement's
control. Escape is a supply mode of discharge, not an absence of it: an act no governance supplies
still lands an outcome, drawn from a distribution the arrangement does not control. **Demand is
never unmet, only ungoverned.**

The unit is the **outcome-relevant alternative**, not the act. One act may carry several: a
timeout has a *when-to-stop* alternative, fixed by the deadline, and a *what-to-return* alternative,
drawn from whatever partial state obtained.

**Exhaustiveness here is provable, not enumerated.** Given the standing configuration and the
ground, the resolution is determined or it is not; if it is not, what determines it is inside the
arrangement's control or outside it. Two dichotomies, three values, no remainder. This is the
repair that retired `DDD-frame-15`, whose four modes — filed decision, judgment, arrangement
default, uncontrolled draw — were exhaustive only by enumeration over loci that turned out not to
be disjoint. A declared default satisfied two of them completely, and nothing but *declaredness*
would have separated the two, which is the one thing this document may not use here.

**The seam this claim must not cross.** The three values partition **discharge** — the
production of a determinate at the act. They do not partition **governance-supply**, and the
store partition (`{rule, check, actor, nothing}` — no fifth source) is not this partition under
new names: there, escape is *nothing*, because the question is what governance supplied, and
nothing did; here, the same act's demand is discharged by an *uncontrolled draw*, because the
question is what the world produced, and the world never produces nothing. A check, likewise, is
an assurance position, not a discharge value. The two partitions answer different questions about
the same act, and neither reduces to the other.

**Governance status is not an axis here, and the values are named so it cannot become one.**
*Fixed*, *resolved* and *drawn* share no word with `term:store`, with the timing terms, or with
`term:escape`. The retired mode list borrowed *filed decision* and *judgment* from the store
vocabulary while partitioning a different object — and `term:judgment` carries an accountability
clause ("a judgment allocation naming no accountable party is not an allocation") that a discharge
value cannot carry, since an ungoverned actor's variation still discharges. Two objects under one
word is a defect the shared names caused; distinct names are the cheaper half of the repair.

**This axis does not stand alone, and the others are not restated as claims** because they are
already canon. `DDD-frame-16`, below, says discharge is act-indexed. The second — at which *level*
the arrangement committed in advance — is `14`'s, and `14` §2 states the composition from its own
side, where the term it needs is established. A trained carrier decoding greedily is *fixed* here
and committed at the level of its policy there, and both readings are true at once. That
composition is what the flat mode list could not represent, and it is why trained inference read as
three incompatible things.

**Discharge is act-indexed** (`DDD-frame-16`). Standing supply is inherited per act; occasioned
supply is produced per act; there is no act-free discharge. Governance never chooses *whether*
demand is supplied — only *by what*, chosen in advance or defaulted at the act.

**Distribution-weighting — an exposition note, deliberately not a claim.** Discharge is
distribution-weighted: demand comes due where acts concentrate, at the rate the ground
distribution `P` supplies them. This is the measure's own `P` (`core/09`) read back, a
projection of the measure rather than a further claim, and it files as this paragraph — the
flag is the finding.

## 5. What this document does not do

It adds no store — the partition `{rule, check, actor, nothing}` is untouched, `DDD-frame-17`
partitions discharge rather than supply (§4), and `DDD-delivery-01` is a correctness condition
on *reading* allocation, not a fifth cell. It does not amend maturation — the harvest-channel
condition (`08`) gains a consuming-side consequence, named in canon at `core/09` §7a
(`DDD-frame-14`); the instruments that run on it file with the projection that carries
diachronic claims. It closes no open generator — the empty-option-set generator recorded in the
escape reconciliation stays open and unexamined.
