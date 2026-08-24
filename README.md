# Actor-Indexed Determination

> **Where you cannot check the work, check the worker.**

A framework for deciding **where determinations are supplied, how they are assured, and who answers for them** — at the level of individual decisions rather than whole jobs.

It applies to any arrangement that determines choices against ground: programs, models, humans, organisations, markets, immune systems, and compositions of them.

\---

## The problem

**Who does the work?**

Every organisation has had to answer this, and the instruments for answering it all make the same move: where you cannot check the work, check the worker.

Grade, seniority, licence, certification — each is a standing claim about a supplier, used where the output itself cannot be verified directly.

That move worked while unverifiable work had only one practical kind of answerer: a person whose identity could carry assurance beyond the act itself. Classical programs could determine, but only what had already been fixed for them. They could not take the residual judgment for which the worker's identity was the assurance mechanism.

There is now another kind of determiner, and the old instruments do not transfer cleanly.

A licence is worth something because the licensed person outlives the claims they make and can remain answerable for them; today's model deployments generally do not provide that continuity. A grade is informative because human capability is correlated broadly enough for classification to carry useful information across cases; model capability is sharply uneven — superhuman in one region and incompetent in the one beside it. And a credential is issued by an institution that carries stake in what it certifies. A benchmark can provide evidence about performance on the predicate it checks, but it issues no standing, carries no consequence, and answers for no later determination.

The question therefore needs a smaller unit.

**Work decomposes into decisions.**

Ask, for each decision:

1. **What must be determined?**
2. **What ground does the determination depend on?**
3. **Can the result be checked?**
4. **From where is the determination supplied?**
5. **Who carries the consequence if it is wrong?**

Every determination can still be delegated to a person. What changes is that the allocation is made **per decision rather than per job**.

Where the work can be checked, assurance can attach to the check rather than to the identity of the worker. Where it cannot, the worker — or more precisely the arrangement that authorises the determination — remains load-bearing.

Different allocations therefore carry different costs, different assurance, different residual discretion, and different answers to who is accountable.

> **The framework does not tell you which to choose. It tells you what you are choosing between, and it makes the choice one you make on the record.**

\---

## The model

The framework begins with two primitives:

> **Decisions** — the things determined.  
> **Ground** — what they are determined against.

A **determination** is the resolving of a decision against ground.

An **actor** is a system capable of performing such a resolution. Actorhood does not imply intelligence: a thermostat qualifies; a falling rock does not.

An **arrangement** is the larger composition through which a resolution is produced and governed: executor, prior commitments, ground channels, checks, reviewers, record, and accountable principal.

The unit of analysis is therefore not simply a task, nor simply an actor.

Unresolved determination is indexed by:

> **⟨task, ground, acceptance relation, tolerance, arrangement, assurance⟩**

Change one coordinate and the determination problem may change with it.

This is the fuller meaning of **actor-indexed determination**: the determiner is not a constant hidden inside the task. It is a parameter of the arrangement.

See [`core/00-primitives.md`](core/00-primitives.md) and [`core/14-indexed-determination.md`](core/14-indexed-determination.md).

\---

## The four stores

Every governing determination is supplied from one of four places:

|Store|Source|When|Character|
|-|-|-|-|
|**Encoded**|a rule|before the act|paid in advance; amortises|
|**Mechanical**|a check|after the act|expensive to construct; cheap to trust|
|**Judgment**|an actor reading ground|during the act|paid per run|
|**Escaped**|nobody|never|latent defect exposure|

In shorthand:

> **{rule, check, actor, nothing}.**

There is no fifth source.

The partition is deliberately definitional. Its value is not that four stores were "discovered"; its value is that the fourth store makes **decided by nobody** visible as an allocation state.

Redundancy is allowed. A decision may be constrained before the act and checked afterwards.

The forbidden condition is not redundancy.

It is **uncovered demand**.

> **Every governing decision gets made. The only forbidden outcome is the one made by nobody.**

See [`core/01-the-principle.md`](core/01-the-principle.md) and [`core/02-completeness.md`](core/02-completeness.md).

\---

## The central result: check the work or check the worker

The framework's most important result concerns the **acceptance predicate**: the criterion by which an outcome would be judged acceptable.

The irreducible judgment floor is not a property of how "difficult" a task is.

It is a property of whether adequacy can be checked.

> **The floor is non-zero exactly when, and because, you cannot check the work.**

