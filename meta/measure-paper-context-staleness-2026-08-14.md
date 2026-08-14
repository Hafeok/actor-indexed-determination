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

## Scope, and how it was closed

The first pass of this audit ran without the old `measure-paper-context.md`, which lives in the
measure-paper project and is not readable from this repository. Five rows stood unconfirmed:
real movement in canon whose presence in the old file could not be checked.

**Emil supplied the file's relevant lines at the Gate 2 clearance, and every unconfirmed row is now
settled.** The provenance column records how: *confirmed* against a quoted line, *absent* where the
old file carried no corresponding claim.

One limit remains, and it is narrower than the first. The file was read into this session in
extracts, not in full, so a forward-looking phrase not represented in those extracts would not appear
below. The extracts covered the header, caveat 3, the related-work section, the counting-debt line,
the closure line, the Paper A line, and the OPEN list — which is the whole of the file's
forward-looking surface as far as this audit can tell.

## The table

| # | Phrase as carried | Provenance | Live canon says | Verdict |
|---|---|---|---|---|
| 1 | *"Canon source. Projection of `decision-driven-design` at v4.4, principally `core/08-the-measure.md`."* | **Confirmed** — the old header, verbatim | `meta/repo-topology.md` records the split; `meta/CANON-PATCH-REGISTER.md` filing note: *"read `core/08` as `core/09` (the measure) and `core/09` as `core/10` (the floor mechanism)"*; `core/README.md` lists `09 — the measure` | **Wrong in three ways at once.** Wrong repository — `decision-driven-design` is the dependent layer, not this paper's home. Wrong number — `core/08` is v4.3-era, pre-P3.1. Wrong location — pre-split. One header line, three deltas |
| 2 | "the companion framework derives an error floor from it" | **Confirmed** — carried into `core/09` §8 as drafted | `core/11` §4 is titled *"The soft-capacity bound"*; §4.1: *"`p_err` is derived, not assumed … rate-distortion theory"*. The derivation is in **this** repository, and it is one result, not two. "Error floor" appears nowhere in canon | **Stale, and reached a shipped artifact.** Corrected at `a312a55` |
| 3 | "the escape/judgement split named as this note's next result" | **Confirmed** — carried into `core/09` §8 as drafted | `core/11` §7: *"**Closed.** The judgment/escape seam that `core/09` left fused."* Landed, not owed | **Stale, and reached a shipped artifact.** Corrected at `a312a55` |
| 4 | The split, once landed, is landed flat | Implied by row 3's framing | `core/11` §7: *"**What this section does not close.** The intersection is sufficient for escape and is not necessary for it."* `DDD-dec-15` is the scope correction; `DDD-floor-01` is the re-scoped claim | **The correction over-corrects if taken flat.** Landed for capacity-generated escape only |
| 5 | The actor-encoding result is §5.1; the unification is §5.3 | **Confirmed** — the drafted section's own pointers | Live: §6.2 and §6.4. `core/09` carries ten numbered sections since 2026-08-14 | **Stale.** Adapted on insertion; every inherited `§` pointer needs checking |
| 6 | Old caveat 3: *"Escape is not separated from judgment … The floor lives in that split and it is not done. Named as the next result."* | **Confirmed** — the old file, verbatim. **This is where row 3 was inherited from** | `core/11` §7 books it under **Closed**, then bounds it: sufficient for escape, not necessary | **Stale at source.** The drafted paragraph did not invent the claim; it copied it faithfully from a context that had gone stale |
| 7 | Old related-work: rate–distortion as *"the natural home for the escape/judgment split when that result lands"* | **Confirmed** — the old file, verbatim. The second inheritance site | As row 6 | **Stale at source.** The result had landed |
| 8 | Old related-work: *"`core/09` derives `p_err = H_b⁻¹(1 − C/n)` from it."* | **Confirmed present** | `core/11` §4.1 derives it, as **`p_err = H_b⁻¹(1 − r)`, `r = C_resolve / n`** | **Two deltas in one line.** Wrong document — the derivation is `core/11` §4.1, not `core/09`. Wrong form — live canon names the rate `r = C_resolve/n`, distinguishing resolve capacity from hold capacity; the bare `C/n` predates that separation |
| 9 | *"A better decomposition destroys demand"* | **Absent** from the old file | `DDD-measure-08`, status `retired`, superseded by `DDD-measure-03`; `core/09` §4 states the correction | **Movement in canon, no corresponding claim in the old context.** Nothing to correct; recorded so the retirement is not re-imported by a later draft |
| 10 | Old file: *"pays the counting-procedure debt booked in `meta/lineage-and-limits.md` — 'until a counting procedure for governing decisions exists and is shown invariant across two architectures, conservation is an accounting identity, not a measured invariant.'"* | **Confirmed present** | `core/09` header carries the same quotation and the same answer: *"This note supplies the procedure, for closing predicates, and shows the invariance is a theorem rather than an observation"* | **No drift.** The old line and live canon agree, including the quoted debt |
| 11 | Old file: *"per v4.5, closes means operationally closed — the acceptance procedure can be executed over available ground within declared resource, latency and confidence bounds."* | **Confirmed present** | `term:closure`, live: *"A predicate is **closed for an arrangement** when the relevant ground is observable and adequacy can be evaluated within declared resource, latency, and confidence bounds. **Decidable** is reserved for the formal special case."* | **No drift.** Same three bounds, same operational-not-formal register. Live adds one refinement the old line lacks — `decidable` reserved for the formal special case — which sharpens rather than moves it |
| 12 | Paper A §6 gated on evidence campaigns E1–E4 | **Absent** from the old file | `meta/consolidated-state.md` §5: the selection/training ratio is *"falsifiable from existing literature — which **unblocks Paper A §6**"* | **Movement in canon, no corresponding claim in the old context** |

