# Repo Config Contract (v1)

`SET` now has a real repo-config contract.

The first working version is intentionally small and explicit.
It is designed to be:

- easy to review in git,
- easy to validate without extra services,
- stable enough for orchestration,
- reusable later by `lab.abvx` as a read-only data source.

## Canonical format

The first working contract is JSON.

Files:

- `schema/repo-config.v1.json`
- `examples/repo-config.example.json`
- `registry/repos/*.json`

JSON is the pragmatic v1 choice because it gives us a deterministic, dependency-free validator.
We can still add a YAML view later if the dashboard or authoring flow benefits from it.

## Shape

```json
{
  "version": 1,
  "repo": "owner/name",
  "site": {
    "url": "https://example.com"
  },
  "tools": {
    "agentsgen": {
      "init": true,
      "pack": true,
      "check": true,
      "repomap": false,
      "repomap_policy": {
        "compact_budget": 4000,
        "top_ranked_files": 5,
        "focus": null,
        "changed": false
      },
      "snippets": false,
      "analyze_url": null,
      "meta_url": null,
      "proof_loop": {
        "enabled": false,
        "task_id": null,
        "expected_artifacts": []
      }
    },
    "git_tweet": {
      "enabled": false
    },
    "id": {
      "enabled": false,
      "owner_id": null,
      "target": "set",
      "pre_task": false,
      "weekly_review": false
    }
  },
  "presets": [
    "repo-docs"
  ]
}
```

## Rules

- `version` is required and must be `1`
- `repo` is required and must be `owner/name`
- `tools` is required
- `presets` is optional but must use known names
- explicit tool fields win over preset defaults
- `agentsgen.repomap_policy` is optional and currently supports `compact_budget`, `top_ranked_files`, `focus`, and `changed`
- `agentsgen.proof_loop` is optional and currently supports `enabled`, `task_id`, and `expected_artifacts`
- `id` is optional and currently supports repo-local `owner_id`, `target`, `pre_task`, and `weekly_review` gates for ID-compatible repositories
- SET derives a first-class label from that policy for UI/planning: `full` (Full Repo Slice), `focus` (Focused Code Slice), `changed` (Changed Files Slice), `focus+changed` (Hybrid Slice)
- no secrets live in registry config

## Runtime artifacts

`repo-config` is the control-plane contract.
Some enabled features also produce runtime artifacts inside the target repository.

For `ID` integration, the important distinction is:

- config decides whether the ID hooks should run,
- runtime artifacts capture what the hooks resolved for a concrete run.

When `tools.id.enabled = true` and `tools.id.pre_task = true`, `SET` may export:

- `docs/ai/id-bootstrap.json`
- `docs/ai/id-bootstrap.prompt.md`

These are formal runtime outputs, not implementation leftovers.
They are intended for downstream agents and orchestration layers that need a stable, explicit human bootstrap packet.

See `docs/id-bootstrap.md` for the current shape and consumption rules.

The planner can also export `orchestrator-bundle.json` for external agent runners. That bundle is derived from registry config plus resolved planning state; it is not a registry source of truth. See `docs/orchestrator-compatibility.md`.

## Central registry decision

Central registry first lives in `SET`.

Why:

- `SET` is the orchestration contract owner
- the registry belongs closer to execution semantics than to public catalog copy
- `lab.abvx` can read it later without becoming the source of truth too early
- this keeps the first control-plane phase read-only and low-risk

So the near-term model is:

- `SET` owns `schema/`, `examples/`, and `registry/`
- `lab.abvx` can later consume registry data for dashboard/catalog views
- PR-based apply flows can grow from this contract without moving the source of truth yet

## Validation

Use the built-in validator:

```bash
python3 scripts/validate_registry.py
```

This checks:

- supported version
- required keys
- known tool blocks
- known preset names
- simple field types

## agents.knowledge.json

`agents.knowledge.json` is an agent-oriented artifact generated from repository analysis and used by AI tooling at runtime.

- It is not a registry source of truth.
- It is used by `agentsgen` runtime and tooling that consumes local repo intelligence.
- This repository-level contract (`repo-config`) remains separate and is versioned in the registry.

## Initial registry entries

The first registry entries are:

- `markoblogo/AGENTS.md_generator`
- `markoblogo/lab.abvx`

They are examples of two different repo shapes:

- repo-docs only
- repo-docs + site-ai
