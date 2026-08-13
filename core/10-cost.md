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
| §5 | Capacity = bits suppliable per act; the model's escape term = residual exceeding capacity | `DDD-cost-05` | projected, named next result |
| §6 | Actor selection is two-gated: capacity always; assurance where the predicate does not close | `DDD-cost-08` | projected |
| §6 | Closure converts a property's assurance supply from occasioned to standing | `DDD-cost-09` | projected |
| §6 | The sign flip: closure reverses the assurance–class coupling, bounded by coverage | `DDD-cost-11` | projected |
| §7 | Required class = max over the act's capabilities where assurance is not discharged | `DDD-cost-12` | projected |
| §7 | Answer-keyed instruments evidence declared-predicate class only, never open carriage | `DDD-cost-13` | projected |
| §6 | Tempo prunes assurance positions: latency over budget forces assurance pre-act | `DDD-cost-25` | projected |
| §8 | Around/within: encoding loci differ; training buys allocation, not capacity | `DDD-cost-20` | projected |
| §9 | The claim layer is governed by the same two gates | `DDD-cost-22` | projected |

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
supply per act; the model's escape term is the residual exceeding it.** Where `H(V|E)` — the occasioned side — is
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

**Closure converts the locus of assurance supply.** Assurance-by-actor binds assurance to a
scarce carrier, supplied occasioned — at the act, at the carrier's class price. Assurance-by-check
moves it into a mechanism, supplied standing — independent of the act. Closing a predicate
converts a property's assurance supply from occasioned to standing. *(Claim `DDD-cost-09`,
projected.)* The conversion is an economic argument for predicate discipline: carrier-borne
assurance is characteristically the costliest occasioned supply, and closure is what moves it off
the carrier. The soldier again, synchronically: a high-assurance act with no check available
leaves carrier class carrying the assurance at act time — the conversion is exactly the move that
is unavailable there. This claim governs the *locus* of assurance supply; the *class* consequences
of the conversion are the sign flip's, below — adjacent, not identical.

**Closure flips the sign of the assurance–class coupling.** On an open predicate, assurance and
actor class are positively coupled: the more assurance the act needs, the higher the class,
because the carrier is the assurance mechanism. Closure reverses it: high assurance becomes a
reason to encode into the mechanical store, and the required class falls — the actor is left
carrying generation only. Two distinct mechanisms do the lowering: **(i) the assurance gate
lifts** — assurance discharges through the check, and producer identity stops being load-bearing
for the checked property (`DDD-frame-05`); **(ii) the capacity gate softens** — a checker permits
generate-and-test, so a weaker actor with retries and verification composes into effective
capacity exceeding its own; verification converts capacity shortfall into retry cost, borne as an
expectation over the act (`09` §1, nesting). *(Claim `DDD-cost-11`, projected.)*

The flip is bounded, and the bounds are the claim's region:

- **Acceptance-region accessibility still gates generation.** A checker cannot make a weak actor
  find a sparse candidate; the move works where the acceptance region is dense and retries cheap.
- **Retry economics enter the routing.** Weak actor × expected retries × per-act price against
  strong actor × one shot — a computable crossover. Rich rejection payloads shift it: a check
  that explains its rejection turns each retry into a guided step, raising the weak actor's
  effective capacity.
- **Unchecked-property degradation — the safety bound.** High-class actors silently supply
  assurance on properties nobody declared. Downgrade the class and everything outside the
  predicate's coverage degrades without a signal. **Class may fall only as far as the predicate's
  coverage of the act's assurance actually extends.** Skipped, the move is an escape-mode
  generator, not an optimisation.

**Tempo prunes assurance positions.** Assurance mechanisms occupy temporal positions relative
to the act — pre-act (selection, training, encoding, static checks), at-act (monitoring),
post-act (review, audit, consequence) — each with a latency. A mechanism whose latency exceeds
its position's budget — the episode for at-act mechanisms, the consequence horizon for post-act
ones — cannot hold its position, so rising tempo, which compresses both budgets, forces
assurance pre-act, into standing supply or the carrier. *(Claim `DDD-cost-25`, projected.)*
This names the mechanism in the soldier case: no review fits inside the act, so all assurance
is pre-paid into selection.

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

The routing rule (§6) sharpens to a maximum over the vector:

> **Required actor class = the maximum, over the act's capabilities, of the class needed where
> assurance is not mechanically discharged — per capability, not per act.**

One uncovered high-class capability pins the act to the highest class even when everything else
about the act is trivial — the **frontier pin**. Where mechanical coverage of a capability is
partial, the assurance residual attaches to that capability specifically, and the sign flip (§6)
has not occurred for that component: high class is being bought as assurance on everything the
checks do not reach. Close the coverage and the pin releases — **the class saving is gated on
coverage of the binding capability, not on the actor improving.** *(Claim `DDD-cost-12`,
projected; single-domain basis flagged per `DDD-dec-12`.)*

**Bundled pricing buys the vector.** An actor of high class across many capabilities prices as a
bundle; an act with one binding capability pays for all of them. Capability-specialised actors
are the market unbundling this — and evidence for the typed view, since scalar capacity cannot
explain narrow-high beating general-mid on matched acts. The confound, carried honestly:
capability levels within an actor correlate strongly — a general factor — which is why a single
class label works at all. The typed claim earns its keep at the margins where profiles diverge.

**The selection instrument, and its bound.** Where assurance attaches to the actor per
capability, an answer-keyed qualification instrument — an examination, an eval — evidences
demonstrated class on predicates that close. Its verdict cannot evidence open-predicate
carriage: the instrument's own predicate closes while the target predicate does not, so
delegation to the open predicate substitutes the actor's identity for exactly the check the
instrument cannot be. *(Claim `DDD-cost-13`, projected.)* This is why certificates are not
licences for open work: the certificate demonstrates class where checks exist, and the actor is
being selected precisely for where they do not (`DDD-frame-05`'s contrapositive, per §6). The
complementary instrument for open-predicate carriage — a record of matured verdicts — is
pending, and files with the ledger layer's calibration construct.

---

## 8. Around and within: the carrier's two encodings

Standing supply relates to a carrier at one of two loci. **Around-encoding** — context,
retrieval, scaffolds — is standing supply outside the carrier, delivered through the channel at
each act. **Within-encoding** — training — converts judgment allocation to encoded allocation
inside the carrier. **Training buys allocation, not capacity: it does not enlarge the judgment
store.** *(Claim `DDD-cost-20`, projected.)*

Two precision points, carried from the session's corrections. Ownership of the carrier does not
create a principal; it adds the **control linkage** — weights, training data, and change record
governed, in `05`'s accountability register. And the locus distinction is per-act: which path an
arrangement should take quantifies over act volume and closure, and files with the projection
layer.

---

## 9. The claim layer: the same two gates

A claim is an act with a deferred verdict (`09` §1; claim `DDD-frame-12`) — so the routing rule
of §6 applies to it with no new mechanism. *(Claim `DDD-cost-22`, projected.)*

- **Instrument toward closure** where the horizon permits: declared falsifier, metric, horizon.
  Coverage investment on claim predicates obeys the same economics as coverage on any predicate;
  its volume form files with the projection layer.
- **Carrier assurance** where it does not: assurance attaches to the claimant by demonstrated
  class. The instrument bound of §7 applies with full force here — **an answer-keyed instrument
  cannot certify carriage of a deferred-verdict claim** (`DDD-cost-13`): the instrument's
  predicate closes at examination time, and the claim's verdict has not arrived. The instrument
  class for this gate is a record of matured verdicts — pending at queue item 2.12.

Demand does not leave the claim layer when tooling ignores it; it escapes there — verification
investment points at the layer below, and the claims ride ungoverned above it. Mixed inventories
split, exactly as mixed acts do: instrument what can close, select claimants for the rest. A
third disposition exists and is out of the gates' scope: **declared risk acceptance** — a claim
knowingly carried unassured is governed, not escaped; the gates cover assurance, not the
decision to go without it.

---

## 10. Reproduce

One self-contained script regenerates every figure in this note:

- `assets/measure-mdl-demo.py` — the frontier, the degeneracy (§3: all inter-encoding densities
  1.000), the separation of distinctions under description-length pricing, and the residual-floor
  check (§4), on the `09` §3 date task.

Coefficients are stipulated, not measured. The script exercises the projected rate-split; it does
not and cannot confirm the correspondence.
