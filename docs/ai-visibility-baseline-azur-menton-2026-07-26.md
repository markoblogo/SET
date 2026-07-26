# AI Visibility Weekly Artifact

Artifact ID: `ai-visibility-weekly`

## Run metadata

- run_date: 2026-07-26
- bundle_id: `azur-menton-visibility`
- reviewer: Codex
- engines_tested: public web search proxy
- prompt_pack_version: `v0-baseline`
- prior_artifact: none
- run_status: `completed_public_web_proxy`
- run_mode: public web search observations, not authenticated in-product AI-engine answers

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

- prompts_run: 6 proxy prompt families checked
- prompts_skipped_with_reason:
  - full engine-specific AI-answer capture remains pending a direct per-engine run
- entities_in_scope:
  - AzurMenton
  - Menton stay surface
  - related guide/FAQ pages
- owned_domains_in_scope:
  - `azurmenton.com`

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

- mention_rate: medium-low (`2/6` generic prompt families surface the owned property directly; direct brand prompts succeed)
- correct_identity_rate: high on direct brand query, low on generic stay-intent discovery
- owned_source_rate: low on generic discovery prompts, high on exact brand query
- source_depth: good when owned surfaces are reached (homepage plus guide/FAQ/event layers exist), but discovery remains shallow
- confusion_count: 1 recurring pattern and 1 adjacent noise pattern
- opportunity_count: 5 likely public-surface improvements

## Key observations

- strongest visibility win: `azurmenton.com/en` is clear and well-positioned when searched directly, with strong guide and FAQ structure visible from the homepage
- weakest visibility gap: generic “where to stay in Menton” style discovery is dominated by travel guides, hotel lists, and booking pages rather than the owned property surface
- recurring confusion pattern: the main issue is invisibility on generic travel-intent prompts rather than incorrect brand description
- unexpected cited source: travel-guide and hotel-list pages dominate broad Menton accommodation intent
- missing owned source page: stronger comparison / “where to stay in Menton” and scenario-specific pages are likely needed for broader discovery

## Delta vs previous run

- improved: baseline run
- unchanged: baseline run
- worsened: baseline run
- new confusion: baseline run
- removed confusion: baseline run

## Prompt-level notes

- `A01`
  - engines: public web search proxy
  - outcome: strong visibility
  - owned_source_used: yes
  - note: direct brand query returns the official Azur Menton page with a clear beachfront-apartment description

- `A02`
  - engines: public web search proxy
  - outcome: partial visibility
  - owned_source_used: partial
  - note: official site positioning supports suitability, but broad suitability discovery is not yet dominant in search

- `A03`
  - engines: public web search proxy
  - outcome: weak visibility
  - owned_source_used: no
  - note: generic Menton stay prompts are dominated by travel guides, forums, and hotel-list pages

- `A05`
  - engines: public web search proxy
  - outcome: weak visibility
  - owned_source_used: no
  - note: use-case-specific ranking for quiet/family/remote-work stays is not yet owned by Azur Menton pages

- `A07`
  - engines: public web search proxy
  - outcome: strong visibility
  - owned_source_used: yes
  - note: when the brand is queried directly, the official page exposes apartments, guide, events, and FAQ in one source surface

## Recommended actions

- immediate page/content fixes:
  - keep the exact current prompt pack unchanged for the second run so comparisons stay valid;
  - define the exact guide and FAQ pages expected to rank for generic Menton stay questions;
  - prioritize one owned “where to stay in Menton” / scenario-comparison surface.

- later structural fixes:
  - strengthen owned Menton guide pages for generic discovery, not only branded discovery;
  - create clearer stay-scenario pages for family, quiet, sea-view, central, and longer-stay intents;
  - add comparison pages that frame Azur Menton against common Menton stay choices;
  - keep guide, event, and FAQ pages strongly interlinked from the main property surface.

- items to verify in the next run:
  - whether AzurMenton appears at all in AI-engine Menton stay prompts, not only web search;
  - whether owned guides or FAQ pages appear as sources;
  - whether the answer quality changes by stay intent;
  - whether stronger comparison pages improve generic discoverability.

## Decision

- keep prompt pack unchanged next run: yes
- expand scope next run: no
- automation ready: partial
- follow_up_owner_note: treat this as the current public-web baseline; the next pass should run the same prompts inside selected AI engines before changing structure or adding more travel-intent variants
