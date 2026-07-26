# Dependency Risk Check Shortlist

Date: 2026-07-26

This shortlist records where the `dependency-risk-check` contract is currently
worth using.

## Allowed / high-value

These repos should be allowed to use dependency-risk checks because package
changes can materially affect runtime behavior or external boundaries:

- `index`
- `MN7R`
- `CoqPi`
- `liqua`

Why:

- active application code;
- real package churn;
- auth, provider, runtime, map/media, or relay surfaces can be affected by
  third-party dependencies.

## Allowed / selective

These repos may use the contract, but usually only around explicit dependency
changes, not as a standing workflow:

- `SET`
- `abvx-agent-skills`

Why:

- both contain real code and packaging surfaces;
- but dependency risk is a narrower concern than in the larger app repos.

Recommended default:

- run before add/upgrade/release;
- keep it manual or pre-push;
- do not require it for docs-only work.

## Not recommended

These repos should not currently prioritize dependency-risk checks:

- `CortexABV-private`
- `menton`
- `lab.abvx`
- internal review sandboxes
- generated-cache and temporary review repos

Why:

- dependency churn is low or not the main risk surface;
- docs/content/contract truth matters more than package risk in normal work.

## Current rule

Use dependency-risk checks:

- on code-heavy repos with real package churn;
- around add/upgrade/release moments;
- not as a substitute for broader security or quality review.
