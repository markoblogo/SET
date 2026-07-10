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
- `task_contract`: proof-loop settings, expected artifacts, proposal lifecycle, and blockers
- `capabilities`: resolved SET/agentsgen/ID capabilities
- `handoff`: runner-facing guidance and non-goals

`task_contract.recommended_review_lenses` lists optional review gates for external runners and humans. The current default lens set is `assumption-excavation`, `pipeline-readiness-gate`, and `confidence-fragility-review`. These are hints, not runtime dependencies.

`task_contract.proposal_lifecycle` defines a proposal-first settlement model: `run`, `retained_output`, `inspect`, then `select`, `apply`, or `discard`. External runners should keep generated files outside the target workspace until inspection passes and an explicit apply step settles the proposal.

When `--export-dir` is used, the planner also writes `proposal-lifecycle.json` and `rabbithole.seed.md`. The lifecycle file is a compact machine-readable settlement contract. The Rabbithole seed is optional local review material for human-in-the-loop exploration of the plan. Neither is required by SET as a runtime dependency.

## Patterns to adapt

From issue-to-agent runners:

- consume the bundle before creating an isolated agent session
- attach `task_contract.expected_artifacts` to the ticket or run receipt
- block automatic apply when `task_contract.blocked_by` is non-empty
- retain runner output separately until `inspect` passes and the operator chooses `select`, `apply`, or `discard`

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
