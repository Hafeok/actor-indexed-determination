# Indexed determination

<!-- ddd:contract

requires: [determination, ground, tolerance, arrangement, assurance, acceptance-predicate, closure, floor, judgment, act, selection, training, verdict]
establishes: [commitment-level|commitment level, residual-discretion|residual discretion]
status: draft
-->

**Read `00` through `13` first.** This document is deliberately minimal: it states the index that
the rest of canon carries severally, and points at the claims; their files govern, and this prose
is exposition. It establishes two terms and no more — `commitment-level` and `residual-discretion`
(§2), both of them names for content `DDD-frame-02` already states. The tuple itself is a claim,
not a term, and is not minted here. The claims are `DDD-frame-01` (the tuple), `DDD-frame-02` (commitment levels and
residual discretion), `DDD-floor-02` (the relational floor), and the hypothesis set
`DDD-hyp-01` through `DDD-hyp-05` (§4), summarised by `DDD-frame-07`.

**Status: draft, pending ratification** — filed from the Wave 3 session (2026-08-18), drafted
against the Paper A revision foundation (§1.1, §3, §6) with canon at head governing.

## 1. The index

A parameter that never varies is indistinguishable from a constant. The classical allocation
accounts held the arrangement largely fixed while the allocation was analysed, which made the
determiner look like a constant of the analysis. It is a parameter, and not the only one:

> **Unresolved determination is indexed by the tuple ⟨task, ground, acceptance relation,
> tolerance, arrangement, assurance⟩, not by the task alone.** *(`DDD-frame-01`.)*

Canon built the coordinates severally — tolerance and assurance separated in `01`; the
arrangement as the unit of comparison in `00` §3 and `05` §2; ground and the acceptance
predicate in `00` and `03`. The index is those coordinates stated as one relation. Move any
coordinate and the determination problem moves: which distinctions are committed in advance,
which choices remain for the act, which outputs can be checked, whose identity must be trusted,
who answers, and which residual risks stay accepted — or escape.

## 2. Commitment levels and residual discretion

How does an arrangement commit behaviour in advance? *(`DDD-frame-02`.)*

<!-- ddd:embed id=term:commitment-level -->
> A **commitment level** is a level at which an arrangement fixes behaviour in advance:
> **outcome-level** — permitted resolutions fixed directly; **policy-level** — the
> generating procedure fixed; **principal-level** — a determiner selected by qualification
> and case-level resolution delegated. The three compose, and they are levels of
> commitment, not species of actor: the question is never which of three kinds an actor
> is, but at which levels the arrangement has committed.
<!-- /ddd:embed -->

Each level names what an arrangement has already settled before the act begins:

| Level | What is fixed | Instances |
|---|---|---|
| **outcome** | the permitted resolutions themselves | a lookup table, a schema constraint, an invariant admitting one acceptable outcome for a class of cases |
| **policy** | the procedure that generates a resolution | an algorithm, a trained policy, an operating procedure, a controller |
| **principal** | who resolves, selected by qualification, the case delegated | a licensed engineer, a court, a review board |

The levels compose: one deployment can select a principal, bind it to a policy, and enforce
outcome constraints on what results. What the commitments do not reach is left at the act.

<!-- ddd:embed id=term:residual-discretion -->
> **Residual discretion** is the outcome-relevant variation remaining at the act after the
> arrangement's declared commitments are applied. It is not randomness: a deterministic
> arrangement can carry substantial discretion across unfamiliar cases, a randomised one
> can be tightly committed, and a zero-variance arrangement can be consistently wrong.
<!-- /ddd:embed -->

The analytical question is therefore never which of three kinds an actor is; it is at which
levels the arrangement has committed, and what residual discretion is left at the act.

## 3. The relational floor

`03` locates the floor in the acceptance predicate, and closure is closure **for an
arrangement** — the two indexings the floor result already carries. Stated over the full index:

> **The judgment floor is relational: irreducibility is a property of the indexed relation, not
> of the task alone.** *(`DDD-floor-02`.)*

The same nominal task is routine for one arrangement and judgment-heavy for another, and better
ground, contracts, checks, and institutions move the boundary without making the task
"intrinsically" simpler in every sense. Each partial form canon already states — the floor as a
property of the predicate (`03`), of the ⟨actor, predicate⟩ pair (`03`, consequence), of the
arrangement's closure bounds (`term:closure`) — is recovered by holding the remaining
coordinates of the relation fixed.

## 4. What the index predicts

The index is not only an accounting; it predicts. Binary human-versus-model predictions are
replaced by graded hypotheses about arrangements — five, filed as the hypothesis set
`DDD-hyp-01` through `DDD-hyp-05` and summarised by `DDD-frame-07` — under one shared falsifier
discipline: each is stated with the preregistration-shaped null of the arrangement study that
would fire it, the conditions compared are arrangements rather than isolated actor labels, and
nominal difficulty and resources are controlled throughout.

- **H1 — operational evaluability** (`DDD-hyp-01`): advantage shifts toward high-throughput
  computational generation as acceptance becomes operationally evaluable, feedback fast and
  dense, ground accessible, checking cheap, and retries affordable.
- **H2 — ground and judgment dependence** (`DDD-hyp-02`): situated arrangements retain
  advantage as ground goes missing, consequences delay, evaluators disagree, criteria drift,
  and tacit knowledge or normative legitimacy is required.
- **H3 — generator/checker composition** (`DDD-hyp-03`): a generator composed with a checker
  or reviewer beats both generator-alone and judgment-alone baselines where generation
  benefits from breadth, much of acceptance closes, and the open residue can be escalated.
- **H4 — accountability completeness** (`DDD-hyp-04`): trust and deployment follow the
  completeness of the accountability relation (`05`), not the executor's kind.
- **H5 — selection versus training** (`DDD-hyp-05`): reliance on selection rises as
  result-level evaluation slows, loses objectivity, drifts, and thins — where the work cannot
  be checked, the worker is.

Two of the five carry a validity qualification restated on their claim files: instruments that
reach open-predicate carriage attach assurance to claimant identity, so they exist only for
identities that outlive their verdict horizons — cross-identity transfer, model version
succession included, is partial and per-capability, and an answer-keyed instrument cannot
evidence such carriage at all (`DDD-cost-13`).
