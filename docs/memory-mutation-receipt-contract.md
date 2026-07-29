# Memory Mutation Receipt Contract

`SET` can export a compact receipt contract for runners that mutate project
memory, session memory, or reviewed durable notes.

`SET` does not store memory and does not provide a memory runtime. It only
describes the minimum evidence a runner should keep when a memory change is
proposed or applied.

## Purpose

Use this contract when a runner can:

- create or update a reviewed memory item;
- correct an existing note;
- promote working memory into a durable layer;
- quarantine contradictory memory;
- roll back a bad memory mutation.

The goal is reversible, inspectable memory change rather than silent overwrite.

## Receipt shape

```text
mutation_id:
project_scope:
memory_scope:
memory_class:
operation:
reason:
source_evidence:
prior_version:
new_version:
snapshot_or_backup_ref:
review_owner:
decision_state:
applied_at:
```

## Required fields

### `project_scope`

The repo, tenant, or approved session scope where the memory lives.

### `memory_scope`

The narrow target surface, for example:

- session memory;
- project memory;
- tenant memory bank;
- approved follow-up notes;
- personal knowledge core candidate.

### `memory_class`

Suggested classes:

- `working`
- `session`
- `project`
- `canonical`
- `archived`

### `operation`

Suggested operations:

- `create`
- `append`
- `replace`
- `correct`
- `promote`
- `quarantine`
- `rollback`

### `source_evidence`

The receipt should point to the source artifact or reviewed evidence used to
justify the memory mutation.

## Write lifecycle

Recommended flow:

```text
retrieve -> inspect -> draft mutation -> emit receipt -> review -> apply or reject
```

If a runner supports snapshots or versioned memory, record the prior and new
version references. If it does not, record the closest available backup or
pre-apply copy reference.

## Contradiction handling

When a new memory item conflicts with an existing approved one:

- do not silently replace the approved note;
- prefer `quarantine` or `candidate for review`;
- keep the conflict visible in the receipt.

## Boundary

- this contract is proposal-first;
- it does not require a specific provider or database;
- it does not grant automatic memory mutation authority;
- it does not merge personal, project, and product memory by default.
