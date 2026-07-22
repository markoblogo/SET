# External AI Engineering References

Repositories such as [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) are useful implementation catalogs. `SET` treats them as references only.

## Boundary

- no dependency, vendoring, submodule, installer, or runtime adoption;
- no provider, MCP, vector DB, scheduler, or secret added from a reference alone;
- no production claim until a local contract, test, and owner approval exist;
- no bypass of proposal lifecycle, operation receipts, skill-quality validation, or data-egress review.

## Reference Fields

Use this shape when a downstream repo catalogs examples:

```text
category:
source project path:
possible local use:
required adaptation:
secrets/data-egress risk:
allowed pilot projects:
status: reference | candidate | piloted | rejected
```

Good first consumers are private/local AI repos such as CortexABV and CoqPi, where RAG, memory, voice/context, mock evaluation, and local fallback examples can be reviewed without changing production routes.
