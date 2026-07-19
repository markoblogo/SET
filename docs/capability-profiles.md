# Capability Profiles

`SET` profiles select a small, read-only subset of `orchestrator_bundle.context_package`. They are registry configuration, not an installer, runner, hook system, or policy runtime.

## Selection

Set the optional top-level field in a registry entry:

```json
"capability_profile": "research"
```

Omit it for `baseline`. `context_package.capability_profile` records the selected name and exact export list so downstream runners can consume a stable, inspectable contract.

| Profile | Exports | Use when |
|---|---|---|
| `baseline` | context-budget, context-degradation, and loop-readiness hints | a normal planning handoff needs review discipline only |
| `research` | baseline plus research-diversity and optional memory contracts | evaluation or research needs bounded alternatives and project-scoped retrieval guidance |
| `governed-runner` | baseline plus optional memory and governance contracts | a runner is separately implementing measured shadow-first policy decisions |
| `loop-readiness` | context budget, readiness hint, and disabled L1/L2 loop contract | a runner or reviewer needs an explicit report-first recurring-work packet without enabling a runtime |
| `loop-hardening` | context budget, context-degradation review, and disabled loop-hardening contract | repeated delivery needs evidence-based harness removal, immutable runtime-path sprints, and broken-window revalidation without automatic rollback |
| `bounded-orchestration` | context budget, context-degradation review, and disabled planner-review-executor contract | a runner needs bounded plan review, disjoint executor ownership, explicit route evidence, and root-owned verification |
| `git-native-context` | context budget, context-degradation review, and disabled typed-document lifecycle contract | a project needs minimal Git-reviewed ADR/RFC/rule/spec/plan/research/incident context without installing a memory runtime |
| `bug-evidence` | context budget, context-degradation review, and disabled red-to-green evidence contract | a runner needs captured reproduction and fix evidence without adding an autonomous bug scanner |
| `design-taste-review` | context budget, context-degradation review, and disabled taste-review contract | marketing/editorial work needs an explicit design read, bounded redesign audit, and browser verification while product UI remains evidence-routed |
| `agent-operations` | context budget, context-degradation review, and disabled agent-operations contract | a project needs explicit agent cards, operation and decision receipts, adaptation deltas, trust-graded scoped memory, and evidence-backed provider/tool routing without installing an agent runtime |

## Boundary

- Profiles only choose exported hints/contracts; they do not change SET workflows.
- Every optional contract stays disabled until an external runner implements it.
- Profiles never install dependencies, register hooks, execute tools, store memory, or grant mutation/enforcement authority.
- Use snapshot tests whenever an export list changes so a profile cannot silently widen a downstream contract.

See `docs/loop-readiness-contract.md` for the L1/L2 controls and authority boundary.
See `docs/loop-hardening-contract.md` for harness stripping, runtime-path sprint packets, and no-auto-revert broken-window revalidation.
See `docs/bounded-orchestration-contract.md` for the planner, findings, executor-packet, route-state, and root-verification protocol.
See `docs/git-native-context-contract.md` for the minimal document taxonomy, human-gated lifecycle, directed relations, and code-change pattern.
See `docs/bug-evidence-contract.md` for risk-based approval, captured checks, honest status classification, and optional `cpat` linkage.
See `docs/design-taste-review-contract.md` for routing, relative design axes, preservation-first redesign review, and visual verification.
See `docs/agent-operations-contract.md` for agent identity, operation and decision receipts, adaptation deltas, trust-graded memory scopes, public/private state boundaries, provider/tool availability, and authority boundaries.
