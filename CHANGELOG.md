# Changelog — actor-indexed-determination

This repository starts a fresh changelog at the split. The combined `decision-driven-design` corpus's
history stays with the software-projection repository; the claim graph carries the epistemics
regardless of git lineage.

## v5.5.0 — vocabulary and delivery: the ground and delivery areas

Two corpus-earned areas land. The **ground** area names what a determination stands on — the
applicability gate, orthogonal coverage/resolution/assurance typing, the `—(open)` timing value,
and retro-filing's two fields. The **delivery** area names what leaves the act: filing is not
encoding, undelivered supply is an escape generator, and judgement-mediated delivery on both the
source and assurance sides compounds rather than stacks. Carried through four review gates, with
rulings applied between passes. Decision filed as `DDD-dec-17`; release descriptor at
`releases/v5.5.0.yaml`.

### Added
- `core/13-delivery.md` — the delivery area, establishing `term:delivery`, `term:undelivered`
  and `term:presumed-discharge`.
- `core/claims/DDD-ground-01..04` — the ground claims, including retro-filing's two fields
  (`DDD-ground-04`).
- `core/claims/DDD-delivery-01..03` — the delivery claims.
- `core/decisions/DDD-dec-17.yaml` — the decision filed across the gate passes, extended by the
  GATE 4 rulings.
- Three delivery terms in the canonical registry.

### Changed
- `core/09-the-measure.md` — the ground area's exposition.
- `core/claims/DDD-cost-09.yaml` — region gains the per-act-site qualifier by scope extension:
  assurance-by-check is supplied standing at act-sites where the check is act-triggered; the same
  check actor-triggered elsewhere is judgement-mediated supply with its own failure modes.
- `core/claims/DDD-cost-08.yaml` — notes gain the compounding cross-reference: where the gate and
  the decision both reach the act judgement-mediated, the failures correlate.
- `core/00-primitives.md`, `core/06-composition.md`, `core/claims/DDD-measure-01/11/12` — wording
  aligned to the landed vocabulary.

## v5.4.0 — the escape scope correction

Three holding notes independently reported canon's escape definition as too narrow. Tested against
the repository, that report rested on an error: `term:escape` is stated over supply generally and
`term:store` admits no fifth source, so the definition is not capacity-indexed and is not amended.
What was too narrow sat one level down — the **mechanism** asserted a capacity condition as
*necessary* for a category the definition indexes on supply alone. `DDD-floor-01`'s own filed
falsifier named the observation that fires it, and it fired on five instances of ratified canon.
Filed by supersession, not rewriting, per the Wave-1 precedent. Decision filed as `DDD-dec-15`.

### Changed
- `term:escape-mechanism` re-scoped in `core/graph/terms.yaml` and re-projected into `core/11` §3:
  scoped to **capacity-generated** escape, declared sufficient and never necessary, with the
  open-alone disjunct corrected to require a named accountable supplier.
- `core/claims/DDD-floor-01.yaml` — statement re-scoped, region tightened to capacity-generated
  escape, falsifier re-scoped to shed demand. Status retained at `reported`: the assets support
  the re-scoped claim in full, and the generality removed is the generality they never evidenced.
- `core/claims/DDD-cost-05.yaml` — statement amended to the denominational reading; region gains
  the scope.
- `core/claims/DDD-cost-08.yaml` — breaks field, which had named the defective clause as the thing
  that survives.
- `core/11-the-floor-mechanism.md` §§6–8, `core/05-accountability.md` §6, `core/10-cost.md` §5 —
  prose corrected where it carried the superseded quantifier.
- `meta/lineage-and-limits.md` — the register sentence, the framework's own novelty statement,
  which had claimed the identification *of escape* with the intersection. Corrected to
  capacity-generated escape: a false originality claim is the most expensive kind, which is why
  this one file outside `core/` was in scope.

### Added
- `core/decisions/DDD-dec-15.yaml` — the scope correction, with the superseded quantifier recorded
  rather than erased.

### Not changed, deliberately
- `core/claims/DDD-frame-04.yaml` — its "no adequate source-and-assurance combination" was already
  supply-general; the inconsistency dated from v4.4 and resolves in its favour.
- No new claim is minted for escape as the general condition: `term:escape`, `term:store`,
  `term:exhaustiveness` and `DDD-frame-04` already carry it.

## v5.3.0 — Wave 2 curation: the assurance and capability layers

The register ruling (R3, `DDD-dec-12`): a synchronic, actor-general claim evidenced in a single
domain files here at `projected` with the single-domain basis flagged; evidence instances file
where their evidence lives. Diachronic claims stay outside R3's scope and file by layer per the
boundary charter. Applied across the Wave 2 curation, which landed the assurance economics and the
capability typing.

### Added
- `core/claims/DDD-cost-08.yaml` — actor selection is two-gated: capacity always, assurance exactly
  where the acceptance predicate does not close.
- `core/claims/DDD-cost-09.yaml` — closure converts a property's assurance supply from occasioned
  to standing.
- `core/claims/DDD-cost-11.yaml` — the sign flip: closing the predicate reverses the
  assurance–class coupling, bounded by coverage.
- `core/claims/DDD-cost-12.yaml` — required class is the max over the act's capabilities where
  assurance is not discharged.
- `core/claims/DDD-cost-13.yaml` — answer-keyed instruments evidence declared-predicate class only,
  never open carriage.
- `core/claims/DDD-cost-20.yaml` — around/within: encoding loci differ; training buys allocation,
  not capacity.
- `core/claims/DDD-cost-22.yaml` — the claim layer is governed by the same two gates.
- `core/claims/DDD-cost-25.yaml` — tempo prunes assurance positions: latency over budget forces
  assurance pre-act.