Where the acceptance predicate **closes for the arrangement** — relevant ground is observable and adequacy can be evaluated within the required resource, latency, confidence, and assurance bounds — no particular determiner is required for trust. Different paths may produce acceptable outputs because the result itself can be checked.

Where the predicate does **not** close, that route to assurance disappears.

Verification moves from the output toward the supplier:

> **You cannot check the work, so you check the worker.**

This explains why organisations use licences, qualifications, grades, track records, certification, institutional standing, and selection.

They are not merely descriptions of capability.

They are **assurance instruments used where direct result-level evidence is unavailable**.

See [`core/03-the-floor.md`](core/03-the-floor.md), [`core/04-actors.md`](core/04-actors.md), and [`core/10-cost.md`](core/10-cost.md).

\---

## Why models change the allocation problem

Classical programs and humans already occupied opposite ends of an old allocation:

* a **program** can be pinned tightly, but only to what has been fixed for it;
* a **human** can carry unanticipated judgment, but can only be pinned loosely through selection, qualification, procedure, and accountability.

Models introduce a third useful form of commitment.

A program can be pinned **by value**.

A model can be pinned **by binding**.

A human can be pinned **by classification**.

A frozen model is therefore unlike both a traditional program and a person: its behaviour can be bound to a repeatable distribution without being reduced to a predetermined answer.

That makes the allocation problem continuous where it was previously much closer to a switch.

But actor type alone is still too coarse.

The arrangement may commit at several levels:

|Commitment level|What is fixed in advance|
|-|-|
|**Outcome**|permitted resolutions|
|**Policy**|the procedure producing the resolution|
|**Principal**|the determiner authorised to resolve the case|

These levels compose.

What remains after those commitments is **residual discretion**: outcome-relevant variation genuinely left open at the act, holding ground fixed.

The practical question is therefore not:

> \*Should a human or an AI do this job?\*

It is:

> **For this decision, what has already been committed, what remains open, what can be checked, what arrangement can carry the residual, and who answers for it?**

See [`core/04-actors.md`](core/04-actors.md) and [`core/14-indexed-determination.md`](core/14-indexed-determination.md).

\---

## Accountability is separate from execution

Producing a determination and being accountable for it are different roles.

The **executor** makes the determination this run.

The **accountable party** carries the consequence afterwards.

For human work these roles have often coincided, which made the distinction easy to miss. Model execution makes the separation unavoidable.

A well-formed accountability arrangement requires:

* **attribution** — a record connecting the determination to its execution;
* **persistence** — a responsible principal that survives long enough for consequences to land;
* **stake** — something capable of bearing the consequence;
* **sanctionability** — a path by which the consequence can actually be applied.

So:

> **A judgment allocation naming no accountable party is not an allocation. It is Escaped with an executor attached.**

Today's accountability towers generally terminate at an operator, owner, institution, vendor, or other principal rather than at the model itself.

That is contingent, not metaphysical. The framework does not claim models could never participate in an accountability-bearing arrangement.

See [`core/05-accountability.md`](core/05-accountability.md).

\---

## Composition creates seams

Splitting work does not make determination demand disappear.

It creates new determinations at the interfaces between the parts.

These are **seam demand**.

A composite therefore carries the demand of its members **plus the demand created by coordinating them**.

That seam must itself be allocated:

* to an **actor** — an orchestrator carrying judgment;
* to an **encoded mechanism** — fixed coordination rules;
* to a **mechanical check**;
* or to **nobody**, in which case it escapes.

This gives a concrete trade:

> **Actor-at-seam buys adaptivity and pays with a bottleneck and a poisonable centre.**  
> **Mechanism-at-seam buys scale and robustness and pays with rigidity.**

The framework's **compound** is the loop that watches recurring judgment, harvests it into encoding, and pairs that encoding with a check.

The asymptote is the floor: the residual whose acceptance predicate still does not close.

See [`core/06-composition.md`](core/06-composition.md).

\---

## The measure

For the region in which the acceptance predicate closes, the informal conservation principle admits an exact information-theoretic construction.

Let `V` be the verdict induced by the task over the ground distribution.

Then determination demand is identified as:

> **D = H(V)**

measured in bits.

For any admissible encoding `X`:

> **H(V) = I(V;X) + H(V|X)**

Read through the framework:

* `H(V)` — total determination demand;
* `I(V;X)` — demand already captured by the standing side;
* `H(V|X)` — residual demand left at the act.

