# Changelog — actor-indexed-determination

This repository starts a fresh changelog at the split. The combined `decision-driven-design` corpus's
history stays with the software-projection repository; the claim graph carries the epistemics
regardless of git lineage.

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
