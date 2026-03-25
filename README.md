# SET

Thin orchestration repo for the ABVX development tools ecosystem.

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
    agentsgen: "true"
    init: "true"
    pack: "true"
    check: "true"
    analyze: "true"
    analyze_url: "https://example.com"
    autodetect: "true"
    path: "."
```

What v0.1 does:
- installs `agentsgen`
- runs `agentsgen init`
- optionally runs `agentsgen pack`
- optionally runs `agentsgen check --all --ci`
- optionally runs `agentsgen analyze <url>`

## Scope right now

- Freeze the migration map from `LLMO`
- Freeze `SET` v0.1 scope
- Keep the first GitHub Action thin

## Docs

- `docs/llmo-capability-map.md`
- `docs/v0.1-scope.md`
