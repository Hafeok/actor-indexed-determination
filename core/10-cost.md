# Cost

<!-- ddd:contract

requires: [act, actor, demand, judgment, escape, acceptance-predicate, closure|closes|closing, verdict, tolerance, assurance, admission-test]
establishes: [cost-register|cost register, standing-cost|standing cost, occasioned-cost|occasioned cost, capability]
status: settled
-->

**A cost note.** Reproduction script in `core/assets/measure-mdl-demo.py`. Empirical basis filed in
`meta/mdl-cost-manufacturing-assessment-2026-08-08.md`.

**Claims.** The propositions of this note are landed as claim nodes under `core/claims/`
(`DDD-cost-*`); canon authority for each is its claim file, and this document is their exposition.
The mapping:

| Section | Proposition | Claim | Status |
|---|---|---|---|
| §1 | Bits are per-act on both sides; the asymmetry is locus of supply | `DDD-cost-01` | projected |
| §3 | Degeneracy: standing cost linear in `I(V;E)` cannot price distinctions apart | `DDD-cost-02` | reported (arithmetic) |
| §4 | Rate-split: description length prices the standing side, entropy the occasioned side | `DDD-cost-03` | projected |
| §5 | Capacity = bits suppliable per act; escape = residual exceeding capacity | `DDD-cost-05` | projected, named next result |
| §6 | Actor selection is two-gated: capacity always; assurance where the predicate does not close | `DDD-cost-08` | projected |

Where this prose and a claim disagree, the claim governs and the prose is the bug.

**Charter.** This note is synchronic: every quantity in it is a per-act rate, and no statement in it
requires anything to persist between acts. Quantities that do — act volume, crossover volumes, the
optimisation of supply across acts — are outside this repository's charter, per the boundary-charter
ruling recorded in `DDD-dec-09`; that decision also records where each relocated piece of the
earlier, wider note now lives.

**Status.** `09` states a conserved quantity; this note states what is priced. The registers stay
separate deliberately: cost is **not** conserved — `L(mechanism)` has no conservation identity.
Nothing here amends the demand identity; everything here is layered on it.

---

## 1. The register split: demand is conserved, cost is not

The demand identity (`09` §2) is per-act on both sides:

> **H(verdict) = I(verdict;E) + H(verdict|E)** — per act, every term.

The two sides denominate in the same unit — bits of one act's verdict — and differ only in **locus
of supply**. `I(V;E)` is supplied by a **standing artifact**: a mechanism built before any act,
paid for once, present for every act thereafter. `H(V|E)` is supplied by a **contemporaneous
event**: an actor's judgment spent at the act, again at the next act, amortising never.

<a name="cost-register"></a>That difference in locus is what a **cost register** prices and the
demand register cannot see. Write **standing cost** for the price of building and holding the
artifact, and **occasioned cost** for the price of the per-act event — both rates, denominated at
the act. The demand identity fixes, for every candidate encoding `E`, how much of the verdict each
side must supply. Demand says what must be supplied; cost says what supplying it that way is worth.
*(Claim `DDD-cost-01`, projected; falsifier: a case where the two sides of the identity denominate
differently.)*

---

## 2. Cost model 1: standing cost as captured information

The obvious first model prices the standing side by what the encoding captures: standing =
`I(V;E)`. It is wrong, and the way it is wrong is the load-bearing result of this note.

---

## 3. The degeneracy — and what pricing distinctions apart requires

Under model 1, conservation forces the tradeoff flat. For any two encodings, ΔI = −ΔR exactly —
the identity permits nothing else — so every distinction removes precisely as many occasioned bits
as it adds standing bits. Priced in captured information, every distinction has the same density —
one bit of residual removed per standing bit added, identically, across the whole frontier — and
**a cost model linear in captured information cannot price one distinction ahead of another.**
This is an identity consequence, not an observation — *reported as arithmetic*, exercised end to
end by `measure-mdl-demo.py` (all inter-encoding densities 1.000 on the date task). *(Claim
`DDD-cost-02`.)*

The consequence runs forward: **pricing distinctions apart requires standing cost priced as
mechanism description length, not captured information.** `L(mechanism)` is not a conserved
quantity, so it can differ per distinction — which is exactly what the demand register, where
everything is forced to sum to `H(V)`, is structurally unable to express. Also reported as
arithmetic, per the degeneracy.

---

## 4. The rate-split

The non-degenerate pricing takes the two sides at different rates:

