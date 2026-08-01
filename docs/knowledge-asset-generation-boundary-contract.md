# Knowledge Asset Generation Boundary Contract

`SET` may describe AI-generated knowledge assets as reviewed local artifacts.
It does not grant automatic scraping, upload, publication, or durable memory
mutation.

This contract is a compact adaptation of `yusufkaraaslan/Skill_Seekers`: one
explicit source config can produce multiple AI-facing outputs, but source,
provenance, quality, and approval remain first-class.

Source: https://github.com/yusufkaraaslan/Skill_Seekers

## Allowed assets

Generated knowledge assets may include:

- skill drafts;
- repo context packs;
- RAG-ready chunks;
- source manifests;
- quality reports;
- platform projection files.

They are accepted only as local proposal artifacts until reviewed.

## Required controls

Every generation run should record:

- `source_kind`;
- `source_ref`;
- `source_version`;
- `scope_included`;
- `scope_excluded`;
- `generator`;
- `model_or_agent`;
- `target_outputs`;
- `quality_gate`;
- `approval_state`;
- `publication_state`.

## Lifecycle

Use this minimum lifecycle:

- `DRY_RUN`: planned sources and outputs are visible.
- `GENERATED_LOCAL`: assets exist locally only.
- `QUALITY_CHECKED`: structure, provenance, and target fit checked.
- `OWNER_REVIEWED`: accepted, revised, or rejected.
- `PUBLISHED`: separate explicit action, never implicit.

## Not allowed

- broad source discovery without owner-approved scope;
- cloud/vector upload by default;
- marketplace publishing by default;
- generated artifacts becoming canonical without review;
- private or sensitive sources entering public outputs;
- conflict resolution without recorded rationale.

## Project routing

| Target | Boundary |
|---|---|
| `AGENTS.md_generator` | owns source-to-target projection and generated/source boundary |
| `abvx-agent-skills` | owns generated skill review and catalog hygiene |
| `CortexABV-private` | may generate private proposal/review assets only |
| `CoqPi` | may generate selected prep packs only |
| public sites | require explicit source approval and publication review |

## Acceptance rule

A generated knowledge asset is accepted only when source scope is explicit,
provenance is retained, quality checks pass or limitations are named, and a
human has approved any durable or public use.
