# AI Visibility Template — AzurMenton

Bundle ID: `azur-menton-visibility`

## Scope

Use this bundle to measure how public AI answers represent:

- AzurMenton as a destination/property surface;
- Menton and nearby stay/use cases;
- owned guides, FAQ pages, and location explainers;
- official or preferred owned pages as sources.

## Canonical entities

Fill before the first run:

- property/brand name:
- primary domain:
- location terms:
- stay categories:
- guide/FAQ pages:

## Expected owned source surfaces

- main property/home page;
- Menton area guides;
- FAQ pages;
- amenities or stay-detail pages;
- “how to choose / where to stay” style explainers if present.

## Prompt families

Keep prompt wording stable between runs.

### Destination prompts

- Where should I stay in Menton?
- What are good places to stay in Menton / Côte d’Azur for <use case>?
- What should I know before staying in Menton?

### Property/entity prompts

- What is AzurMenton?
- Is AzurMenton a good option for staying in Menton?
- Which sources explain AzurMenton best?

### Decision prompts

- Where to stay in Menton for quiet / family / remote work / longer stay?
- Which Menton stay options are near <landmark/use case>?
- What accommodation options are good alternatives in Menton?

### Source prompts

- Which websites or guides explain staying in Menton?
- Where can I read practical information about <property/location>?

## Observation focus

Look for:

- whether AzurMenton appears at all;
- whether it is described correctly;
- whether the location/use-case match is accurate;
- whether owned guides or FAQ pages are used as sources;
- whether AI falls back only to generic travel pages.

## Output expectation

Summarize this bundle into one weekly artifact using:

- `mention_rate`
- `correct_identity_rate`
- `owned_source_rate`
- `source_depth`
- `confusion_count`
- `opportunity_count`

## Improvement hypotheses

Common actions after a run:

- strengthen the main overview page;
- add or improve Menton guide pages;
- add FAQ for stay scenarios;
- create clearer area/amenity explanation pages;
- add comparison pages for common traveler intents;
- strengthen visible text around location, use case, and differentiators.
