# Migration report — actor-indexed-determination (principle repo)

Execution of the repo split (`DDD-dec-04..07`), principle-repo side. Branched fresh from
`decision-driven-design` at commit `10f6ba6` (branch `claude/repo-split-execution-j46b1q`). Work is
on branch `claude/repo-split-execution-j46b1q`; **nothing is merged** — this report is for Emil's
review before merge, per the kickoff.

## Validation gate — status

| Gate | Result |
|---|---|
| `validate-core-order.py core/` exit 0, zero W4 | **PASS** (0 errors, 0 W4; 100 warnings, all W1/W2/W3 dispositioned below) |
| Every `core/assets/*.py` reproduces its figures | **PASS** (5/5 reproduce; `measure-toy` → `H(verdict)=25.493 bits`, matching §3) |
| `grep -ri "decision-driven-design" core/` returns only the provenance note | **PASS** (core/ is clean; the provenance note lives in the root `README.md`, outside `core/` — the stable layer does not know its dependents) |
| Claim schema (`validate-claims.py core/claims/`) | **PASS** (25 claims valid) |
| No file in both repos except intentional forks | **PASS with classification** (see §7) |

Verbatim validator output is in §8.

## 1. Files moved into this repo (from decision-driven-design)

- **Core documents** `core/00`–`core/10` (reordered — see §2) and the **new** `core/11`.
- **Reproduction assets** `core/assets/`: `measure-toy.py`, `measure-actor-allocation.py`,
  `measure-rag.py`, `floor-mechanism.py`, `perr-rate-distortion.py`, `projections.svg`,
  `projections.html`.
- **Claim set** `core/claims/`: `DDD-frame-01..10`, `DDD-measure-01..13`, `DDD-floor-01`,
  `DDD-agent-01` (the actor-general areas). *Placement call — see §6.*
- **Meta canon**: `meta/lineage-and-limits.md`, `meta/CANON-PATCH-REGISTER.md`, and the principle's
  half of `meta/consolidated-state.md` (split; see §2).
- **Assets** `assets/conservation-principle.{html,svg}`; **glossary** `i18n/ordliste-dansk.md`
  (moved whole, per accepted ⚑).
- **Schema/tooling** `spec/claim-format.md`, `scripts/validate-claims.py` (forks; see §7);
  `validate-core-order.py` (from the migration bundle); `spec/claim-format-2-addendum.md`.

New in this repo: `README.md` (with the provenance note), `CLAUDE.md` (fork), `CHANGELOG.md` (fresh),
`CONTRIBUTING.md`, `core/graph/terms.yaml` (the term registry), `.github/workflows/validate.yml`.

## 2. Every edit beyond a pure move, with the ledger item that licensed it

The reorder followed `migration/core-contracts.md` (the reorder map and the "what old 00 loses"
ledger) and the kickoff's explicit edit list.

