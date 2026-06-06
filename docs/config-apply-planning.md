# Config Apply Planning

`SET` has a planning-only helper for future PR-based config apply flows.

The goal is safe by default:

- read a registry entry from `registry/repos/*.json`
- resolve a concrete `SET` workflow shape
- show the proposed change without writing to any repo
- export a review bundle for a human-in-the-loop path

## Why this exists

Before any write automation, the planner:

- makes generated `with:` inputs visible
- surfaces unmapped tool fields early (`wiring_gaps`)
- keeps plan/apply semantics reviewable and serializable
- gives CI/operability a stable JSON contract for checks

## Command

```bash
python3 scripts/plan_config_apply.py markoblogo/lab.abvx
python3 scripts/plan_config_apply.py markoblogo/lab.abvx --dry-run --format json
python3 scripts/plan_config_apply.py markoblogo/lab.abvx --export-dir /tmp/set-plan
python3 scripts/plan_config_apply.py markoblogo/lab.abvx --repo-root /absolute/path/to/lab.abvx
python3 scripts/plan_config_apply.py markoblogo/AGENTS.md_generator markoblogo/lab.abvx
python3 scripts/plan_config_apply.py --all --format json
```

## Current output

For a single repo, output contains:

- one proposed workflow target: `.github/workflows/set.yml`
- the `uses: markoblogo/SET@main` block
- the resolved `with:` inputs from registry config and presets
- `dry_run` flag (`true` today) for explicit contract clarity
- an `unmapped` list for capabilities not wired into `action.yml` yet
- review payload with generated PR text, gh-ready payload, apply simulation, workflow YAML
- `would_write` field in text mode showing target files for dry-run planning
- `source_config`, `notes`, and review payload fields for downstream tooling

With `--export-dir`, it writes:

- `plan.json`
- `workflow.set.yml`
- `pr-body.md`
- `gh-pr-create.json`
- `apply-simulation.json`

These files are local and review-only. They are not applied to the target repo.

Example dry-run text fragment:

```text
dry_run: true
would_write:
  - .github/workflows/set.yml
next_shell_command: git checkout -b codex/set-plan-markoblogo-SET
```

For multiple repos, planner emits:

- compact text summary in text mode
- `plans[]` array in JSON mode
- optional batch export with `batch-summary.json` and per-repo directories

When `--repo-root` is provided, planner adds read-only `workflow_check` with status:

- `matches`
- `drift`
- `missing`

## Current limits

- no writes to target repos
- no PR creation
- no branch creation
- no repo mutation
- no multi-workflow planning yet
