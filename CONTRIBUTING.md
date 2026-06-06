# Contributing to SET

## Add a new repo to the registry

1. Copy an existing file from `registry/repos/` and rename it to `registry/repos/<owner>_<repo>.json` (replace `/` with `_`).
2. Fill the `repo`, optional `site`, `tools`, and `presets` fields according to `docs/repo-config.md`.
3. Validate locally:

```bash
python3 scripts/validate_registry.py
```

4. Check planned workflow output:

```bash
python3 scripts/plan_config_apply.py <owner/repo> --format json --dry-run
```

If `unmapped` shows any entries, add corresponding wiring in `action.yml` or adjust the registry config.

5. Open a PR to `markoblogo/SET` with only the new/updated registry JSON and optional docs updates.

## CI and local checks

- Keep planner and registry contracts unchanged unless you can justify a migration plan.
- For changes in schema, scripts, or planner contracts, update `docs/repo-config.md` and `docs/config-apply-planning.md` first.
- If you change generated review payload fields, update downstream docs that reference them.

