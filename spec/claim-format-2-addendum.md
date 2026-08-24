# Claim format — proposed format 2 (additive)

## Transclusion source — `canonical_home`, `canonical_md`

Two optional fields, enabling a claim to serve as the canonical source for a byte-exact
block embedded in a core document:

```yaml
canonical_home: 03-the-floor.md    # the ONE core doc allowed to embed this claim
canonical_md: |                    # the exact markdown block that doc must carry
  > **...**
```

**Migration note: all format-1 claims are valid unchanged.** A claim without
`canonical_md` simply does not participate in transclusion checking. This is a shape
change (two fields added), hence a format bump per the spec's own versioning rules —
not a content change.

Rationale: the repo already holds one YAML per claim under `core/claims/`; a parallel
claims registry would duplicate canon. The terms registry (`core/graph/terms.yaml`) is
new — terms had no prior home — but claims extend in place.
`validate-core-order.py` reads both sources.

## Retirement provenance — `retired_from`

One optional field, legal only on a claim whose `status` is `retired`, naming the maturity
the claim held immediately before it was retired:

```yaml
status: retired
retired_from: established | reported | projected | unrecoverable
```

**The defect it repairs.** `retired` is a lifecycle state occupying a maturity field. Once a
claim takes it, the field no longer distinguishes a claim that reached `established` and did
not survive from a young claim that was replaced — and that distinction is exactly what an
outside reader of a public registry needs. `DDD-measure-06` held `established` from v4.5 to
v5.9; nothing in its header says so.

**`unrecoverable` is a value, not a gap.** Where the prior maturity cannot be established from
the graph, from git, or from the seed and changelog, the field records that it was searched for
and not found. It is never inferred and never reconstructed: a recorded loss is a fact, and a
guessed status would read as authoritative. A claim taking `unrecoverable` states in `notes`
what was searched. `DDD-frame-09` and `DDD-measure-08` are the exemplars — both were already
`retired` in this repository's first commit, so their transitions predate the repository.

**Migration note: all format-1 claims are valid unchanged.** The field is optional, and a claim
that is not `retired` never carries it, so no live claim is touched — four files in total.

**Why this and not a lifecycle field.** The alternative, and the conceptually correct one, is a
`lifecycle: active | retired` field orthogonal to maturity, letting `status` keep the maturity
the claim actually held. It is booked as a format-2 candidate and deliberately not taken here.
The reason is a difference in kind rather than in size: `retired_from` is additive, so every
existing claim and every existing reader stays correct, whereas `lifecycle` removes a value
from `status`'s range and thereby changes what an unchanged claim file means to an unchanged
consumer. That is a format version's work, not an addendum's.
