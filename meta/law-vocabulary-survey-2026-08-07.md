# Self-referential "law" in `core/` — vocabulary survey, 2026-08-07

**Report only. Nothing in `core/` has been changed.** Line numbers are keyed to `ba4d964`
(current HEAD of `claude/reference-closure-audit-core-p4vydw`); re-locate by quoted sentence
before applying any fix. Companion to `meta/reference-audit-2026-08-07.md`.

**Method.** Case-insensitive grep for `\blaw` and inflections over all `core/*.md`,
`core/README.md`, `core/graph/terms.yaml` (canonical_md blocks included), and
`core/claims/*.yaml` (all prose fields). Compound sweep (`lawlike`, `law-like`, `bylaw`,
`lawful`) returned nothing beyond the hyphenated `physical-law` at `01`:23, which the main
pattern catches.

**Raw count: 35 matching lines, 38 tokens** (31 `law`, 4 `Law`, 3 `laws`; three lines carry two
tokens: `00`:11, `00`:47, `01`:22). **Zero hits in `core/graph/terms.yaml` and zero in
`core/claims/*.yaml`** — no ratified canonical_md and no claim statement uses the word at all.

## Counts by bucket and by file

| File | S | C | H | A | Total |
|---|---|---|---|---|---|
| 00-primitives.md | 5 | 3 | 9 | – | 17 |
| 01-the-principle.md | – | 3 | 4 | – | 7 |
| 04-actors.md | – | 5 | – | – | 5 |
| 09-the-measure.md | – | – | – | 1 | 1 |
| 10-the-floor-mechanism.md | – | – | – | 1 | 1 |
| 11-the-licensing-instance.md | 3 | – | – | – | 3 |
| README.md | – | – | 1 | – | 1 |
| graph/terms.yaml, claims/ | – | – | – | – | 0 |
| **Total** | **8** | **11** | **14** | **2** | **35** |

The headline: **`01` itself is clean** (also-check 1, below), **ratified canon is clean**
(also-check 2), and the S residue lives in exactly two documents — `00` (5) and `11` (3). `11`
is the sharper case: `00` at least carries a register note instructing the reader to substitute
on read; `11` has no such note, so its three uses are naked.

---

## S — self-reference (8 hits; all EDITORIAL, none in ratified canon)

All eight pass the audit's test — substituting "principle" changes no assertion. None sits
inside a canonical_md block or a claim field.

| File:line | Verbatim sentence | Proposed replacement | Class |
|---|---|---|---|
| 00:26 | "The framework has been carrying a distinction it does not need, and the distinction has been hiding what the law is about." | **None needed** — this sentence is deleted wholesale by Emil's ratified §1 rewrite (pending, recorded in the audit report's §8 supersession note). Fallback if that rewrite is not applied: "…hiding what the principle is about." | EDITORIAL |
| 00:44–45 | "**The law is not about building. It is about the requirements for making a determinate choice at all.**" | "**The principle is not about building. It is about the requirements for making a determinate choice at all.**" | EDITORIAL |
| 00:214 | "And that is *why* the law stayed invisible." | "And that is *why* the principle stayed invisible." | EDITORIAL |
| 00:227 | "**The law was always true. It was unobservable, because the demand had nowhere to go.**" | "**The principle was always true. It was unobservable, because the demand had nowhere to go.**" | EDITORIAL |
| 00:247 | "**The law does not describe how to build things. It describes what is required to determine anything at all — and what necessarily happens to a determination nobody makes.**" | "**The principle does not describe how to build things. …**" (rest unchanged) | EDITORIAL |
| 11:109 | "That is the price of covering a floor you cannot encode away — and it is exactly the price the law says must be paid somewhere." | "…and it is exactly the price the principle says must be paid somewhere." | EDITORIAL |
| 11:146 | "**The organism runs both because neither store can carry the whole demand** — the law forcing a split, not an engineering preference." | "…— the principle forcing a split, not an engineering preference." | EDITORIAL |
| 11:175 | "If the law were about engineering, it could not be here." | "If the principle were about engineering, it could not be here." (the following "It is here. So it is not." is unchanged and still lands) | EDITORIAL |

Two scoping notes for the fix:

1. **Interaction with the pending §1 rewrite.** 00:26 disappears when the ratified rewrite
   lands; a law→principle diff should be built after (or aware of) that patch so the two do not
   collide in the same lines.
