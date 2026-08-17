# Primitives

<!-- ddd:contract

requires: []
establishes: [determination, decision, ground, tolerance, admission-test, actor, arrangement, last-decision|last decision in the chain, poisoned-ground|poisoned ground, granularity-bound|granularity bound, encode-verify-split|encode/verify split, act, determinable, determinate]
status: settled
-->

*Register note: the framework's own claim is a principle, not a law (see `01`, "Register"). The
word "law" is retained below only where it refers to **Tesler's** or **Ashby's** laws, or is used
as a deliberate rhetorical foil ("a law about X").*

**Status:** the reframing is a clarification, not a new claim. It changes nothing about what the
principle asserts, only about what it is understood to range over. The load-bearing claims are
stated and made falsifiable in their own documents — `01` states the conservation principle, and
`02` the exhaustiveness of the four stores. Nothing in this document should be read as evidence
for those.

---

## 1. The collapse

**There is no act beneath the decisions.**

It is tempting to treat the act as the primitive and decisions as the
specification wrapped around it: decide the constraints, then act. But
"which voltage to the motor, now" is a decision. "Which word next" is a
decision. "Fire or hold" is a decision. Descend as far as you like and you
never reach a floor of pure action that decisions merely describe. It is
decisions the whole way down. What looked like the act was the last
decision in the chain — the one closest to the world, whose determination
is expressed rather than passed on.

<!-- ddd:embed id=term:last-decision -->
> The **last decision in the chain** — the one closest to the world, whose determination is
> expressed rather than passed on.
<!-- /ddd:embed -->

> **The principle is not about building. It is about the requirements for making a determinate choice
> at all.**

It reads as a law about software engineering for the same reason thermodynamics reads as a law
about steam engines to someone standing next to one. Engineering is where we found it. It is not
what it is about.

The collapse removes the act as a floor. It does not remove the act as a unit. The chain
terminates: the last decision is expressed, an outcome exists, and the outcome is judged.
Reclaim the name for that bounded episode.

<!-- ddd:embed id=term:act -->
> The **act** — the bounded episode of determination running from its first governing
> decision to an expressed outcome; the unit demand is counted in. Derived, not primitive:
> an act is decisions resolved against ground. Its exact individuation is earned in `09` —
> one verdict, one act, where the measure exists.
<!-- /ddd:embed -->

There is no act *beneath* the decisions. There is an act *made of* them. The document
already knew this: the encode/verify split is stated relative to the act, and the
admission tests presuppose an outcome to judge.

---

## 2. Two primitives

Once the act dissolves, the framework has exactly two primitives.

<!-- ddd:embed id=term:decision -->
> **Decisions** — the things determined.
<!-- /ddd:embed -->
<!-- ddd:embed id=term:ground -->
> **Ground** — what they are determined against.
<!-- /ddd:embed -->

That is the whole ontology. Every act of determination — by rule, by check, or by an actor in
the moment — **reads ground in order to resolve a choice.** There is no third thing.

<!-- ddd:embed id=term:determination -->
> **Determination** is the resolving of a decision against ground — by a rule, a check, or an
> actor in the moment. Nothing else resolves anything.
<!-- /ddd:embed -->

The apparatus holds against this without strain:

| Apparatus | A statement about |
|---|---|
| The four stores (`01`) | *where the determination lives* |
| The Polanyi floor | *how much determination can be moved off an actor* |
| The seam-demand identity (`06`) | *decisions created between decomposed decisions* |
| Poisoned ground | *corrupting what a determination reads against* |
| The encode/verify split | *dividing demand between encoding before the act and verifying after it* |
| Tolerance | *which choices count as decisions at all* |
| Assurance (`01`) | *how much evidence the allocation must carry* |

<!-- ddd:embed id=term:poisoned-ground -->
> **Poisoned ground** — ground that is present but false: the substrate a determination reads has
> been corrupted, so a correct determiner resolves wrongly with full authority. The logic is
> sound; the ground is the attack surface.
<!-- /ddd:embed -->

