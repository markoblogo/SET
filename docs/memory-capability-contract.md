# Memory Capability Contract

`SET` can describe an optional project-memory capability for downstream runners without storing memory or providing an MCP server.

The planner exports this contract under:

```text
orchestrator_bundle.context_package.memory_capability
```

The default is `enabled: false`. A runner may implement the capability with RMS Memory MCP, another local service, or a project-specific adapter. The contract is intentionally provider-neutral.

## Capabilities

### `search`

Search the current project's memory before planning or mutating code. A provider may combine full-text and semantic retrieval. Full-text remains the fallback when semantic indexing is unavailable.

### `read`

Read the complete source document after a relevant search result. Search snippets are context hints, not sufficient evidence for a write or architectural decision.

### `write`

Persist a reviewed decision, constraint, or durable lesson. Writes are not implicit side effects of a successful run. They must remain proposal-first and pass an audit/inspection step before apply.

## Isolation

- memory is scoped per project, keyed by the `repo` identity in the bundle;
- cross-project reads are disabled by default;
- a runner must not merge personal, project, and product memory into one unscoped search space;
- linked source files and raw notes remain read-only unless an explicit user-approved apply path says otherwise.

## Retrieval

The contract describes capability, not a mandatory implementation:

- `full_text` supports exact names, paths, identifiers, and quotes;
- `semantic` supports concept-level recall and paraphrases;
- `hybrid-when-available` combines both and falls back to full-text;
- every returned memory item should retain its source path and project scope.

### Tiered loading

When a runner needs more than snippet-level recall, prefer a three-level load
shape instead of dumping every retrieved document into active context:

- `L0` — abstract/index view: short identity, scope, and why this item might
  matter;
- `L1` — overview view: compact summary or reviewed section map;
- `L2` — detail view: exact passage, file, or evidence slice actually required
  for the decision.

The safe default is to start at `L0`, promote only the few relevant items to
`L1`, and open `L2` only for the sources that survive review. A runner may use
other names, but the escalation boundary should stay explicit and inspectable.

### Retrieval trajectory

Every non-trivial retrieval should be explainable as a short receipt:

```text
request_id:
project_scope:
retrieval_mode:
query_or_goal:
items_considered:
items_opened:
levels_touched:
final_items_used:
dropped_items_with_reason:
```

This trajectory is operational evidence, not hidden chain-of-thought. It helps
review whether the runner widened context too early, used stale notes, or
skipped authoritative sources.

### Retrieval observability

If a runner implements project memory, it should surface at least:

- last successful refresh or index build time;
- stale/missing-source warning;
- current indexing state (`ready`, `refreshing`, `failed`, `unknown`);
- last retrieval failure class;
- whether a result came from `L0`, `L1`, or `L2`.

These are review signals only. `SET` does not require a server, virtual
filesystem, or specific memory backend.

## Write gate

The recommended write lifecycle is:

```text
search -> read -> draft memory proposal -> inspect/audit -> apply or discard
```

Before `apply`, the runner should record:

- project scope and target path;
- why the memory is durable rather than session-specific;
- source/evidence references;
- proposed operation (`create`, `append`, or `replace`);
- backup or snapshot location;
- audit result and operator decision.

## Boundary

`SET` exports the contract and expected policy. External runners own memory storage, indexing, MCP transport, credentials, and runtime state. `abvx-agent-skills` defines how an agent should use the capability safely. A memory provider must not become a hidden source of completion evidence or silently rewrite `AGENTS.md`, raw notes, or product files.
