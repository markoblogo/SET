# Live Web Research Boundary Contract

`SET` may describe live web research as a scoped source-intake capability. It
does not grant broad scraping, scheduled automation, public publishing, or
external actions.

This contract adapts the useful part of `MODSetter/SurfSense`: typed live data
connectors, cited briefs, and report-only alerts for agents.

Source: https://github.com/MODSetter/SurfSense

## Default stance

Live web research is disabled unless a task declares:

- target source family;
- query or URL scope;
- connector risk profile;
- expected output artifact;
- review owner.

## Allowed connector classes

- search results;
- public pages;
- public social posts and comments;
- video transcripts and comments;
- public job listings;
- public business/place profiles and reviews;
- product listings and public reviews.

## Required controls

Every live research run should record:

- `source_family`;
- `connector`;
- `query_or_url_scope`;
- `time_window`;
- `rate_or_cost_limit`;
- `tos_or_legal_risk`;
- `public_private_classification`;
- `citation_quality`;
- `brief_output`;
- `review_state`;
- `retention`;

## Lifecycle

- `REQUESTED`: source family and scope are declared.
- `COLLECTED`: connector results are stored as raw evidence refs.
- `SYNTHESIZED`: cited brief or alert is produced.
- `REVIEWED`: owner/editor accepts, revises, or rejects.
- `RETAINED`: reviewed artifact is kept with provenance.
- `DISCARDED`: weak, risky, stale, or irrelevant evidence is removed.

## Not allowed

- broad crawling without allowlisted source scope;
- scheduled agents that publish or message externally;
- treating scraped public data as verified truth;
- using social data without legal/source-policy review;
- auto-importing connector output into durable memory;
- auto-publishing briefs to MediaHub, project pages, or social channels.

## Project routing

| Target | Status | Boundary |
|---|---|---|
| `index` / MediaHub | allowed_optional | report-only source digest and review artifacts |
| `CoqPi` | allowed_optional | finder research only, no outreach |
| `CortexABV-private` | allowed_optional | private proposal evidence only |
| `MN7R` | allowed_optional | market-intelligence signals only, no trading trigger |
| public sites | review_only | visibility/review research, no direct publication |

## Acceptance rule

A live web research connector is accepted only when output remains a cited,
reviewed artifact. Any scheduled mode starts as report-only and cannot mutate
production, send messages, or publish content without a separate approved route.
