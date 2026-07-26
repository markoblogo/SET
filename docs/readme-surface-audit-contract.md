# README Surface Audit Contract

`SET` can describe a compact local audit contract for public-facing repository
READMEs.

This contract is for README homepage quality review only. It is not permission
to rewrite a repository narrative, generate decorative assets by default, or
publish branding claims without evidence.

## Purpose

Use it when a repository README functions as a real public entry surface and
needs review for:

- clarity;
- hierarchy;
- trust;
- maintenance cost.

The first step is audit, not redesign.

## Audit-first flow

The default sequence is:

```text
read-only audit -> shortlist issues -> choose rewrite scope -> preview -> explicit approval -> apply
```

Reading the README for context does not grant permission to rewrite it.

## Audit lenses

Review the README through four lenses:

- `clarity` — is the project identity, audience, and purpose obvious in the
  first screen;
- `hierarchy` — are sections ordered so a new visitor can understand what the
  project is, what it does, and how to use it;
- `trust` — are claims backed by real proof, demos, docs, tests, releases, or
  visible artifacts;
- `maintenance_cost` — would the README become fragile, decorative, or hard to
  keep true after normal development changes.

## Allowed modes

- `audit-only` — no file edits, findings only;
- `whole-readme` — review or redesign the full README after explicit approval;
- `asset-only` — produce standalone README assets only after explicit approval.

The recommended default is `audit-only`.

## Proof rule

README surfaces must not:

- invent capabilities;
- imply production readiness without evidence;
- imply live status from unverified local/demo state;
- depend on decorative assets to carry the meaning of the project.

Any claim that changes trust meaning should point to one of:

- docs;
- runnable verification;
- public demo;
- release artifact;
- repository evidence.

## Asset boundary

Animated heroes, SVG titles, GIFs, and similar assets are optional and should
be used only when:

- the repo is genuinely public-facing;
- the project already has stable visual language;
- the asset does not replace proof;
- embedding the asset was explicitly approved.

## Good fit

Use this on repos that act as:

- public project homepages;
- public product or framework entry surfaces;
- public catalog or distribution surfaces.

## Bad fit

Do not prioritize this on repos that are:

- private or internal;
- docs/manual-heavy operational repos;
- mostly contracts/config with low public-discovery value;
- volatile engineering sandboxes where README churn would outpace truth.

## Boundary

- no automatic README rewrite;
- no automatic asset embedding;
- no turning internal repos into marketing surfaces by default;
- no replacing product/docs review with visual polish;
- no proof-free beautification.
