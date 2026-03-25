# LLMO Capability Map

This document maps the reusable parts of `LLMO` into the future ABVX ecosystem.

## Summary

`LLMO` contains three reusable capabilities and a much larger SaaS shell.

The reusable capabilities should move into `agentsgen`.
The SaaS shell should not move unless a separate product decision is made later.

## Reusable capabilities

### 1. Analyzer Pro

Source file:
- `pages/api/analyzer-pro.ts`

What it does:
- fetches an external URL
- checks for `llms.txt`
- extracts plain text from HTML
- computes a score from deterministic checks
- optionally asks OpenAI for a structured visibility assessment
- returns:
  - score
  - visibility
  - factors
  - recommendations

What should happen next:
- migrate into `agentsgen analyze <url>`
- output should be deterministic JSON plus optional markdown summary
- database logging and auth checks should be removed

What is reusable:
- scoring structure
- prompt shape
- recommendation logic
- URL fetching and basic text extraction

What should be dropped:
- NextAuth
- Supabase logging
- pricing / entitlement logic
- UI-specific response shape

### 2. Metadata generator

Source file:
- `pages/api/metadata.ts`

What it does:
- fetches an external URL
- extracts visible text
- prompts OpenAI for:
  - title
  - description
  - keywords
  - shortDescription
- returns structured JSON

What should happen next:
- migrate into `agentsgen meta <url>`
- output should be JSON-first and optionally written to a repo-safe artifact

What is reusable:
- prompt intent
- output schema
- URL fetching and extraction pattern

What should be dropped:
- NextAuth dependency
- payment flow assumptions
- page/UI-specific download behavior

### 3. Site llms.txt generator

Source file:
- `app/api/tasks/generate-llms/route.ts`

What it does today:
- generates a directory-wide `llms.txt` from database entries
- serves it directly or writes into `public/llms.txt`

What should happen next:
- do not port the directory/database version directly
- instead reuse the idea for `agentsgen pack --site <url>`
- target behavior should be site-oriented, not marketplace-oriented

Reusable pieces:
- output discipline
- `llms.txt` generation as a deterministic artifact

What should be dropped:
- Supabase dependency
- directory aggregation logic
- cron/serverless write assumptions

## Not worth migrating as-is

These parts are ecosystem noise for the current plan and should not move into `agentsgen` or `SET`:

- Stripe
- Supabase auth/data model
- NextAuth
- admin panel
- reminders
- subscription checks
- agency/team features
- analytics shell
- directory marketplace product logic

## Important note

There is also an older `pages/api/analyze.ts`, but it is a demo-style endpoint with random scoring.
It should not be used as the migration source of truth.

The real migration source of truth is:
- `pages/api/analyzer-pro.ts`
- `pages/api/metadata.ts`
- `app/api/tasks/generate-llms/route.ts`

## Migration order

1. `agentsgen analyze <url>`
2. `agentsgen meta <url>`
3. `agentsgen pack --site <url>`
4. archive `LLMO` when replacement commands are stable
