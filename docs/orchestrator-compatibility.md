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
- `context_package`: repomap policy, optional ID bootstrap artifact hints, and one selected capability-profile export
- `task_contract`: proof-loop settings, expected artifacts, proposal lifecycle, and blockers
- `capabilities`: resolved SET/agentsgen/ID capabilities
- `handoff`: runner-facing guidance and non-goals

`task_contract.recommended_review_lenses` lists optional review gates for external runners and humans. The current default lens set is `assumption-excavation`, `pipeline-readiness-gate`, `confidence-fragility-review`, `hypothesis-diversification`, `context-degradation-review`, `agent-tool-contract-review`, and `loop-readiness-review`. These are hints, not runtime dependencies.

`context_package.capability_profile` records the selected profile and its exact exports. Profiles are registry-selected, planning-only, and do not install dependencies, grant tool authority, or enable a runtime. `baseline` exports context and loop review hints; `research` adds diversity and optional project-memory guidance; `governed-runner` adds optional memory and shadow-first governance contracts; `loop-readiness` adds a disabled L1/L2 report-first contract; `bounded-orchestration` adds a disabled planner-review-executor handoff contract; `git-native-context` adds a disabled minimal typed-document lifecycle and relation contract; `bug-evidence` adds a disabled captured red-to-green evidence contract. See `docs/capability-profiles.md`, `docs/loop-readiness-contract.md`, `docs/bounded-orchestration-contract.md`, `docs/git-native-context-contract.md`, and `docs/bug-evidence-contract.md`.

When selected by the `research` profile, `context_package.research_diversity_hint` asks runners to generate distinct hypotheses or bounded proposals before validation when first-answer mode collapse is risky. It is deliberately a review hint, not a SET runtime. See `docs/research-diversity-hint.md`.

`context_package.context_budget_hint` and `context_package.context_degradation_review` ask runners to review context poisoning, lost-in-the-middle failures, distraction, context clash, and stale carryover before handoff or apply. See `docs/context-budget-hint.md`.

`context_package.loop_readiness_hint` asks runners to keep recurring work report-only until cadence, state, isolation, verifier, budget, run log, rollback, and human gate are explicit. See `docs/loop-readiness-hint.md`.

`task_contract.proposal_lifecycle` defines a proposal-first settlement model: `run`, `retained_output`, `inspect`, then `select`, `apply`, or `discard`. External runners should keep generated files outside the target workspace until inspection passes and an explicit apply step settles the proposal.

When selected by `research` or `governed-runner`, `context_package.memory_capability` is provider-neutral and disabled by default. If a runner implements it, it must provide per-project isolation, hybrid/full-text retrieval, and audit-gated proposal-first writes. See `docs/memory-capability-contract.md`.

When selected by `governed-runner`, `context_package.agent_governance_capability` is provider-neutral and disabled by default. It defines a shadow-first policy decision before significant tool calls, three outcomes (`allow`, `deny`, `require_approval`), append-only provider-owned audit records, and telemetry for tool calls, tokens, estimated cost, and latency. It records a short operational reason, never hidden chain-of-thought. A runner must keep protected evidence and secrets out of public outputs. See `docs/agent-governance-capability-contract.md`.

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

From diversity-first research:

- generate alternatives before arguing for the strongest one
- record evidence needs and disconfirming signals
- rank by evidence readiness, not model-stated probability
- hand off to validation, proof-loop artifacts, or human review

From context engineering:

- keep authoritative constraints close to the active plan
- demote stale summaries and supporting-only context
- move bulky evidence into artifacts instead of prompt payloads
- review context degradation before runner handoff, memory write, or proposal apply

From loop engineering:

- keep new loops report-only before promotion
- require durable state, verifier, budget, run log, rollback, and human gate
- use worktree, branch, sandbox, or retained-output isolation for proposal-first loops
- keep scheduling, recurrence, and runner state outside SET

## Non-goals

`SET` should not grow a kanban board, agent scheduler, worktree manager, diversity sampling runtime, tool-call proxy, policy-enforcement service, or autonomous loop runtime. Those are product/runtime layers. `SET` stays useful by keeping the contract small, explicit, and reviewable.
