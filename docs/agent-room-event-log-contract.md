# Agent Room Event Log Contract

`SET` may describe a room-like event log as the unit of record for agent work.
It does not require Buzz, Nostr, a relay, chat hosting, or a new collaboration
runtime.

This contract adapts the useful part of `block/buzz`: humans, agents, workflow
steps, reviews, git events, and approvals can share one auditable event stream.

Source: https://github.com/block/buzz

## Goal

Keep the record of work in one place:

- what was requested;
- who or what acted;
- what evidence was produced;
- what changed;
- what review happened;
- what approval or rejection closed the loop.

## Event actors

Every event should identify its actor:

- `owner`;
- `human_reviewer`;
- `agent`;
- `tool`;
- `workflow`;
- `external_system`.

For agents and tools, record declared authority and actual route used.

## Event types

Minimum useful event types:

- `request`;
- `context`;
- `plan`;
- `patch`;
- `test_result`;
- `review`;
- `approval`;
- `rejection`;
- `merge_or_ship_decision`;
- `follow_up`.

## Required fields

Every room event should include:

- `event_id`;
- `room_id`;
- `project_id`;
- `actor_id`;
- `actor_type`;
- `authority`;
- `timestamp`;
- `event_type`;
- `summary`;
- `evidence_refs`;
- `related_commit_or_pr`;
- `approval_state`.

## Boundaries

Do not use this contract to enable:

- always-on shared agent chat;
- autonomous external action;
- hidden workflow state outside receipts;
- cross-project memory leakage;
- unsigned or unattributed critical events;
- branch merge or public ship without owner-approved evidence.

## Acceptance rule

A room-like event log is accepted only when it remains scoped to one unit of
work, keeps actor identity explicit, preserves review evidence, and does not
replace existing `SET` route, approval, or verification contracts.
