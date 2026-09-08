# Web UI preset

Use `web-ui` for a pull request that changes browser-facing behavior: pages,
components, routes, styles, accessibility, or client-side data flow.

```yaml
- uses: markoblogo/SET@v0.3.1
  with:
    workflow_preset: web-ui
    path: "."
```

The preset runs:

- `agentsgen init`
- `agentsgen pack`
- `agentsgen check --all --ci`
- `agentsgen understand --changed` with a frontend-focused query

Explicit `repomap_focus` and `repomap_changed` inputs override the preset. This
makes it possible to narrow a large repository to one application or package.

## External companions

The preset prepares a reviewable code slice. It does not install or execute
external tools.

- [Modern Web Guidance](https://github.com/GoogleChrome/modern-web-guidance)
  can supply current implementation guidance for HTML, CSS, accessibility,
  browser APIs, and client-side JavaScript.
- [PR Lens](https://github.com/coldteadotai/pr-lens) can render a local
  architecture or data-flow diagram for a substantial pull request.

For private code, prefer PR Lens local rendering and keep the generated
`.pr-lens/` directory uncommitted. Publishing a canvas or installing the hosted
GitHub App is a separate data-sharing decision.

## Boundaries

`web-ui` does not run a browser, perform visual QA, call a model, install either
companion, or prove production behavior. Keep browser evidence and deployment
verification as separate release gates.