| Edit | Licence |
|---|---|
| **New `00-primitives.md`** (was `00-determination.md`). Removed §3 "four stores, restated"; removed §6 (ensemble) and §7 (immune) → doc 11; trimmed the funnel/maturation sentence in §5 (08 owns it); softened the preamble "demand is conserved" to a pointer to `01`. Added a `ddd:contract` block and a new §3 "Actor and arrangement, minimally". | core-contracts "what old 00 loses" ledger; contract-block instruction; accepted ⚑ item 5 (minimal actor/arrangement) |
| **New `11-the-licensing-instance.md`** — old 00 §6+§7, extracted verbatim, headings renumbered (6→1, 7→2), with a contract block and a one-line intro. | reorder map row "11 … from old 00 §6–§7"; accepted ⚑ item 8 (ensemble in 11) |
| **Closure-sense fix** in doc 11: "It closes the **encoded** store" → "It **rules out** the encoded store". core-contracts suggested "fills", but *fills* **inverts the meaning** (the passage says encoding is *unavailable*); "rules out" achieves the stated goal (kill the `closure` alias collision) without the error. | kickoff edit list ("closure-sense fix at old 00 line 160"); **deviation flagged** — see §5 |
| **`04-actors.md`**: excised §4 (Composite actors) **and** §5 (the compound) — both duplicated in `06` and both forward-referencing `06`'s seam/orchestrator terms — replaced with a pointer to `06`; reduced §2's duplicated floor statement to a `ddd:ref` to `03`/`term:floor`. `06` made the canonical composition home (its back-pointer to "04 §5" removed). | reorder map "04 minus §4 → 06"; core-contracts "reduce 04 §2 to a one-line backward reference". **Scope note in §5** (the map named §4; §5 had to follow to avoid genuine forward edges) |
| **`05` / `07` verdict rephrasings.** `07`: three colloquial "verdict" → "ruling" (the framework declining to rule), killing the alias collision. `05`: its two uses are `H(verdict)` — direct citations of `09`'s notation in a passage that explicitly defers to `09`; rephrasing the notation would misrepresent it, so left as legal citational pointers (W1, §4). | core-contracts 05/07 edit notes; the `05` handling is a **flagged reading** (§5) |
| **`09` register fix**: "specification demand" → "determination demand" throughout, with one parenthetical at the Definition noting the engineering-projection term. The parenthetical points at **no downstream path** (SDP). | accepted ⚑ item 1; package §2 (core/09) |
| **`ddd:contract` block** prepended to every doc `01`–`10` (and authored for `00`/`11`). Multi-line `establishes`/`requires` normalised to single lines — the validator's parser is line-based and silently drops wrapped continuation lines. | step 4 (contract blocks); **tooling note in §5** |
| **`core/graph/terms.yaml`** populated: one entry per establishes-term (52 terms), `established_by` matching each doc. Five terms embedded byte-exact (`term:floor`, `term:closure`, `term:seam-identity`, `term:conservation`, `term:determination-intelligence-separation`) with `ddd:embed` markers. | step 4 (populate graph to zero W4) |
| **SDP path-stripping**: removed dangling `apparatus/…` and `applications/sdlc` prose paths from `00`, `03`, `09`, `10` (they point at the software layer, which is now a separate repo). Concepts kept; paths dropped or genericised to "the software projection". | SDP gate ("the stable layer does not know its dependents"); the paths became invalid on the split |
| **`core/09.md`** two refs to `meta/way-of-working.md`/`meta/conversion-protocol.md` genericised (those files stay with the software projection). | keep the cross-repo fork set minimal (§7) |
| **`core/README.md`** rewritten for the reorder (new 00 name, new 11, the contract/embed discipline) and de-referenced from its dependent. | reorder (README must track the new order) |

No prose was reworded beyond the above. Where a passage looked like it wanted a change outside this
list, it was flagged (§5), not made.

## 3. The core reorder, as landed

`00` primitives · `01` principle · `02` completeness · `03` floor (canonical closure + floor embeds)
· `04` actors (minus composite/compound) · `05` accountability · `06` composition (canonical) · `07`
determination≠intelligence · `08` projections · `09` the measure (determination demand) · `10` floor
mechanism · `11` the licensing instance. Every `ddd:contract` edge points backward; the reading order
is the dependency order, machine-checked.

## 4. W1 dispositions (every one)

