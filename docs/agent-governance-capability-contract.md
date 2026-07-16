# Agent Governance Capability Contract

`SET` can describe an optional agent-governance capability for downstream runners without intercepting tool calls, storing telemetry, or operating a policy service.

The planner exports the contract under:

```text
orchestrator_bundle.context_package.agent_governance_capability
```

The default is `enabled: false` and `mode: shadow-first`.

## Decision point

A runner evaluates a significant tool call or external side effect before it executes it. The permitted outcomes are:

- `allow` — action may proceed under the runner's normal controls;
- `deny` — action must not execute;
- `require_approval` — retain the exact proposed action and wait for a one-shot human approval.

Every decision should carry `task_id`, `correlation_id`, `action_kind`, `action_fingerprint`, a short operational reason, and the decision. `action_fingerprint` binds an approval to the exact deferred action. The reason explains the policy-relevant fact; it is not hidden chain-of-thought.

## Policy controls

A provider may implement the contract with an allowlist or denylist, protected-path/data boundaries, per-intent rate and spend limits, approval gates, and a circuit breaker for repeated denials or failures.

Protected evidence, credentials, and personal data must stay outside public responses and public ledgers. Approval must bind to the exact deferred action and expire after one use.

## Audit and telemetry

The runner owns append-only storage. For each action or decision it should retain only the operational receipt needed for review.

Telemetry fields:

- `tool_calls`
- `tokens`
- `estimated_cost`
- `latency_ms`

The shadow evaluation dimensions are factual safety, unnecessary tool calls, cost, latency, stopping correctness, and abstention quality. Current delivery remains unchanged until a separate promotion gate has a sufficient, factual-safe corpus.

## Boundary

`SET` exports the capability contract only. It does not execute or proxy tool calls, store secrets or protected evidence, retain hidden reasoning, provide a policy API, or turn on enforcement. The consumer chooses the implementation and must preserve existing public/protected boundaries and review gates.

## Reference

This contract adapts the small, portable policy-and-telemetry ideas from [Osmantic/ODS](https://github.com/Osmantic/ODS), particularly its Agent Policy Engine and Token Spy. It does not adopt ODS as a SET dependency or runtime.
