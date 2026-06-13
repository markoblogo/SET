# ID Bootstrap Runtime Artifact

`SET` can export a formal runtime packet for downstream agent runs when repo-local `ID` integration is enabled and `pre_task` is executed.

Canonical outputs:

- `docs/ai/id-bootstrap.json`
- `docs/ai/id-bootstrap.prompt.md`

These files are not registry config.
They are resolved runtime artifacts produced from the repo-local `ID` hook output at action execution time.

## Purpose

The packet gives downstream agents a stable, machine-readable consumption order for human bootstrap files.

It exists so downstream tools do not have to:

- guess which `ID` file to start from,
- reconstruct bootstrap order from hook logs,
- or treat `soul.md` support as an undocumented convention.

## Generation contract

`SET` writes the packet only when all of the following are true:

- `tools.id.enabled = true`
- `tools.id.pre_task = true`
- the repo-local hook runner exists at `scripts/run_integration_hook.sh`
- the `pre_task` hook returns the expected resolved bootstrap fields

Current source fields:

- `primary_human_bootstrap`
- `preferred_human_bootstrap`
- `profile_core`
- `handshake`
- `soul`
- `integration_guide`

## JSON shape

Current shape:

```json
{
  "version": 1,
  "generated_by": "set",
  "generated_at": "2026-06-13T15:29:18Z",
  "id": {
    "owner_id": "markoblogo",
    "target": "set",
    "primary_human_bootstrap": "profiles/markoblogo/soul.md",
    "preferred_human_bootstrap": [
      "profiles/markoblogo/soul.md",
      "profiles/markoblogo/profile.core.md",
      "profiles/markoblogo/handshake.md"
    ],
    "profile_core": "profiles/markoblogo/profile.core.md",
    "handshake": "profiles/markoblogo/handshake.md",
    "soul": "profiles/markoblogo/soul.md",
    "integration_guide": "integrations/set/README.md"
  },
  "usage": {
    "purpose": "Resolved human bootstrap packet for downstream agent runs.",
    "instructions": [
      "Start with primary_human_bootstrap.",
      "Expand through preferred_human_bootstrap only when more human context is needed.",
      "Treat these files as human-context and operating-constraints inputs, not as repo evidence."
    ]
  }
}
```

## Semantics

- `primary_human_bootstrap` is the required starting point.
- `preferred_human_bootstrap` is the ordered widening path.
- `soul` / `profile_core` / `handshake` are convenience aliases for consumers that want named slots in addition to ordered traversal.
- `usage.instructions` is normative guidance for downstream consumption.

## Stability

For now, treat these guarantees as stable:

- file path: `docs/ai/id-bootstrap.json`
- top-level `version`
- top-level `generated_by`
- `id.primary_human_bootstrap`
- `id.preferred_human_bootstrap`
- `usage.instructions`

Fields may expand over time, but consumers should avoid assuming that undocumented fields are exhaustive.

## Relationship to other artifacts

- `repo-config` describes whether `ID` integration should run.
- `docs/ai/id-context.json` from `agentsgen` describes the repo-side handoff surface.
- `docs/ai/id-bootstrap.json` from `SET` describes the resolved human bootstrap packet at runtime.

So:

- `agentsgen` publishes the repo bridge contract.
- `ID` resolves the human-side bootstrap order.
- `SET` exports the runtime packet that makes that order explicit for downstream execution.
