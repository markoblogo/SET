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
