# Config Apply Planning

`SET` now has a planning-only helper for future PR-based config apply flows.

The goal is simple:

- read a real repo-config entry from `registry/repos/*.json`
- convert it into a proposed `SET` workflow shape
- show the intended change without writing anything to a target repo
- optionally export a review bundle for a human-reviewed PR later

## Why this exists

Before adding any repo mutation or PR automation, we want one safe intermediate layer:

- review the intended workflow inputs
- spot unmapped tool fields
- keep config-apply semantics explicit
- make the future PR shape easy to inspect before any apply step exists

## Command

```bash
python3 scripts/plan_config_apply.py markoblogo/lab.abvx
python3 scripts/plan_config_apply.py markoblogo/lab.abvx --format json
python3 scripts/plan_config_apply.py markoblogo/lab.abvx --export-dir /tmp/set-plan
```

## Current output

The planner currently emits:

- one proposed workflow target: `.github/workflows/set.yml`
- the `uses: markoblogo/SET@main` block
- the resolved `with:` inputs derived from registry config
- an `unmapped` list for registry fields not yet wired into the action
- a review payload with PR title/body and ready-to-review workflow YAML

When `--export-dir` is used, the planner writes:

- `plan.json`
- `workflow.set.yml`
- `pr-body.md`

These files are local review artifacts only. They are not applied to the target repo.

## Current limits

- no writes to target repos
- no PR creation
- no branch creation
- no repo mutation
- no multi-workflow planning yet

This is intentionally a planning layer only.
