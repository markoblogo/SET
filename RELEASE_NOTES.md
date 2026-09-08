# SET 0.4.0 — focused web UI reviews

Add the optional `web-ui` preset for repo-docs validation plus a changed-only,
frontend-focused repository map. Explicit focus and changed-file overrides stay
reviewable in exported workflows, including clearing the preset focus.

The README now includes PR Lens architecture and data-flow diagrams generated
locally without the hosted App or a second model. Generated workflows use SET
v0.4.0; agentsgen remains pinned to v0.5.0.

## SET 0.3.1 — ID bootstrap paths

Pass the selected repository path to the ID bootstrap exporter. With a non-root target, JSON and prompt packets now land under that target's docs/ai directory.

Generated workflows use SET v0.3.1. agentsgen remains pinned to v0.5.0.
This patch supports the installed hook introduced by ID 0.5.0.
