# Design Blueprint Contract

`SET` can describe a compact local `DESIGN.md` contract for repositories that
benefit from a durable design blueprint.

This is not a design runtime, not a replacement for product requirements, and
not permission to create decorative documentation everywhere by default.

## Purpose

Use it when a repository has a real visual surface and repeatedly pays a cost
 for missing design context:

- layout and interaction decisions are rediscovered each session;
- reviewers need one stable source for visual intent;
- product, marketing, or editorial work drifts because design rationale lives
  only in chat or screenshots.

## What `DESIGN.md` is for

`DESIGN.md` should capture durable design intent, not temporary critique notes.

Recommended minimum structure:

- `surface` — what this interface or page family is;
- `audience` — who it is for;
- `visual_language` — the intended tone, density, rhythm, and level of
  expressiveness;
- `layout_rules` — the important structural constraints and repeated patterns;
- `interaction_rules` — motion, feedback, and behavior expectations where they
  materially affect the experience;
- `must_keep` — elements that redesigns should preserve unless explicitly
  changed;
- `verification` — how to review the surface in practice.

It should stay compact enough to be read before a real UI pass.

## Good fit

Use this where design intent is durable and materially affects execution:

- product surfaces with recurring UI work;
- public-facing sites or landing pages with a stable visual direction;
- content-heavy surfaces where hierarchy and reading experience matter;
- map, dashboard, or browser-like interfaces with repeatable interaction rules.

## Weak fit

Do not add `DESIGN.md` just because a repo has a frontend.

Weak fit cases:

- utility or infra repos with incidental UI only;
- private orchestration or policy repos where visual output is secondary;
- early experiments where visual direction is not yet stable;
- repos where README or component comments already fully cover the durable
  design constraints.

## Workflow

The default flow is:

```text
audit current surface -> decide if durable design intent is missing -> create or refresh DESIGN.md -> use it as review context -> verify in browser/device
```

`DESIGN.md` is a design-context layer, not a ship/no-ship gate by itself.

## Boundary

- no mandatory `DESIGN.md` across all repos;
- no replacing product specs, tickets, or owner approval;
- no turning transient experiments into documentation debt;
- no using `DESIGN.md` as proof of visual quality without browser or device
  verification;
- no decorative prose when a shorter operational rule would do.
