# Loop Readiness Hint

`SET` can describe whether a handoff is ready for a recurring or semi-autonomous agent loop. It does not run, schedule, or govern that loop.

## Purpose

External runners may turn a SET handoff into repeated work: daily triage, PR babysitting, CI sweeping, dependency updates, changelog drafting, or issue triage. Before that happens, the runner or human reviewer should check loop readiness.

The planner exposes this as:

```text
orchestrator_bundle.context_package.loop_readiness_hint
```

It is a review hint only.

## Readiness Levels

- `L0`: not loop-ready.
- `L1`: report-only.
- `L2`: proposal-first.
- `L3`: governed loop.

The safe default is `L1 report-only` until state, verifier, budget, run log, rollback, and human gate are explicit.

## Checks

Review:

- cadence and stop rule;
- durable state outside the model;
- scope and denied targets;
- worktree, branch, sandbox, or retained-output isolation;
- verifier or maker-checker gate;
- token, time, retry, and spend budget;
- run log and failure record;
- rollback or discard path;
- human gate for writes, merges, releases, destructive actions, and external side effects.

## Boundaries

`SET` does not:

- schedule loops;
- spawn recurring agents;
- manage worktrees;
- auto-fix, auto-merge, deploy, or release.

Use `loop-readiness-review` from `abvx-agent-skills` when the runner supports skill loading.
