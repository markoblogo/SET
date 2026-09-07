# Advanced SET guide

Start with the [quickstart](../README.md).

## Core workflow

`SET` is intentionally review-first:

```text
resolve repo config -> plan -> inspect -> approve -> apply in target repo
```

Owner-facing and agent-facing phase vocabulary stays compact:

```text
Discuss -> Plan -> Execute -> Verify -> Ship
```

In `SET`, heavy research, planning, and execution work should run in bounded
fresh packets while the main thread stays lean. A ship claim is valid only
after a verification artifact or receipt exists for the reviewed scope.

The planner can export:

- `plan.json`
- `workflow.set.yml`
- `pr-body.md`
- `orchestrator-bundle.json`
- `proposal-lifecycle.json`
- optional `rabbithole.seed.md`

See [docs/config-apply-planning.md](config-apply-planning.md) and
[docs/orchestrator-compatibility.md](orchestrator-compatibility.md).

## Workflow presets

- `repo-docs`: `init + pack + check`
- `site-ai`: `repo-docs + site pack + analyze + meta`
- `minimal`: bootstrap-only baseline

## ID integration

When repo-local `ID` hooks are enabled, `SET` resolves the preferred human
bootstrap order and exports:

- `docs/ai/id-bootstrap.json`
- `docs/ai/id-bootstrap.prompt.md`

Expected bootstrap order:

1. `soul.md`
2. `profile.core.md`
3. `handshake.md`

`SET` treats those packets as runtime interfaces for downstream agent runs, not
as hidden action internals. See [docs/id-bootstrap.md](id-bootstrap.md).

## Outputs

Depending on preset and config, `SET` can drive production of:

- `AGENTS.md`, `RUNBOOK.md`
- `llms.txt` / `LLMS.md`
- `docs/ai/id-context.json`
- `docs/ai/id-bootstrap.json`
- `docs/ai/id-bootstrap.prompt.md`
- repo maps and AI docs under `docs/ai/`
- proof-loop artifacts under `docs/ai/tasks/<task-id>/`

When execution docs or operator-facing runbooks are meant to be acted on under
high context-switching or ADHD-style working conditions, prefer ADHD-shaped
output: next action first, numbered bounded steps, visible current state,
concrete estimates, and one explicit next move.

## Companion layers

- `agentsgen`: repo-scoped agent context
- `ID`: portable human context
- `lab.abvx`: public catalog and read-only surface

Practical split:

- use `ID` for the human;
- use `agentsgen` for the repository;
- use `SET` when you want orchestration around both.

## Registry contract

`SET` owns the orchestration registry and repo-config contract:

- schema: `schema/repo-config.v1.json`
- docs: [docs/repo-config.md](repo-config.md)
- runtime artifact docs: [docs/id-bootstrap.md](id-bootstrap.md)
- example: `examples/repo-config.example.json`
- registry entries: `registry/repos/*.json`

## Optional capability contracts

`SET` can export compact optional contracts without becoming a runtime for
them.

Core orchestration and proof:

- [docs/loop-readiness-contract.md](loop-readiness-contract.md)
- [docs/loop-hardening-contract.md](loop-hardening-contract.md)
- [docs/bounded-orchestration-contract.md](bounded-orchestration-contract.md)
- [docs/ship-router-contract.md](ship-router-contract.md)
- [docs/bug-evidence-contract.md](bug-evidence-contract.md)
- [docs/agent-governance-capability-contract.md](agent-governance-capability-contract.md)
- [docs/task-closeout-audit-contract.md](task-closeout-audit-contract.md)

Context, memory, and agent operations:

