# AI Visibility Template — Personal Site And Projects

Bundle ID: `personal-site-visibility`

## Scope

Use this bundle to measure how public AI answers represent:

- the owner identity;
- named projects;
- books;
- public product surfaces;
- official domains/pages.

## Canonical entities

Fill before the first run:

- owner name:
- primary personal domain:
- project domains:
- book titles:
- public profiles:

## Expected owned source surfaces

- homepage / about page;
- project overview pages;
- dedicated book pages;
- author/profile page;
- FAQ or explainer pages where applicable.

## Prompt families

Keep prompt wording stable between runs.

### Identity and author prompts

- Who is <owner name>?
- What projects is <owner name> known for?
- What books or publications are associated with <owner name>?

### Project discovery prompts

- What is <project name>?
- Which projects are related to <domain>?
- What does <project/domain> do?

### Comparative prompts

- Which projects cover <problem area>?
- What are notable independent projects in <category>?
- Which sites or creators publish about <topic>?

### Source prompts

- Where can I read about <project/book>?
- What is the official site for <project/book>?
- Which sources explain <project/category> best?

## Observation focus

Look for:

- mention vs no mention;
- correct identity;
- correct project-to-owner linkage;
- correct book-to-owner linkage;
- owned domain/page used as source;
- recurring confusion with similarly named entities.

## Output expectation

Summarize this bundle into one weekly artifact using:

- `mention_rate`
- `correct_identity_rate`
- `owned_source_rate`
- `confusion_count`
- `opportunity_count`

## Improvement hypotheses

Common actions after a run:

- create or strengthen an author page;
- create missing dedicated project pages;
- create dedicated book pages with clearer metadata;
- improve project overview language;
- add FAQ or “what this is / who it is for” pages;
- add comparison or category-positioning pages.