<!-- ddd:embed id=term:encode-verify-split -->
> The **encode/verify split** — the division of a determination's demand between pre-resolving
> ground into the encoded store before the act and verifying the residual mechanically after it.
<!-- /ddd:embed -->

Nothing needs a third primitive. Nothing is left over. The act (§1) is not a third; it is
composed of the two.

---


---

## 3. Actor and arrangement, minimally

Two nouns the consequences need early, defined here at the minimum and no more. The theory that
earns them waits for its documents: pinning resolution, selection and training in `04`, the
accountability conditions in `05`.

<!-- ddd:embed id=term:actor -->
> An **actor** is a system that resolves decisions by reading ground: variation in declared
> ground can alter the resolution through an internal pathway that selects among
> alternatives. A thermostat qualifies; a falling rock does not. Actorhood does not require
> intelligence.
<!-- /ddd:embed -->

<!-- ddd:embed id=term:arrangement -->
> The **arrangement** is the composition through which a resolution is produced and governed:
> executor, prior commitments, ground channels, checks, reviewers, record, and accountable
> principal. The unit of comparison is the arrangement, not the isolated actor.
<!-- /ddd:embed -->

Nothing predictive is claimed here. These are the nouns; the theory is downstream.

---

## 4. The admission tests

This generalisation is dangerous, and the danger is precise: *"the act is a decision"* is one
step from *"everything is decisions,"* which explains nothing because it excludes nothing.

**"Makes a determinate choice against a substrate" must remain a real predicate, not a universal
solvent.**

<!-- ddd:embed id=term:admission-test -->
> **A choice is a decision iff varying *the choice* moves the outcome past tolerance.**
>
> **A fact is ground iff varying *the world* moves the outcome past tolerance.**
<!-- /ddd:embed -->

Same tolerance, same granularity bound; two different things varied.

<!-- ddd:embed id=term:tolerance -->
> **Tolerance** is the declared boundary of acceptable outcome deviation. It indexes
> everything: a choice is a governing decision, and a fact is ground, only relative to a
> declared tolerance. Without one, the decision set is not well-formed.
<!-- /ddd:embed -->

<!-- ddd:embed id=term:granularity-bound -->
> The **granularity bound** — the tolerance-indexed criterion fixing which choices enter the
> governing set: a choice is a governing decision iff varying it moves the outcome past the
> declared tolerance.
<!-- /ddd:embed -->

These tests **exclude**, and must be allowed to. A rock falling is not deciding where to land.
Describing it in choice-language is *you authoring ground, not the rock reading it* — it inspects
nothing, nothing it "reads" could vary and change what it does, and there is no substrate against
which it resolves anything. It fails both tests.

**Apply the tests or the framework becomes vacuous. A law that admits everything forbids
nothing.**

---

## 4a. The determinable

What do the tests admit choices *over*? Varying a choice presupposes a dimension along which it
varies, and a tolerance presupposes a grain at which variation counts. That object has a name,
and the name is a century old (W. E. Johnson, *Logic* Part I, ch. XI, 1921).

<!-- ddd:embed id=term:determinable -->
> The **determinable** — an outcome-relevant dimension of variation at the declared
> tolerance: the object determination resolves, and the dimension of comparability an axis
> names. Determinateness comes in orders — red → scarlet → this shade — and the declared
> tolerance names the order at which the framework stops distinguishing.
<!-- /ddd:embed -->

<!-- ddd:embed id=term:determinate -->
> The **determinate** — one specific way of occupying a determinable: what discharge
> produces. A determinate is a way of being, not the determinable plus a differentia, and
> determinates under one determinable are constitutively exclusive at their grain.
<!-- /ddd:embed -->

Four structural facts travel with the name, each landing on something already built. The
relation is **not genus–species**: scarlet is a way of being red, not red plus a differentia —
an axis is a dimension with a range, never a class hierarchy. Determinates under one
determinable are **constitutively exclusive**: nothing is scarlet and crimson at the same grain,
which is what lets one resolution settle a determinable. Determinateness comes in **orders**,
and the declared tolerance names the order at which the framework stops distinguishing — ±50 m
and ±0.5 m are different tasks by order, not degree. And the determinable is the **dimension of
comparability** — what makes two resolutions comparable at all.