- [docs/memory-capability-contract.md](memory-capability-contract.md)
- [docs/memory-mutation-receipt-contract.md](memory-mutation-receipt-contract.md)
- [docs/agent-operations-contract.md](agent-operations-contract.md)
- [docs/skill-quality-pipeline-contract.md](skill-quality-pipeline-contract.md)
- [docs/gepa-style-optimization-contract.md](gepa-style-optimization-contract.md)
- [docs/superpowers-methodology-donor-note.md](superpowers-methodology-donor-note.md)
- [docs/email-intake-boundary-contract.md](email-intake-boundary-contract.md)
- [docs/knowledge-distillation-boundary-contract.md](knowledge-distillation-boundary-contract.md)
- [docs/knowledge-asset-generation-boundary-contract.md](knowledge-asset-generation-boundary-contract.md)
- [docs/ai-engineering-reference-index-note.md](ai-engineering-reference-index-note.md)
- [docs/optical-transfer-boundary-contract.md](optical-transfer-boundary-contract.md)
- [docs/agent-room-event-log-contract.md](agent-room-event-log-contract.md)
- [docs/browser-helper-boundary-contract.md](browser-helper-boundary-contract.md)
- [docs/live-web-research-boundary-contract.md](live-web-research-boundary-contract.md)
- [docs/codex-security-repo-selection-matrix.md](codex-security-repo-selection-matrix.md)
- [docs/search-discoverable-code-contract.md](search-discoverable-code-contract.md)
- [docs/twelve-factor-agent-adaptation.md](twelve-factor-agent-adaptation.md)

Frontend, product, and content review:

- [docs/creator-intent-lens.md](creator-intent-lens.md)
- [docs/design-taste-review-contract.md](design-taste-review-contract.md)
- [docs/design-blueprint-contract.md](design-blueprint-contract.md)
- [docs/readme-surface-audit-contract.md](readme-surface-audit-contract.md)
- [docs/dependency-risk-check-contract.md](dependency-risk-check-contract.md)
- [docs/chat-surface-boundary-contract.md](chat-surface-boundary-contract.md)
- [docs/code-review-helper-boundary-contract.md](code-review-helper-boundary-contract.md)

Operational references and analytics:

- [docs/agent-traversal-review-note.md](agent-traversal-review-note.md)
- [docs/terminal-agent-multiplexer-reference.md](terminal-agent-multiplexer-reference.md)
- [docs/external-ai-engineering-references.md](external-ai-engineering-references.md)
- [docs/ai-visibility-audit-contract.md](ai-visibility-audit-contract.md)
- [docs/donor-adaptation-target-matrix.md](donor-adaptation-target-matrix.md)
- [docs/500-ai-agents-donor-shortlist.md](500-ai-agents-donor-shortlist.md)
- [docs/project-portfolio-adaptation-matrix.md](project-portfolio-adaptation-matrix.md)
- [docs/agents-marketplace-owner-routing.md](agents-marketplace-owner-routing.md)

For profile selection and export behavior, see
[docs/capability-profiles.md](capability-profiles.md).

## Recommended read order

Start here:

- [docs/repo-config.md](repo-config.md)
- [docs/config-apply-planning.md](config-apply-planning.md)
- [docs/orchestrator-compatibility.md](orchestrator-compatibility.md)
- [docs/id-bootstrap.md](id-bootstrap.md)

Then read by need:

- context budget and diversity:
  [docs/context-budget-hint.md](context-budget-hint.md),
  [docs/research-diversity-hint.md](research-diversity-hint.md)
- scope and capability routing:
  [docs/v0.1-scope.md](v0.1-scope.md),
  [docs/capability-profiles.md](capability-profiles.md),
  [docs/llmo-capability-map.md](llmo-capability-map.md)
- reference material:
  [docs/references/open-notebook.md](references/open-notebook.md),
  [docs/references/agent-orchestrators.md](references/agent-orchestrators.md),
  [docs/donor-adaptation-target-matrix.md](donor-adaptation-target-matrix.md),
  [docs/project-portfolio-adaptation-matrix.md](project-portfolio-adaptation-matrix.md),
  [docs/agents-marketplace-owner-routing.md](agents-marketplace-owner-routing.md)

## Why the README is compact

The top-level README stays focused on:

- what `SET` is;
- how to run it;
- what it emits;
- where deeper contracts live.

Detailed adaptation contracts remain in `docs/` so the homepage does not turn
into an always-growing changelog of every imported idea.

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md).
