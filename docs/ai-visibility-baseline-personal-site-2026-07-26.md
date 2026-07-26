# AI Visibility Weekly Artifact

Artifact ID: `ai-visibility-weekly`

## Run metadata

- run_date: 2026-07-26
- bundle_id: `personal-site-visibility`
- reviewer: Codex
- engines_tested: pending live selection
- prompt_pack_version: `v0-baseline`
- prior_artifact: none
- run_status: `pending_live_observation`

## Scope snapshot

This baseline run is prepared for the owner's public personal and project surfaces.

Initial owned/public surfaces to confirm before live execution:

- `abvx.xyz`
- `1d3x.com`
- `books.1d3x.com`

Initial entity groups to confirm before live execution:

- owner identity / author surface;
- named public projects;
- named books and book series;
- primary official domains and overview pages.

## Coverage

- prompts_run: 0 live prompts executed in this artifact yet
- prompts_skipped_with_reason: all prompt observations pending live engine execution
- entities_in_scope:
  - owner identity
  - ABVX
  - 1D3X
  - books / book-library surfaces
- owned_domains_in_scope:
  - `abvx.xyz`
  - `1d3x.com`
  - `books.1d3x.com`

## Prompt pack

Stable baseline prompt set for the first two runs:

- `P01` — Who is <owner name>?
- `P02` — What projects is <owner name> known for?
- `P03` — What books or publications are associated with <owner name>?
- `P04` — What is ABVX?
- `P05` — What is 1D3X?
- `P06` — Which projects are related to `1d3x.com`?
- `P07` — Which projects or publications are related to `abvx.xyz`?
- `P08` — Where can I read about <project name>?
- `P09` — What is the official site for <project name or book>?
- `P10` — Which sources explain <project/category> best?

## Scorecard

- mention_rate: pending_live_observation
- correct_identity_rate: pending_live_observation
- owned_source_rate: pending_live_observation
- source_depth: pending_live_observation
- confusion_count: pending_live_observation
- opportunity_count: pending_live_observation

## Key observations

- strongest visibility win: not recorded yet
- weakest visibility gap: not recorded yet
- recurring confusion pattern: likely risk around generic/non-owner meanings of `1d3x`; confirm during live run
- unexpected cited source: not recorded yet
- missing owned source page: to be determined from live results

## Delta vs previous run

- improved: baseline run
- unchanged: baseline run
- worsened: baseline run
- new confusion: baseline run
- removed confusion: baseline run

## Prompt-level notes

- `P01`
  - engines: pending
  - outcome: pending_live_observation
  - owned_source_used: pending_live_observation
  - note: identity/author baseline

- `P02`
  - engines: pending
  - outcome: pending_live_observation
  - owned_source_used: pending_live_observation
  - note: project discovery baseline

- `P03`
  - engines: pending
  - outcome: pending_live_observation
  - owned_source_used: pending_live_observation
  - note: books/publications baseline

- `P04`
  - engines: pending
  - outcome: pending_live_observation
  - owned_source_used: pending_live_observation
  - note: ABVX entity baseline

- `P05`
  - engines: pending
  - outcome: pending_live_observation
  - owned_source_used: pending_live_observation
  - note: 1D3X entity baseline; watch for name collision/confusion

## Recommended actions

- immediate page/content fixes:
  - confirm the canonical public entity list before the first live run;
  - confirm the exact preferred official domains/pages for owner, projects, and books;
  - keep this prompt pack unchanged for the second run so the delta is meaningful.

- later structural fixes:
  - if live runs show identity confusion, add or strengthen a dedicated owner/about page;
  - if books are weakly surfaced, strengthen dedicated book pages and author linkage;
  - if projects are cited via shallow pages only, create deeper overview/FAQ/comparison pages.

- items to verify in the next run:
  - whether owned pages are used as cited or implied sources;
  - whether project-to-owner and book-to-owner linkage is correct;
  - whether `1d3x` identity collides with unrelated public meanings.

## Decision

- keep prompt pack unchanged next run: yes
- expand scope next run: no
- automation ready: no
- follow_up_owner_note: complete one real live-engine pass on the current prompt set before adding new entities or dashboards
