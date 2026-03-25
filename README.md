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

## Scope right now

- Freeze the migration map from `LLMO`
- Freeze `SET` v0.1 scope
- Keep the first GitHub Action thin

## Docs

- `docs/llmo-capability-map.md`
- `docs/v0.1-scope.md`
