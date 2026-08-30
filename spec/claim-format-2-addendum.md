# Claim format — additive extensions in force, and the format-2 bump they do not need

**Status of this file, stated because its title used to say something else.** Everything here is
**in force now**, enforced by `validate-core-order.py` and `scripts/validate-claims.py`, and every
claim in both repositories still declares `format: 1` — validly, because each addition below is
*additive*: an optional field, or a rule whose hit list against the existing corpus is empty. No
format-1 claim needs an edit to remain valid, so none has had one.

This file previously called itself *"proposed format 2"* while its first two fields were already
being enforced on 62 embedded blocks. The self-description was inconsistent with the practice, and
it is the description that was wrong.

**What would need the bump, and does not exist yet.** A format version is owed when a change is not
additive — when it removes a value from a field's range, changes what an existing field means, or
makes an unchanged claim file invalid. The first such change already has a name: the `lifecycle`
field booked under `DDD-dec-32`, which removes `retired` from `status`'s range and thereby changes
what every unchanged claim file says to every unchanged reader. **Format 2 is reserved for it.**
Spending a format version on changes that break nothing would leave the real migration without a
number to arrive under.

---

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

## Falsifier presence at every live status — a rule altered

Rule 2 of `spec/claim-format.md` states the falsifier condition for `projected` and is
silent for `reported` and `established`. Under this addendum it holds for every live
status:

> A claim at `projected`, `reported` or `established` carries a `falsifier`, or — for
> `conceptual` and `normative` kinds — a `test`. `retired` claims are exempt: a retired
> claim's statement is a retirement record and has no falsifier.

**Migration note: all format-1 claims satisfy it unchanged.** The hit list against the
corpus at `v5.10.0` is empty — 0 of 89 claims across both repositories.

**Why it is worth a rule.** `DDD-measure-06` sat at `established` from v4.5 to v5.9 with
no stated observation that would fire against it. That was legal: rule 2 required a
falsifier for `projected` and said nothing for `established`, so the strongest status
canon offers carried the weakest evidential requirement. The node was eventually found by
an external reader working through the argument; **the repository could have found it by
reading the file.**

**A definition's falsifier is its `test`, and that is not an exemption.** §1 gives `test`
to `conceptual` and `normative` kinds and names its three forms — counterexamples, coding
reliability, explanatory utility. Those are the three ways a definition fails: it carves
the wrong joint, it cannot be applied consistently, or it earns nothing. Sixteen of the
twenty-nine `conceptual`/`projected` claims are definitions, and all four claims carrying
a `test` and no `falsifier` are among them (`DDD-dec-31`). The substitution is available
to the kinds the spec gives `test` to, and to no others.

**The strict reading is not adopted here.** That every claim carries a `falsifier`, with
no near-definitional exception, is ruled — and it fires on seven claims that must each be
written with a ruling. It ships as a warning until they are, and the ruling that lands the
last of them is the one that promotes it.


## Audience denomination — `denominations:`

One optional field on a **terms-registry** entry, recording what a named audience calls the same
object. Additive: an entry without it is unchanged and valid.

```yaml
- id: term:verdict
  term: verdict
  denominations:
    - audience: engineering
      name: specification demand
      note: the measure is identical either way
```

**The rule it files.** **Canon is the naming authority. A projection denominates for its audience,
and the denomination is recorded on the term rather than invented downstream.** A projection may
render `denominations:` for its audience; it may not mint a name canon does not carry.

**Why a field and not a parenthetical.** Canon has practised this in exactly one place and never
named it as a rule: `term:verdict`'s canonical text carried *"(in the engineering projection this
same quantity is denominated in the vocabulary of the domain and called* **specification demand***)"*.
Carrying it inline has three costs, and the third is the one that bites:

1. **It is unreadable to a projection.** A generator cannot extract a name from prose, so every
   downstream rendering re-authors the denomination — which is exactly the mint canon forbids.
2. **It taxes every reader for one audience's benefit.** The parenthetical interrupts a definition
   for readers who are not that audience.
3. **It puts a load-bearing word inside canonical text for a second purpose.** The parenthetical is
   where `projection` does denomination duty inside a settled entry, while `term:projection` names
   an axis of the compound. **Moving the denomination out is the cheapest available repair of that
   collision** — cheaper than renaming either object.

**This is the same shape as two defects already ruled**: Paper A's appendix rendering `id | status |
statement` and no `kind` when the graph had carried `kind` since format 1, and
`spec/claim-format.md` §5's status semantics living in a projection rather than in the schema. **The
projection carrying what the schema should say** is the repeating error; a field is the repair.

**No validator check is proposed.** `denominations:` is inert data with no consistency condition a
checker could evaluate — a name is right or wrong by ruling, not by rule. The instrument here is the
field plus the review discipline, as with `canonical_home`.

**First and only instance at filing:** `term:verdict`. The primer is the first projection that will
need the field at scale, and it is the second consumer that made it worth filing now rather than
with the primer.
