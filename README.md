# Actor-Indexed Determination

**The Conservation Principle of Determination Demand** — a theory of where determinations come from,
what they cost, and which actor should make each one. Actor-general: it ranges over anything that
determines choices against ground — a program, a model, a human, a market, an immune system.

This is the **principle repository**: the stable, actor-general layer. Its software projection —
*Decision-Driven Design* — lives in a separate repository, which pins this repo's canon remotely and
renders it toward engineering checkers. Per the Stable Dependency Principle, **this repository carries
no reference to its dependents**: the stable layer does not know who consumes it.

---

## The one idea

Four classical results govern how work is allocated in engineered systems — Brooks's essential
complexity, Tesler's conservation of complexity, Ashby's requisite variety, Meyer's contracts. Each
quantifies over an **actor** — the thing that makes a determination against some ground — and **none
makes that actor explicit.** Supplying the missing parameter changes their predictions. Two
consequences follow:

1. **The irreducible floor of a task is a property of its *acceptance predicate*, not of the task.**
   Zero where you can check the answer; non-zero where you cannot; and *whether you can* is, in
   general, undecidable. → [`core/03-the-floor.md`](core/03-the-floor.md)

2. **Selection intensity is inversely proportional to acceptance-predicate closure.** *Training* is
   what you do when you can check the work; *selection* is what you do when you cannot — you check the
   worker instead. Falsifiable across professions. → [`core/04-actors.md`](core/04-actors.md)

And, for tasks whose acceptance predicate closes, **determination demand is measurable** — it is the
Shannon entropy of the verdict, and conservation is the chain rule of entropy
([`core/09`](core/09-the-measure.md)). The measure exists exactly where the predicate closes, and
vanishes precisely at the floor.

---

## Layout

```
core/           the claim graph — canon, versioned; read 00 → 11 in order
  graph/        canonical term registry (terms.yaml); docs embed from here
  claims/       one YAML per claim (DDD-frame-*, DDD-measure-*, DDD-floor-01, DDD-agent-01)
  assets/       reproduction scripts; a claim whose computation fails demotes until fixed
meta/           lineage-and-limits, the canon patch register, the principle's consolidated state
spec/           the claim-format schema (format 1) + the format-2 addendum (embed fields)
assets/         the conservation-principle figure
i18n/           Danish glossary of core terms
validate-core-order.py    ordering + graph-transclusion checker for core/
scripts/validate-claims.py claim/decision schema validator
```

Each core document opens with a `ddd:contract` block (requires / establishes); the read order is the
dependency order and every edge points backward. `python3 validate-core-order.py core/` enforces it
(exit 0, zero W4). Canonical term and claim definitions live in the graph and are **embedded** into
their one home document; everywhere else they are **referenced**.

---

## Register

This is a **principle**, not a physical law: "determination demand" has no measured unit (unlike
Ashby's variety, counted in bits). Where the word "law" appears it is homage, in the sense of
*Tesler's Law* and *Ashby's Law*, and it is flagged. The framework's honesty about its own status is
load-bearing — see [`core/01-the-principle.md`](core/01-the-principle.md) and
[`meta/lineage-and-limits.md`](meta/lineage-and-limits.md).

---

## Provenance

This repository was split from the combined `decision-driven-design` corpus (owner `Hafeok`) as the
execution of a filed decision, `DDD-dec-04`. It was branched fresh (no shared git history) from that
repository at commit **`10f6ba6`** (branch `claude/repo-split-execution-j46b1q`). The combined repo's
`CHANGELOG.md` stays behind with the software projection; this repository starts a fresh changelog.
The claim graph carries the epistemic history regardless of git lineage.

- Split decisions: `DDD-dec-04` (split), `DDD-dec-05` (org stays a directory in the projection),
  `DDD-dec-06` (sequencing + this repo's name), `DDD-dec-07` (execution decoupled from the measure
  note). These decision records live in the software-projection repository, which is where program
  decisions belong.
