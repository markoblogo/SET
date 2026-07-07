# Orchestrator Compatibility

`SET` can act as an upstream contract layer for external agent orchestrators without becoming an agent runner.

## Boundary

`SET` owns:

- repo registry config
- workflow preset resolution
- review-first planning output
- repo context surfaces from `agentsgen`
- optional `ID` bootstrap packets
- proof-loop artifact expectations

External orchestrators own:

- spawning coding agents
- assigning tickets or intents
- worktree/container isolation
- retries, scheduling, and runner state
- branch and PR automation
- cost tracking and long-running session control

## Compatibility model

The planner emits an `orchestrator_bundle` in JSON output and writes `orchestrator-bundle.json` when `--export-dir` is used.

The bundle is intentionally read-only and planning-only. It is meant for Sortie/Symphony-like systems that need a stable repo handoff before they spawn agents.

Useful fields:

- `repo`: target repository identity
- `target_workflow`: proposed SET workflow path, action ref, preset, and inputs
- `context_package`: repomap policy and optional ID bootstrap artifact hints
- `task_contract`: proof-loop settings, expected artifacts, and blockers
- `capabilities`: resolved SET/agentsgen/ID capabilities
- `handoff`: runner-facing guidance and non-goals

## Patterns to adapt

From issue-to-agent runners:

- consume the bundle before creating an isolated agent session
- attach `task_contract.expected_artifacts` to the ticket or run receipt
- block automatic apply when `task_contract.blocked_by` is non-empty

From proof-of-work orchestrators:

- use proof-loop artifacts as the durable review surface
- treat CI, review notes, and expected artifacts as completion evidence
- keep branch/PR mutation outside SET planning mode

From coordination protocols:

- treat the bundle as a context package, not a project-management object
- use `repo`, `target_workflow`, and expected artifacts as stable handoff inputs
- keep runtime claims, locks, heartbeats, and runner state in the external system

## Non-goals

`SET` should not grow a kanban board, agent scheduler, worktree manager, or autonomous loop runtime. Those are product/runtime layers. `SET` stays useful by keeping the contract small, explicit, and reviewable.
