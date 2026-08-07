# Reference-closure audit of `core/` — 2026-08-07

**Repository state audited:** `Hafeok/actor-indexed-determination` @ `720fd8b` (post-split principle
layer). The task named `Hafeok/decision-driven-design`; this repository is where `core/` now lives
after the split (UNVERIFIED — Emil review: I have assumed the task predates the split rename).

**Baseline:** `validate-core-order.py core/` — 0 errors, 52 warnings (all W1/W2, zero W4).
`validate-claims.py core/claims/` — 25 claims valid. All five `core/assets/*.py` scripts were
re-run fresh and reproduce the figures published in `09` and `10` exactly (measure-toy: 25.493
bits, both decompositions; actor-allocation: three sums 25.493; RAG: H(A)≈2.61 invariant;
floor-mechanism: escape 0/2.49/3.99/5.99/9.97; perr-rate-distortion: limits 0 and 0.5).

**Nothing in this audit has been applied to `core/`.** The EDITORIAL fixes appear only as a diff
inside this report (§8) and are not committed anywhere.

---

## 1. Reader model (the acceptance predicate, applied literally)

A competent software engineer or research reviewer who:

- has read `core/` files in the declared order, up to and including the file under audit, and
  nothing beyond it;
- has read no `meta/`, no projections, no papers, no issues, no prior conversation;
- knows standard external literature only where the text cites it by name.

A reference is closed if this reader can resolve it without leaving the text they have already
read. Everything else is an instance.

## 2. The declared order

Taken from the source `validate-core-order.py` uses: `sorted(core.glob("[0-9][0-9]-*.md"))`
(line 145) — lexicographic filename order:

`00-primitives` → `01-the-principle` → `02-completeness` → `03-the-floor` → `04-actors` →
`05-accountability` → `06-composition` → `07-determination-and-intelligence` → `08-projections` →
`09-the-measure` → `10-the-floor-mechanism` → `11-the-licensing-instance`.

`core/README.md` states the same order. `core/claims/*.yaml` and `core/graph/terms.yaml` are not
in the reading order; they were audited as canon storage (instances found there are listed in
their own tables) but not held to the sequential reader model.

Evidence bearing on whether this order is itself wrong is recorded separately in §7, not assumed
away.

## 3. Classification policy for borderline cases

Applied uniformly, so the tables are reproducible:

- **A forward use accompanied by an explicit target citation *and* an in-place gloss sufficient
  to parse the sentence is closed** under the reader model (the reader resolves it from text
  already read). Recorded as W where the gloss is thin, not inflated into R1. This covers most of
  the validator's 45 W1 warnings (e.g. `01`'s tower/`05` §7, `05`'s overflow ∩ open/`10`,
  `05`'s H(verdict)/`09`, `04`'s funnel/`08` at line 280).
