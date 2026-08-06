# Definition worklist — terms awaiting a canonical block

Generated during the repo split. The term graph (`graph/terms.yaml`) is **complete** — every term
below has an `established_by` entry, so `validate-core-order.py` passes with zero W4. What each lacks
is `canonical_md`: the exact markdown block the home doc should embed. To define a term:

1. Write its canonical block into `graph/terms.yaml` under that term's `canonical_md:`.
2. Wrap the identical block in its home doc between `<!-- ddd:embed id=term:KEY -->` and
   `<!-- /ddd:embed -->` (byte-for-byte; the validator's E6 checks the match).

Five terms are already done as exemplars: `closure`, `floor`, `conservation`, `seam-identity`,
`determination-intelligence-separation`. The `anchor` column points at the line in the home doc that
already reads like the definition — usually the right block to wrap.

## Structural terms (required by later documents — highest priority)

| term | home | suggested anchor line |
|---|---|---|
| `term:acceptance-predicate` | 03-the-floor.md | L20: > **The intrinsic floor is a property of the acceptance predicate, not of the decision.** |
| `term:actor` | 00-primitives.md | L83: > **An actor is anything that determines choices against ground** — anything that passes t |
| `term:admission-test` | 00-primitives.md | L6: establishes: [determination, decision, ground, tolerance, admission-test, actor, arrangeme |
| `term:arrangement` | 00-primitives.md | L87: > **An arrangement is the composition through which a resolution is produced** — the actor |
| `term:assurance` | 01-the-principle.md | L37: > **For a task at a declared assurance level, and within a fixed decomposition of that tas |
| `term:capacity` | 10-the-floor-mechanism.md | L81: > **(1) Overflow** — demand exceeds resolve capacity. |
| `term:composite-actor` | 06-composition.md | L6: establishes: [seam|seam demand, seam-identity|seam-demand identity, composite-actor|compos |
| `term:decision` | 00-primitives.md | L52: > **Decisions** — the things determined. |
| `term:demand` | 01-the-principle.md | L38: > determination demand is conserved.** |
| `term:determination` | 00-primitives.md | L205: > anything at all — and what necessarily happens to a determination nobody makes.** |
| `term:escape` | 01-the-principle.md | L122: > **This asymmetry is why everything drifts toward escape.** A capacity-bound actor under  |
| `term:ground` | 00-primitives.md | L53: > **Ground** — what they are determined against. |
| `term:judgment` | 01-the-principle.md | L75: | **Judgment** | — | during the act | an actor reading ground, **with an accountable party |
| `term:overflow` | 10-the-floor-mechanism.md | L81: > **(1) Overflow** — demand exceeds resolve capacity. |
| `term:pinning-resolution` | 04-actors.md | L19: 1. Actors differ in **pinning resolution** — how tightly their behaviour can be constraine |
| `term:seam` | 06-composition.md | L22: > A composite carries the demand of its parts, **plus** the seam demand `S` created *betwe |
| `term:store` | 01-the-principle.md | L41: > Reduce the demand in one store and it **relocates**; it does not vanish. |
| `term:tolerance` | 00-primitives.md | L104: > **A choice is a decision iff varying *the choice* moves the outcome past tolerance.** |
| `term:verdict` | 09-the-measure.md | L62: > **verdict** be the correct output the predicate assigns to each point of the input space |
| `term:verdict-entropy` | 09-the-measure.md | L6: establishes: [verdict|verdict function, verdict-entropy|verdict entropy, chain-rule-identi |

## Result terms (terminal in the DAG, but central concepts — define these too)

| term | home | suggested anchor line |
|---|---|---|
| `term:accountability` | 05-accountability.md | L57: > **Accountability completeness is a property of an arrangement, not a capacity of an acto |
| `term:answerability` | 05-accountability.md | L180: - **Answerability** — the obligation to produce the chain: which determinations were made, |
| `term:assurance-tower` | 05-accountability.md | L20: on actors (§§1–6) and the **assurance tower** (§7). Neither is cited from elsewhere in the |
| `term:attribution` | 05-accountability.md | L124: This makes the condition **provenance-shaped, and therefore checkable**. Attribution over  |
| `term:diversity` | 11-the-licensing-instance.md | L63: > **Diversity in a population is how you carry judgment demand that exceeds any single act |
| `term:encoded` | 01-the-principle.md | L73: | **Encoded** | constraint | before the act | a rule | amortises · cheap to state, **expen |
| `term:ensemble-actor` | 11-the-licensing-instance.md | L6: establishes: [ensemble-actor|ensemble actor, diversity, redundancy, swarm-gate|the gate on |
| `term:exhaustiveness` | 02-completeness.md | L6: establishes: [exhaustiveness, governing-decision|governing decision] |
| `term:funnel` | 08-projections.md | L32: > **The funnel** is the compound over **depth**: pay once at the top, and every decision * |
| `term:governing-decision` | 02-completeness.md | L18: > Every governing decision is determined by exactly one of: a **rule** (encoded), a **chec |
| `term:liability` | 05-accountability.md | L164: | Liability | **no** — requires the arrangement | |
| `term:maturation` | 08-projections.md | L30: > **Maturation** is the compound over **repetition**: pay once, and every future *run* is  |
| `term:mechanical` | 01-the-principle.md | L74: | **Mechanical** | criterion | after the act | a check | pays the **executability tax** ·  |
| `term:orchestrator` | 06-composition.md | L136: > **The channel is the platform.** Not the graph, not the ledger, not the orchestrator — t |
| `term:p-err` | 10-the-floor-mechanism.md | L106: > **escape = (open residual) × p_err(load)** |
| `term:path-degeneracy` | 03-the-floor.md | L6: establishes: [acceptance-predicate|acceptance predicate, closure|closes|closed|closing, fl |
| `term:projection` | 08-projections.md | L19: > **Figure:** `assets/projections.svg` (static) · `assets/projections.html` (interactive — |
| `term:redundancy` | 11-the-licensing-instance.md | L74: > **Redundancy buys reliability. Diversity buys coverage.** |
| `term:seam-occupancy` | 06-composition.md | L39: allocation is a real design fork, and its name is **seam occupancy** — *who or what sits a |
| `term:selection` | 04-actors.md | L145: > **Selection is verification relocated from the act onto the actor's identity.** |
| `term:swarm-gate` | 11-the-licensing-instance.md | L6: establishes: [ensemble-actor|ensemble actor, diversity, redundancy, swarm-gate|the gate on |
| `term:training` | 04-actors.md | L128: > ## **Closure decides whether training is *available*. Cost decides the *ratio* when it i |

## Trim candidates (notations / instances / aliases — define OR remove from the contract, your call)

| term | home | note |
|---|---|---|
| `term:chain-rule-identification` | 09-the-measure.md | names a result/claim, not a term |
| `term:escape-mechanism` | 10-the-floor-mechanism.md | the result `overflow ∩ open` — a claim, not a term |
| `term:immune-system` | 11-the-licensing-instance.md | a worked instance, not a term; moved to `establishes` only to satisfy the validator |
| `term:last-decision` | 00-primitives.md | phrase 'last decision in the chain' — likely folds into `determination` |
| `term:seam-information` | 09-the-measure.md | notation `I(V;S)` — alias of the seam, not a separate term |
