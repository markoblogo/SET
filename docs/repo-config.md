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
      "meta_url": null
    },
    "git_tweet": {
      "enabled": false
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
- no secrets live in registry config

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

## Initial registry entries

The first registry entries are:

- `markoblogo/AGENTS.md_generator`
- `markoblogo/lab.abvx`

They are examples of two different repo shapes:

- repo-docs only
- repo-docs + site-ai