> **Description length prices the standing side; entropy prices the occasioned side** — MDL's
> `L(model)` and `L(data|model)`, with the model the mechanism the arrangement stands up, and the
> data the residual verdicts its actor must supply at the act.

The correspondence is a modelling claim, **projected**, and its per-act discriminating prediction
is the **occasioned floor**: under any finite mechanism the residual `H(V|E)` reaches zero only
when the acceptance predicate closes and the mechanism carries the whole verdict; short of that,
the per-act occasioned cost is bounded below by a non-zero floor. Falsifier: occasioned per-act
cost driven to zero under a mechanism short of closure.

**Empirical basis, filed and graded** (`meta/mdl-cost-manufacturing-assessment-2026-08-08.md`):
the public manufacturing data is abundantly consistent with the generic two-part form but was
never collected to discriminate the MDL form. The experience-curve meta-analyses are structurally
floor-free — pure power laws, a floor term never tested — so the strongest datasets are silent on
the floor; within-part moulding cost-vs-volume data is the accessible discriminating test; and no
prior MDL-to-manufacturing-cost application was found. The correspondence is therefore projected
on basis, not reported. *(Claim `DDD-cost-03`.)*

---

## 5. Capacity and escape, named

The cost register gives capacity its per-act denomination: **capacity is the bits an actor can
supply per act; escape is the residual exceeding it.** Where `H(V|E)` — the occasioned side — is
greater than what the actor can supply at the act, the excess is supplied by nobody, and the
demand escapes. Projected and **named as the next result**: the model that earns it lands with the
floor-mechanism work (`11`), where hold and resolve capacity already have their bits. *(Claim
`DDD-cost-05`.)*

---

## 6. Actor selection: the two gates

Acts differ in residual demand `H(V|E)`; actors differ in what they can supply per act and in the
assurance their class carries. Selection of the actor for the act is governed by two gates, and
the gates cover different regions of the act:

- **Capacity gates always.** The actor must carry the act's residual at the declared tolerance,
  or the excess escapes (§5).
- **Assurance gates where the predicate does not close.** Where a property is checked, producer
  identity is not epistemically necessary for it (`DDD-frame-05`; `07` §2) — assurance discharges
  through the check, and actor choice above the capacity bar is free there. The contrapositive is
  the gate: **for every unchecked property, producer identity is load-bearing**, so assurance
  must attach to the actor — qualification, track record, certification, class. Actor assurance
  is what fills the space mechanical verification vacates: check the work where you can; check
  the worker where you cannot check the work. Mixed acts split — check what closes, select for
  the rest.

This is what legitimises cheapest-sufficient routing where predicates close, and only there.
Selection additionally carries **tail-risk assurance**: a checker vouches for the acts it sees; a
selected actor is vouched for on the acts nobody foresaw — low variance under conditions no
output-check would have exercised. That is part of what a higher class buys, and why selection
persists even where predicates mostly close. The tendency in pure form is the soldier: no mid-act
verification is possible, so assurance is pre-paid entirely into selection, and the class of
soldier is the assurance mechanism. *(Claim `DDD-cost-08`, projected.)*

Routing requires per-act demand and per-act assurance need to be declared — which the acceptance
predicate and the declared tolerance already provide in a governed arrangement. **Actor selection
is downstream of predicate discipline, not a separate practice.**

---

## 7. Capability: typing the capacity

Capacity (§5) is not a scalar.

<!-- ddd:embed id=term:capability -->
> A **capability** is a typing over an actor's pathways: the class of ground a pathway can
> read — visual, repository, physical, tool-mediated — and the class of distinctions it can
> resolve against it. Not a third primitive: it classifies the two primitives' traffic.
<!-- /ddd:embed -->

The requirement side derives from the admission test (`00` §4), applied per ground type:

> **An act requires capability X iff its verdict varies with ground accessible only through
> X-type pathways.**

Grounded, exclusionary, no free parameter. `04`'s capability envelope is this typing read
per-actor: the envelope is an actor's profile of classes across capabilities.

---

## 8. Reproduce

One self-contained script regenerates every figure in this note:

- `assets/measure-mdl-demo.py` — the frontier, the degeneracy (§3: all inter-encoding densities
  1.000), the separation of distinctions under description-length pricing, and the residual-floor
  check (§4), on the `09` §3 date task.

Coefficients are stipulated, not measured. The script exercises the projected rate-split; it does
not and cannot confirm the correspondence.
