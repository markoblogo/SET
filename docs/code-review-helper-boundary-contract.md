# Code Review Helper Boundary Contract

`SET` may describe a compact local boundary for `Open Code Review`
(`alibaba/open-code-review`) as an optional second reviewer on diffs before
push or PR.

This is a local execution helper, not a required runtime layer, not a CI gate
by default, and not authority to comment on PRs, auto-fix code, or replace
tests, smoke checks, or owner review.

## Purpose

Use this helper only where all are true:

- the repository is code-heavy enough that diff review has signal;
- agent-written changes can compound before PR review;
- the owner wants one extra local pass before publish;
- findings remain proposal-first and can be rejected with reason.

## Allowed role

Recommended role:

- second reviewer on current diff before push or PR;
- optional branch-range review before handoff;
- optional full-file scan only for unfamiliar or risky code areas.

Not recommended as first adoption:

- required background daemon;
- mandatory per-commit hook across all repositories;
- automatic PR comments;
- automatic fix application as the default flow.

## Repository shortlist

Good current fit:

- `index` including internal Cortex paths;
- `MN7R`;
- `CoqPi`;
- `CortexABV-private`.

Conditional maintainer-only fit:

- `SET`;
- `abvx-agent-skills`;
- `AGENTS.md_generator`.

Poor fit:

- mostly editorial/content repositories;
- design-only or artifact-only repositories;
- repos where docs/copy dominate and code review would mostly add noise.

## Minimal local workflow

Use the helper as a pre-push or pre-PR pass:

1. establish the repo-specific business context;
2. review the current diff or branch range;
3. keep only concrete findings with file/line anchors;
4. fix or reject with reason;
5. still run the repo's normal checks and owner review.

Example local commands:

```bash
ocr review --audience agent -b "repo-specific context"
ocr review --audience agent -b "repo-specific context" --from main --to <branch>
ocr scan path/to/risky/file.ts
```

## Boundary

- no auto-publish, auto-merge, or auto-comment authority;
- no replacing repo checklists, docs drift review, or route review;
- no assuming high recall just because findings are precise;
- no mandatory install outside repositories that opt in;
- no treating tool output as proof that the change is safe to ship.
