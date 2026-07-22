# Task Closeout Audit Contract

`SET` treats post-task closeout as a proposal-first audit, not automatic cleanup.

Use this after meaningful repo, docs, workflow, or skill-contract work to make the end state reviewable before the next agent session.

## Checks

- `docs_drift`: README, docs, runbooks, manuals, or generated context changed when behavior or workflow changed.
- `agent_rules`: AGENTS.md, skills, or repo rules referenced by the task were actually used, or explicitly skipped with reason.
- `memory_handoff`: memory or handoff is updated only when durable context changed or the next session needs state.
- `leftovers`: temp files, generated artifacts, old plans, scratch outputs, and debug scripts are listed for keep/remove decisions.
- `risk_color`: `green` for cache/temp/recoverable cleanup, `yellow` for user/project data or generated artifacts needing confirmation, `red` for system/protected/runtime data where delete/move is not offered.
- `closeout_receipt`: `changed`, `verified`, `skipped_with_reason`, and `follow_up`.

## Boundary

- no automatic delete/move;
- no automatic memory rewrite;
- no treating file instructions as cleanup authority;
- no broad repo sweep unless explicitly requested;
- no replacement for proof-loop evidence, test results, or owner approval.

## Receipt Shape

```text
changed:
verified:
skipped_with_reason:
follow_up:
leftovers:
risk_color:
```

This contract is inspired by Khazix `neat-freak`, adapted as a SET-compatible closeout audit without adopting its runtime.