For a decomposition `S`:

> **H(V) = I(V;S) + H(V|S)**

so the information absorbed by the decomposition is the seam term.

A "better" decomposition does not destroy demand. It **pre-pays more of it into the seam**, leaving cheaper parts.

This construction is exact once the framework's quantities are identified with the information-theoretic ones.

It has a hard boundary:

> **Where the acceptance predicate does not close, there is no verdict function with the required ground truth, so `H(V)` is undefined.**

The measure does not cross the floor.

That is a limit of the framework, not a quantity silently assumed to exist.

See [`core/09-the-measure.md`](core/09-the-measure.md).

\---

## Demand is not cost

The measure says **what must be supplied**.

It does not say **what supplying it in a particular way costs**.

Those are separate registers.

Standing mechanisms are paid for differently from per-act judgment. Description length, search cost, actor capacity, retry economics, assurance, latency, and expected damage are not made commensurable merely because the demand identity is measured in bits.

So:

> **Demand is conserved. Cost is not.**

The cost model therefore asks which supply arrangement is cheapest while remaining adequate at the declared tolerance and assurance level.

See [`core/10-cost.md`](core/10-cost.md).

\---

## Capacity and escape

An actor has two relevant capacities:

* **hold capacity** — how much governing ground it can have available at once;
* **resolve capacity** — how much it can jointly resolve.

Capacity-generated escape requires two conditions:

> **overflow ∩ open**

The residual exceeds what the actor can resolve **and** no verifier catches what gets shed.

Overflow on a closing predicate becomes retry cost.

An open predicate within capacity remains judgment.

Overflow on an open predicate produces escape.

This also yields a mechanical account of one class of hallucination: output decoupled from correct ground because that ground is absent, false, or present but unresolved.

See [`core/11-the-floor-mechanism.md`](core/11-the-floor-mechanism.md).

\---

## Determination is not intelligence

The framework makes no claim that an actor must be intelligent.

A thermostat determines.

A program determines.

A model determines.

A human determines.

Actorhood means resolving choices against ground, not possessing intelligence.

This separation is deliberate.

It means model performance can be analysed without first resolving the philosophical question of whether a model "understands" what it is doing.

Where outputs can be checked, attribution of intelligence is unnecessary for trusting the output.

Where outputs cannot be checked, performance itself becomes difficult to establish.

The framework therefore does **not** claim that LLMs are intelligent or that they are not.

See [`core/07-determination-and-intelligence.md`](core/07-determination-and-intelligence.md).

\---

## A worked instance outside software

The actor-general vocabulary is tested against the vertebrate immune system.

The mapping is not intended as metaphor:

|Store|Immune-system instance|
|-|-|
|**Encoded**|innate immunity|
|**Mechanical**|thymic negative selection|
|**Judgment**|adaptive per-encounter response|
|**Escaped**|a pathogen no response catches|

The case also supplies an ensemble actor: diversity across a population carries coverage no single member can.

> **Redundancy buys reliability. Diversity buys coverage.**

The immune system matters because no engineer specified it. If the framework's categories only worked for deliberately engineered systems, the actor-general claim would fail here.

See [`core/12-the-licensing-instance.md`](core/12-the-licensing-instance.md).

\---

## What the framework predicts

The full indexed model currently carries five arrangement-level hypotheses:

1. **Operational evaluability**  
Advantage shifts toward high-throughput computational generation as acceptance becomes more evaluable, feedback faster and denser, checking cheaper, and retries affordable.
2. **Ground and judgment dependence**  
Situated arrangements retain advantage as ground becomes unavailable, consequences delay, criteria drift, evaluators disagree, or normative legitimacy and tacit carriage matter.
3. **Generator/checker composition**  
Generator + checker arrangements should outperform either generator-alone or judgment-alone baselines where much of acceptance closes and the open residue can be escalated.
4. **Accountability completeness**  
Trust and deployment should track the completeness of the accountability arrangement rather than the executor's kind.
5. **Selection versus training**  
Reliance on selection should rise as result-level evaluation becomes slower, less objective, less stationary, and less dense.

In the shortest form:

> **Where the work can be checked, check the work. Where it cannot, check the worker.**

These hypotheses are **projected**, not reported findings.

See [`core/14-indexed-determination.md`](core/14-indexed-determination.md).

\---

## What this framework does not claim

It does **not** claim:

