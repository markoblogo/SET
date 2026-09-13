# Security policy

## Supported version

Security fixes are applied to the latest released version of SET.

## Reporting

Report suspected vulnerabilities through GitHub's private vulnerability reporting for this repository. If that option is unavailable, open an issue that contains no secret, exploit, or private repository data and ask the maintainer for a private channel.

Include the SET version, agentsgen version, affected preset or CLI command, expected boundary, and a minimal redacted reproduction.

## Product boundary

SET exports plans and invokes explicitly selected repository tooling. It does not provide an autonomous agent runner, retain credentials, apply planner output, commit changes, create pull requests, or publish generated artifacts. Treat generated workflows and plans as proposals until they are reviewed in the target repository.
