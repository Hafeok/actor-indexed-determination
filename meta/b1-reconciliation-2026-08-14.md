# B1 reconciliation — the actor-capacity blocker, checked against live `core/11`

| Field | Value |
|---|---|
| **Kind** | Evidence about a holding note. **Not canon**, and not an amendment to the note |
| **Source of truth** | `Hafeok/actor-indexed-determination` at `3ae3ddc` |
| **Filed** | 2026-08-14, Gate 3 of the related-work gate-pass session |
| **Consumer** | The corpus-test session, queued next, which consumes the ruling-16 evidence |

**Provenance limit, stated first.** The holding note (revision 8) is in Emil's hands and was not
readable from this session. B1's booking — *"the actor-capacity model, unratified, blocked behind
§11a–e"* — and the fact that the note's §13 leans on that shape are taken from the session prompt,
not from the note. What §11a–e are, and whether they cleared, cannot be checked here. Everything
below is what **live canon** says about the capacity model's status; the note is not amended, and
Emil holds the pen on it.

---

## 1. What is landed

The actor-capacity model is not unratified. It is settled canon, and has been since v5.4.

| Object | Where | Status |
|---|---|---|
| `term:capacity` — hold and resolve capacity, in bits | `core/11` §2 | **settled** |
| `term:overflow` — hold-overflow and resolve-overflow | `core/11` §2 | **settled** |
| `term:escape-mechanism` — overflow ∩ open | `core/11` §3 | **settled** |
| `term:p-err` — the soft-capacity bound | `core/11` §4.1 | **settled** |
| `DDD-floor-01` — the cleaving claim itself | `core/11` | **reported**, changed v5.4 |

Both assets reproduce. `core/assets/floor-mechanism.py` regenerates §3's hard-capacity table exactly;
`core/assets/perr-rate-distortion.py` regenerates §4's limits. Re-run on 2026-08-13 and again on
2026-08-14.

**`DDD-floor-01`'s own notes diagnose B1's booking, in canon's voice:**

> *"Restatused projected → reported in the verification pass: the seed, drafted from projections
> pinned at v4.4/v4.5, treated the actor-capacity model as future work, but live canon supplies it —
> `core/11` derives and demonstrates it, and both assets reproduce."*

That is the same failure this session's staleness audit documents elsewhere: **a forward-looking
phrase pinned to a v4.4/v4.5 projection, outliving the work it was waiting on.** B1 as booked is a
third instance of it. The blocker cleared; the booking did not.

## 2. What remains open

Three things, and none of them is ratification of the capacity model.

**2.1 The non-capacity remainder — open by ruling, not blocked behind anything.** `core/11` §7 states
the limit in its own words: *"The intersection is sufficient for escape and is not necessary for
it."* `DDD-dec-15` is the scope correction of 2026-08-13; `DDD-floor-01` is the re-scoped claim, and
its `region:` now reads *"Capacity-generated escape only … Escape arising where no supplier took the
governing decision up at all is outside this claim's region."*

This remainder is **outside** the capacity model, not downstream of it. Nothing about ratifying
`core/11` further would close it, because it is not the kind of thing `core/11` is about.

**2.2 Real-actor calibration.** `C_resolve` and `C_hold` are given constants. `core/11` §7: deriving
them from actor architecture is *"an empirical calibration problem, not a proof"* — construct tasks
of known bit-demand, find where error departs from zero. Nobody has published the measurement. **This
needs a rig, not a ruling.**

**2.3 The formal write-up.** `DDD-floor-01`'s `region:` books it: *"The formal write-up (paper-3) and
any real-actor calibration remain open."* `owner: paper-3`.

**Two flags already standing on `DDD-floor-01`, both bearing on the corpus session:**

- **The open conjunct is actor-indexed.** Flagged by Emil at GATE 2 and carried forward: *"no verifier
  **the actor holds**" … is ill-defined where no actor was assigned to the decision at all.* The
  capacity account's second conjunct does not merely fail on the membership cases — it does not parse
  on them.
- **The empty-option-set generator is unexamined.** `UNVERIFIED — Emil review`: whether an empty
  closing set is a third route to unsupplied determination, or an instance of the
  no-applicable-source route, is open.

## 3. B1's residual, restated

B1 books one blocker. Live canon holds three open items with three different dispositions, and the
booking's shape — *unratified, blocked behind* — fits none of them.

| B1 as booked | What it actually is |
|---|---|
| The actor-capacity model is unratified | **Discharged.** Four settled terms, one reported claim, two reproducing assets |
| Blocked behind §11a–e | **Not checkable here**, and moot for ratification — the model is landed regardless of what §11a–e resolved |
| — | **Open (empirical):** real-actor calibration of `C_hold` and `C_resolve`. A rig problem |
| — | **Open (exposition):** the formal write-up, `owner: paper-3` |
| — | **Open (scope):** the non-capacity escape remainder — outside the model by ruling, not behind it |

Anything in the note's §13 that leans on *"unratified"* leans on a cleared blocker. Anything that
leans on *"blocked behind"* treats a scope boundary as a dependency. Those are different repairs, and
they are Emil's to make.

## 4. A count discrepancy, flagged not repaired

Canon states the instance count two ways, and the claim governs the prose.

- **`DDD-floor-01` notes — five instances of ratified canon:** `05` §7's tower, `05` §8's unqualified
  declarer, `06`'s unanticipated situation at an encoded seam, `10` §9's claim layer, **and `11` §6's
  own Missing row** — plus a sixth, non-canon instance, the ground-applicability holding note's Q4
  limb 1.
- **`core/11` §7 prose — four.** It omits `11` §6's own Missing row.

The claim file is canon authority, so the count is **five**. The prose in `core/11` §7 is the bug,
and per the repository's standing rule it is flagged here rather than silently harmonised. The corpus
session should work from five.

## 5. What the corpus-test session should read differently

**Canon now separates two accounts of escape**, and the separation is ratified rather than
conjectural:

- a **capacity-shaped** account — demand an actor took up, exceeded its budget, and shed with no
  verifier to catch it;
- a **membership-shaped** account — a governing decision no supplier took up at all, escaped because
  `term:escape` is stated over supply generally and `term:store` admits no fifth source.

Five things follow for the escape-adjacent specimens.

1. **Read every escape-adjacent specimen against both accounts, and record both verdicts.** The live
   question is whether the budget account and the membership account classify the same specimen the
   same way. Canon has already ruled that they come apart — on five instances.
2. **Report the instances. Do not rule on the accounts.** `DDD-dec-15` settled the scope; it did not
   settle which account is primary, and this session has no standing to.
3. **Expect the capacity account to be undefined, not merely false, on some specimens.** The open
   conjunct is actor-indexed, and where no actor was assigned there is no actor whose verifier
   holdings can be asked about. A specimen that will not classify is a datum, not a coding failure —
   record it as undefined rather than forcing it.
4. **Do not read an absence of counter-instances as a demonstration.** `DDD-floor-01` is explicit that
   limb two of its falsifier — escape on decisions with a held verifier — did not fire on the previous
   corpus, that this is *"an absence of counter-instances, not a demonstration"*, and that no necessity
   claim is filed on it. The same discipline applies to whatever the new corpus does not turn up.
5. **The empty-option-set generator is unexamined and may be a third route.** If a specimen looks like
   an empty closing set rather than either account, flag it against `DDD-floor-01`'s standing
   `UNVERIFIED` note rather than assigning it to the nearer of the two.
