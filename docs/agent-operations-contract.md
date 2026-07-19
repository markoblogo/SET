# Agent Operations Contract

`SET` can export a disabled, provider-neutral contract for describing concrete agents, long-running operations, scoped memory, and provider/tool capabilities. It does not install LobeHub or create an agent runtime.

Select the profile with:

```json
"capability_profile": "agent-operations"
```

The planner exports it under:

```text
orchestrator_bundle.context_package.agent_operations_contract
```

## Agent capability card

An agent card describes an actual configured worker, not a reusable method. Skills continue to describe how work should be done.

Required fields:

- `agent_id`, `purpose`, `responsibilities`, `owner`;
- `authority`: `read`, `proposal`, `write`, or `external_action`;
- `models`, `tools`, and `knowledge_bases`;
- `allowed_schedules` and `approval_boundary`;
- `last_confirmed_capabilities` with `checked_at`, evidence, and status.

Declared capabilities are not effective authority. A card must fail closed when its owner, approval boundary, or current capability evidence is missing.

## Async operation receipt

Long-running and scheduled work uses a stable `operation_id` and retains:

```text
operation_id, agent_id, project_id, requested_by, authority,
queued_at, status, result_summary, evidence, approval_required
```

Allowed states:

```text
QUEUED -> RUNNING -> NEEDS_APPROVAL -> SUCCEEDED | FAILED | CANCELLED
```

`RUNNING` may settle directly as `SUCCEEDED`, `FAILED`, or `CANCELLED` when no approval is required. `NEEDS_APPROVAL` freezes the exact proposed external action; approval is one-shot, action-bound, and does not widen the agent card. A receipt records operational facts, never hidden reasoning, credentials, private source material, or unrestricted logs.

## Memory scopes

Every memory record declares exactly one scope:

- `personal`: owner preferences;
- `project`: repository or product context;
- `agent`: reviewed professional knowledge for one agent;
- `run`: temporary operation state.

Each record retains `provenance`, `owner`, `editability`, and `retention`. Cross-project reads and automatic scope promotion are disabled by default. `run` memory expires or is explicitly promoted through review; no successful operation silently becomes durable memory.

## Provider and tool registry

Each provider, tool, or MCP record declares:

- supported modalities, tool calling, structured output, streaming, and async operations;
- execution location: `local` or `cloud`;
- required secret names, never values;
- data-egress boundary;
- availability: `declared`, `probed`, `confirmed`, or `unavailable`;
- cost and rate-limit observations with `observed_at` and source;
- authority and side effects.

Agents may route only through capabilities sufficient for the task. `declared` is documentation, `probed` is reachability evidence, `confirmed` is successful relevant-path evidence, and `unavailable` blocks the route. Cost, limits, models, and availability are time-bound observations.

## Boundary

- disabled by default and planning-only;
- no agent creation, scheduling, execution, memory storage, provider probing, or MCP installation;
- no authority inferred from models, tools, schedules, or marketplace presence;
- external actions, messages, transactions, production writes, and protected data require their existing project and human gates;
- project implementations own persistence, redaction, retention, cancellation, idempotency, and runtime verification.

## Reference

Adapted at the contract level from LobeHub's agent-as-unit, scheduled operation, structured memory, and multi-provider ideas. SET does not copy or depend on the LobeHub runtime, marketplace, or codebase.
