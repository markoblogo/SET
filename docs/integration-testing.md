# Integration and release checks

Supported pair: SET 0.4.0 + agentsgen 0.5.0.

CI runs planner/registry tests and a real composite-action workflow on an isolated
Node fixture. That workflow generates docs, validates them, removes the configured
npm script, and requires the subsequent agentsgen check to fail.

Release gates also build and install the wheel into a fresh environment, invoke
the installed planner with a repo-local config from outside the source checkout,
and verify that exported workflows are pinned to the supported SET release.

Local check: `python -m pytest -q` and `python scripts/validate_registry.py`.
Central-registry commands require a source checkout; the installed package's
portable entrypoint is `set-plan-config-apply --config /path/to/.set.json`.
