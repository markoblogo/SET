# Design Blueprint Shortlist

Date: 2026-07-26

This shortlist records where a repo-level `DESIGN.md` is currently worth
allowing in the ABVX-style repo set.

## Allowed / high-value

These repos have recurring visual decisions and enough surface complexity to
benefit from a durable design blueprint:

- `lab.abvx`
- `index`
- `liqua`
- `menton`
- `DMVg`

Why:

- each has real page, product, or visual-system surfaces;
- design intent affects repeated implementation and review decisions;
- a compact design blueprint can reduce rediscovery and review drift.

## Allowed / selective

These repos may use `DESIGN.md`, but only for clearly bounded surfaces rather
than as a repo-wide ritual:

- `MN7R`
- `CoqPi`
- `cardputer`

Why:

- they contain interfaces or human-facing flows where some visual or
  interaction guidance is useful;
- but their core value is operational, product, or device behavior, so
  `DESIGN.md` should stay narrow and optional.

Recommended default:

- add it only for a specific app/surface family;
- keep it shorter than the product or technical docs;
- pair it with real browser or device verification.

## Not recommended

These repos should not currently standardize on `DESIGN.md`:

- `SET`
- `CortexABV-private`
- contract-heavy or governance-only repos
- private runtime-control repos without meaningful visual surface
- generated, temporary, or review-sandbox repos

Why:

- visual direction is not their main coordination problem;
- the maintenance cost is higher than the likely benefit;
- other contracts or operational docs already carry the durable value.

## Current rule

Allow `DESIGN.md` only where:

- the repo has a stable human-facing surface;
- design intent is repeatedly reused;
- the file can stay compact and truth-maintained.
