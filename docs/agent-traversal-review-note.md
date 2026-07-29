# Agent Traversal Review Note

`SET` may point to a local visualization helper such as `mindwalk` when the
goal is to inspect how an agent traversed a repository during a coding session.

This is an optional observability aid, not a runtime dependency, CI gate, or
quality score.

## Purpose

Use a traversal review when a team wants to understand:

- whether the agent wandered too broadly before finding the right files;
- whether search, read, and edit activity stayed near the expected focus set;
- whether a new rule, skill, or repo-doc change reduced wasted traversal;
- whether repeated file reopens suggest unclear structure or weak naming.

## Good uses

- compare before/after a repo-doc or skill change;
- inspect one difficult coding session after the fact;
- diagnose read/search imbalance on medium or large repos;
- support search-discoverable-code and lean-context improvements with evidence.

## Bad uses

- treating a pretty map as proof the outcome was correct;
- making it a required step for every task;
- using it as background telemetry on all repos by default;
- widening it into a new runtime or monitoring layer.

## Minimal review questions

1. Did the session spend too long outside the expected module or directory set?
2. Were the same files reopened repeatedly without converging on a fix?
3. Did edits cluster near the files that search and reading suggested?
4. Would tighter naming, smaller docs, or a better skill have shortened the path?
5. Is this worth a repo-local rule, or was it just a one-off hard task?

## Local helper shape

For `mindwalk`, the useful local modes are:

```bash
mindwalk map <repo>
mindwalk open <session.jsonl> --no-open
mindwalk serve --no-open
```

Treat the output as review material only. Findings should flow into repo docs,
skills, or contracts only after human review.

## Boundary

- local-only by default;
- no project dependency;
- no required installation for downstream repos;
- no automatic scoring or policy enforcement.
