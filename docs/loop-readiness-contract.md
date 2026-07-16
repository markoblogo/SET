# Loop Readiness Contract

`SET` can export an optional `loop-readiness` capability profile for an external runner or reviewer. It is a contract for bounded recurring work, not a scheduler, agent runtime, tool proxy, or permission system.

## Selection

```json
"capability_profile": "loop-readiness"
```

The profile exports `context_budget_hint`, `loop_readiness_hint`, and `loop_readiness_contract` in `orchestrator_bundle.context_package`. It is disabled by default and grants no authority.

## Levels

| Level | Authority | Minimum controls |
|---|---|---|
| `L1` | report-only | one goal and explicit non-goals, watched scope, durable state, append-only run log, budget, early exit/stop rules, escalation |
| `L2` | proposal-first assisted | all L1 controls plus isolated retained output/branch/worktree/sandbox, separate maker-checker verification, named proof, discard or rollback notes, human approval before side effects |

Every run record names the run, goal, scope, level, discovered items, proposed actions, verification, escalations, budget consumed, and outcome. Keep operational reasoning short; do not store hidden reasoning, secrets, or protected evidence in the packet.

## Boundary

- Do not use this profile to enable unattended execution, auto-merge, deployment, publishing, or scheduled work.
- Keep writes, merges, releases, destructive actions, and external effects behind a human gate even at L2.
- Promote beyond L2 only in a separately governed runtime with its own permissions, telemetry, and rollback policy.

Use the `loop-run-contract` ABVX Agent Skill to draft and review an L1/L2 packet before an external runner consumes it.
