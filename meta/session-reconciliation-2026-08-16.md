# Session reconciliation — a superseded prompt caught at Gate 0 (2026-08-16)

**What this note projects:** the Gate 0 finding of the vocabulary-and-delivery canon session as it
fired on 2026-08-16, derived at upstream `0388985` (`v5.5.0-3-g0388985`) and downstream `4848b9e`.
Filed on Emil's ruling of 2026-08-17. It is a record about the arrangement, not a canon change: it
mints nothing, supersedes nothing, and no claim rests on it.

## The finding

A session prompt was issued to file four earned canon objects. Its earned scope had already been
filed, ratified and merged before the session fired. Gate 0's identity checks caught the
supersession, and the session drafted nothing.

## How it arose

The prompt was authored on 2026-08-15, against the queue as it then stood. On that day the queue was
accurate: the corpus test of 2026-08-14 had met the four SR-10 criteria, and its Gate 4 ruling fixed
the four filings as evidenced. The prompt was correct when written.

Between its authoring and its firing, the work was done. The `claude/earned-canon-vocab-delivery-k4ngl4`
session ran the same four filings through five gates, each closed on an Emil ruling, and both
registers merged: upstream PR #10 as `e8663b8`, tagged **v5.5.0** on Emil's approval; downstream
PR #21 as `4848b9e`. The tag was cut at 13:00 CEST on 2026-08-16. This session fired afterwards,
carrying a prompt that described a queue two states behind the repository.

The prompt anticipated drift and instructed that it be reconciled at Gate 0 — *"upstream has moved
past v5.4.0 with the related-work merge"*. Upstream had moved further than the prompt could know: it
had moved past the prompt itself.

## What Gate 0 checked

Refs and identities read at fetch, all verified against the repositories rather than against any
session record:

| Object | Ref / identity |
|---|---|
| `actor-indexed-determination` head | `0388985a94e3ed68d9cece1897f127391b0fbb5f` = `v5.5.0-3-g0388985` |
| v5.5.0 (the merge it tags) | `e8663b8` |
| `decision-driven-design` head | `4848b9e15ea49bc923b2d23933e2c05a21202ba0` (merge of PR #21) |
| `product-cli` (read-only evidence source, untouched) | `d506ac94310bb24e3c6a1b786034046ac0d024b0` |
| Evidence document, last touched | `b2d5b279e9120fc967212813fd65a907761f828f` |
| Evidence document, merged as PR #20 | `886035ba61f37d06ba771b30e748a5f29f7b3bb2` |
| Evidence document identity | 1,261 lines / 12,313 words / sha256 `32985f6d83d80fbc4d9f7b4e12e4530f5d55ff96519b3fa0308cc5aa1d9412ce` |

The evidence document was unchanged. That is the load-bearing check: the same evidence would have
forced the same statements against identifiers that already held them.

The four filings were then confirmed present at head, by reading the registers:

| Earned filing | Landed as | Register |
|---|---|---|
| Applicability gate — at least one named ground axis | `DDD-ground-01` (axis-type mark filed as a maturity state) | upstream |
| Four-state typing and the `—(open)` timing value | `DDD-ground-02`, `DDD-ground-03` | upstream |
| Position/region vocabulary, 22-axis registry seed | `graph/axis-registry.yaml` (`axis-registry/v1`, `artefact-not-canon`, 22 axes) | downstream |
| Delivery vocabulary | `core/13-delivery.md`; `term:delivery`, `term:undelivered`, `term:presumed-discharge`; `DDD-delivery-01/02/03`; `DDD-delivery-04` | both |

Both Gate 0 questions the prompt reserved for Emil were already answered on the record. Retro-filing's
two fields were ruled **in** and filed as `DDD-ground-04`. The queued delivery filings were located,
reconciled and filed **once**, as `DDD-delivery-01/02/03` with the `00-primitives` term-collision
repair. Session decisions `DDD-dec-17` (upstream) and `DDD-dec-18` (the pin advance, downstream) were
in place.

## What was refused, and on what ground

Drafting the four filings would have minted duplicates against `DDD-ground-01`…`04` and
`DDD-delivery-01`…`04`. That was refused on this framework's own discipline, on three counts at once:

- canon changes by supersession, never by rewriting;
- identifiers are never reused, and renumbering is forbidden;
- nothing files without its gate's ruling — yet every one of these objects already carried a
  recorded Emil ruling.

The refusal cost nothing, because there was nothing to file. The evidence was unchanged, so no new
statement was available to draft. A session that had proceeded on the prompt's authority would have
produced a second set of identifiers for statements canon already held, and the duplication would
have been discovered downstream of the filing rather than upstream of it.

## Why this is worth a page

The gate did the job the gate exists to do. Gate 0's identity checks are ordinarily a formality —
confirm the refs, confirm the evidence document, proceed. Here they were the whole session. The
check that catches a stale evidence document caught a stale *prompt*, which is the same failure at a
different layer: a governing artefact, authored against a state of the world, arriving after that
state had moved.

This is the session's own vocabulary applied to the session. A prompt is authored governance
delivered to an act. Its delivery is judgement-mediated: nothing mechanical compares a prompt's
premises against the registers it names, so the reconciliation depended entirely on the reading at
Gate 0. Had the gate passed on presumption — the checks *look* routine, and a pass is
indistinguishable between applied-and-satisfied and never-reached — the session would have drafted
against superseded ground. That indistinguishability is `term:presumed-discharge`, filed by the very
session whose supersession this note records.

The instance is recorded here, not as a claim. No statement is minted from a single occurrence, and
this one is uncorroborated. It is filed as evidence about the arrangement: the second observed
instance of a governing artefact whose non-arrival or stale arrival is the phenomenon the delivery
vocabulary names, after the five arrival failures already recorded in `DDD-dec-17`. If the
`meta/sessions` working convention recommended to the freight session is taken up, this instance
belongs in its evidence.

## What this session landed

One commit, routed on Emil's ruling: the `DDD-dec-17` DRAFT-marker flip prepared post-merge on the
`k4ngl4` branch (`768741a`) and held there for routing. Upstream only. No downstream change, no pin
movement, no new identifier.

Validators at the routing, unchanged from the v5.5.0 baseline: 46 claims valid, 5 decisions valid;
core-order 14 documents, 65 terms, **0 errors, zero W4**, warning profile 52 W1 and 7 W2. Downstream
was not touched and remains at 25 claims, 13 decisions, 0 errors and 0 warnings, with 28 pins
resolving against `v5.5.0` and no basis-loss warnings.

## What did not ride in

The prompt's excluded list holds in full: the exhaustiveness/defence-in-depth wording seam; the
capacity model and everything magnitude-shaped; the store partition, which was never on trial; and
Q25–Q33 of the ground-axes note, Q33 with its own ruled routing. The prompt is superseded, not
stretched. A superseded prompt confers no authority on the material it excluded.

The queue after v5.5.0 stands exactly as recorded at that session's close, and none of it is this
session's: **freight** — carrying the capacity residue, the E13/W5 region-and-statement
instrumentation extension with `DDD-dec-18` as its evidence, the `core/11` §7 four-versus-five prose
defect, and the `meta/sessions` convention — then the **Q25/Q27/Q30 filing wave**, then **Wave 3 and
Paper A**. The capacity scoping session remains cancelled per the Gate 5 queue correction.