* that models should replace humans;
* that humans should retain every open-predicate decision;
* that models are intelligent;
* that models cannot become accountability-bearing;
* that benchmarks are useless;
* that every difficult task has a non-zero judgment floor;
* that every easy task has a zero floor;
* that determination demand can be measured where the acceptance predicate does not close;
* that the four stores are an empirical discovery;
* that cost is conserved;
* or that the framework can determine the correct organisational allocation for you.

The framework supplies a vocabulary, a set of structural claims, a partial measure, and falsifiable hypotheses.

**The allocation remains a governance decision.**

\---

## Register

This repository uses **principle**, not physical **law**.

For closing predicates, the information-theoretic identification gives determination demand a unit and makes the conservation identity exact.

For open predicates, that measure does not exist. Conservation remains an accounting principle rather than a measured invariant.

The distinction is deliberate.

Claims are marked as settled, projected, reported, or draft where appropriate. Met falsifiers and retired formulations are retained in the record rather than silently removed.

\---

## Read the theory

The dependency order is the reading order.

### Settled core

|#|Document|Role|
|-|-|-|
|00|[`primitives`](core/00-primitives.md)|decisions, ground, determination, actor, arrangement, admission tests|
|01|[`the principle`](core/01-the-principle.md)|determination demand and the four stores|
|02|[`completeness`](core/02-completeness.md)|why the store partition is exhaustive by construction|
|03|[`the floor`](core/03-the-floor.md)|irreducibility lives in predicate closure|
|04|[`actors`](core/04-actors.md)|pinning resolution, selection and training|
|05|[`accountability`](core/05-accountability.md)|executor vs accountable principal|
|06|[`composition`](core/06-composition.md)|seam demand, orchestrators, mechanisms, compound|
|07|[`determination and intelligence`](core/07-determination-and-intelligence.md)|why determination does not imply intelligence|
|08|[`projections`](core/08-projections.md)|funnel and maturation|
|09|[`the measure`](core/09-the-measure.md)|verdict entropy and the chain-rule identification|
|10|[`cost`](core/10-cost.md)|standing vs occasioned supply and actor routing|
|11|[`the floor mechanism`](core/11-the-floor-mechanism.md)|capacity, overflow and escape|
|12|[`the licensing instance`](core/12-the-licensing-instance.md)|ensemble actors and the immune-system instance|

### Draft extensions

|#|Document|Role|
|-|-|-|
|13|[`delivery`](core/13-delivery.md)|whether authored governance actually reaches the act|
|14|[`indexed determination`](core/14-indexed-determination.md)|the full index, commitment levels, residual discretion, hypothesis set|

Draft status is substantive: these documents are part of the working theory but have not yet been ratified as settled canon.

\---

## Repository layout

```text
core/
  00-14               theory documents, dependency ordered
  claims/              one canonical record per claim
  graph/               canonical term registry
  assets/              reproduction scripts

meta/                   lineage, limits, review record, canon decisions
spec/                   claim and embed schemas
assets/                 presentation assets
i18n/                   translated terminology
scripts/                validators and repository tooling

validate-core-order.py  dependency/order validation
```

Each core document declares a `ddd:contract` containing its dependencies and the concepts it establishes.

The claim graph is the canonical epistemic layer. Expository prose may change; claims retain their status, falsifiers, evidence, and history.

\---

## Validation and reproduction

Validate the core dependency order:

```bash
python3 validate-core-order.py core/
```

Validate claim records:

```bash
python3 scripts/validate-claims.py
```

The information-theoretic, cost, and floor-mechanism notes point to their reproduction scripts in `core/assets/`.

A computation supports only the claim it actually exercises. Arithmetic identities are not presented as empirical evidence, and toy demonstrations are not presented as external validation.

\---

## Relationship to Decision-Driven Design

This repository contains the **actor-general theory layer**.

**Decision-Driven Design** is its software-engineering projection: the same determination model expressed in the vocabulary of engineering specifications, architecture, delivery, and verification.

The dependency runs one way.

This repository does not depend on its projections.

\---

## Provenance

This repository was split from the combined `decision-driven-design` corpus as the execution of the repository-separation decisions recorded in the claim/decision history.

The repository has independent git history from the split point. The claim graph, rather than git history alone, carries the epistemic history of the theory.

\---

## The one line

> **For every decision, ask what must be determined, what ground it depends on, whether the work can be checked, where the determination is supplied, and who answers for it. Where you can check the work, check the work. Where you cannot, check the worker.**

