# Chat Surface Boundary Contract

`SET` can describe a compact local boundary for projects that may expose an AI
assistant through chat or instant-messaging surfaces.

This is a planning and review contract only. It is not a bot runtime, plugin
marketplace, IM gateway, or permission to connect a repo to Telegram, Discord,
Slack, WeChat, WhatsApp, or any other external channel.

## Purpose

Use this contract when a project is evaluating whether a chat-facing surface is
appropriate at all.

The goal is to decide:

- whether chat is the right product surface;
- what the assistant may do in that surface;
- what must stay blocked or handoff-only;
- whether the project should remain site/app/manual-first instead.

## Chat surface card

Every candidate chat surface should declare:

```text
surface_id:
channel:
user_type:
primary_jobs:
allowed_message_types:
allowed_outputs:
authority:
approval_boundary:
retention_class:
```

Suggested values:

- `channel`: `internal_chat`, `owner_only_chat`, `customer_chat`,
  `support_chat`, `community_chat`, `private_test_chat`
- `authority`: `read`, `proposal`, `handoff_only`, `write`, `external_action`

Declared capability is not effective authority. A chat surface fails closed
when authority, source boundaries, or retention rules are missing.

## Good fit

Chat-first surfaces are a reasonable candidate when:

- the user intent is short, repeated, and conversational;
- fast clarification is more valuable than structured editing;
- the product already has bounded, reviewable source material;
- abstain/handoff behavior is acceptable for unsupported requests.

## Bad fit

Chat-first surfaces are a poor fit when:

- the work needs rich structured UI, tables, or multi-step editing;
- the workflow requires exact review of documents, diagrams, or financial data;
- unsupported answers would create operational, contractual, or safety risk;
- the product still lacks a clean source-of-truth layer.

## Required guardrails

Before a chat surface is allowed, define:

- source boundary;
- outbound-action boundary;
- approval and handoff rule;
- retention rule;
- failure/abstain behavior;
- user-visible scope statement.

At minimum, unsupported or high-risk requests must resolve to:

- `abstain`;
- `clarify`;
- `handoff`;
- or `proposal_only`.

## Plugin and integration boundary

If a chat surface later uses plugins, adapters, or IM integrations, each one
must separately declare:

- required secrets;
- data egress;
- install status;
- local/cloud execution;
- authority and side effects;
- reviewed / confirmed / unavailable state.

No plugin or chat connector should be adopted merely because a platform
supports it.

## Boundary

- no automatic plugin installation;
- no marketplace-driven adoption;
- no external messaging/channel connection by default;
- no treating a chat surface as equivalent to a product backend or system UI;
- no widening authority from `read` or `proposal` to outbound action without a
  separate explicit review.