2. **Consequence for `00`'s register note (00:10–13).** The note currently instructs: *where
   this document says "the law," read "the principle."* That clause is a reading patch over
   exactly these five `00` hits. Once they are substituted, the clause becomes vacuous and the
   note could shrink to its second half (the Tesler/Ashby citation licence and the rhetorical
   foil licence). Whether to shrink it is part of the fix's scope — flagged here, not proposed.

---

## C — classical citation (11 hits; must survive untouched)

| File:line | Verbatim (trimmed to the citation) | Referent |
|---|---|---|
| 00:12 | "where it refers to **Tesler's** or **Ashby's** laws" | Tesler, Ashby |
| 00:181 | "in the sense of *Tesler's Law* and *Ashby's" | Tesler |
| 00:182 | "Law* — homage, not physics (`01`, \"Register\")" | Ashby (wrapped line) |
| 01:21 | "*Tesler's Law of Conservation of Complexity*" | Tesler |
| 01:22 | "*Ashby's Law of Requisite Variety* — both of which use \"law\" as homage" | Ashby |
| 01:23 | "(Ashby) explicitly refused physical-law status even with a unit in hand" | Ashby |
| 04:21 | "**Re-indexing the classical laws by actor changes their predictions.**" | the classical laws collectively |
| 04:436 | "The classical laws are correct. They are stated for an **unexamined actor**." | ditto |
| 04:453 | "**Tesler's law cannot tell you that LLMs change where the complexity should sit.**" | Tesler |
| 04:465 | "**Ashby's law is silent on the market for variety.**" | Ashby |
| 04:528 | "…and that no classical law can produce:" | the classical laws collectively |

As predicted, `04` is dense with C and contains **no** S — its five hits are all citations of
the classical results it re-indexes. Nothing in this bucket needs touching.

---

## H — hard cases (14 hits; no wording proposed)

Three sub-shapes.

### H1 — the thermodynamics comparison (the known member): `00`:47–49

> "It reads as a law about software engineering for the same reason thermodynamics reads as a
> law about steam engines to someone standing next to one. Engineering is where we found it. It
> is not what it is about."

