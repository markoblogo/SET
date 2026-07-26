# AI Visibility Weekly Artifact

Artifact ID: `ai-visibility-weekly`

## Run metadata

- run_date: 2026-07-26
- bundle_id: `personal-site-visibility`
- reviewer: Codex
- engines_tested: public web search proxy
- prompt_pack_version: `v0-baseline`
- prior_artifact: none
- run_status: `completed_public_web_proxy`
- run_mode: public web search observations, not authenticated in-product AI-engine answers

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

- prompts_run: 5 proxy prompt families checked
- prompts_skipped_with_reason:
  - full engine-specific AI-answer capture remains pending a direct per-engine run
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

- mention_rate: medium-high (`4/5` proxy prompt families returned a relevant entity or official/public owner surface)
- correct_identity_rate: medium (`3/5`; strong for owner identity and `1d3x`, weak for `ABVX`, partial for books)
- owned_source_rate: medium (`3/5`; official/public owned surfaces observed for owner identity and `1d3x`, weak for `ABVX`)
- source_depth: shallow-to-mixed (profile pages and homepage-level surfaces dominate; deeper book-source visibility is weak)
- confusion_count: 2 major patterns
- opportunity_count: 4 likely public-surface improvements

## Key observations

- strongest visibility win: `1d3x.com` is directly discoverable with a clear infrastructure description and linked ecosystem surfaces
- weakest visibility gap: `ABVX` is heavily confused with the public stock ticker for Abivax rather than the owner's ecosystem
- recurring confusion pattern: owner identity is visible through LinkedIn/Notion/Behance, but `ABVX` as a bare token loses to unrelated finance/biotech results
- unexpected cited source: the Notion profile appears as a strong owner-identity surface alongside LinkedIn
- missing owned source page: a stronger canonical owner/about page and stronger direct public book landing pages are still needed for cleaner attribution

## Delta vs previous run

- improved: baseline run
- unchanged: baseline run
- worsened: baseline run
- new confusion: baseline run
- removed confusion: baseline run

## Prompt-level notes

- `P01`
  - engines: public web search proxy
  - outcome: strong visibility
  - owned_source_used: yes, partial
  - note: owner identity is discoverable through LinkedIn, Notion, and Behance; official owned-site dominance is not yet established

- `P02`
  - engines: public web search proxy
  - outcome: partial visibility
  - owned_source_used: partial
  - note: project linkage exists, but project discovery is fragmented across profile surfaces rather than one canonical owner/project hub

- `P03`
  - engines: public web search proxy
  - outcome: partial visibility
  - owned_source_used: weak
  - note: at least one book by Anton Biletskiy-Volokh is discoverable, but book-surface authority is not concentrated on a strong owned destination

- `P04`
  - engines: public web search proxy
  - outcome: weak visibility
  - owned_source_used: no
  - note: `ABVX` is dominated by Abivax ticker/finance results; this is the clearest current identity collision

- `P05`
  - engines: public web search proxy
  - outcome: strong visibility
  - owned_source_used: yes
  - note: `1d3x.com` ranks with a clear description; source depth improves further through SPIKE and Context pages

## Recommended actions

- immediate page/content fixes:
  - define one canonical owner page that clearly links owner identity, products, books, and official domains;
  - strengthen public book landing surfaces so search results can attribute books back to the owner more directly;
  - keep this prompt pack unchanged for the second run so the delta is meaningful.

- later structural fixes:
  - add or strengthen a dedicated owner/about page on an owned domain rather than relying on profile platforms alone;
  - create stronger project overview and comparison pages for named products;
  - create stronger dedicated book pages and cross-links between books, author, and ecosystem pages.

- items to verify in the next run:
  - whether owned pages are used as cited or implied sources in AI-engine answers, not just web search;
  - whether project-to-owner and book-to-owner linkage is correct;
  - whether `ABVX` can be disambiguated with stronger surrounding public text and canonical pages.

## Decision

- keep prompt pack unchanged next run: yes
- expand scope next run: no
- automation ready: partial
- follow_up_owner_note: use this artifact as the current web baseline, then run the same prompt pack inside selected AI engines before changing pages or dashboard scope