## The old file's OPEN list, settled against live canon

Five items, each a forward-looking phrase by construction. Same format.

| # | Old OPEN item | Live canon says | Verdict |
|---|---|---|---|
| O1 | Whether the RAG instance is claimed as evidence | `DDD-measure-05`, `region:` *"simulation only; a tractability result, **not evidence of conservation**"*; its asset note: *"answer generated independently of retrieval, so closer to construction than measurement — never present as conservation in the wild"* | **Settled: no.** Canon refuses the claim explicitly. But see the standing flag below — `core/09` §6.3's prose does not yet match |
| O2 | Chained seams before submission | `core/09` §9 caveat 3: *"chained seams, multi-actor compositions, and non-uniform ground should still be worked before publication"*; `core/06` line 185 names them *"exactly the cases still owed a worked instance"* | **Still open, unchanged.** The one item on the old list that moved not at all |
| O3 | The correspondence campaign — protocol or run? | `DDD-measure-07`, status `projected`, `evidence: []`, with a named falsifier and `breaks: DDD-measure-01 — this is its falsifier run as a campaign`. `meta/repo-topology.md` files the correspondence's *life* — interface contract, `closesAt`, amortisation over `N` — with the ledger layer, outside this repository's charter | **Protocol, not run.** The falsifier is written and the evidence list is empty. Note the charter consequence: the campaign cannot be run from this repository |
| O4 | Where the escape/judgment split files | `core/11-the-floor-mechanism.md`, §§2–4 and §7 | **Settled.** It filed in `core/11`, and it filed *partially* — capacity-generated escape only, per `DDD-dec-15` |
| O5 | The information-theorist certification | `core/09` §9 caveat 3: *"an information theorist should certify the framing"*; `core/11` §7: *"The toys are demonstrations, not certification — an outside reviewer should check the identification, as with `core/09`"* | **Still open, and now owed twice.** `core/11` inherited the same debt |

## What reached shipped artifacts

Emil's standing instruction was to list these and not fix them. Rows 6 and 7 above are their origin:
the drafted paragraph did not invent the v4.4 shape, it copied it faithfully.

| Site | Status |
|---|---|
| `core/09` §8, the rate–distortion paragraph | **Repaired** at `a312a55`, at the gate, under ruling 1 as amended |
| `core/09` §6.4 | **Live.** Reads as necessary-and-sufficient; predates `DDD-dec-15`. Out of scope this session |
| `core/README.md` line 23 | **Live.** Unqualified index gloss of the escape mechanism. Out of scope this session |

So the v4.4 shape survives in **two places still standing**, not one. Neither was found by reading
the draft carefully. Both were found by reading the referent, which is the whole finding.

**A third divergence, already flagged by the repository's own mechanism and not a product of this
audit.** `DDD-measure-05`'s `notes:` records that `core/09` §6.3 presents the RAG run as
*"conservation of specification demand, measured on a deployed system pattern rather than a toy"*,
which overstates the claim's own region. The claim keeps the honest form and the prose is the bug,
flagged for Emil review. It bears on O1 and it is `§§1–7` content, so it is listed here and not
touched.

## What remains

1. **Three live sites, all canon content edits.** `core/09` §6.4, `core/README.md` line 23, and the
   `DDD-measure-05`/§6.3 tension. Each needs its own gated session; none is repaired here.
2. **O2 and O5** — the worked-example gap and the outside certification. Both are genuine standing
   debts, not staleness.
3. **A pass over any other artifact drafted against the v4.4 context.** The related-work section was
   the known case, and the audit has not established that it was the only one.
