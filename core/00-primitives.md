# Primitives

<!-- ddd:contract

requires: []
establishes: [determination, decision, ground, tolerance, admission-test, actor, arrangement, last-decision|last decision in the chain]
status: settled
-->

*This document fixes the vocabulary everything else is stated in, and does no more than that. It
makes no falsifiable claim of its own — the load-bearing claims are stated, and made falsifiable,
in the documents that follow. Nothing here should be read as evidence for them.*

---

## 1. The collapse

The natural picture has two kinds of thing in it: choices, which get made, and acts, which carry
them out. On that picture the act is the primitive and the choices are the constraints wrapped
around it. Decide, then act.

**There is no act.**

"Which voltage to the motor, now" is a decision. "Which word next" is a decision. "Fire or hold"
is a decision. Descend as far as you like and you never reach a bedrock of *pure action* that
decisions merely describe. It is decisions the whole way down. What looks like *the act* is the
**last decision in the chain** — the one closest to the world, whose determination is expressed
rather than passed on.

<!-- ddd:embed id=term:last-decision -->
> The **last decision in the chain** — the one closest to the world, whose determination is
> expressed rather than passed on.
<!-- /ddd:embed -->

> **None of this is about building. It is about what is required to make a determinate choice at
> all.**

It reads as a claim about software engineering for the same reason thermodynamics reads as a claim
about steam engines to someone standing next to one. Engineering is where it was found. It is not
what it is about.

---

## 2. Two primitives

Once the act dissolves, two primitives remain.

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

Everything said later is a statement about one of these two, or about the relation between them:
where a determination is held, how much of it can be moved off whoever holds it, what corrupts
what it is resolved against, and how much evidence it has to carry. Nothing needs a third
primitive. Nothing is left over.

---

## 3. Actor and arrangement, minimally

Two nouns the rest of the argument needs early, defined here at the minimum and no more.

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

Nothing predictive is claimed here. These are the nouns; the theory that earns them comes later.

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

These tests **exclude**, and must be allowed to. A rock falling is not deciding where to land.
Describing it in choice-language is *you authoring ground, not the rock reading it* — it inspects
nothing, nothing it "reads" could vary and change what it does, and there is no substrate against
which it resolves anything. It fails both tests.

**Apply the tests, or the vocabulary becomes vacuous: a predicate that admits everything forbids
nothing.**

---

## 5. The one line

> **This is not an account of how to build things. It is an account of what is required to
> determine anything at all — and of what necessarily happens to a determination nobody makes.**