The stack downward is then short: a decision is a determinable taken up by governance; a
determination is the passage from determinable to determinate; and what no governance takes up
is still a determinable — resolved, when its act completes, by whatever resolves it.

**Constitutive priority follows.** A determination selects a determinate, and determinates exist
only as ways of occupying a determinable, so declaring the determinable space precedes any
determination over it. The symmetry keeps this from circling: within each act, ground is prior;
in a registry's growth, decisions are prior — dimensions enter by naming rulings. One relation
is constitution, the other is history. *(Claims `DDD-frame-13` and `DDD-ground-05`, projected;
their files govern, and this prose is exposition.)*

---

## 5. The name

*Full treatment: `01-the-principle.md` ("Register").*

The reframing forces a naming question, and the answer is a **two-level structure**, not a
replacement — and, after external review, a **downgrade of register.**

**"Specification" is a domain word.** It means *the thing you write down before you build*. An
immune system has no specification; a market has no specification. Using it in the general
statement drags the reader back into the engineering frame the principle is not confined to, and
invites the misreading that the principle is about *documents* — the error behind "CMSes are going
away."

**"Conservation" and "demand" survive; "law" does not.** Conservation is the load-bearing claim.
Demand means *what must be supplied*, agnostic about who supplies it. But **there is no measured
quantity**, so the correct register is **principle**, in the sense of *Tesler's Law* and *Ashby's
Law* — homage, not physics (`01`, "Register").

So the two-level structure is:

> ### The Conservation Principle of Determination Demand
> *(`core/` — actor-general. Ranges over anything that determines choices against ground.)*
>
> ### Conservation of Specification Demand
> *(the **engineering projection** — the same principle, denominated in the vocabulary of a domain
> where determinations are called specifications.)*

**Specification is what determination demand is called when the actor is building software.**

*A note on presentation.* "I have found a law governing immune systems, markets, and your codebase"
earns the skepticism it will receive. "Here is a conservation *principle* in software engineering —
which turns out to be the projection of something more general, and which I am careful not to call
a law, because I have no unit" is the same claim in the order, and the register, that earns belief.

---


---

## 6. Why it was not written down

*This section explains. It does not argue. A good story about why nobody found your idea is exactly
the kind of thing that feels like evidence and is not. Do not cite it as though it were.*

The obvious account — *we only had humans in the choice-making category* — is close, and not quite
right.

**Classical programs were always actors**, degenerate ones, every decision pre-made at authoring
time. And that is *why* the principle stayed invisible. A program **cannot take** an unallocated
decision; its judgment store is fixed at zero. So the allocation question had two answers: encode
it, or a human carries it. Not a spectrum. **A light switch.**

Nobody writes a conservation law for a light switch.

What appeared is narrower and sharper than "a second actor." It is the **first actor pinnable by
binding** — non-deterministic, but with a distribution that can be frozen. For the first time, the
judgment store has a **carrier that is neither a person nor zero.**

The allocation became **continuous**. Demand can now sit anywhere on the spectrum, placement is a
real choice with real prices, and — decisively — **it can be got wrong in ways that look right.**

> **The principle was always true. It was unobservable, because the demand had nowhere to go.**
>
> **A conserved quantity is invisible until something moves.**

The same shape as the CMS correction: build cost collapsed and revealed that *specification* had
been load-bearing all along. Here, the actor spectrum opened and revealed that *allocation* had
been load-bearing all along. Nothing became true. Something became **visible**, because a cost that
had pinned everything in place stopped.

Which accounts for the surrounding fields holding the pieces without assembling them. Polanyi had
the floor without the stores. Software engineering had specification without conservation.
Counterintelligence had poisoned ground without knowing it generalised. Immunology had all four
stores and no reason to call them that. Each field found the fragment its own domain made visible —
and **assembly requires seeing the quantity move**, which nothing could, until a binding-pinned
actor existed to move it.

---

## 7. The one line

> **The principle does not describe how to build things. It describes what is required to determine
> anything at all — and what necessarily happens to a determination nobody makes.**
