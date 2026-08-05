# Contributing

This is the **principle repository** — the actor-general core. It benefits from contact with other
people's domains, and from adversarial review of the load-bearing claims.

**Where issues go.** Falsification of a **core claim** — the floor, selection-vs-training, the
measure, conservation — belongs **here**, as an issue against `core/`. Domain **projections** —
applying the principle to software or any other domain and finding where it bends — belong in the
software-projection repository, not here: the stable layer does not track its dependents.

## What is most useful here

- **Falsification.** The load-bearing claims are meant to be falsifiable. If you can exhibit an open
  predicate whose performance is nonetheless reliably assessable, or a closing predicate where
  path-degeneracy fails, you have broken `core/03` and `core/07`. Say so, in an issue.
- **Counterexamples to conservation.** The principle holds only *within a fixed decomposition*. A case
  where it fails even there matters.
- **Prior art we missed.** The framework is a synthesis and credits its ancestors
  (`meta/lineage-and-limits.md`). If we are reinventing something uncredited, name it.

## What the framework will not do

- Claim physical-law status without a measurable quantity.
- Group opposite error directions under one "mechanism" (the apophenia the review correctly flagged).
- Assert intelligence where the acceptance predicate does not close, or deny it there either — the
  framework declines that ruling on purpose.

## Discipline

Corrections propagate. A change to a `core/` claim must be reflected in `meta/consolidated-state.md`,
the authoritative status document, and the graph must stay valid: `validate-core-order.py core/`
(exit 0, zero W4) and `validate-claims.py core/claims/` gate every push. Where documents conflict,
`core/` wins, and `consolidated-state` records the resolution. Every canon-changing commit cites its
basis (`Basis:` line) — see `CLAUDE.md`.
