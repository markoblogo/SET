# Knowledge Distillation Boundary Contract

`SET` may describe a local knowledge-distillation capability for capturing,
classifying, recalling, and synthesizing project knowledge. It does not grant
automatic memory mutation, feed monitoring, or team-brain authority.

This contract is a compact adaptation of the useful part of
`norrietaylor/distillery`: capture knowledge at the moment of insight, keep
provenance, review new entries, and synthesize from cited retained knowledge.

Source: https://github.com/norrietaylor/distillery

## Default stance

Knowledge distillation is disabled unless a repo or local operator session
explicitly enables it.

The accepted minimum is:

- capture compact entries, not raw session dumps;
- classify before trust;
- retain provenance and owner;
- deduplicate before adding durable memory;
- synthesize only from cited retained entries.

## Allowed stages

| Stage | Purpose | Boundary |
|---|---|---|
| `capture` | record a decision, rationale, bug lesson, source note, or meeting fact | compact entry only |
| `classify` | route to project, sensitivity, trust, and retention | review queue first |
| `recall` | search retained entries | provenance required |
| `synthesize` | combine retained entries into an answer or brief | cite retained sources |
| `radar` | review external GitHub/RSS/feed signals | proposal-only |

## Not allowed

- hosted demo storage for private project or personal data;
- automatic ambient ingestion without explicit source scope;
- cross-project memory transfer without owner review;
- raw transcript, mailbox, or file dumps as durable entries;
- public output based on private entries without promotion approval;
- feed signals that trigger external actions directly.

## Required receipt

Every retained entry or synthesis should record:

- `entry_id`;
- `project_id`;
- `source_kind`;
- `source_ref`;
- `captured_at`;
- `classification`;
- `sensitivity`;
- `retention`;
- `dedup_status`;
- `trusted_state`;
- `owner_review`;
- `derived_output_refs`.

## Project routing

| Project | Status | Boundary |
|---|---|---|
| `CortexABV-private` | allowed_optional | private proposal and owner-review memory only |
| `CoqPi` | allowed_optional | pre-call/post-call notes only, selected context required |
| `index` / MediaHub | allowed_optional | reviewed digest and source-radar artifacts only |
| public sites | review_only | public claim/source logs only |
| finance, contracts, payments | blocked | no memory-derived external action |

## Acceptance rule

A knowledge-distillation setup is accepted only when storage is local or
explicitly approved, new entries pass through review/classification, and
synthesis remains source-cited. Any background feed monitoring starts as
proposal-only and cannot mutate durable memory without review.
