# core/claims/

The claim graph as files: one YAML file per claim node, `DDD-<area>-<nn>.yaml`, each declaring
`format: 1` per `spec/claim-format.md` (or format 2, additively, for claims that serve as embed
sources). These files **are** the graph and grep is the query engine.

Canon authority for a converted claim lives here, not in the prose it was extracted from. Where a
`core/` document and its claim disagree, the disagreement is a bug in the prose — flagged in the
claim's `notes:`, not silently harmonised.

**Areas held here (the principle layer):** `measure`, `frame` (actor-indexed determination),
`floor`, `agent`. The software-projection areas — `tool`, `org`, `sim` — live with the projection
repository and pin this repo's claims where they depend on them. New areas are cheap; renumbering is
forbidden; retired claims keep their IDs (`DDD-measure-08` is the exemplar).

**Flags awaiting Emil review.** Claims whose `notes:` carry `UNVERIFIED` could not be confirmed from
repo contents — Paper A / foundation-revision material not yet in `core/` (`frame-01`, `frame-02`,
`frame-07`) or session-authored predictions (`agent-01`). They are flagged, never struck, and never
presented as canon.

**Validate:** `python3 scripts/validate-claims.py core/claims/`
