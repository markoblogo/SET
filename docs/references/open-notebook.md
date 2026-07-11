# Open Notebook Reference

`lfnovo/open-notebook` is a reference project for a possible local research-context layer. It is not a SET dependency, an ABVX product, or a service that is installed by default.

Reference: <https://github.com/lfnovo/open-notebook>

## Useful ideas

- Keep a private, self-hosted corpus of PDFs, web pages, audio, video, and Office files.
- Add full-text/vector search and context-aware conversations over selected sources.
- Keep model choice replaceable: hosted APIs, Ollama, or LM Studio.
- Expose the research layer through REST/MCP when another tool needs grounded context.
- Treat source selection and citations as part of the research workflow, not as an implicit global memory.

## ABVX use case

The strongest future fit is a separate research pipeline:

`research corpus -> search/context -> reviewed notes or extracts -> Cardputer/reader materials`

This could support book preparation, agent-tool research, and source-backed planning without turning `SET` into a notebook or RAG runtime. Obsidian remains the authoring/staging layer; Open Notebook would be a possible ingestion, search, and analysis layer if the workflow later justifies a service.

## Do not import yet

- Do not add Open Notebook, SurrealDB, LangChain, or its Docker stack to SET or the ABVX products.
- Do not treat its "fully local" mode as automatic: hosted providers still send content to their APIs; Ollama/LM Studio are required for a local model path.
- Do not run it on Cardputer. Use it, if needed later, to prepare compact text, metadata, or other reader inputs for the device.

## Revisit trigger

Reconsider a local deployment when at least one of these becomes real:

- the book/reader workflow needs repeatable search across a growing personal corpus;
- Rabbithole or agent skills need a persistent, source-grounded research backend;
- manual Obsidian search and one-off extraction are consuming more time than maintaining a local service.

Until then, keep this as an architecture reference only.
