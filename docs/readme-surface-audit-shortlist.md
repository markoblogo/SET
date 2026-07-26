# README Surface Audit Shortlist

Date: 2026-07-26

This shortlist records where the `readme-surface-audit` contract is currently
appropriate in the ABVX-style repo set.

## Allowed / high-value

These repos have a real public-facing README surface and can benefit from
audit-first README work:

- `SET`
- `lab.abvx`
- `abvx-agent-skills`
- `index`
- `liqua`

Why:

- they function as public entry points;
- visitors need fast orientation and trust signals;
- README hierarchy and proof quality materially affect perception and adoption.

## Allowed / selective

These repos may use the contract, but only when the README is serving external
positioning rather than internal operations:

- `MN7R`
- `CoqPi`

Why:

- both have meaningful public/project-facing README value;
- but both also have operational depth, so decorative or over-marketing rewrites
  should be avoided.

Recommended default:

- start with `audit-only`;
- keep rewrites narrow;
- avoid asset-heavy README work unless there is explicit public-facing intent.

## Not recommended

These repos should not currently prioritize README-surface beautification:

- `CortexABV-private`
- `menton` when the work target is guides/content rather than repo homepage
- internal review sandboxes
- generated-cache or temporary review repos
- contract-heavy/private/runtime-control repos without public discovery value

Why:

- public README polish is not their main bottleneck;
- the maintenance cost and false-positioning risk are higher than the benefit.

## Current rule

The contract should be used:

- first on public-facing repos;
- second as an audit;
- only later as a rewrite or asset pass if the audit shows a real trust or
  orientation problem.
