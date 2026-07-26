# Agents Marketplace Owner Routing

When an external repo looks like a multi-agent marketplace, plugin ecosystem,
or multi-harness skill catalog, `SET` should route the useful parts to the
correct owner layer instead of absorbing the whole pattern.

This note is the compact adaptation of what is useful from repos such as
`wshobson/agents`.

## Routing rule

Ask three questions in order:

1. Does this change how repo contracts are emitted or validated across
   harnesses?
2. Does this change how reusable skills are evaluated, cataloged, or published?
3. Does this change orchestration, ownership, or cross-repo adaptation policy?

## Owner layer mapping

Route the idea to:

- `AGENTS.md_generator` when the value is:
  - multi-harness export;
  - generated vs source contract boundaries;
  - repo-readable manifests;
  - harness-specific projections;
  - drift validation for generated contract surfaces.

- `abvx-agent-skills` when the value is:
  - skill quality evaluation;
  - catalog hygiene;
  - skill publishing discipline;
  - progressive-disclosure packaging;
  - validation and evidence for reusable skill behavior.

- `SET` when the value is:
  - owner-layer routing;
  - portfolio-wide adaptation policy;
  - orchestration contracts;
  - cross-repo decision about where a donor idea belongs.

## What `SET` should not do

`SET` should not:

- mirror a plugin marketplace;
- become a general skill catalog;
- own harness-native repo exports;
- own per-skill quality metadata that belongs in the skill repo.

## Practical default

For marketplace-like donor repos:

- first adapt export/validation ideas into `AGENTS.md_generator`;
- then adapt skill-quality/catalog ideas into `abvx-agent-skills`;
- finally add only the owner-routing note or policy consequence into `SET`.
