# CLAUDE.md

Guidance for agents working in the `actor-indexed-determination` (principle) repository.

## What this repo is

The framework is a **claim graph**, not a set of documents. Files are a storage format; the graph is
the object. This is the **stable, actor-general layer** of the split: it holds the canonical claims
and terms that the software-projection repository pins remotely. Per the Stable Dependency Principle,
**this repository carries no reference to its dependents** — do not add references to the software
projection, its apparatus, or its applications anywhere under `core/`.

Read `core/README.md`, then, before changing any claim or converting any prose:

- `spec/claim-format.md` — the claim schema (format 1) and its validation rules.
- `spec/claim-format-2-addendum.md` — the additive fields (`canonical_md`, `canonical_home`) that let
  a claim serve as an embed source; all format-1 claims remain valid unchanged.
- `core/graph/terms.yaml` — the canonical term registry. Every term a doc `establishes` has an entry
  here; edit canonical text **here**, never in the doc, and re-project.

## Working on canon

**The repo is ground truth, always.** Verify against the live repo before landing anything in
`core/`; never carry a claim's statement, status, or evidence on the confidence of prose, and where
evidence is executable, verify against a fresh run of the asset. Computations that back a reported
claim live in `core/assets/` and must reproduce — a claim whose computation fails demotes until fixed.

- **Canon authority lives in the claim files and the term registry.** For a converted document,
  `core/claims/*.yaml` and `core/graph/terms.yaml` govern; the prose is their exposition. Prose that
  contradicts its claim is a bug in the prose — flag it in the claim's `notes:`, do not silently
  harmonise.
- **The reading order is the dependency order.** Each doc's `ddd:contract` declares what it requires
  and establishes; every edge must point backward. A forward edge is an escaped seam.
- **Never present an identity holding as evidence for the framework.** State which is arithmetic and
  which is a modelling claim, always.
- **Flag, don't guess.** Reasoning not confirmed by canon or a named principal is marked
  (`UNVERIFIED — Emil review`), never asserted.
- **Validate before commit.** All three must pass:
  - `python3 validate-core-order.py core/` — exit 0, zero W4
  - `python3 scripts/validate-claims.py core/claims/`
  - for any decisions, `python3 scripts/validate-claims.py core/decisions/ --decisions`

## Cite claim IDs in commit messages

**Every commit that changes canon must cite the claim or term IDs it rests on**, as a `Basis:` line
(e.g. `Basis: DDD-frame-01; term:closure`). This is `DDD-agent-01` applied to this repo's own agents:
long-running agent drift is **escaped decisions caused by basis loss** — context decay removes claim
nodes from the agent's ground, so later edits revert to model priors with no `basedOn` edge. The
remedy is **basis as query, not context residue**: fetch the governing claim from `core/claims/` and
cite it. An edit to `core/` whose commit message names no basis is, by this repo's own ontology, a
candidate escaped decision about the framework itself.

Retired claims are never deleted — they stay in the graph with the correction that killed them
(`core/claims/DDD-measure-08.yaml` is the exemplar). IDs are never reused; renumbering is forbidden.
