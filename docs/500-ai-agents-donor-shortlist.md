# 500 AI Agents Donor Shortlist

Date: 2026-07-30

Source index:

- [ashishpatel26/500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects)

This document is a compact donor shortlist derived from the index above.

It is not a recommendation to adopt the source repo, its frameworks, or its
runtime patterns wholesale. Use it only to identify narrow candidate patterns
for adaptation into ABVX-style local contracts, artifacts, or private pilots.

## Status labels

- `candidate donor` — a narrow pattern is worth adapting locally.
- `reference only` — useful architecture/example surface, but not a direct
  adaptation target.
- `do not use` — high risk of noise, runtime drag, or misfit with current
  project boundaries.

## Shortlist

| Source | Best target repo | Why useful | Adaptation boundary | Status |
| --- | --- | --- | --- | --- |
| [CrewAI Meeting Assistant Flow](https://github.com/crewAIInc/crewAI-examples/tree/main/flows/meeting_assistant_flow) | `CoqPi` | Good donor for pre-call prep, agenda/context intake, and post-call recap structure. | Adapt only workflow shape and operator-facing artifacts; do not adopt CrewAI runtime or background automation. | `candidate donor` |
| [CrewAI Prep for a Meeting](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/prep-for-a-meeting) | `CoqPi` | Good donor for compact preparation packets and bounded participant/context checklists. | Keep it as a local prep contract; no autonomous outreach, no hidden data pulls. | `candidate donor` |
| [AutoGen Whisper transcript/translate agent](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_video_transcript_translate_with_whisper) | `CoqPi` | Useful reference for transcript-processing and translation flow shape. | Reference transcript pipeline ideas only; do not import AutoGen orchestration or notebook-style runtime assumptions. | `reference only` |
| [TrustBoost PII Sanitizer](https://github.com/teodorofodocrispin-cmyk/TrustBoost-PII-Sanitizer) | `CoqPi` | Strong donor for fail-closed redaction and privacy-before-LLM boundaries. | Adapt only privacy/redaction policy and receipt shape; no chain/on-chain or external proof assumptions. | `candidate donor` |
| [LangGraph Adaptive RAG](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/rag/langgraph_adaptive_rag.ipynb) | `index` | Good donor for query-dependent retrieval depth and retrieval-strategy switching. | Adapt retrieval-routing logic only; no framework/runtime adoption. | `candidate donor` |
| [LangGraph Corrective RAG](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/rag/langgraph_crag.ipynb) | `index` | Useful for retrieval-quality correction before generation and report synthesis. | Keep it as a retrieval-quality pattern, not a LangGraph dependency. | `candidate donor` |
| [Agno Media Trend Analysis Agent](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/media_trend_analysis_agent.py) | `index` | Good donor for trend-synthesis artifact structure and source-cluster summarization. | Adapt report/output shape only; no Agno framework adoption. | `candidate donor` |
| [Agno Research Agent](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/research_agent.py) | `index` | Useful reference for structured research report layout and decomposition. | Reference only; do not treat generic journalism/research style as repo truth. | `reference only` |
| [LangGraph Agentic RAG](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/rag/langgraph_agentic_rag.ipynb) | `CortexABV-private` | Good donor for retrieval-route selection and multi-strategy recall gating. | Adapt only retrieval decision logic and evidence framing; no runtime/framework import. | `candidate donor` |
| [OWASP Agent Memory Guard](https://github.com/OWASP/www-project-agent-memory-guard) | `CortexABV-private` | Strong donor for memory poisoning defense, trust checks, and memory-ingress skepticism. | Adapt as memory-ingress and review policy only; no broad security theater or unscoped memory platform changes. | `candidate donor` |
| [LangGraph Multi-Agent Workflow (Supervisor)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/multi_agent/agent_supervisor.ipynb) | `CortexABV-private` | Useful architecture reference for supervisor topology and specialist-agent coordination. | Reference orchestration shape only; do not import a multi-agent runtime over existing bounded contracts. | `reference only` |
| [Agno Thinking Finance Agent](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/thinking_finance_agent.py) | `MN7R` | Useful reference for finance-analysis output structure and reasoning sections. | Adapt reporting structure only; do not import stock-market assumptions into commodity workflows. | `reference only` |
| [Agno Financial Reasoning Agent](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/reasoning_finance_agent.py) | `MN7R` | Useful reference for structured market commentary and analyst-style synthesis. | Keep as report-shape reference only; no direct market model or provider dependency. | `reference only` |
| [Microsoft OptiGuide](https://github.com/microsoft/OptiGuide) | `MN7R` | Good donor for optimization framing and scenario-comparison artifact ideas. | Adapt optimization/compare artifact patterns only; do not adopt a heavyweight optimization runtime by default. | `candidate donor` |
| [LangGraph Customer Support Agent](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/customer-support/customer-support.ipynb) | `DMVg` | Useful reference for guided interaction flow and state-machine conversation boundaries. | Reference only; do not transform DMV into a generic support-bot product layer. | `reference only` |
| [AgentEval](https://github.com/microsoft/autogen/blob/0.2/notebook/agenteval_cq_math.ipynb) | `SET` | Good donor for eval framing and artifactized agent assessment patterns. | Adapt only evaluation artifact structure and scoring discipline; no AutoGen notebook/runtime dependency. | `candidate donor` |
| [AgentOps tracking example](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_agentops.ipynb) | `SET` | Useful reference for observability dimensions across agent runs and tool use. | Reference observability dimensions only; no external telemetry service as default ABVX policy. | `reference only` |
| [AutoGen planning agents notebook](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_planning.ipynb) | `SET` | Useful reference for planner/coder separation and explicit staged work. | Reference only; existing SET orchestration contracts remain primary. | `reference only` |

## Things to reject from this index by default

- broad framework adoption because a demo exists;
- multi-agent teams for their own sake;
- cloud-first examples that require permanent new services or secret surfaces;
- stock-trading bots as direct product donors for commodity workflows;
- support/chatbot examples that widen authority beyond current repo boundaries;
- tutorial notebooks presented as if they were production-hardening guidance.

## Practical next-pass candidates

If a later pass should extract something concrete, start here:

1. `CoqPi`
   - meeting prep
   - post-call recap
   - PII/redaction donor layer

2. `index`
   - adaptive/corrective RAG donor notes
   - media trend synthesis artifacts

3. `CortexABV-private`
   - memory-ingress defense note
   - retrieval-route decision note

4. `MN7R`
   - optimization/reporting artifact note

5. `SET`
   - eval and observability reference note

## Boundary

This shortlist is a reference-selection artifact.

It does not authorize installation, framework adoption, secret setup, MCP
exposure, runtime changes, or production routing by itself.
