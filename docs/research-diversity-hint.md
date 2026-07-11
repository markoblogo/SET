# Research Diversity Hint

`SET` may point external runners and reviewers toward diversity-first research, but it does not implement a diversity runtime.

## Purpose

Some agent runs collapse onto the first plausible explanation, plan, or edit. For research-heavy or adversarial tasks, the safer contract is:

```text
question -> distinct hypotheses -> evidence needs -> disconfirming signals
         -> adversarial review -> validation or human decision
```

The planner exposes this as `orchestrator_bundle.context_package.research_diversity_hint` and as the `hypothesis-diversification` review lens in `task_contract.recommended_review_lenses`.

## Use When

- market, incident, product, or architecture analysis needs competing explanations;
- a SET handoff should ask a runner for alternatives before proof-loop validation;
- SkillOpt-style work should generate several bounded edit proposals before testing one;
- a confident generated plan needs adversarial review before apply.

## Contract

The hint asks a runner or human reviewer to:

1. generate distinct hypotheses or bounded proposals;
2. record supporting evidence needed for each one;
3. record disconfirming signals for each one;
4. remove duplicates and wording variants;
5. rank by evidence readiness, not by model confidence;
6. hand off to proof-loop artifacts, validation checks, or human review.

## Boundaries

This is a review hint only.

`SET` does not:

- run a diversity sampling runtime;
- use model-stated probabilities as calibrated probabilities;
- make financial, trading, legal, medical, or safety decisions;
- add autonomous execution from this pattern.

For finance or commodity-market work, this can support scenario generation and officer-style adversarial review. It must not be used for position sizing, default decisions, or automatic trading.

## Related Skill

Use `hypothesis-diversification` from `abvx-agent-skills` when the runner supports skill loading.
