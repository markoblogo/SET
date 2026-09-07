# SET 0.3.0 — portable planning, pinned execution

- Plan from a validated repo-local `.set.json` with `--config`, including automatic discovery when no repository is specified. No central registry contribution required.
- Keep planning exports separate from applying target changes. Existing central-registry workflows remain available in a source checkout.
- Pin generated workflows to SET v0.3.0 and the action's agentsgen default to v0.5.0.
- Pass action input values through environment variables instead of interpolating them as shell source.
- Shorten onboarding, add a complete artifact-producing workflow, and link the standalone agentsgen path.
- Test the installed wheel outside the checkout and run a real agentsgen integration in CI.

Upgrade: `pipx upgrade abvx-set` or change your workflow to `markoblogo/SET@v0.3.0`. For immutable dependencies, use reviewed commit SHAs. An explicit `agentsgen_ref` override still takes precedence.
