# Email Intake Boundary Contract

`SET` may describe email access as a local, opt-in intake capability. It does
not grant mailbox authority, outbound messaging authority, or background
monitoring authority.

This contract is a compact adaptation of the useful part of
`nikolausm/imap-mcp-server`: scoped IMAP search/read tools with explicit
read-only and allowlist modes.

Source: https://github.com/nikolausm/imap-mcp-server

## Default stance

Email intake is disabled unless a project or local operator session explicitly
enables it.

The default approved mode is:

```json
{
  "IMAP_MCP_READ_ONLY": "true"
}
```

For higher-risk sessions, prefer an explicit allowlist:

```json
{
  "IMAP_MCP_ENABLED_TOOLS": "imap_search_emails,imap_get_email,imap_get_latest_emails,imap_find_thread_messages,imap_list_folders,imap_get_unread_count"
}
```

## Allowed use

- search for owner-approved messages or threads;
- read selected messages for preparation, research, or source review;
- list folders and unread counts when needed for intake triage;
- extract compact facts with provenance;
- write only into private, reviewed storage or local session artifacts.

## Not allowed

- send, reply, forward, move, delete, flag, or edit account settings;
- monitor whole mailboxes by default;
- ingest attachments or raw messages into durable memory without review;
- use mailbox content for public outputs without redaction and source approval;
- treat email access as permission to contact people.

## Required receipt

Every email-intake run should record:

- `account_scope`;
- `folder_scope`;
- `query_or_thread`;
- `tools_enabled`;
- `read_only_confirmed`;
- `messages_reviewed`;
- `data_retained`;
- `redaction_applied`;
- `next_action_requires_owner_approval`.

## Project routing

| Project | Status | Boundary |
|---|---|---|
| `CoqPi` | allowed_optional | prep/research only, no outbound email |
| `CortexABV-private` | allowed_optional | private proposal/research intake only |
| `index` / MediaHub | allowed_optional | newsletter/source digest only after explicit scope |
| public sites | review_only | source material only, no automated CRM behavior |
| finance, contracts, payments | blocked | no email-driven external action |

## Acceptance rule

An email-intake setup is accepted only when the effective MCP tool list is
read-only or explicitly allowlisted, credentials remain local, and the run has a
human-readable receipt. Any outbound action requires a separate owner-approved
workflow outside this contract.
