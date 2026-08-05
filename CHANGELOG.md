# Changelog — actor-indexed-determination

This repository starts a fresh changelog at the split. The combined `decision-driven-design` corpus's
history stays with the software-projection repository; the claim graph carries the epistemics
regardless of git lineage.

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