- `core/claims/DDD-frame-11.yaml`, `DDD-frame-12.yaml` — the frame claims the wave earned.
- `core/decisions/DDD-dec-12.yaml` — the register ruling (R3), with R4b recorded alongside.
- `term:capability` in the canonical registry.

### Changed
- `core/10-cost.md` — §§6–9 built out: the two gates, capability typing, around/within, the claim
  layer.
- `core/09-the-measure.md`, `core/06-composition.md` — exposition aligned to the landed claims.

## v5.2.0 — the boundary charter applied to cost

The boundary charter (R4, Emil 2026-08-09): the principle layer is synchronic and stateless —
one actor, one act, four stores; any statement requiring anything to persist between acts files
with the projection. Applied to the cost layer by supersession of the Wave-1 co-location plan —
a basis update, not a defect. Decision filed as `DDD-dec-09`.

### Changed
- `core/10-cost.md` carved to the per-act layer: the register split (`DDD-cost-01`, whole), the
  degeneracy's per-act core (flat tradeoff, density 1, conservation-forced), and the rate-split
  (description length prices the standing side, entropy the occasioned side) with the per-act
  occasioned-floor falsifier. Act volume, crossover volumes `N*`, and the `N`-denominated MDL
  total relocate with the projection layer.
- `core/claims/DDD-cost-02.yaml`, `DDD-cost-03.yaml` — statements re-cut to the per-act cores;
  the volume halves file with the projection as new claims citing these IDs as basis.
- `core/assets/measure-mdl-demo.py` trimmed to the per-act demonstrations: frontier, densities
  (all 1.000 under information pricing), separation under description-length pricing, residual
  floor. Volume sweeps relocate with the projection layer.

### Removed (relocated, IDs intact)
- `core/claims/DDD-cost-04.yaml` — the actor-table regime reading quantifies over act volume;
  relocated whole per `DDD-dec-09`. Claims relocate, never renumber; the ID is not reused.
- Term `act-volume` — no upstream statement may quantify over it under the charter.

### Added
- `core/decisions/DDD-dec-09.yaml` — the boundary charter applied to cost by supersession;
  records the relocation map.

## v5.1.0 — the act as unit of account; the cost register

The act reclaimed as the bounded episode of determination — derived, composed of the two
primitives, never a third — and the cost layer landed as its own core file. Ratified by Emil in
the act-primitive session (2026-08-08); decision filed as `DDD-dec-08`.

### Added
- `core/10-cost.md` — the cost register: standing vs occasioned supply denominated per act; the
  degeneracy result (information-linear standing cost is crossover-degenerate, so a graded
  build-out requires description-length pricing); the MDL correspondence, projected, with its two
  discriminating falsifiers; capacity/escape per act named as the next result.
- `core/claims/DDD-cost-01..05` — the cost claims, statuses as filed (02 reported as arithmetic,
  the rest projected).
- `core/decisions/DDD-dec-08.yaml` — the first decision filed in the principle repo (dec-01..07
  stayed with the software projection at the split).
- `core/assets/measure-mdl-demo.py` — reproduces the degeneracy and the graded build-out.
- `meta/mdl-cost-manufacturing-assessment-2026-08-08.md` — empirical basis, filed as basis not
  claims.
- Terms: `act` (00, canonical), `act-individuation` (09, canonical); `cost-register`,
  `standing-cost`, `occasioned-cost`, `act-volume` (10, registry-only).

### Changed
- `core/00-primitives.md` §1 — headline sharpened to "There is no act beneath the decisions";
  the reclamation added after the collapse (the act as unit, not floor); §2 notes the act is
  composed of the two primitives. The collapse argument itself stands verbatim.
- `core/09-the-measure.md` §1 — every quantity restated as per-act; the prior N=1 assumption
  exposed; act individuation filed where the predicate's measure exists (one act = one verdict).

### Renumbered
- `core/10..11` shift to `core/11..12` to seat cost directly after the measure. Live references
  swept; dated archival records keep their as-written numbering.

## v5.0.0 — the split

The actor-general principle layer, extracted into its own repository as the execution of `DDD-dec-04`.
Branched fresh from the combined corpus at commit `10f6ba6`. No claim's **status** changed in the
split; this is a relocation and a reordering, not a revision.

**Contents.** `core/00`–`core/11` (the reordered core), the canonical term registry
(`core/graph/terms.yaml`), the principle's claim set (`DDD-frame-*`, `DDD-measure-*`, `DDD-floor-01`,
`DDD-agent-01`), the reproduction assets, `meta/lineage-and-limits.md`, the canon patch register, the
principle's consolidated state, the claim-format schema, and the core-order + claim validators.

**The core reorder** (applied as part of the split, per `core-contracts.md`):

- New **`00-primitives.md`** — determination, the two primitives, the admission tests, minimal actor
  and arrangement, and the name. Sheds the four-stores restatement (01 is canonical), the ensemble and
  immune sections (→ `11`), and the funnel preview (08 owns it).
- New **`11-the-licensing-instance.md`** — ensemble actors, diversity vs. redundancy, the swarm gate,
  and the immune system as the licensing instance; legal only after `10` supplies capacity.
- `04` sheds its composite-actor/compound sections to `06`, now the canonical composition home; its
  duplicate floor statement reduces to a reference to `03`.
- `09` register fixed to *determination demand* (its engineering projection, *specification demand*,
  noted once).
- A `ddd:contract` block added to every document; the canonical term graph populated; the reading
  order made machine-checkable (`validate-core-order.py`, exit 0, zero W4).

Full detail: `migration-report.md`.
