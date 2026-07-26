# Dependency Risk Check Contract

`SET` can describe a compact local dependency-risk-check policy for repositories
that actively add, upgrade, or trim third-party packages.

This is a review contract only. It is not a package manager, not a dependency
bot, not a full security program, and not permission to auto-upgrade or
auto-remove dependencies.

## Purpose

Use this contract to review dependency risk before package changes compound into
security, license, typo-squat, or maintenance problems.

The goal is to decide:

- whether a proposed dependency change is acceptable;
- whether a package introduces known vulnerability or typo-squat signals;
- whether the dependency belongs in the repo at all;
- whether the change should be blocked, deferred, or accepted with evidence.

## Trigger points

Run a dependency-risk check when one of these happens:

- adding a new package;
- upgrading a package or lockfile range;
- replacing one provider/library with another;
- removing or consolidating dependencies in a sensitive code path;
- preparing a release or push after meaningful dependency churn.

Do not run it mechanically on every trivial commit.

## Audit scope

The review should look for:

- known vulnerabilities;
- typo-squat or suspicious package-name risk;
- license incompatibility or uncertainty;
- stale or abandoned package signals;
- dependency sprawl where a simpler existing package would suffice.

## Receipt

Each non-trivial dependency review should keep a short receipt:

```text
review_id:
repo:
ecosystem:
package_or_range:
change_type:
issue_type:
severity:
source:
decision:
follow_up:
```

Suggested `decision` values:

- `accept`
- `defer`
- `replace`
- `remove`
- `reject`

## Good fit

Use this in repos where:

- package churn is real;
- app/runtime/security boundaries matter;
- dependencies affect auth, network, provider, build, or user-visible flows;
- agents may add packages quickly during implementation.

## Bad fit

Do not prioritize this in repos that are:

- mostly docs/content;
- private contract/config surfaces with rare dependency changes;
- static reference or archive repos with near-zero package churn.

## Boundary

- no automatic dependency upgrades;
- no automatic lockfile churn from findings alone;
- no treating a clean dependency scan as proof of application security;
- no replacing threat modeling, tests, smoke checks, or code review;
- no mandatory always-on MCP/runtime requirement.
