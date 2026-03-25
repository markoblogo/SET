# Config Apply Planning

`SET` now has a planning-only helper for future PR-based config apply flows.

The goal is simple:

- read a real repo-config entry from `registry/repos/*.json`
- convert it into a proposed `SET` workflow shape
- show the intended change without writing anything to a target repo

## Why this exists

Before adding any repo mutation or PR automation, we want one safe intermediate layer:

- review the intended workflow inputs
- spot unmapped tool fields
- keep config-apply semantics explicit

## Command

```bash
python3 scripts/plan_config_apply.py markoblogo/lab.abvx
python3 scripts/plan_config_apply.py markoblogo/lab.abvx --format json
```

## Current output

The planner currently emits:

- one proposed workflow target: `.github/workflows/set.yml`
- the `uses: markoblogo/SET@main` block
- the resolved `with:` inputs derived from registry config
- an `unmapped` list for registry fields not yet wired into the action

## Current limits

- no writes
- no PR creation
- no branch creation
- no repo mutation
- no multi-workflow planning yet

This is intentionally a planning layer only.
