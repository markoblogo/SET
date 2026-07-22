# Terminal Agent Multiplexer Reference

This is a read-only reference for tools such as [herdr](https://github.com/ogulcancelik/herdr), a terminal-native agent multiplexer.

`SET` should not vendor or require a terminal multiplexer. The useful part is the runner capability shape a downstream operator may expose while consuming `orchestrator-bundle.json`.

## Useful Capabilities

- visible agent/session state: `blocked`, `working`, `done`, plus explicit waiting-for-human states;
- durable terminal panes that can detach and reattach without losing process state;
- real terminal output as evidence, not a rewritten dashboard interpretation;
- isolated panes per agent/task, with clear ownership of workspace and files;
- optional socket/API surface for runners that need to wait on panes or read bounded output.

## SET Boundary

- SET exports planning contracts; it does not create panes, spawn agents, or manage sessions.
- A multiplexer may display SET-derived route state, but it must not treat display state as approval.
- File ownership, root verification, operation receipts, and validation gates remain in the repo contract, not in the terminal UI.
- AGPL/commercial license review is required before organizational adoption of herdr itself.

## Fit

- Good fit: local multi-agent review sessions, SET bundle inspection, detached long-running verification, blocked-state visibility.
- Poor fit: production scheduling, provider routing, protected-data storage, automatic approval, public deployment.
