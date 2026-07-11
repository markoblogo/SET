# Agent Orchestrators Reference

`andyrewlee/awesome-agent-orchestrators` is a discovery catalog for agent runners, worktree/session managers, multi-agent coordination systems, swarms, and autonomous loops.

Reference: <https://github.com/andyrewlee/awesome-agent-orchestrators>

This is a read-only ecosystem reference. It is not a dependency, runtime registry, or recommendation to install every listed project.

## Local use

Use the catalog when a concrete task needs a runner or coordination layer that the current local workflow does not provide.

Compare candidates against these criteria:

- worktree or workspace isolation;
- human approval gates;
- persistence and resumability;
- verification and proof artifacts;
- rollback or discard behavior;
- provider and agent-runtime support;
- local execution, security boundaries, and operational cost.

The default selection loop is:

`task need -> shortlist -> capability comparison -> isolated audit -> install or reject`

Periodically select only one or two projects for a focused audit. Do not install systems opportunistically from the list.

## ABVX boundary

The catalog reinforces the existing separation:

- `SET` owns the upstream workflow and proposal contract;
- an external runner owns sessions, worktrees, scheduling, and execution;
- `AGENTS.md_generator` and `abvx-agent-skills` provide repo context and execution discipline;
- the runner must return inspectable artifacts before an explicit apply/discard decision.

`SET` should consume stable runner capabilities through `orchestrator-bundle.json`, not embed a runner, kanban board, scheduler, or swarm runtime.

## Audit checklist

Before local installation or product adaptation, record:

1. What specific workflow gap does this project fill?
2. Which of the comparison criteria above are implemented and tested?
3. What data, credentials, processes, containers, or network access does it require?
4. Does it preserve proposal-first and human-gated settlement?
5. Can it be removed without changing the ABVX contract layer?

Keep the audit result next to the relevant project decision. Revisit the catalog when a real workflow gap appears, not as a general installation queue.