- **A one-line table gloss is not a definition** when the term does later load-bearing work
  (`00`'s apparatus table rows for poisoned ground and the encode/verify split → R2).
- **A term is one instance** however many sites use it; all sites are listed on its row.
- **Ordinary-language uses** of words that later become terms (e.g. "redundancy" in `01`/`02`,
  "training" in `03`:111, "attribution" in `01`:186) are not instances.
- Dual-coded rows (e.g. R4+R5) count under each code in the summary.
- Anything resting on my inference rather than on canon is marked **UNVERIFIED — Emil review**.

Codes: R1 forward reference · R2 dangling reference · R3 uncited external · R4 conversational
residue · R5 inverted dependency · R6 definitional drift. Remedy class: EDITORIAL (changes no
claim's assertion) / SUBSTANTIVE (does; requires Emil's ratification, not applied).

---

## 4. Per-file instance tables

### 4.1 `core/00-primitives.md`

| Line | Quoted phrase | Code | Defined where, if anywhere | Remedy | Class |
|---|---|---|---|---|---|
| 28 | "We spoke of **governing decisions** as decisions *about an act*" | R4 | — ("we spoke" presupposes a discourse the reader was not part of) | ~~rephrase to name the source~~ **SUPERSEDED** — the whole §1 opening is replaced by Emil's ratified rewrite; see the supersession note in §8 | EDITORIAL |
| 77 | "The Polanyi floor" | R3 | Polanyi's tacit-knowledge result first glossed at `04`:505–508; never at first use | add one-line gloss/citation at first use | EDITORIAL |
| 78 | "The seam-demand identity" | R1 | `06`:19 (five documents later) | add forward citation in the table row | EDITORIAL |
| 79 | "Poisoned ground — *corrupting what a determination reads against*" | R2 | nowhere — this table gloss is the only definition; load-bearing at `04`:496, `10`:224 (Poisoned cause), `11`:151/153/174 | promote to the term registry (candidate C1, §6) | EDITORIAL¹ |
| 80 | "The encode/verify split — *whether you author the ground a determination reads*" | R2 | nowhere; load-bearing at `03`:158, `09`:216, `09`:247 | promote to the term registry (candidate C2, §6) | SUBSTANTIVE² |
| 123–126 | "A choice is a **decision** iff varying *the choice* moves the outcome past tolerance" | R6 | vs `01`:48–49 and `02`:90: "a choice is a **governing decision** iff varying it moves the outcome past tolerance" — the same iff defines two different terms | reconcile whether the test admits *decisions* or *governing decisions*, or state that they coincide | SUBSTANTIVE |
| 128 | "Same tolerance, same granularity bound" | R2 | nowhere; used again at `01`:48, `05`:268 | promote to the term registry (candidate C5, §6) | SUBSTANTIVE² |
| 151 | "*Full treatment: … and `meta/lineage-and-limits.md`.*" | R5 | `meta/` | drop the meta half — the register question is treated in `01`, which is in core | EDITORIAL |
| 159–160 | "the error behind \"CMSes are going away\"" | R4 | nowhere in core | gloss in one line or delete; gloss wording cannot be drawn from canon | SUBSTANTIVE |
| 174 | "see the software projection" | R5 | the dependent repository — forbidden by this repo's own SDP rule (`CLAUDE.md`) | delete the pointer | EDITORIAL |
| 198 | "its judgment store is fixed at zero" | R1 | judgment store: `01`:92–98 | add citation (`01`) | EDITORIAL |
| 214 | "The same shape as the CMS correction" | R4 | nowhere in core | gloss or delete, as 159 | SUBSTANTIVE |
| 219–221 | "Polanyi had the floor without the stores. … Counterintelligence had poisoned ground" | R3/R2 | shared with rows 77 and 79 | covered by those remedies | — |

¹ usage is univocal; the drafted wording still requires ratification before landing.
² definition must choose between divergent readings — see §6.

W (borderline, not inflated): rows 76/82 of the same table ("The four stores", "Assurance") are
forward but row-glossed and pre-declared by the Status note (lines 15–18); §5's "'Conservation'
and 'demand' survive" (162) is signposted to `01`; "first actor pinnable by binding" (204) is
glossed in place ("a distribution that can be frozen"); Tesler/Ashby name-drops in the register
note (12) are glossed in `01`.

### 4.2 `core/01-the-principle.md`

| Line | Quoted phrase | Code | Defined where, if anywhere | Remedy | Class |
|---|---|---|---|---|---|
| 10 | "Read `00-determination.md` first" | R2 | no such file — the document is `00-primitives.md` | fix the filename | EDITORIAL |
| 29 | "the framework's honesty about its own status is load-bearing (see `meta/lineage-and-limits.md`)" | R5 | support lives only in `meta/` | delete the pointer or restate the needed content in one line | EDITORIAL |
| 44 | "both are concessions the review forced" | R4 | "the review" has no antecedent anywhere in core | drop the appeal | EDITORIAL |
| 48 | "The **granularity bound** is tolerance-indexed" | R2 | nowhere (see `00`:128) | registry candidate C5 | SUBSTANTIVE |
| 57–58 | "the **seam** — the interface contract the decomposition brings into existence" | R6 | vs `06`:22–24 (seam demand = demand *created between* the parts) and `06`:32 (the interface contract *pays `S` down* — it is not `S`) | align `01`'s gloss with `06`'s canonical wording | SUBSTANTIVE |
| 105–109 | embed `term:assurance`: "**Tolerance** — which outcome deviations are acceptable — and **assurance** — …" | R6 | second canonical definition of *tolerance*, differing from `term:tolerance` (`00`:131–133: "the declared boundary of acceptable outcome deviation. It indexes everything…") | restrict `term:assurance`'s canonical_md to assurance; one canonical wording for tolerance | SUBSTANTIVE |
| 191 | "Full attribution and the corresponding retreats: `meta/lineage-and-limits.md`" | R5 | content only in `meta/` | the in-doc lineage list (183–189) already carries the load; accept as supplementary pointer or delete | EDITORIAL |

W: "`core/05` §7's tower" (51) — signposted and glossed ("a tower of assurance declarations");
seam forward citation (`core/09` §4, line 59) — signposted; "capacity" (149, 153) — ordinary
sense before `10`'s term; executor/accountable party (111–116) — defined in place, `05` §6 cited.

### 4.3 `core/02-completeness.md`

| Line | Quoted phrase | Code | Defined where, if anywhere | Remedy | Class |
|---|---|---|---|---|---|
| 88, 94–95 | "that is set by the **assurance level** (`00`, admission tests)… raise the assurance level and more choices cross into the governing set" | R6 | contradicts `01`:48–50: "two distinct variables … **must not be fused**: tolerance … assurance … The granularity bound is **tolerance-indexed** … Change the tolerance and you change the set." `00`'s admission tests are tolerance-indexed. | reconcile which variable indexes the governing set — this is the exact fusion `01` forbids | SUBSTANTIVE |
| 94 | "(see the finiteness argument in `03-the-floor.md`, which depends on it)" | R2 | `03` contains no finiteness argument (checked: no such passage) | delete the cross-reference; separately flag the phrase "keeps the **store** count finite" — UNVERIFIED, but "store count" (which is four by construction) appears to be a prose bug for the governing-decision count | EDITORIAL |

W: `meta/` pointer at 104 (the claim it supports is carried by `01`, in core).

### 4.4 `core/03-the-floor.md`

| Line | Quoted phrase | Code | Defined where, if anywhere | Remedy | Class |
|---|---|---|---|---|---|
| 10–11 | "a 'zero-floor postulate' that survived external review only in narrowed form" | R4 | the postulate itself is quoted verbatim at 144 (closed); "external review" is not | keep the quotation; drop or neutralise the review appeal | EDITORIAL |
| 157–158 | "it is the move the whole software-projection apparatus operationalises (contracts, checks, the encode/verify split)" | R5 (+R2) | the dependent repository; encode/verify split undefined in core (see `00`:80) | delete the clause — the preceding claim stands without it | EDITORIAL |

W: "Kalai & Vempala" (115) lacks year/venue — citation by name only; forward "Consequence" section
(166–176) is signposted (`04-actors.md`) and its two results are re-derived in `04`.

### 4.5 `core/04-actors.md`

| Line | Quoted phrase | Code | Defined where, if anywhere | Remedy | Class |
|---|---|---|---|---|---|
| 10 | "**Destination:** `core/04-actors.md`" | R4 | migration-workflow residue | delete | EDITORIAL |
| 12–13 | "It survived external adversarial review intact" | R4 | the review is not in core | trim to the content claim | EDITORIAL |
| 22–23 | "Composite actors allocate **seam demand** … *seam occupancy* — actor vs. mechanism" | R1 | `06`:19–51 | add citation (`06`) at the claims list | EDITORIAL |
| 55 | "bias and correlated error belong to the residual account" | R2 | nowhere — sole occurrence in the repository | define in place or delete; any definition would be invented (UNVERIFIED what it names) | SUBSTANTIVE |
| 227 | "the failure mode the conservation claim was corrected for in v4.0" | R4 | version history is outside core (root `CHANGELOG.md`) | drop the version handle | EDITORIAL |
| 428 | "the compound loop that harvests seam-judgment into seam-encoding" | R2 | "the compound" is a section heading in `06` and a load-bearing term in `08`'s canonical definitions; established as a term nowhere | promote `term:compound` (candidate C3, §6) | EDITORIAL¹ |
| 496 | "(The rigorous ancestor of poisoned ground.)" | R2 | see `00`:79 | registry candidate C1 | — |
| 500 | "an immune system in original antigenic sin" | R3 | uncited, unglossed immunology | one-line gloss (standard literature) | EDITORIAL |
| 519–520 | "it will be dismissed for the reasons the adversarial review already gave" | R4 | the reasons are nowhere in core | delete the appeal | EDITORIAL |

W: "last wind" (49) and "capability envelope" (40) are defined in place at first use but are
unregistered vocabulary reused later (`05`:303 reads the envelope result back) — registry
candidates if Emil wants them pinned; heading numbering jumps §4 → §6 (no §5) — renumbering
residue, see §7.4; "`core/04` §3's two-factor form" (118–119) is a within-file forward
self-citation, resolved by end of file.

### 4.6 `core/05-accountability.md`

| Line | Quoted phrase | Code | Defined where, if anywhere | Remedy | Class |
|---|---|---|---|---|---|
| 10–15 | "**Destination:** … shifts former `05`–`09` to `06`–`10` (see the canon patch register, P3.1)" | R4+R5 | `meta/CANON-PATCH-REGISTER.md` | trim the preamble to the dependency declaration | EDITORIAL |
| 20–23 | "if the tower is held back for a later release … One edit to `01`'s store table ships alongside (register P3.3)" | R4+R5 | release planning + `meta/` register | delete | EDITORIAL |
| 57–59 vs 64–68 vs 95–97 | (a) "linked to a persistent responsible principal, an attributable record, a defined stake, and an enforceable consequence path" · (b) canonical embed: "attribution of the determination, a persistent answerable party, and a borne consequence" · (c) "**Persistence** … **Stake** … **Sanctionability**" | R6 | all three in this file; (a) has four elements, (b) and (c) three, and (b)'s *attribution* is not (c)'s *sanctionability* | reconcile the condition set (or state explicitly that (a) is accountability-*completeness* of an arrangement and (b)/(c) its actor-facing decomposition, and make the wording match) | SUBSTANTIVE |
| 130–136 | embed `term:attribution` spliced mid-sentence ("Attribution over a ⟨embed⟩ determination record is not documentation…") | W-format | — | restore the sentence around the embed | EDITORIAL |
| 148 | "articulability is traded away by the mechanism that manufactures the transfer floor" | R2 | nowhere — sole occurrence; "transfer floor" is not `03`'s floor by name | define, or replace with the established term if synonymous (UNVERIFIED which is intended) | SUBSTANTIVE |
| 229–230 | "(canon patch register, P3.3)" | R5 | `meta/` | delete the parenthetical | EDITORIAL |
| 267–268 | "The assurance level fixes which choices are governing decisions at all (`00`, admission tests; `01`, granularity bound). Vary it and the set resizes." | R6 | same drift as `02`:88 — `01`:48–50 says the set is tolerance-indexed and forbids the fusion | reconcile with `02`:88 and `01`:48 in one decision | SUBSTANTIVE |
| 341 | "where the reversibility window is zero" | R2 | nowhere — sole occurrence | define in place (one line) | SUBSTANTIVE |

W: "Overflow ∩ open" (247) — forward to `10` but declared in the header as citational and glossed
in the sentence before it; "H(verdict)" (285–296) — forward to `09`, signposted and glossed;
"escalation" (220) — defined in place.

### 4.7 `core/06-composition.md`

| Line | Quoted phrase | Code | Defined where, if anywhere | Remedy | Class |
|---|---|---|---|---|---|
| 56 | "a **mechanism** (selection dynamics, stigmergy, price-clearing)" | R3 | stigmergy uncited, unglossed | one-line gloss or citation | EDITORIAL |
| 145 | "**Vertebrate immunity** has judgment and encoding and **no channel** (the Weismann barrier)" | R3 | named, not glossed | one-line gloss ("no inheritance path from soma to germline") | EDITORIAL |

W: `|D_comp| = |D_single| + |S|` notation (19) — glossed by the following line, made exact in
`09`; "clonal selection" (81) — listed as an example, mechanism explained only in `11`:50–53;
immune-system machinery (84, 133) does load-bearing expository work five documents before `11`
licenses the instance — recorded as order evidence, §7.2.

### 4.8 `core/07-determination-and-intelligence.md`

| Line | Quoted phrase | Code | Defined where, if anywhere | Remedy | Class |
|---|---|---|---|---|---|
| 10 | "**Destination:** `core/07-determination-and-intelligence.md`" | R4 | residue | delete | EDITORIAL |

W: "A third form of this falsifier was offered in earlier versions of this document and has been
met" (208–214) — version history, but deliberately kept as a receipt and resolved in place
("Satisfiability answers it"); closed enough under the reader model.

### 4.9 `core/08-projections.md`

| Line | Quoted phrase | Code | Defined where, if anywhere | Remedy | Class |
|---|---|---|---|---|---|
| 10–11 | "**Location:** … Patch addition to the shipped 4.0 core." | R4 | release history outside core | trim to the dependency sentence | EDITORIAL |
| 13–16, 158–191 | "the reference model" (exhibited "feedback loops 'at odd times'"); §5's diagnostic is declared "**reported**, not projected" | R2+R4 | nowhere — no such model exists in `core/assets/`, and the quoted phrase "at odd times" is residue of an unshared observation | land the reference model as a reproducible core asset, or demote §5's history from *reported*; by `CLAUDE.md`'s own rule a reported claim whose computation is not in `core/assets/` and does not reproduce must demote | SUBSTANTIVE |
| 62 | "or it is exactly the unpinned quantity the review caught in 'demand'" | R4 | "the review" has no antecedent in core | rephrase without the appeal | EDITORIAL |
| 27–29 vs 30–33 | prose: "the same mechanism — **the encoded store amortising a cost paid once** — viewed on two different axes" · canonical embed: "the same mechanism — **the compound** — run along two different axes" | R6 (+R2 compound) | both in this file; the canonical wording depends on an unestablished term | align after `term:compound` is ratified (C3) | SUBSTANTIVE |

W: "RDF and event sourcing" (55) — engineer-standard; `meta/` pointer (225) — the debt is stated
in place; "the orange curve in the diagram" (103) — figure shipped in `core/assets/`.

### 4.10 `core/09-the-measure.md`

| Line | Quoted phrase | Code | Defined where, if anywhere | Remedy | Class |
|---|---|---|---|---|---|
| 10–12 | "Also suitable as a standalone paper (*\"Determination Demand Is Verdict Entropy…\"*)" | R4 | paper-pipeline residue | delete the aside | EDITORIAL |
| 16 | "(canon authority lives in the claim files; see `CLAUDE.md`)" | R5 | repo root, outside core; the same convention is stated in `core/claims/README.md` | repoint to `core/claims/README.md` | EDITORIAL |
| 216, 247 | "RAG is the encode/verify split running in production" · "the **encode/verify split**" (listed as one of the framework's claims) | R2 | see `00`:80 — and note `09`'s reading (pre-resolving ground into retrieved context) is not obviously `00`'s reading (authoring the ground a determination reads); the promotion must decide | registry candidate C2 | SUBSTANTIVE |
| 294 | "The two quantities this release separates" | R4 | release-cycle residue | "this document separates" | EDITORIAL |

W: `meta/` debt pointer (43) — the debt is quoted verbatim in place, which closes it: this is the
pattern the R5 remedies elsewhere should copy.

### 4.11 `core/10-the-floor-mechanism.md`

| Line | Quoted phrase | Code | Defined where, if anywhere | Remedy | Class |
|---|---|---|---|---|---|
| 10 | "**Location:** `core/10-the-floor-mechanism.md`." | R4 | residue | delete | EDITORIAL |
| 12 | "and the closure principle (an actor's own prior output is not ground)" | R2+R6 | nowhere — not in any contract, registry, or claim; and the name collides with `term:closure` (`03`), which names an unrelated property (predicate closure) | promote under a non-colliding name (candidate C4, §6); the rename is Emil's | SUBSTANTIVE |
| 16–17 | "reproduce a field observation (a code-generation task that 'passed validation but failed inspection')" | R4 | the observation exists only in unshared context | land the observation as citable evidence, or mark it explicitly as anecdote rather than reproduction target | SUBSTANTIVE |
| 109 | "`core/00` §6.1's immune floor is this intersection" | R2 | `00` has no §6.1 and no immune floor; the only in-core statement of the immune floor is `11` §1.1 — *later* in the order | repoint (creates a forward edge — see §7.1) or relocate the instance; either way the current reference is dead | SUBSTANTIVE |
| 185–188 | "This is exactly the fix observed in the field: a code-generation task that produced gibberish…" | R4 | as 16–17 | same decision as 16–17 | SUBSTANTIVE |
| 204 | "*\"We can't trust a skill works as intended\"* is the correct verdict" | R4 | unattributed quotation from an unshared discussion | rephrase without the quotation | EDITORIAL |
| 205 | "Its full treatment lives in the software projection." | R5 | the dependent repository | delete | EDITORIAL |
| 224 | "own prior output consumed as ground (`closure-principle`)" | R2 | `closure-principle` is not a graph id; note it evades E9 because the validator's ref-check only parses HTML-comment refs, not backticked ids | resolved by candidate C4 | SUBSTANTIVE |
| 249 | "*Passed validation, failed inspection* is this, observed." | R4 | as 16–17 | same | SUBSTANTIVE |

### 4.12 `core/11-the-licensing-instance.md`

| Line | Quoted phrase | Code | Defined where, if anywhere | Remedy | Class |
|---|---|---|---|---|---|
| 12–13 | "It relocates here from the old `00`'s closing sections — the material was never wrong, only early." | R4 | repo history the reader has no access to | delete | EDITORIAL |
| 90–91 | "the same structure as denying single-point authorship of ground (`The Adversarial Ground`)" | R2 | no document of that name exists in core (UNVERIFIED — Emil review: presumably a pre-split or projection document) | delete the citation; the sentence stands without it | EDITORIAL |
| 118 | "The admission tests (§4) still gate" — inside the `term:swarm-gate` canonical embed | R2 | "§4" is a dangling section pointer (this document has no §4; the tests are `00` §4 — residue of the material's former home inside old `00`) | fix to "(`00` §4)" in `core/graph/terms.yaml` and re-project the embed; note this edits Emil-ratified canonical_md and should be confirmed even though it changes no assertion | EDITORIAL |
| 126 | "the vacuous generalisation §4 exists to prevent" | R2 | same dangling pointer | "`00` §4" | EDITORIAL |
| 151, 153, 174 | "both poisoned-ground attacks" · "Autoimmune disease is poisoned ground" · "a genuine Polanyi floor … both poisoned-ground attacks" | R2 / R3 | poisoned ground: see `00`:79 (candidate C1); Polanyi floor: see `00`:77 | covered by those remedies | — |
| 160 | "The benign-looking binary, exactly." | R4 | the cybersecurity example this points at is never given in core | delete the sentence | EDITORIAL |

W: "The signature, in a body." (156) — deictic, but the apposition ("*Confident, well-reasoned,
catastrophic*") arguably supplies the antecedent; "masquerade" (158) — standard security
vocabulary, though used as if a framework category; "V(D)J recombination" (40) — glossed in place.

### 4.13 `core/graph/terms.yaml`

| Line | Quoted phrase | Code | Defined where, if anywhere | Remedy | Class |
|---|---|---|---|---|---|
| 3 | "canonical_md blocks adopted from Emil's ratified proposals (batch in meta/CANON-PATCH-REGISTER.md)" | R5 | `meta/` | provenance comment, not a claim dependency — acceptable, or move the provenance note to `meta/` | W |
| 130–133 | `term:assurance` canonical_md opens by defining **Tolerance** | R6 | duplicate of `term:tolerance` with differing wording — see `01`:105–109 row | restrict to assurance | SUBSTANTIVE |
| 282–283 | `term:projection` canonical_md: "the same mechanism — **the compound** — run along two different axes" | R2 | "the compound" established nowhere; also load-bearing in `term:funnel` and `term:maturation` canonical_md | candidate C3 — three canonical definitions currently rest on an unregistered term | SUBSTANTIVE |
| 397–398 | `term:swarm-gate` canonical_md: "(§4)" | R2 | same as `11`:118 | fix with `11`:118 | EDITORIAL |

### 4.14 `core/claims/`

| File:line | Quoted phrase | Code | Defined where, if anywhere | Remedy | Class |
|---|---|---|---|---|---|
| README:12–13 | "The software-projection areas — `tool`, `org`, `sim` — live with the projection repository and pin this repo's claims" | R5 | the dependent repository | this is a layer statement rather than a claim dependency, but it is a literal reference to the dependent under `core/`, which `CLAUDE.md` forbids without exception — Emil should either exempt layer statements or reword to name no dependent | flag |
| DDD-frame-01:14 | "Paper A / foundation-revision material … NOT stated in any core/ document" | R5 | external paper draft | already correctly `UNVERIFIED`-flagged by the repo's own mechanism; no further action | — |
| DDD-frame-02:13 | "(meta/way-of-working §4, meta/graph-tool-ontology §2)" | R2 | neither file exists in this repository (`meta/` holds only CANON-PATCH-REGISTER, consolidated-state, lineage-and-limits) | amend the note to record that the scaffolding did not migrate in the split | EDITORIAL |
| DDD-frame-07:14 | "(meta/way-of-working §4, paper-4 row)" | R2 | same absent file | same | EDITORIAL |

W: `DDD-measure-08`'s notes cite "CHANGELOG 4.1", "patch register P1", "commit c64f360" —
provenance trail in `notes:`, resolvable from the repository's own history; `owner: paper-3/-4`
fields are claim-format metadata, not prose references.

---

## 5. Summary counts

By code (dual-coded instances count under each code; a term with many sites counts once):

| Code | Count | Notes |
|---|---|---|
| R1 | 3 | `00`:78, `00`:198, `04`:22 — most forward uses were closed by gloss+citation (policy §3) and sit in the W list |
| R2 | 16 | 8 undefined load-bearing terms (poisoned ground, encode/verify split, compound, granularity bound, closure principle, transfer floor, residual account, reversibility window) + 6 dead cross-references (`01`:10, `02`:94, `10`:109, `11`:90, `11`:118/126, claims frame-02/07) + `08`'s reference model + `10`:224 pseudo-id |
| R3 | 4 | Polanyi floor, original antigenic sin, stigmergy, Weismann barrier |
| R4 | 24 | dominated by three families: review appeals with no antecedent (5), release/version residue (7), unshared field observations and deictic examples (6), plus Destination/Location headers (6) |
| R5 | 13 | 3 references to the software projection inside `core/` prose (`00`:174, `03`:157, `10`:205 — direct violations of the repo's own SDP rule), 7 `meta/` dependencies, `09`:16 CLAUDE.md, 2 in claims |
| R6 | 7 | decision vs governing decision; tolerance defined twice canonically; governing-set index (tolerance vs assurance) drifting in `02` and `05` against `01`; accountability condition sets; seam gloss; projection mechanism wording; closure/closure-principle name collision |

By file (instances surfacing in that file; shared terms attributed to first site):

| File | R1 | R2 | R3 | R4 | R5 | R6 | Total |
|---|---|---|---|---|---|---|---|
| 00-primitives | 2 | 3 | 1 | 3 | 2 | 1 | 12 |
| 01-the-principle | – | 1 | – | 1 | 2 | 2 | 6 |
| 02-completeness | – | 1 | – | – | – | 1 | 2 |
| 03-the-floor | – | – | – | 1 | 1 | – | 2 |
| 04-actors | 1 | 2 | 1 | 4 | – | – | 8 |
| 05-accountability | – | 2 | – | 2 | 3 | 2 | 9 |
| 06-composition | – | – | 2 | – | – | – | 2 |
| 07-det-and-intelligence | – | – | – | 1 | – | – | 1 |
| 08-projections | – | 1 | – | 3 | – | 1 | 5 |
| 09-the-measure | – | – | – | 2 | 1 | – | 3 |
| 10-the-floor-mechanism | – | 3 | – | 5 | 1 | – | 9 |
| 11-the-licensing-instance | – | 3 | – | 2 | – | – | 5 |
| graph/terms.yaml | – | 1 | – | – | – | 1 | 2 |
| claims/ | – | 2 | – | – | 2 | – | 4 |
| **Total** | **3** | **19** | **4** | **24** | **12** | **8** | **70** |

(The two tallies differ slightly because the by-file table counts each surfacing site of shared
codes once per file; the by-code table deduplicates terms across files. Both countings are stated
so neither is mistaken for the other.)

The dominant finding is not any single instance but the pattern: **R4 residue concentrates in the
documents' preambles** (Destination/Location/patch/release notes — mechanical to strip), while
**the load-bearing gaps are the eight R2 terms and the three governing-set R6 drifts**, which are
few but sit under canonical definitions.

---

## 6. Canonical term registry candidates (R2 and R6)

All drafted wordings below are **DRAFT — UNVERIFIED — they require Emil's ratification and must
not land without it.** Where canon offers divergent readings I have recorded both rather than
choosing.

**C1 — `term:poisoned-ground`** (R2; sites `00`:79/221, `04`:496, `10`:224, `11`:151/153/174).
Usage is univocal across all sites. Draft:

> **Poisoned ground** — ground that is present but false: the substrate a determination reads has
> been corrupted, so a correct determiner resolves wrongly with full authority. The logic is
> sound; the ground is the attack surface.

**C2 — `term:encode-verify-split`** (R2; sites `00`:80, `03`:158, `09`:216/247). The two in-core
glosses do **not** obviously agree, which is itself drift the promotion must settle:
`00`:80 reads it as *authorship* ("whether you author the ground a determination reads");
`09`:216 reads it as *allocation* ("converts ground into encoded specification, leaving the model
to carry the residual as judgment", with the mechanical store verifying). Draft (allocation
reading, per the majority of load-bearing use — UNVERIFIED which reading is intended):

> The **encode/verify split** — the division of a determination's demand between pre-resolving
> ground into the encoded store before the act and verifying the residual mechanically after it.

**C3 — `term:compound`** (R2; sites `04`:428/538, `06` §"The compound", `08` throughout, and
inside the canonical_md of `term:projection`, `term:funnel`, `term:maturation`). Three ratified
canonical definitions currently rest on this unregistered term. Draft, assembled from `06`:

> **The compound** — the loop that harvests recurring seam-judgment into the encoded store over a
> write-back channel, always paired with a mechanical check on what was harvested, so that each
> cycle shrinks per-run judgment toward the floor.

**C4 — the "closure principle"** (R2+R6; sites `10`:12, `10`:224). Needs promotion **under a
non-colliding name** — `term:closure` (`03`) already names predicate closure, an unrelated
property. Name choice is Emil's (e.g. `term:own-output-rule`). Draft:

> An actor's **own prior output is not ground**: consuming it as ground substitutes the actor's
> model of the world for the world — the reflexive case of poisoned ground.

**C5 — `term:granularity-bound`** (R2; sites `00`:128, `01`:48, `05`:268). Blocked on the R6
decision below — the definition must commit to what indexes the bound. Draft (tolerance-indexed,
per `01`'s explicit statement):

> The **granularity bound** — the tolerance-indexed criterion fixing which choices enter the
> governing set: a choice is a governing decision iff varying it moves the outcome past the
> declared tolerance.

**R6 registry decisions required (no drafts offered where the decision is genuinely open):**

1. **Governing-set index** (`01`:48–50 tolerance vs `02`:88/94–95 and `05`:267–268 assurance).
   `01` explicitly forbids the fusion the other two commit. One of the two readings must be
   corrected; correcting either changes what a claim asserts. SUBSTANTIVE, Emil only.
2. **Decision vs governing decision** in the admission test (`00`:123 vs `01`:48–49, `02`:90).
   Either the terms coincide (then say so once) or the test defines only one of them.
3. **Tolerance's duplicate canonical wording** inside `term:assurance` — restrict that entry to
   assurance.
4. **Accountability's three condition sets** (`05`) — one canonical set, or an explicit
   completeness/decomposition relation between them.
5. **`term:governing-decision`** is registry-only (no canonical_md); once (2) is settled it should
   receive one, since the conservation statement itself quantifies over governing decisions.
6. **Projection/funnel/maturation canonical_md** — re-ratify wording after C3 lands (they
   currently define via the unregistered "compound").

**Not proposed for the registry:** transfer floor (`05`:148), residual account (`04`:55),
reversibility window (`05`:341) — each has exactly one site; any definition I drafted would be
invention rather than recording. Recommend define-in-place by Emil or removal.

---

## 7. Evidence bearing on the declared order (recorded separately, as instructed)

1. **`10`:109 depends on material that now lives after it.** "`core/00` §6.1's immune floor" is
   dead (no such section), and the only in-core statement of the immune floor is `11` §1.1 —
   *after* `10`. `11`:12–13 records the relocation from old `00`. As ordered today, `10`'s
   "worked instance" paragraph cannot be written without a forward edge. Either the immune-floor
   instance belongs before `10`, or the paragraph should be dropped from `10` and left to `11`.
   This is the one place the audit found the declared order and the content genuinely fighting.
2. **`06` builds on the immune instance five documents before `11` licenses it.** The
   matched-pair invariant's exemplar ("This is what the thymus is", `06`:133) and the
   no-poisonable-centre argument (`06`:84) do load-bearing expository work, while `core/README.md`
   declares `11` the licensing instance, "legal only after `10`". The validator cannot see this
   (illustrative prose, no contract edge). UNVERIFIED — Emil review: whether pre-licensing
   *illustrative* use is legal by the framework's own doctrine, or whether `06` should carry a
   forward-instance flag.
3. **`04` §6's second contribution rests on `06`'s results.** `04`:536–538 lists the seam results
   among "the two results that are ours" while deferring their statement to `06` (`04`:424–430).
   Consistent with the declared order only if a claims-summary may cite forward; otherwise
   evidence that composition belongs before the re-indexing, or that the re-indexing's seam bullet
   belongs after `06`.
4. **Renumbering residue, not order error:** `04` jumps §4 → §6 with no §5; `05`'s preamble
   records "shifts former `05`–`09` to `06`–`10`". Explains the stale `§4`/`§6.1` pointers found
   above; no action beyond the fixes already listed.
5. `05`'s declared forward references to `09`/`10` are citational only and are glossed at the use
   sites — consistent with the declared order.

---

## 8. EDITORIAL fixes as a unified diff (NOT applied, NOT to be committed without review)

Scope: only remedies classed EDITORIAL above. The diff was generated against `720fd8b` on a
scratch copy; both validators pass on the patched copy (`validate-core-order.py`: 0 errors, 52→50
warnings; `validate-claims.py`: 25 valid). It includes the matched pair of edits to
`11`/`terms.yaml` for the "(§4)" fix so the E6 byte-match holds — note that pair touches
Emil-ratified canonical_md and should be confirmed even though it changes no assertion. The two
claim-note amendments (frame-02, frame-07) are listed in §4.14 but deliberately left out of the
diff, since claim files are canon authority.

**Supersession note (2026-08-07, second pass).** The first hunk of the `00-primitives.md` diff
below — the `00`:28 "We spoke of…" rephrasing — is **superseded by Emil's ratified rewrite of
§1's opening and has been removed from the diff.** History, so the two are not applied twice:
that hunk *was* applied to the tree in commit `2633bcf` (Phase 2a of the fix run), so `00` §1
briefly read "Earlier statements of the framework spoke of…". Emil's ratified replacement covers
the section heading through the end of the "It is decisions the whole way down" paragraph — it
deletes that sentence *and* the "has been carrying a distinction" sentence above it, which shares
the same R4 defect (one instance, fixed together). The ratified patch, built against `3300f8c`
and validated on a scratch copy (0 errors, 52 warnings — unchanged; 25 claims valid), is recorded
here and is **not applied**:

```diff
diff --git a/core/00-primitives.md b/core/00-primitives.md
index c2702eb..67dc437 100644
--- a/core/00-primitives.md
+++ b/core/00-primitives.md
@@ -22,19 +22,16 @@ for those.
 
 ## 1. The collapse
 
-The framework has been carrying a distinction it does not need, and the distinction has been
-hiding what the law is about.
-
-Earlier statements of the framework spoke of **governing decisions** as decisions *about an act* — the act was the primitive, the
-decisions were the specification wrapped around it. Decide the constraints, then act.
-
 **There is no act.**
 
-"Which voltage to the motor, now" is a decision. "Which word next" is a decision. "Fire or hold"
-is a decision. Descend as far as you like and you never reach a floor of *pure action* that
-decisions merely describe. It is decisions the whole way down. What we called *the act* was the
-**last decision in the chain** — the one closest to the world, whose determination is expressed
-rather than passed on.
+It is tempting to treat the act as the primitive and decisions as the
+specification wrapped around it: decide the constraints, then act. But
+"which voltage to the motor, now" is a decision. "Which word next" is a
+decision. "Fire or hold" is a decision. Descend as far as you like and you
+never reach a floor of pure action that decisions merely describe. It is
+decisions the whole way down. What looked like the act was the last
+decision in the chain — the one closest to the world, whose determination
+is expressed rather than passed on.
 
 <!-- ddd:embed id=term:last-decision -->
 > The **last decision in the chain** — the one closest to the world, whose determination is
```

The `term:last-decision` embed sitting immediately after the replaced range is **retained**, per
the stop-gate in Emil's instruction: the "isolated repetition of the last-decision clause" is not
verbatim prose — it is the canonical `ddd:embed id=term:last-decision` block, byte-paired with
`core/graph/terms.yaml` (E6) and the term's only embed (deleting it would orphan the
canonical_md, W3), and it bolds the term where the ratified wording does not. It therefore
carries something the replacement lacks and was not deleted.

```diff
diff --git a/core/00-primitives.md b/core/00-primitives.md
index b6284f9..c8bd4d6 100644
--- a/core/00-primitives.md
+++ b/core/00-primitives.md
@@ -73,13 +73,13 @@ The apparatus holds against this without strain:
 
 | Apparatus | A statement about |
 |---|---|
-| The four stores | *where the determination lives* |
+| The four stores (`01`) | *where the determination lives* |
 | The Polanyi floor | *how much determination can be moved off an actor* |
-| The seam-demand identity | *decisions created between decomposed decisions* |
+| The seam-demand identity (`06`) | *decisions created between decomposed decisions* |
 | Poisoned ground | *corrupting what a determination reads against* |
 | The encode/verify split | *whether you author the ground a determination reads* |
 | Tolerance | *which choices count as decisions at all* |
-| Assurance | *how much evidence the allocation must carry* |
+| Assurance (`01`) | *how much evidence the allocation must carry* |
 
 Nothing needs a third primitive. Nothing is left over.
 
@@ -148,7 +148,7 @@ nothing.**
 
 ## 5. The name
 
-*Full treatment: `01-the-principle.md` ("Register") and `meta/lineage-and-limits.md`.*
+*Full treatment: `01-the-principle.md` ("Register").*
 
 The reframing forces a naming question, and the answer is a **two-level structure**, not a
 replacement — and, after external review, a **downgrade of register.**
@@ -171,7 +171,7 @@ So the two-level structure is:
 >
 > ### Conservation of Specification Demand
 > *(the **engineering projection** — the same principle, denominated in the vocabulary of a domain
-> where determinations are called specifications; see the software projection.)*
+> where determinations are called specifications.)*
 
 **Specification is what determination demand is called when the actor is building software.**
 
diff --git a/core/01-the-principle.md b/core/01-the-principle.md
index 806c345..35be895 100644
--- a/core/01-the-principle.md
+++ b/core/01-the-principle.md
@@ -7,7 +7,7 @@ establishes: [demand|determination demand, conservation|conservation principle,
 status: settled
 -->
 
-**Read `00-determination.md` first.** It establishes the two primitives (decisions and ground)
+**Read `00-primitives.md` first.** It establishes the two primitives (decisions and ground)
 and the admission tests. This document states the principle those primitives obey.
 
 ---
@@ -41,7 +41,7 @@ law that overclaims.
 > Reduce the demand in one store and it **relocates**; it does not vanish.
 <!-- /ddd:embed -->
 
-Two qualifiers carry the whole weight, and both are concessions the review forced:
+Two qualifiers carry the whole weight, and both are deliberate concessions:
 
 **"At a declared assurance level."** Two distinct variables live under this qualifier and must not
 be fused: **tolerance** — which outcome deviations are acceptable — and **assurance** — the strength
diff --git a/core/02-completeness.md b/core/02-completeness.md
index c0e9ae1..e228f89 100644
--- a/core/02-completeness.md
+++ b/core/02-completeness.md
@@ -91,7 +91,7 @@ the **assurance level** (`00`, admission tests):
 
 Below tolerance, a choice is not a governing decision and is not in the accounting at all — it is
 *substrate*, inspected in order to act, not demand to be allocated. This is what keeps the store
-count finite (see the finiteness argument in `03-the-floor.md`, which depends on it): raise the
+count finite: raise the
 assurance level and more choices cross into the governing set; lower it and fewer do. The partition
 is complete *at a declared tolerance*, and undefined without one.
 
diff --git a/core/03-the-floor.md b/core/03-the-floor.md
index 292b56b..26a163a 100644
--- a/core/03-the-floor.md
+++ b/core/03-the-floor.md
@@ -154,8 +154,7 @@ absence:
 
 This is more useful than the original, because it tells you *where to look*: to lower a task's floor,
 you do not train harder — **you find or construct a closing predicate.** That is the move that
-actually works, and it is the move the whole software-projection apparatus operationalises (contracts, checks,
-the encode/verify split).
+actually works.
 
 **Retired:** the slogan *"there is no tacit knowledge in digital work."* Not defensible against
 Collins's collective tacit knowledge, and not needed — the predicate-located version is both correct
diff --git a/core/04-actors.md b/core/04-actors.md
index 7a43552..1185446 100644
--- a/core/04-actors.md
+++ b/core/04-actors.md
@@ -7,11 +7,8 @@ establishes: [pinning-resolution|pinning resolution, selection, training]
 status: settled
 -->
 
-**Destination:** `core/04-actors.md`
-
 **Status.** This is the part of the framework with the least prior art and the strongest claim to
-novelty. It survived external adversarial review intact — not because it was overlooked, but
-because there is little to hit it with: the classical results have an **actor slot that nobody
+novelty: the classical results have an **actor slot that nobody
 filled in**, and this document fills it.
 
 The load-bearing claims here are:
@@ -20,7 +17,7 @@ The load-bearing claims here are:
 2. The **intrinsic floor is a property of the acceptance predicate, not of the decision** — which
    yields *selection intensity is inversely proportional to predicate closure.*
 3. Composite actors allocate **seam demand** across the same four stores, and *seam occupancy* —
-   actor vs. mechanism — is a real design fork with a real price.
+   actor vs. mechanism — is a real design fork with a real price (`06`).
 4. **Re-indexing the classical laws by actor changes their predictions.** This is the contribution.
 
 ---
@@ -224,7 +221,7 @@ That is checkable against existing professional data, with both factors independ
 
 **Guard against unfalsifiability.** "Cost" must be operationalised by that proxy and fixed in
 advance. Otherwise any observed ratio can be explained post hoc by positing an unmeasured cost —
-which is exactly the failure mode the conservation claim was corrected for in v4.0. **Pre-register the
+which is exactly the failure mode the conservation claim was previously corrected for. **Pre-register the
 cost proxy, or the claim is not a claim.**
 
 ---
@@ -517,7 +514,7 @@ addresses.
 ## 7. The honest statement of the contribution
 
 Not *"I have reframed Tesler, Ashby, Brooks, Meyer, and Kalman."* That is true, and it will read as
-grandiose, and it will be dismissed for the reasons the adversarial review already gave.
+grandiose, and it will be dismissed.
 
 The defensible framing is smaller and lands harder:
 
diff --git a/core/05-accountability.md b/core/05-accountability.md
index 6b01a0d..35369be 100644
--- a/core/05-accountability.md
+++ b/core/05-accountability.md
@@ -7,20 +7,15 @@ establishes: [accountability, attribution, answerability, liability, assurance-t
 status: settled
 -->
 
-**Destination:** `core/05-accountability.md` — immediately after `04-actors.md`, which it extends.
-This seats accountability with the actor model and shifts former `05`–`09` to `06`–`10` (see the
-canon patch register, P3.1). Actor-general, denominated in determinations. Depends on `00` (admission tests), `01` (the four stores), `03` (the
-floor lives in the acceptance predicate) and `04` (pinning-resolution spectrum). Forward-references
-`09` (the measure) and `10` (escape = overflow ∩ open), both of which now sit later in the read
-order; the dependency is citational, not definitional.
+Extends `04-actors.md`. Actor-general, denominated in determinations. Depends on `00` (admission
+tests), `01` (the four stores), `03` (the floor lives in the acceptance predicate) and `04`
+(pinning-resolution spectrum). Forward-references `09` (the measure) and `10` (escape = overflow ∩
+open), both later in the read order; the dependency is citational, not definitional.
 
 **Status: projected.** Derived, unexercised. Falsifiers stated per claim. Nothing here is reported.
 
-This document **introduces** two things core does not currently contain: an accountability condition
-on actors (§§1–6) and the **assurance tower** (§7). Neither is cited from elsewhere in the repo, so
-there are no dangling forward-references — but §7 is a substantive addition in its own right, and if
-the tower is held back for a later release, §§1–6 stand without it and §7 lifts out cleanly. One
-edit to `01`'s store table ships alongside (register P3.3).
+This document **introduces** two things core does not otherwise contain: an accountability condition
+on actors (§§1–6) and the **assurance tower** (§7).
 
 ---
 
@@ -127,14 +122,15 @@ What is required is a continuity binding act to consequence:
 
 > **The thing sanctioned later must be identifiably the thing that determined earlier.**
 
-This makes the condition **provenance-shaped, and therefore checkable**. Attribution over a
+This makes the condition **provenance-shaped, and therefore checkable**.
 
 <!-- ddd:embed id=term:attribution -->
 > **Attribution** — provenance-shaped, and therefore checkable: the record connecting the
 > determination to the execution that produced it.
 <!-- /ddd:embed -->
-determination record is not documentation *of* accountability; it is the substrate that makes
-accountability capacity computable rather than assumed.
+
+Attribution over a determination record is not documentation *of* accountability; it is the
+substrate that makes accountability capacity computable rather than assumed.
 
 ---
 
@@ -226,8 +222,8 @@ immediate cost, and suppressing it does not.
 ## 6. The two roles in the Judgment store
 
 `01` gives Judgment's source as *an actor reading ground*. That is correct and stays. It elides one
-distinction that matters as soon as the executing actor is not a human — and the elision is patched
-directly into `01`'s store table alongside this chapter (canon patch register, P3.3):
+distinction that matters as soon as the executing actor is not a human — and `01`'s store table now carries the
+split:
 
 - **Executor** — the actor making the determination this run.
 - **Accountable party** — the actor bound to it afterwards.
diff --git a/core/07-determination-and-intelligence.md b/core/07-determination-and-intelligence.md
index 597cb81..a487bbc 100644
--- a/core/07-determination-and-intelligence.md
+++ b/core/07-determination-and-intelligence.md
@@ -7,8 +7,6 @@ establishes: [determination-intelligence-separation|determination is not intelli
 status: settled
 -->
 
-**Destination:** `core/07-determination-and-intelligence.md`
-
 **Status.** The positive claim (*determination ≠ intelligence*) is a **consequence** of the
 admission tests and is not optional — the framework collapses without it. The negative result
 (*the LLM-intelligence debate is structurally undecidable*) is a **derivation** from the
diff --git a/core/08-projections.md b/core/08-projections.md
index 81b29a0..8bc01e9 100644
--- a/core/08-projections.md
+++ b/core/08-projections.md
@@ -7,8 +7,8 @@ establishes: [projection, funnel, maturation]
 status: settled
 -->
 
-**Location:** `core/08-projections.md`. Depends on the principle (`01`), the floor (`03`), and the
-compound loop in composition (`06`). Patch addition to the shipped 4.0 core.
+Depends on the principle (`01`), the floor (`03`), and the
+compound loop in composition (`06`).
 
 **Status:** the correction in this document (funnel as *cost*, not *count*) resolves a modelling
 error that produced spurious feedback loops in the reference model. That diagnostic history is
@@ -59,8 +59,8 @@ neither community noticed they were describing one thing).
 
 ## What "cost" is
 
-"Cost" cannot stay a vibe with axes, or it is exactly the unpinned quantity the review caught in
-"demand." So, precisely:
+"Cost" cannot stay a vibe with axes, or it is an unpinned quantity of exactly the kind "demand"
+itself once was. So, precisely:
 
 **Cost is not tokens, dollars, or wall-clock time.** Those are *substrate-specific prices* — they
 vary by actor (a human-hour versus a GPU-second), so they cannot be the quantity the projection is
diff --git a/core/09-the-measure.md b/core/09-the-measure.md
index 1c43db0..21ce2ab 100644
--- a/core/09-the-measure.md
+++ b/core/09-the-measure.md
@@ -7,13 +7,11 @@ establishes: [verdict|verdict function, verdict-entropy|verdict entropy, chain-r
 status: settled
 -->
 
-**A formal note.** Location: `core/09-the-measure.md`. Reproduction scripts in
-`core/assets/measure-*.py`. Also suitable as a standalone paper
-(*"Determination Demand Is Verdict Entropy: Conservation as the Chain Rule"*).
+**A formal note.** Reproduction scripts in `core/assets/measure-*.py`.
 
 **Claims.** The propositions of this note are landed as claim nodes under `core/claims/`
 (`DDD-measure-*`); canon authority for each is its claim file, and this document is their
-exposition (canon authority lives in the claim files; see `CLAUDE.md`). The mapping:
+exposition (canon authority lives in the claim files; see `core/claims/README.md`). The mapping:
 
 | Section | Proposition | Claim |
 |---|---|---|
@@ -291,7 +289,7 @@ identical verdict entropy can differ unboundedly in generation cost — a lookup
 instance over the same input space carry the same `H(verdict)`, and one is answered by indexing
 while the other is NP-hard to solve. Closure decides whether the floor is zero and whether the
 measure exists; generation cost is a second, independent variable the measure does not see
-(`core/03` §2, `core/04` §2). The two quantities this release separates must not be re-fused through
+(`core/03` §2, `core/04` §2). The two quantities are separated deliberately and must not be re-fused through
 the measure.
 
 ---
diff --git a/core/10-the-floor-mechanism.md b/core/10-the-floor-mechanism.md
index c831997..47ce3db 100644
--- a/core/10-the-floor-mechanism.md
+++ b/core/10-the-floor-mechanism.md
@@ -7,7 +7,7 @@ establishes: [capacity, overflow, escape-mechanism|overflow ∩ open, p-err|p_er
 status: settled
 -->
 
-**Location:** `core/10-the-floor-mechanism.md`. Completes `core/03` (the floor is in the acceptance
+Completes `core/03` (the floor is in the acceptance
 predicate) by supplying the *mechanism*: how, and exactly when, demand escapes. Depends on the
 measure (`core/09`), the matched-pair invariant (`core/06`), and the closure principle (an actor's own prior output is not ground). Reproduction: `assets/floor-mechanism.py` and `assets/perr-rate-distortion.py`.
 
@@ -201,8 +201,8 @@ It satisfies condition (2) by construction, so the moment condition (1) is met (
 sits in the escape intersection and fails *silently*.
 
 Its reliability is therefore not authored in — it is `1 − (overflow × openness)`, and it degrades
-under load. *"We can't trust a skill works as intended"* is the correct verdict, mechanically: an
-unverified skill is protected from overflow-escape by nothing. Its full treatment lives in the software projection.
+under load. That an unverified skill cannot be trusted to work as intended is the correct verdict,
+mechanically: an unverified skill is protected from overflow-escape by nothing.
 
 ---
 
diff --git a/core/11-the-licensing-instance.md b/core/11-the-licensing-instance.md
index 5e8fac9..8ff0c9c 100644
--- a/core/11-the-licensing-instance.md
+++ b/core/11-the-licensing-instance.md
@@ -9,9 +9,7 @@ status: settled
 
 **Read `00` through `10` first.** This is the capstone worked instance: it is legal only after
 `10` supplies capacity and overflow, because ensemble theory (diversity carrying judgment demand
-that exceeds any single actor's capacity) depends on them. It relocates here from the old
-`00`'s closing sections — the material was never wrong, only early.
-
+that exceeds any single actor's capacity) depends on them. 
 ## 1. Ensemble actors
 
 The immune system forces an addition, and it is **not a fifth store**. It is a *strategy for
@@ -87,8 +85,7 @@ thousand *different* ones recognise ten thousand.
 
 **The variance is not a defect tolerated for robustness. The variance is the capability.**
 
-And this is the same structure as denying single-point authorship of ground (`The Adversarial
-Ground`). Redundant *uncorrelated* channels defeat an adversary who can author only one. Diverse
+And this is the same structure as denying single-point authorship of ground. Redundant *uncorrelated* channels defeat an adversary who can author only one. Diverse
 *uncorrelated* detectors cover a space no single detector can. In both, the value lies in the
 actors being **decorrelated** — and in both, **correlation is the failure mode.**
 
@@ -115,7 +112,7 @@ says must be paid somewhere.
 
 <!-- ddd:embed id=term:swarm-gate -->
 **A swarm is an actor only if it genuinely determines choices against ground.** The admission
-tests (§4) still gate, and they must.
+tests (`00` §4) still gate, and they must.
 <!-- /ddd:embed -->
 
 A flock turning together is mostly **not** making a determination — local rules producing global
@@ -123,7 +120,7 @@ pattern, with no choice resolved against a substrate. Ant colony foraging is clo
 pheromone field is genuine ground, read and written.
 
 **The immune system passes. Not everything swarm-shaped will.** Without the gate, "swarms are
-intelligent actors" becomes exactly the vacuous generalisation §4 exists to prevent.
+intelligent actors" becomes exactly the vacuous generalisation `00` §4 exists to prevent.
 
 ---
 
diff --git a/core/graph/terms.yaml b/core/graph/terms.yaml
index db6e281..1e0596f 100644
--- a/core/graph/terms.yaml
+++ b/core/graph/terms.yaml
@@ -395,7 +395,7 @@ terms:
     status: settled
     canonical_md: |
       **A swarm is an actor only if it genuinely determines choices against ground.** The admission
-      tests (§4) still gate, and they must.
+      tests (`00` §4) still gate, and they must.
   - id: term:immune-system
     term: immune-system
     aliases: [immune system]
```

---

## 9. Mechanisation note (R1/R2/R5 as validator codes)

**R1** is already approximated by W1: the validator has the index it needs (term → establishing
doc position, plus aliases). Promoting it to an error requires distinguishing licensed forward
pointers from escaped ones — add a declared `forward:` field to `ddd:contract` and error (say E12)
on any registry-term match in a document earlier than the term's home that is neither declared nor
inside an embed/ref marker. Gloss-sufficiency is not mechanically decidable; E12 enforces
declaration, not closure.

**R2, cross-reference form:** fully mechanical. Build an index of core filenames and per-file
heading/section anchors; error (E13) on any `NN-*.md`, `core/NN`, or `§n` reference that does not
resolve, and extend the E9 ref-check to backticked graph ids (which currently evade it —
`10`:224). This alone catches `01`:10, `02`:94, `10`:109, `10`:224, `11`:118/126. The vocabulary
form (poisoned ground) needs a closed lexicon — e.g. require every bold-at-first-use term to
appear in the registry — otherwise heuristic only.

**R5:** fully mechanical (E14): error on `meta/` paths, projection/paper names, or repo-external
paths in core prose, with an allowlist for claim `notes:` provenance. Catches every R5 found here.

R3, R4, R6 remain editorial judgement.

---

*Audit method: every core document read in full in declared order; every candidate term
grep-verified across `core/` before classification; all five assets re-run. Classifications and
drafted definitions are mine and unratified; rows marked UNVERIFIED are flagged for striking.*
