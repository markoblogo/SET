# Context Budget Hint

`SET` can tell external runners which context risks to review, but it does not manage model context windows or rewrite runner prompts.

## Purpose

Long agent runs can fail because the wrong context is present, not because the model lacks information. The common failure modes are:

- context poisoning;
- lost-in-the-middle;
- distraction;
- context clash;
- stale carryover.

The planner exposes two read-only hints:

- `orchestrator_bundle.context_package.context_budget_hint`
- `orchestrator_bundle.context_package.context_degradation_review`

These sit beside memory and research-diversity hints. They are contract guidance for external runners and human reviewers, not runtime dependencies.

## Review Contract

Before runner handoff, proposal apply, memory write, or large documentation update:

1. identify authoritative context sources;
2. demote stale or supporting-only context;
3. keep decisive constraints close to the active plan;
4. move bulky evidence into files or artifacts;
5. check for poisoning, lost-in-middle, distraction, clash, and stale carryover.

## Boundaries

`SET` does not:

- run context repair automatically;
- manage model context windows;
- choose or rewrite runner prompts;
- persist memory;
- let memory or prior task history override the current user message.

Use `context-degradation-review` from `abvx-agent-skills` when the runner supports skill loading.
