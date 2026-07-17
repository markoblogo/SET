# Git-Native Context Contract

`SET` can export a disabled, provider-neutral contract for minimal project context stored as Git-reviewed typed Markdown. It does not install Archcore or any other context runtime.

Select it with:

```json
"capability_profile": "git-native-context"
```

The contract appears at `orchestrator_bundle.context_package.git_native_context_contract` and grants no write authority.

## Minimal document types

- `adr`: a finalized architecture or technical decision and its rationale.
- `rfc`: a proposed significant change still open for review.
- `rule`: an imperative engineering or operating standard.
- `spec`: a normative behavior contract for a component, interface, schema, protocol, or subsystem.
- `plan`: bounded implementation work, dependencies, acceptance criteria, and verification.
- `rnd`: a time-boxed investigation that ends in a recommendation and next action.
- `cpat`: a durable code-change or incident pattern.

Adding another type requires an explicit project-level contract change. Topic alone never justifies a new type.

## Lifecycle

Every document starts as `draft`. Valid terminal decisions are `accepted` and `rejected`. Agents may propose acceptance but must not set `accepted` without explicit human approval recorded as `approved_by`, `approved_at`, and `approval_reference`.

Rejected documents remain in Git when they preserve a useful dead end or superseded decision. Deletion follows the host repository's normal explicit approval and recovery rules.

## Directed relations

Relations contain `source`, `type`, and `target`:

- `implements`: source realizes or formalizes target.
- `depends_on`: source requires target.
- `extends`: source builds on target.
- `related`: symmetric conceptual association.

Both documents must exist first. Duplicate and self-referential relations are invalid. Relation direction is semantic evidence, not an automatic lifecycle transition.

## Code Change Pattern

A `cpat` requires:

```text
symptom:
root_cause:
change:
scope:
verification:
prevention:
```

`verification` names observed evidence, not an intended check. `prevention` identifies the durable test, guard, documentation, diagnostic, or process change that reduces recurrence.

## Storage and authority

The portable representation is typed Markdown with YAML frontmatter in a repo-owned directory. Writes follow `proposal -> inspect -> apply`. Existing project truth remains authoritative: `AGENTS.md`, `docs/ai`, product contracts, protected evidence stores, runtime ledgers, signed agreements, and code.

## Attribution

Adapted from the minimal reusable parts of [archcore-ai/cli](https://github.com/archcore-ai/cli): typed Git-native documents, lifecycle states, directed relations, and code-change patterns. This contract does not adopt Archcore's CLI, MCP server, hooks, session injection, full taxonomy, or sync runtime.