Two tokens in one comparison: C (thermodynamics) and S (this principle). What the passage is
doing: dissolving the misreading that the principle is about software, by analogy with a
genuine law misread as being about its discovery site. Substitution on the S side ("It reads as
a principle about software engineering") breaks the analogy's symmetry — the comparison works
*because* both sides are (or seem) laws. Constraint already established in the audit run: this
paragraph is the **only** text in `00` motivating actor-generality, and `01`'s Register section
cannot substitute (it argues measurability only) — any rewrite must preserve that motivation.

What would have to be decided: whether "**reads as** a law" already does the work — i.e.
whether the S-side token asserts law-status or only reports the *appearance* of it.
UNVERIFIED — Emil review, my reasoning: if the adjacent blockquote at 00:44 is substituted
("The principle is not about building"), the following "It reads as a law about software
engineering" arguably becomes fully coherent and even sharper — the principle merely *reads as*
a law, thermodynamics *is* one, and the sentence never asserts law-status. Under that reading
this H case needs no rewrite at all. Strike if you read "It reads as a law" as still conceding
the register.

No other hit has this two-sided shape; H1 has exactly one member.

### H2 — the register apparatus (mention, not use): 00:10, 00:11, 00:13, 00:179, 00:195, 00:198, 01:15, 01:17, 01:26, README:13

These quote, define, or legislate about the *word* — the register note (00:10–13), §5's naming
verdict ("'Conservation' and 'demand' survive; 'law' does not", 00:179), the delivery note's
deliberately-wrong quoted claim and its correction ("I have found a law governing immune
systems…" / "…careful not to call a law, because I have no unit", 00:195/198), `01`'s Register
heading, its definition of a physical law, and the ratified rule itself ("Where the word 'law'
appears in this repository, it is homage, and it is flagged", 01:26), and the README index line.
Substitution is incoherent here — you cannot substitute inside a sentence about the word — and
these lines *are* the downgrade. They survive as long as any "law" token survives anywhere.
The only decision they raise is the shrink-the-note question in S scoping note 2.

### H3 — licensed rhetorical foils: 00:158, 00:218, 01:30

| Site | Verbatim |
|---|---|
| 00:158 | "**Apply the tests or the framework becomes vacuous. A law that admits everything forbids nothing.**" |
| 00:218 | "Nobody writes a conservation law for a light switch." |
| 01:30 | "A principle that admits what it cannot prove is worth more than a law that overclaims." |

What these do: gnomic maxims whose force leans on law-as-genre — laws *forbid*, physicists
*write* conservation laws, and 01:30's whole point is the principle/law contrast. The register
note explicitly licenses this shape ("used as a deliberate rhetorical foil ('a law about X')"),
so these are pre-flagged, not residue. Substitution weakens or destroys them (01:30 becomes
circular). What would have to be decided: whether the foil licence survives the vocabulary
purge at all; if it does, these stand as-is. UNVERIFIED — Emil review: classifying 00:158 and
00:218 as licensed foils rather than S rests on my reading that their subjects are generic
("a law", counterfactual authorship) rather than a direct naming of this principle; strike and
re-bucket to S if you read them as naming it.

---

## A — ambiguous (2 hits; one named result, two sites)

| File:line | Verbatim | The two readings |
|---|---|---|
| 10:115 | "## 4. The soft-capacity law, and a corrected prediction" | **S reading:** a named result of this framework styled "law" — 01:26's rule (homage, flagged) is satisfied by neither site, so under this reading it must be renamed. **C-adjacent reading:** the referent is `p_err = H_b⁻¹(1 − r)` — Shannon's rate–distortion bound, a genuine theorem *with a unit* — so the law-ness is inherited from classical information theory, arguably homage in exactly the licensed sense (though 01:23 notes even Ashby refused the title with a unit in hand). |
| 09:256 | "…the two overflow modes, and the intersection result `escape = overflow ∩ open` with a formula in bits, plus a soft-capacity law derived from rate-distortion theory." | Same term, same two readings — one instance, two sites. |

Not guessed. Whichever way it is ruled, 01:26's rule requires *something*: either rename (the
obvious candidate is "the soft-capacity **bound**", which is also more accurate to what §4.1
derives — a lower bound — but that is a wording choice and is not proposed here) or an explicit
homage flag at both sites.

---

## Also-check findings

**1. Does `01` say it anywhere itself? No.** All seven of `01`'s hits are the Register argument
(H2), classical citations (C), or the closing foil (H3). `01`'s title, statement, and one-line
all say "principle". The ratified source of the downgrade is clean — there is no
highest-priority S hit.

**2. Ratified canon is clean.** Zero hits in `core/graph/terms.yaml` (no canonical_md contains
the word) and zero in any `core/claims/*.yaml` field. No SUBSTANTIVE-by-default S hits exist.
The entire S bucket is prose, and all of it is EDITORIAL.

**3. The retired-slogan pattern: the downgrade has no retirement record.** `03`:159 carries the
audit's exemplar ("**Retired:** the slogan *'there is no tacit knowledge in digital work.'*"),
and retired claims exist as nodes (`DDD-measure-08`, `DDD-frame-09`). The law→principle
downgrade has nothing comparable: it exists as `01`'s Register *argument*, `00`'s register
*note*, and `00` §5's naming *verdict* ("'law' does not [survive]") — an argument, a reading
patch, and a decision, but no **Retired:** marker and no claim node (verified: no claim file
contains the word "law" at all; `DDD-frame-10`'s note mentions the register only in passing).
Emil's hypothesis is confirmed by the pattern: a downgrade with no retirement record is exactly
how eight self-referential uses survived — five of them in the document that carries the
register note instructing readers to un-read them.

---

## Mechanisation note

An S/C split is mechanically approximable, not decidable. A validator pass would need: (i) the
C allowlist this survey built — possessive/named anchors (`Tesler's law`, `Ashby's law`, `Law
of Requisite Variety`, `Law of Conservation of Complexity`, `classical law(s)`, `physical-law`,
`thermodynamics` within the same sentence); (ii) a mention exemption for quoted `"law"` and for
sentences whose subject is the word (the H2 apparatus); (iii) a foil exemption, which is not
lexically decidable — H3 and H1 both turn on what the sentence is *doing*, not on nearby
tokens. Flag any remaining `\blaw` token as a **warning**, not an error: the legitimate
residual classes (foil, two-sided comparison) are exactly the ones the lexical pass cannot
clear, so an error code would either over-fire or need per-site suppression comments. It
belongs beside E13/E14 in the same lexical sweep, as a W-class code with the allowlist stored
next to the term registry. It would have caught all 8 S hits and both A sites; it would
mis-flag the 3 foils and the thermodynamics line — 11 true, 4 false, tolerable for a warning.

*(~170 words)*

---

*Classifications are mine and unratified. UNVERIFIED items flagged inline: the H1 "reads as"
observation, and the H3 foil bucketing of 00:158/00:218. Everything else is quoted verbatim
from the tree at `ba4d964`.*
