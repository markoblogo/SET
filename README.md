# SET

Thin orchestration repo for the ABVX development tools ecosystem.

It stays deliberately small: presets define a baseline, and explicit inputs override the preset when you need per-repo control.

Current working definition:
- `agentsgen` = repo intelligence runtime
- `SET` = orchestration layer / GitHub Action entrypoint
- `lab.abvx` = public catalog and later control plane
- standalone tools such as `git-tweet` stay independent and are integrated by contract

This repo starts intentionally small.

## Example usage

```yaml
- uses: markoblogo/SET@main
  with:
    workflow_preset: "site-ai"
    agentsgen: "true"
    init: "true"
    pack: "true"
    site_pack: "true"
    site_url: "https://example.com"
    check: "true"
    analyze: "true"
    analyze_url: "https://example.com"
    meta: "true"
    meta_url: "https://example.com"
    autodetect: "true"
    path: "."
```

Preset baselines:
- `minimal` -> repo bootstrap only
- `repo-docs` -> init + pack + check
- `site-ai` -> repo-docs + site pack + analyze + meta

What v0.1 does:
- installs `agentsgen`
- runs `agentsgen init`
- optionally runs `agentsgen pack`
- optionally runs `agentsgen pack --site <url>`
- optionally runs `agentsgen check --all --ci`
- optionally runs `agentsgen analyze <url>`
- optionally runs `agentsgen meta <url>`
- supports `workflow_preset` baselines with explicit input override
- writes a compact GitHub Actions summary for the resolved run plan


## Repo config contract

`SET` now owns the first real repo-config contract and central registry baseline.

- Contract docs: `docs/repo-config.md`
- Canonical schema: `schema/repo-config.v1.json`
- Example config: `examples/repo-config.example.json`
- Central registry (first home): `registry/repos/*.json`
- Validate locally: `python3 scripts/validate_registry.py`


## Config apply planning

Planning-only helper for future PR-based config apply:

- Docs: `docs/config-apply-planning.md`
- Command: `python3 scripts/plan_config_apply.py markoblogo/lab.abvx`
- JSON mode: `python3 scripts/plan_config_apply.py markoblogo/lab.abvx --format json`

## Scope right now

- Freeze the migration map from `LLMO`
- Freeze `SET` v0.1 scope
- Keep the first GitHub Action thin

## Docs

- `docs/llmo-capability-map.md`
- `docs/v0.1-scope.md`
