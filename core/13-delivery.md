# Delivery

<!-- ddd:contract

requires: [store, mechanical, judgment, escape, assurance, act, maturation]
establishes: [delivery, undelivered, presumed-discharge|presumed discharge]
status: draft
-->

**Read `00` through `12` first.** This document is deliberately minimal: it establishes the
delivery vocabulary and points at the claims and the evidence; the corpus test that earned it
(2026-08-14) carries the weight. The claims are `DDD-ground-01` through `DDD-ground-03` for the
applicability side and `DDD-delivery-01` through `DDD-delivery-03` here; their files govern, and
this prose is exposition.

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

## 4. What this document does not do

It adds no store — the partition `{rule, check, actor, nothing}` is untouched, and
`DDD-delivery-01` is a correctness condition on *reading* allocation, not a fifth cell. It does
not amend maturation — the harvest-channel condition (`08`) gains a consuming-side consequence,
filed with the projection that carries diachronic claims. It closes no open generator — the
empty-option-set generator recorded in the escape reconciliation stays open and unexamined.