46 W1 warnings. **All are legal forward pointers** — a doc previewing or citing a result established
in a later document, with an explicit `core/NN` cross-reference, each passing the deletion test (the
sentence is a signpost; deleting it does not break the doc's own argument). None is a genuine
backward-dependency violation (an "escaped edge"). Several are self-declared citational — e.g.
`05`'s preamble states outright that its `09`/`10` references are "citational, not definitional", and
the new `00` §3 and `04` §4 pointers are deliberate "stated here, detailed later" signposts. The
corpus is written with heavy forward cross-referencing by design; rewriting 46 sites to suppress the
linter would damage that and is not warranted. Grouped by the doc that establishes the term:

| Established in | Count | Previewing docs (disposition: legal forward pointer) |
|---|---|---|
| `01-the-principle` | 5 | `00` (demand, conservation, stores, judgment, assurance — the register note previews 01) |
| `02-completeness` | 3 | `00`, `01` (exhaustiveness, governing decision) |
| `03-the-floor` | 3 | `00`, `02` (floor, closing — `02` explicitly cites `03`) |
| `04-actors` | 5 | `00` §3 (new, by design), `03` (selection/training — `03`'s "Consequence" cites `04`) |
| `05-accountability` | 3 | `00`, `01` (accountability, attribution) |
| `06-composition` | 7 | `00`, `01`, `04` (seam, seam-identity, composite actors, seam occupancy — `04` §4 is the new pointer) |
| `08-projections` | 3 | `00`, `04` (projection, funnel — explicit `core/08` refs) |
| `09-the-measure` | 1 | `05` (`H(verdict)` — citational, §2) |
| `10-the-floor-mechanism` | 11 | `01,04,05,06,07,08,09` (capacity, overflow, overflow∩open — all explicit `core/10` previews) |
| `11-the-licensing-instance` | 4 | `01`, `02` (redundancy — generic word), `00`, `04`, `06` (immune system — illustrative) |

**Disposition for all 46: leave as legal forward pointers.** No relocation required.

## 5. Flags awaiting Emil

**⚑ judgment calls (all accepted by Emil, "accept and continue", recorded in `migration/README.md`):**
1. core/09 register fix in place, one parenthetical — **done**.
2. Fresh git init + provenance note at `10f6ba6` — **done** (README §Provenance).
3. Name `actor-indexed-determination` (DDD-dec-06) — **done**.
4. `i18n/ordliste-dansk.md` moved whole — **done**.
5. `00` minimal actor/arrangement — **done** (new §3, admission-test + composition phrasing only).
6. `assurance` split across `01`/`05` — **done** (`assurance` in 01, `assurance-tower` in 05; two keys).
7. Closure-sense fix — **done, with a deviation**: used "rules out", not core-contracts' "fills",
   because "fills" inverts the meaning. **Please confirm the wording.**
8. Ensemble theory in `11` — **done**.

**New flags surfaced during execution (please rule):**
- **`04` §5 removed, not only §4.** The reorder map named §4; but §5 (the compound) is duplicated in
  `06` and forward-references `06`'s terms, so leaving it would create genuine forward edges. I moved
  the compound's canonical home to `06` and pointed `04` at it. This is a larger cut than the map's
  one line — flagged for confirmation.
- **`05`'s two `H(verdict)` uses were left**, not rephrased (core-contracts asked for "2× verdict in
  05"). They are notation citations inside a passage that explicitly defers to `09`; rephrasing would
  misrepresent `09`'s formula. Left as W1 legal pointers. **Confirm.**
- **Contract-block parser limitation.** `validate-core-order.py`'s contract parser is line-based and
  silently drops terms on wrapped `establishes`/`requires` continuation lines. I kept every contract
  field on one line rather than patch the parser. A parser fix (handle continuations) would be more
  robust — flagged as a tooling follow-up.
- **Term embedding is partial (5 of 52).** Zero-W4 is met (every establishes-term has a graph entry).
  Only 5 terms with clean, unambiguous verbatim definition blocks were `ddd:embed`-ed byte-exact; the
  other 47 have registry entries but no embed (W3, §below). Embedding the rest would require authoring
  canonical definition blocks for abstract terms (e.g. *attribution*, *orchestrator*, *answerability*)
  that the prose does not currently isolate as a single block — that is **authoring canon**, out of a
  pure migration's scope. **Recommend**: Emil either authors canonical blocks for the remaining terms,
  or trims those docs' `establishes` lists to the terms that genuinely have canonical statements.
- **`meta/way-of-working.md`, `meta/conversion-protocol.md`, the claim-conversion skill, and
  `spec/claim-format.md` + `scripts/validate-claims.py`** placement — see §7.
- **The measure-note gate** was superseded by `DDD-dec-07` (Emil) before execution; recorded.

## 6. Placement calls beyond the settled §2 table

The package's §2 table places files; it does not place individual claims or several meta files. My
calls (flagged for Emil, landed on the unmerged branch for review):

- **Claims → principle:** `frame` (the contribution), `measure` (the formal backbone), `floor`, and
  `agent` (actor-general — the basis-loss claim `DDD-agent-01`, which both repos' CLAUDE.md invoke).
- **Claims → DDD (kept there):** `org` (seeds the organizations directory, `DDD-dec-05`), `tool` (the
  graph tool — software infrastructure), `sim` (the tool's predictive models, about "the DDD graph").
- **Decisions → DDD:** all of `DDD-dec-01..07` stay with the software projection — decisions are
  volitional program acts, and the split decisions reference DDD-local org claims; the principle repo,
  as the stable layer, holds none.
- **Meta:** `way-of-working`, `conversion-protocol`, `graph-tool-*`, `seed/` stay with the program
  (DDD); `lineage-and-limits` and `CANON-PATCH-REGISTER` moved to principle per §2.

## 7. Files present in both repos, classified

The gate allows only `CLAUDE.md` and the validator. Beyond those, the duplicates are:

| File | Content in the two repos | Justification |
|---|---|---|
| `CLAUDE.md` | **different** (forked) | gate-allowed |
| `validate-core-order.py` | **different** (principle: ordering+transclusion; DDD: upstream E12/E13/W5) | gate-allowed ("the validator") |
| `scripts/validate-claims.py` | identical | claim tooling both repos need (each has claim/decision files); validator-class fork — **flagged** |
| `spec/claim-format.md` | identical | claim schema both repos' claims declare (`format: 1`); validator-class fork — **flagged** |
| `LICENSE.md`, `.gitignore` | identical | universal infrastructure |
| `README.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `core/claims/README.md`, `meta/consolidated-state.md` | **different per repo** | not shared canon — each repo's own document (`consolidated-state` is a `split` per §2) |

No canonical claim, term, or core document exists in both repos. **Flag:** the two identical forks
(`validate-claims.py`, `claim-format.md`) exceed the literal "CLAUDE.md + validator" wording; I read
them as validator-class shared tooling/schema. Emil to confirm, or to move claim tooling upstream-only.

## Tag / v5.0.0 — a delivery caveat

`v5.0.0` is required as the DDD upstream pin. **The annotated tag push is blocked by the egress
proxy**: every `refs/tags/` push disconnects mid-sideband ("remote end hung up"), while the identical
commit pushed cleanly as a branch. As a working stand-in, **`v5.0.0` exists as a branch ref** (created
via the GitHub API) at the canon commit, so `git clone --branch v5.0.0` resolves and the DDD upstream
check passes now. The annotated tag exists locally. **Action for Emil / a follow-up with tag-push
access:** run `git push origin v5.0.0` (the tag), then delete the `v5.0.0` **branch** stand-in — the
pin discipline is "tag, never a branch", and a moving branch must not remain the pin.

## 8. Validator output, verbatim

### `validate-core-order.py core/` (principle)
```
12 documents, 52 terms, 52 graph objects, 5 embedded, 0 errors, 100 warnings
core: OK — edges point backward, embeds match the graph
```
(0 errors; W4 count 0. The 100 warnings are 46 W1 (§4, all legal forward pointers), 7 W2
(contract `requires` a term whose surface form is absent though the concept is present — stale-import
candidates, left), and 47 W3 (registry terms not embedded — the partial-embed flag in §5).)

### `validate-core-order.py core/` (decision-driven-design, upstream checks against v5.0.0)
```
  upstream  7 pins resolved against the pinned ref, 0 basis-loss warnings

upstream-only mode: 0 errors, 0 warnings
upstream: OK — every pin resolves at the pinned ref; no drift
```
E12 and W5 were verified to fire on tampered pins (a non-existent id → E12; a mismatched
`status_at_pin` → W5), then the tamper reverted — the check is not vacuous.

## Do not merge

Per the kickoff: this is delivered on branches for Emil's review. Nothing is merged. The DDD-side
report is `migration-report.md` in the `decision-driven-design` repo.
