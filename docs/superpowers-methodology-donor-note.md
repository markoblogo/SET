# Superpowers Methodology Donor Note

`obra/superpowers` is a useful methodology donor, not a default runtime for
`SET`.

The useful part is the explicit development discipline around skills,
owner-readable design, planning, verification, and branch finish receipts. The
unsafe part is adopting a full mandatory workflow that can override repo-local
authority, existing `SET` contracts, or human review gates.

Source: https://github.com/obra/superpowers

## Adopted minimum

Use these ideas as optional vocabulary in `SET` profiles and contracts:

- `skill-trigger discipline`: before widening work, name the relevant local
  skill or contract, or record `SKIPPED_WITH_REASON`.
- `design-before-plan`: for non-trivial changes, produce a short design/spec
  chunk before an implementation plan.
- `branch-finish receipt`: separate "code changed" from "verified", "reviewed",
  "ready for PR", "merged", "kept open", or "discarded".
- `skill behavior evals`: treat skills as versioned artifacts whose behavior can
  be checked with fixtures, rollout evidence, and held-out validation.
- `multi-harness awareness`: route harness packaging and generated surfaces to
  `AGENTS.md_generator`, not into `SET` policy files.

## Boundary

Do not import these as defaults:

- mandatory full Superpowers installation;
- automatic subagent-driven development;
- worktree-per-task as a universal rule;
- rigid TDD enforcement for every task type;
- telemetry-bearing visual companion features;
- any workflow that claims execution authority without the existing `SET`
  approval, route, and verification states.

## Target routing

| Target | What belongs there |
|---|---|
| `SET` | methodology boundary, route states, approval gates, branch-finish receipts |
| `AGENTS.md_generator` | multi-harness projection, generated/source-owned boundary, session-start hints |
| `abvx-agent-skills` | skill trigger discipline, skill eval tiers, catalog-quality gates |
| Project repos | only local notes when a project needs the pattern for real execution |

## Acceptance rule

A Superpowers-derived change is accepted only when it stays small, disabled by
default, and names the existing ABVX contract it extends. If it duplicates an
existing contract without adding a sharper check, reject it with a source-linked
reason.
