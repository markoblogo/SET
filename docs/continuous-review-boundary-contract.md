# Continuous Review Boundary Contract

`SET` may describe a compact local continuous-review policy for repositories
where agent-written code changes accumulate fast enough that early review is
worth the extra loop.

This is an optional local workflow aid. It is not a required daemon, not a
global git-hook policy, and not a source of authority to comment on PRs, push
fixes, or rewrite branches automatically.

## Purpose

Use continuous review only where all are true:

- the repository has frequent code commits, not mostly docs/content edits;
- agent-written changes can compound quickly between commits;
- early findings are cheaper to fix than late PR review;
- the repo has a clear owner boundary for accepting or rejecting findings.

## Allowed modes

- `manual` — run review explicitly when the developer chooses;
- `pre-push` — review the branch before push or PR;
- `post-commit optional` — local per-commit review may exist, but only for a
  repo that explicitly opts in;
- `refine-before-ship` — run one branch-level re-review before merge or handoff.

The recommended starting mode is `manual` or `pre-push`, not always-on
background automation.

## Review receipt

Every continuous-review pass should keep a compact receipt:

```text
review_run_id:
repo:
mode:
commit_or_range:
findings_opened:
findings_fixed:
findings_rejected_with_reason:
findings_deferred:
review_status:
```

This is an operational ledger, not hidden reasoning.

## Good fit

Good candidates:

- evolving application codebases;
- repos with auth, workflows, schedulers, integrations, or user-visible state;
- repos where agents commit often during implementation.

Poor candidates:

- mostly documentation or content repositories;
- contract-only repos with sparse code changes;
- repos where every commit would trigger mostly noise or stylistic findings.

## Boundary

- no global install across all repos by default;
- no mandatory background daemon for every repository;
- no automatic PR comments on first adoption;
- no automatic fix commits without explicit repo policy;
- no treating review findings as authoritative without owner/developer judgment;
- no replacing tests, smoke checks, or domain review.
