# AI Visibility Audit Contract

`SET` can carry a compact local contract for repeated AI-visibility audits across public surfaces such as personal sites, project pages, books, and hospitality/property guides.

This is an audit loop, not a GEO runtime, crawler, SEO platform, or automatic content optimizer.

## Purpose

Use it to answer recurring questions such as:

- which projects, books, or properties appear inside AI answers;
- whether identity, positioning, and source attribution are correct;
- which owned pages become source surfaces;
- what public page or FAQ gap is blocking visibility.

## Operating loop

Default cadence is weekly or biweekly.

Each run should keep the same:

- target bundle;
- prompt pack;
- engine set;
- scoring method;
- artifact format.

This preserves comparability across runs.

## Target bundles

Start with two bounded bundles:

- `personal-site-visibility`
- `azur-menton-visibility`

Each bundle defines:

- canonical entities to look for;
- owned domains/pages expected to help;
- prompt families;
- optional comparison entities;
- exclusions and scope notes.

## Observation packet

Each prompt/engine observation should retain:

```text
run_date:
bundle_id:
engine:
prompt_id:
query:
mentioned_entities:
correct_identity: yes | partial | no
owned_source_used:
source_urls:
confusion_note:
improvement_hypothesis:
reviewer_note:
```

## Weekly artifact

Each run should produce one dated weekly artifact summarizing:

- prompts tested;
- engines tested;
- mention rate;
- correct-identity rate;
- owned-source citation rate;
- recurring confusion patterns;
- page-level opportunities;
- delta vs previous run;
- next actions.

Use the template in `docs/ai-visibility-weekly-artifact-template.md`.

## Scorecard

Keep the scorecard compact and stable:

- `mention_rate`: how often the entity appeared at all;
- `correct_identity_rate`: how often the entity was named and described correctly;
- `owned_source_rate`: how often an owned page/domain appeared as a source;
- `source_depth`: whether the answer relied on homepage only, deep page, FAQ, guide, or book page;
- `confusion_count`: wrong identity, wrong project, wrong book, wrong location, or mixed claims;
- `opportunity_count`: plausible site/document improvements created by the run.

## Practical use

This contract is meant to drive regular analytics, not a one-off experiment.

Typical use:

1. run the same bundle on a fixed cadence;
2. write one weekly artifact;
3. compare with the prior artifact;
4. decide whether a public surface needs:
   - a new overview page;
   - a clearer FAQ;
   - a dedicated book/project page;
   - a better author/about page;
   - a stronger Menton/location guide;
   - a structured comparison page.

## Boundary

- no automatic crawling, scraping, or indexing;
- no automatic site edits;
- no automatic provider spend or external tool signup;
- no production claim from one run alone;
- no treating generated answers as authoritative facts about the project;
- no automatic score inflation from changing prompts between runs;
- no private/project-internal facts in public visibility prompts unless explicitly intended.

## Recommended rollout roadmap

### Milestone 0 — baseline setup

Target date: August 2, 2026

- finalize the two target bundles;
- freeze the first canonical prompt packs;
- run the first baseline audit for both bundles;
- save the first two weekly artifacts.

### Milestone 1 — repeatable manual loop

Target date: August 16, 2026

- complete at least two runs per bundle with unchanged prompt packs;
- start comparing deltas, not absolute impressions;
- identify the first 3-5 recurring source/page gaps.

### Milestone 2 — action linkage

Target date: September 6, 2026

- link visibility findings to concrete public-surface work items;
- separate content fixes, structure fixes, and identity/positioning fixes;
- track whether a site change improves a later audit.

### Milestone 3 — semi-automation decision

Target date: October 4, 2026

- decide whether the loop is stable enough for scheduled execution;
- if yes, automate only artifact assembly and delta comparison first;
- keep prompt review and final interpretation human-reviewed.

## Next moves

The next development steps should be:

1. create the two bundle templates and keep them stable;
2. run one baseline for each bundle;
3. run a second pass on the same bundles without changing prompts;
4. only then decide whether to add a scheduler, storage schema, or dashboard;
5. expand to more projects only after the first two bundles produce actionable deltas.

This contract is adapted from the useful `open-geo` idea, but reduced to a local, repeatable, artifact-first audit loop suitable for `SET`.
