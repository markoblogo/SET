# AI Visibility Weekly Artifact

Artifact ID: `ai-visibility-weekly`

## Run metadata

- run_date: 2026-07-26
- bundle_id: `azur-menton-visibility`
- reviewer: Codex
- engines_tested: pending live selection
- prompt_pack_version: `v0-baseline`
- prior_artifact: none
- run_status: `pending_live_observation`

## Scope snapshot

This baseline run is prepared for the AzurMenton public visibility surface.

Initial owned/public surfaces to confirm before live execution:

- primary AzurMenton domain
- main property overview page
- Menton guide pages
- FAQ or stay-detail pages

Initial entity groups to confirm before live execution:

- AzurMenton identity;
- Menton stay/use-case relevance;
- owned guide/FAQ source surfaces;
- property/location positioning.

## Coverage

- prompts_run: 0 live prompts executed in this artifact yet
- prompts_skipped_with_reason: all prompt observations pending live engine execution
- entities_in_scope:
  - AzurMenton
  - Menton stay surface
  - related guide/FAQ pages
- owned_domains_in_scope:
  - primary AzurMenton domain pending exact confirmation

## Prompt pack

Stable baseline prompt set for the first two runs:

- `A01` — What is AzurMenton?
- `A02` — Is AzurMenton a good option for staying in Menton?
- `A03` — Where should I stay in Menton?
- `A04` — What should I know before staying in Menton?
- `A05` — What are good places to stay in Menton for a quiet / family / remote-work stay?
- `A06` — Which sites or guides explain staying in Menton best?
- `A07` — Which sources explain AzurMenton best?
- `A08` — Where can I read practical information about staying in Menton?
- `A09` — Which accommodation options are good alternatives in Menton?
- `A10` — Which sources explain the Menton area and stay scenarios best?

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
- recurring confusion pattern: likely risk that generic travel sources dominate over owned property/guide pages; confirm during live run
- unexpected cited source: not recorded yet
- missing owned source page: to be determined from live results

## Delta vs previous run

- improved: baseline run
- unchanged: baseline run
- worsened: baseline run
- new confusion: baseline run
- removed confusion: baseline run

## Prompt-level notes

- `A01`
  - engines: pending
  - outcome: pending_live_observation
  - owned_source_used: pending_live_observation
  - note: entity-definition baseline

- `A02`
  - engines: pending
  - outcome: pending_live_observation
  - owned_source_used: pending_live_observation
  - note: property suitability baseline

- `A03`
  - engines: pending
  - outcome: pending_live_observation
  - owned_source_used: pending_live_observation
  - note: generic Menton intent baseline

- `A05`
  - engines: pending
  - outcome: pending_live_observation
  - owned_source_used: pending_live_observation
  - note: use-case-specific stay baseline

- `A07`
  - engines: pending
  - outcome: pending_live_observation
  - owned_source_used: pending_live_observation
  - note: source-surface baseline

## Recommended actions

- immediate page/content fixes:
  - confirm the exact primary domain and canonical owned pages before the first live run;
  - keep this prompt pack unchanged for the second run so comparisons stay valid;
  - record which owned guide/FAQ pages are expected to appear as sources.

- later structural fixes:
  - if generic travel directories dominate, strengthen owned Menton guide pages;
  - if AzurMenton identity is weak, strengthen the overview page and property explainer;
  - if stay scenarios are vague, create clearer FAQ and use-case pages;
  - if owned pages are cited shallowly, add deeper location/amenity/comparison surfaces.

- items to verify in the next run:
  - whether AzurMenton appears at all in Menton-related prompts;
  - whether the property is described correctly;
  - whether owned guides or FAQ pages appear as sources;
  - whether the answer quality changes by stay intent.

## Decision

- keep prompt pack unchanged next run: yes
- expand scope next run: no
- automation ready: no
- follow_up_owner_note: complete one real live-engine pass on the current prompt set before adding more destinations, traveler segments, or dashboard layers
