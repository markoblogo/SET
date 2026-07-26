# Twelve-Factor Agent Adaptation

`SET` takes selected ideas from `humanlayer/12-factor-agents` as local doctrine only. It does not install an agent framework or redefine `SET` as an agent runtime.

## What is adopted

### 3. Own your context window

`SET` treats context as an explicit product surface:

- compact startup docs;
- bounded context packets;
- scoped memory hints;
- explicit repo-local read order;
- context-budget hints before broad retrieval.

Context is owned, not left to default thread accumulation.

### 4. Tools are just structured outputs

`SET` prefers typed packets over free-form tool chatter:

- orchestrator bundles;
- receipts;
- review findings with stable ids;
- capability and route states;
- proposal lifecycle artifacts.

The contract value is typed handoff, not a general-purpose tool loop.

### 5. Unify execution state and business state

Where practical, `SET` prefers one retained event or artifact stream rather than a second orchestration meta-model. Review state, proposal state, receipt state, and retained outputs should explain what happened without a hidden scheduler state machine.

### 6 + 8. Launch/Pause/Resume and own your control flow

`SET` treats pause/resume and approval boundaries as first-class workflow structure:

- proposal-first planning;
- explicit owner review before application;
- handoff/resume artifacts rather than in-memory waiting;
- no silent continuation past review gates.

### 9. Compact errors into context

Errors should become bounded evidence:

- explainable failure packets;
- retained verification results;
- small next-step hints instead of broad logs;
- report-first loop contracts before retry.

### 10. Small, focused agents

`SET` exports small contracts and capabilities. It does not become an omni-agent platform, scheduler, model router, or general orchestration appliance.

### 12. Stateless reducer

`SET` uses this as an architectural test for local contracts:

- can a flow be resumed from retained artifacts;
- can a review state be reconstructed from typed evidence;
- can the next step be chosen without hidden mutable runtime state.

If not, the flow is likely too implicit.

## What is not adopted

- no trigger-from-anywhere expansion as a default surface;
- no global agent framework;
- no automatic human-contact channel;
- no persistent multi-agent runtime;
- no framework-first rewrite of existing projects.

## Boundary

The usable pattern is:

- extract a small principle;
- rename it into ABVX terms;
- bind it to explicit authority and evidence rules;
- keep it disabled or opt-in by default;
- attach it to an existing product or contract.

That is the adaptation. The upstream doctrine is a source, not a dependency.
