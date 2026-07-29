# Search-Discoverable Code Contract

`SET` can export a compact code-writing contract for projects where agents and
humans navigate primarily through plain-text search rather than IDE-only
 affordances.

This is a review and authoring contract, not a mandatory style regime and not a
replacement for repo-local conventions.

## Purpose

Use this contract when a project wants code that is easier to find, read, and
change through:

- `rg` or grep-style search;
- short diff review windows;
- agent-first repository navigation;
- lower token waste during code reading.

## Core rules

### Names are search queries

- Prefer exported/public names that are specific enough to grep uniquely in the
  real repo.
- Generic verbs should carry their object: `validateSmtpConfig`, not
  `validateConfig`.
- Prefer one concept, one spelling across the repo; avoid near-synonyms such as
  `orgId` vs `organizationId` unless the repo already chose one form.

### Filenames should be discoverable

- Avoid bare-role filenames such as `utils.ts`, `helpers.ts`, `types.ts`, or
  `config.ts` when the file holds a specific domain concept.
- Prefer concept-named modules that answer one likely search question.

### Thin orchestrators, named concept homes

- Keep orchestration files thin and let the real implementation live in a
  concept-named module.
- A reader landing on an orchestrator should be one hop away from the actual
  logic, not trapped in a wall of mixed responsibilities.

### Searchable comments and literals

- Important exported code paths should have a short doc comment when the
  signature does not reveal the critical constraint.
- Write the plain-language phrase a reader would actually search for.
- Error messages, event names, and codes should stay grep-able as full literals
  when practical.

### Behavior and name drift

- If behavior changes materially, check whether the name is now misleading.
- If code moves, the old implementation site should disappear in the same
  change unless an explicit compatibility shim is required.

## What this is good for

- medium and large repos where agents search before reading deeply;
- shared code with multiple modules and repeated domain vocabulary;
- repos where token economy and fast code localization matter.

## What this is not for

- tiny single-file prototypes where extra naming ceremony adds more cost than
  value;
- purely editorial/content repositories;
- forcing repo-wide renames without clear payoff and verification.

## Review checklist

Before accepting a change, ask:

1. would one search for the new exported name likely find the implementation;
2. did the patch introduce avoidable naming collisions or weak generic names;
3. do filenames and module boundaries reflect the concept a maintainer would
   search for;
4. are key error/event strings still easy to trace back to source;
5. did behavior drift without the name being reconsidered.

## Boundary

- this contract is guidance, not a blanket rename mandate;
- repo-local conventions may override individual naming preferences;
- readability, compatibility, and diff safety still outrank cosmetic naming
  purity.
