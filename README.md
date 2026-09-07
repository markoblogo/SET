# SET

Run agentsgen in GitHub Actions, or preview a workflow for your repository before applying it.

[![CI](https://github.com/markoblogo/SET/actions/workflows/ci.yml/badge.svg)](https://github.com/markoblogo/SET/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/markoblogo/SET)](https://github.com/markoblogo/SET/releases)

SET is an optional orchestration layer for [agentsgen](https://github.com/markoblogo/AGENTS.md_generator).
Use agentsgen directly if you only need to generate or check AGENTS.md.
SET adds workflow presets and reviewable planning exports. No AI runtime or API key
is needed for the basic repo-docs workflow.

## Quick start

Add `.github/workflows/set.yml` to your repository:

```yaml
name: Generate agent docs
on: workflow_dispatch
permissions:
  contents: read
jobs:
  docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
      - uses: markoblogo/SET@v0.3.1
        with:
          workflow_preset: repo-docs
          path: "."
      - uses: actions/upload-artifact@v4
        with:
          name: proposed-agent-docs
          include-hidden-files: true
          path: |
            AGENTS*.md
            RUNBOOK*.md
            .agentsgen.json
            agents.entrypoints.json
            llms.txt
            docs/ai/
```

The `repo-docs` preset runs init, pack, and check using **agentsgen v0.5.0**.
Download and review the artifact before committing it. SET does not commit or push.
Existing handwritten files without markers produce generated siblings; a failing
check means adoption needs review. For an existing config, set `init: "false"`
when you only want pack generation and validation.

For immutable dependencies, pin SET and `agentsgen_ref` to reviewed release SHAs.
Use the [agentsgen PR guard](https://github.com/markoblogo/AGENTS.md_generator#add-a-pull-request-guard)
for read-only validation of committed instructions on every PR.

## Plan locally, without a central registry

Requires Python 3.10+ and pipx:

```sh
pipx install abvx-set==0.3.1
```

Create `.set.json` in your repository:

```json
{
  "version": 1,
  "repo": "your-account/your-repo",
  "tools": {
    "agentsgen": {"init": true, "pack": true, "check": true}
  },
  "presets": ["repo-docs"]
}
```

```sh
set-plan-config-apply --config .set.json --repo-root . --format json --export-dir .set-plan
```

Inspect `.set-plan/workflow.set.yml` and `.set-plan/pr-body.md`. The planner exports
proposals only; it does not change `.github/workflows/` or apply a plan.
With no repo arguments, a local `.set.json` is discovered automatically.
Explicit repo names and `--all` still support the central registry in a source checkout.

## Choose a preset

| Preset | Behavior |
| --- | --- |
| minimal | Bootstrap docs |
| repo-docs | Init, context pack, validation |
| site-ai | Repo docs plus site analysis; consult advanced requirements |

Optional ID hooks, proof artifacts, and capability profiles are described in the
[advanced guide](docs/advanced-guide.md). Profile exports describe contracts;
they do not install runtimes or grant execution permissions.

## Compatibility and ownership

| Project | Responsibility |
| --- | --- |
| [agentsgen 0.5.0](https://github.com/markoblogo/AGENTS.md_generator) | Detect, generate, preserve handwritten text, validate command references |
| SET 0.3.1 | Choose steps, export plans, invoke the pinned agentsgen version |
| [abvx-agent-skills](https://github.com/markoblogo/abvx-agent-skills) | Optional reusable agent workflows |

See [integration checks](docs/integration-testing.md), [configuration schema](schema/repo-config.v1.json),
and [contributing](CONTRIBUTING.md). Report reproducible failures with both versions
and a redacted minimal `.set.json`.
