# Design Taste Review Contract

`SET` can export the optional `design-taste-review` profile for bounded frontend review. It adapts a small set of useful taste heuristics without installing a design runtime or treating subjective style as policy.

## Route

- Marketing, editorial, portfolio, and brand-forward surfaces route to `frontend-taste-layer`.
- Product UI routes first to Lazyweb evidence and the relevant UX or critique skill.
- Existing product tasks, design systems, approved assets, accessibility requirements, and owner decisions take precedence.

## Review packet

1. State one design read: surface, audience, and visual language.
2. Calibrate three relative axes: composition variance, motion, and density. Do not assign universal defaults.
3. For redesigns, list what must be preserved before proposing changes.
4. Check repeated layout families and section rhythm.
5. Keep motion only when it communicates hierarchy, feedback, state, or narrative.
6. Verify desktop, mobile, reduced motion, and every visible string in a real browser.

## Boundary

The profile is disabled, review-and-proposal-only, and planning-only. It does not install libraries, generate assets, change copy, mutate a project, or approve deployment. Source inspection and build output are not visual verification.
