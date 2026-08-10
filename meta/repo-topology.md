# The framework describes its own repository topology

**Location:** `meta/repo-topology.md`. Filed 2026-08-10 (Wave 2 curation, GATE A filings), from
the 2026-08-09 boundary-charter session; affirmed in session, formulations ratified at filing.
Meta, not core: this file names the programme's repositories, which `core/` may not (Stable
Dependency Principle — the stable layer carries no reference to its dependents).

---

## The split is a decomposition, and it has a seam

A repository split is a decomposition, so the composition result applies to it (`core/06`): the
split manufactured seam demand, and that demand had to be allocated. `graph/upstream.yaml` in
the dependent repository is the seam contract — the one-time specification that pays the seam
down — and the E12/E13/W5 checks are its mechanical verification. An encoded seam and a check on
what crosses it: the matched pair, exactly as `core/06` prescribes.

The 2026-08-09 boundary charter (`DDD-dec-09`; adopted downstream as `DDD-dec-10`) was a
high-information seam: heavy pre-payment into the boundary — the persistence test, the pin
discipline — buying two simpler parts. Decomposition B's pattern, applied to the repository
itself.

## SDP orders splits; the cost layer times them

A package earns separation when its stability diverges from its neighbours' and consumers want
to pin it independently. That is an N*-type decision — the crossover machinery of the ledger
layer applied to repository structure. **Do not split ahead of the crossover.**

The seam itself splits across the charter boundary: its arithmetic — the chain-rule identity,
the declared ground distribution — is synchronic and lives with the principle (`core/09`); its
life — choosing `S`, the interface contract, the `I(V;S)` ↔ interface-cost correspondence with
its `closesAt`, amortisation over `N` — persists between acts and lives with the ledger layer
(`decision-driven-design`).

## Standing consequences

- **R4b, ruled (a)** (Emil, 2026-08-10, Wave 2 GATE A; recorded as `DDD-dec-11` in
  `decision-driven-design`): DDD is the actor-general name of the ledger method; engineering is
  its home domain, not its boundary. The downstream repository is the canonical home of Layer 2
  as such. This repository stays silent on inter-act persistence beyond `DDD-dec-09`, which
  stands as its sole acknowledgment of the layer — no thin anchors.
- **Rider** (Emil, same ruling): `decision-driven-design` deliberately holds both Layer 2
  general canon and engineering instances. If their stability diverges, that is a future seam
  under this corollary — split at its crossover, not before.
- **First future split candidate:** the claim-format specification (`spec/claim-format.md`) —
  the interface between canon and all tooling, the most SDP-stable object in the system.
