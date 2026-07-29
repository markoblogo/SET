# Codex Security Repo-Selection Matrix

`SET` may describe `openai/codex-security` as a local, optional second
reviewer for security-shaped diffs.

It is not a required runtime, not a default CI gate, not authority to comment
on pull requests, and not a substitute for tests, smoke checks, receipts, or
owner review.

## Purpose

Use this matrix to answer three questions before a local scan:

1. is this repository a good fit;
2. is this specific diff security-shaped enough to justify the scan;
3. what should the scan explicitly ignore.

## Global boundary

Allowed role:

- local second reviewer before push or PR;
- optional narrow review of a risky subtree or changed file set;
- proposal-first findings with explicit accept/reject handling.

Not allowed as default policy:

- mandatory install across every repo;
- automatic PR comments;
- automatic fixes as the primary path;
- security-scan output treated as ship proof by itself.

Typical local run:

```bash
npx codex-security scan .
```

## Trigger classes

Run only when the diff materially touches one or more of these classes:

- auth, secrets, tokens, credentials, API keys;
- IPC, API, backend, worker, scheduler, automation, publishing routes;
- retrieval/runtime logic, provider routing, tool routing;
- session payloads, tenant boundaries, admission policy, protected/public seams;
- Electron or app-shell bridges;
- external integrations with write or sensitive read paths.

Usually skip when the diff is only:

- docs or README wording;
- editorial/content copy;
- catalog metadata;
- purely visual/UI tweaks with no execution or data-boundary effect;
- static assets with no runtime behavior change.

## Repository matrix

| Repo class | Status | Run for | Skip for | Notes |
| --- | --- | --- | --- | --- |
| `CoqPi` | allow | Electron, IPC, realtime/session payloads, backend key handling, auth, runtime integrations | prose-only, UI-only, content-only changes | strong fit |
| `index` incl. Cortex runtime paths | allow | automation, publishing flows, backend/runtime scripts, retrieval/runtime logic, auth, secrets, boundary-sensitive paths | editorial, catalog, copy-only, visual-only changes | strong fit |
| `CortexABV-private` | allow | admission, retrieval/runtime logic, credential handling, proposal execution boundaries, tenant/data-isolation contracts | narrative docs, public-copy-only changes | strong fit |
| `ABVXsite/cortex-abv` | allow | observer logic, proposal-pack shaping, policy/executor boundaries, runtime adapters, token handling | public-copy-only, docs-only, catalog-only changes | scoped fit |
| `DMV` / `liqua` app-shell repos | allow_conditional | app-shell, map/runtime logic, API/integration boundaries, auth, automation-sensitive changes | copy-only or purely visual diffs | moderate fit |
| `MN7R` | allow_conditional | auth, monitor/reporting/scheduler behavior, relay logic, operational scripts | guide copy-only or content-only changes | good fit when runtime-heavy |
| `SET` | maintainer_only | orchestration planning logic, capability/profile exports, route semantics, generated-vs-owned boundaries | descriptive docs unless behavior claims changed | use sparingly |
| `AGENTS.md_generator` | maintainer_only | export validation, generated/committed boundaries, harness-specific projections | normal prose/docs edits | use for generator/runtime code only |
| `abvx-agent-skills` | maintainer_only | catalog generation, validators, packaging/publish scripts | skill prose/content-only edits | usually not needed |
| editorial/content repos | deny | none by default | almost all changes | too noisy |
| design/artifact-only repos | deny | none by default | almost all changes | low signal |

## Selection rule

Choose `codex-security` only if all are true:

1. the repo is `allow`, `allow_conditional`, or `maintainer_only`;
2. the current diff matches at least one trigger class;
3. the repo's normal checks still run separately;
4. findings will be handled as proposals, not auto-applied truth.

If any of those fail, skip the scan.

## Interaction with other local helpers

- Use `Open Code Review` when the main question is general diff quality,
  blast radius, or review breadth.
- Use `codex-security` when the main question is auth, isolation, secret
  handling, route safety, or boundary misuse.
- It is valid to run both on the same diff, but only for repos where the extra
  review signal is worth the time.

## Minimal receipt

When a scan is used, keep a minimal local note:

- repo;
- diff scope;
- why it matched the trigger class;
- accepted findings;
- rejected findings with reason;
- follow-up check still required.
