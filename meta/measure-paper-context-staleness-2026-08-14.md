# Staleness audit — the v4.4 measure-paper context, checked against live canon

**Filed** 2026-08-14, at the Gate 2 hold of the related-work gate-pass session.
**Source of truth** `Hafeok/actor-indexed-determination` at `a312a5570b3a2386f075f0cd6362df9b99142721`.
**Companion** `meta/measure-paper-context.md`, the replacement projection.
**Kind** Evidence about a projection. Not canon.

---

## Why this audit exists

A paragraph drafted against the v4.4 project context was filed into `core/09` §8 on 2026-08-14
carrying two clauses live canon contradicts. It was caught at the gate only because the ruling that
replaced it required its pointers to be verified against live text first. That is a narrow escape,
not a working control, and the class of failure is worth naming: **a forward-looking phrase outlives
the work it was waiting on.**

The check run here is the one the rate–distortion clause failed. Every forward-looking phrase —
"not done", "next result", "pending", "blocked behind" — is checked against the live section that
would have settled it, and the live text is quoted rather than paraphrased.

## Scope limit, stated plainly

**The old `measure-paper-context.md` is not in this repository and was not available to this
session.** It lives in the measure-paper project, which this session cannot read and must not write
to. A complete sweep of *every* forward-looking phrase in that file therefore could not be run.

What was audited instead:

- the phrases provably carried by the v4.4 context, because they surfaced in prose drafted against it
  — the related-work section artifact of 2026-08-13 is the specimen, and its `§` pointers are a
  fingerprint of the copy it was written against;
- the location facts Emil supplied at the Gate 1 clearance;
- the settled-since items live canon records in its own change history, which any v4.4-era context
  would have carried in its forward-looking form.

The provenance column below says which is which. Rows marked *unconfirmed* describe real movement in
canon whose presence in the old file could not be checked. **A full sweep still needs the file.**

## The table

| # | Phrase as carried | Provenance | Live canon says | Verdict |
|---|---|---|---|---|
| 1 | The measure paper is `core/08`, in `decision-driven-design` | Emil, Gate 1 clearance | `meta/CANON-PATCH-REGISTER.md` filing note: *"read `core/08` as `core/09` (the measure) and `core/09` as `core/10` (the floor mechanism)"*; `meta/repo-topology.md` records the split, and `core/README.md` lists `09 — the measure` | **Moved twice.** Renumbered by P3.1, then relocated by the repository split. `decision-driven-design` is now the dependent repository, not this paper's home |
| 2 | "the companion framework derives an error floor from it" | Confirmed — carried into `core/09` §8 as drafted | `core/11` §4 is titled *"The soft-capacity bound"*; §4.1: *"`p_err` is derived, not assumed … rate-distortion theory"*. The derivation is in **this** repository, and it is one result, not two. "Error floor" appears nowhere in canon | **Stale, and reached a shipped artifact.** Corrected at `a312a55` |
| 3 | "the escape/judgement split named as this note's next result" | Confirmed — carried into `core/09` §8 as drafted | `core/11` §7: *"**Closed.** The judgment/escape seam that `core/09` left fused."* Landed, not owed | **Stale, and reached a shipped artifact.** Corrected at `a312a55` |
| 4 | The split, once landed, is landed flat | Implied by row 3's framing | `core/11` §7: *"**What this section does not close.** The intersection is sufficient for escape and is not necessary for it."* `DDD-dec-15` is the scope correction; `DDD-floor-01` is the re-scoped claim | **The correction over-corrects if taken flat.** Landed for capacity-generated escape only |
| 5 | The actor-encoding result is §5.1; the unification is §5.3 | Confirmed — the drafted section's own pointers | Live: §6.2 and §6.4. `core/09` carries ten numbered sections since 2026-08-14 | **Stale.** Adapted on insertion; every inherited `§` pointer needs checking |
| 6 | Capacity-generated escape stated as necessary-and-sufficient | Inferred — the v4.4 shape | `core/09` §6.4, live: *"The point at which `H(verdict\|X)` exceeds effective capacity is where demand begins to escape"* — necessary-and-sufficient in form, and predating `DDD-dec-15` | **Stale, and live in a shipped artifact.** Listed, not fixed — `§§1–7` are out of this session's scope |
| 7 | `escape = overflow ∩ open`, unqualified | Inferred — the v4.4 shape | `core/README.md` line 23, live: *"**11 — the floor mechanism** · escape = overflow ∩ open"*, with no sufficient-not-necessary qualifier | **Stale in form, and live in a shipped artifact.** An index gloss rather than a claim, but it is the repository's front door. Listed, not fixed |
| 8 | `p_err` is an assumed logistic | Unconfirmed | `core/11` §4.1: *"An earlier version of this document assumed a logistic for `p_err`. It is instead **derived**"*; `meta/consolidated-state.md`: *"**CLOSED (v4.2)**"* | **Settled since.** Substituting the derived bound changed every number and no structural claim |
| 9 | "A better decomposition destroys demand" | Unconfirmed | `DDD-measure-08`, status `retired`, superseded by `DDD-measure-03`; `core/09` §4 states the correction | **Settled since.** The claim is retired, never deleted |
| 10 | The counting-procedure debt is outstanding | Unconfirmed | `core/09` header: *"This note supplies the procedure, for closing predicates, and shows the invariance is a theorem rather than an observation"* | **Settled since**, for the closing region only |
| 11 | Measuring demand on open predicates is an outstanding debt | Unconfirmed | `core/11` §7: *"**Not open — a boundary.** … **This is the framework's stated limit, not an unpaid debt**"* | **Reclassified.** It must not appear on any ledger as unpaid work |
| 12 | Paper A §6 is gated on evidence campaigns E1–E4 | Unconfirmed | `meta/consolidated-state.md` §5: the selection/training ratio is *"falsifiable from existing literature — which **unblocks Paper A §6**"* | **Settled since.** Unblocked |

## What reached shipped artifacts

Emil's standing instruction was to list these and not fix them. Three, one of which is already
repaired.

| Site | Status |
|---|---|
| `core/09` §8, the rate–distortion paragraph | **Repaired** at `a312a55`, at the gate, under ruling 1 as amended |
| `core/09` §6.4 | **Live.** Reads as necessary-and-sufficient; predates `DDD-dec-15`. Out of scope this session |
| `core/README.md` line 23 | **Live.** Unqualified index gloss of the escape mechanism. Out of scope this session |

So the v4.4 shape survived in **two places still standing**, not one. Neither was found by reading
the draft carefully. Both were found by reading the referent, which is the whole finding.

## What a complete sweep still needs

1. The old `measure-paper-context.md`, so rows 8–12 can be confirmed or struck and so any phrase not
   represented above can be caught.
2. A decision on the two live sites. Both are `§§1–7` or `core/README.md`, and both were held out of
   scope deliberately; neither is repaired by this session.
3. A pass over any other artifact drafted against the v4.4 context. The related-work section was the
   known case, and it was not the only one.
