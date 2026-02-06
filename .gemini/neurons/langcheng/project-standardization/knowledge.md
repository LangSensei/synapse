# Knowledge: The Synapse System Protocol

## System Overview
Synapse is a dual-layered cognitive architecture for AI-native software engineering. It separates long-term project wisdom (Cortex) from short-term task execution (Neuron).

## Architectural Layers

### 1. Cortex (Global Intelligence)
Stored in `.gemini/cortex/`. This is the project's permanent memory.
- **manifesto.md**: The "Constitution". Rules, standards, and stack guardrails.
- **atlas.md**: The "Encyclopedia". Technical findings, decision logs, and verified patterns.

### 2. Neuron (Working Memory)
Stored in `.gemini/neurons/{user}/{task_id}/`. This is private and ephemeral.
- **Skill-Managed Workflow**: Use `planning-with-files` to manage state. All generated files (`task_plan.md`, `findings.md`, `progress.md`) **must** be scoped to the specific `task_id` directory to prevent cross-task pollution.
- **The Synapse Mandate**: Every task directory must culminate in a `knowledge.md` file, which serves as the bridge between execution and the Cortex.

### 3. Skills (Executable Knowledge)
Stored in `.gemini/skills/`.
- Specialized capabilities (e.g., `planning-with-files`) that are versioned with the repository to ensure all agents follow the same operational procedures.

## The Knowledge Promotion Cycle
1. **Execution**: Work is done in the Neuron workspace.
2. **Distillation**: Insights are synthesized into `knowledge.md`.
3. **Promotion**: Upon task completion, `knowledge.md` content is integrated into the Cortex (`atlas.md` or `manifesto.md`).

## Verification Patterns
- **User Initialization**: Always verify the user's alias (lowercase, no special characters) to create a personalized neuron space.
- **Root Gateway**: `GEMINI.md` at the project root provides high-level pointers to the Cortex and protocol state.

## Security & Privacy
- **Private Neurons**: The `.gemini/neurons/` directory should be ignored by version control to protect user-specific workspace data and secrets.
- **Public Cortex**: `.gemini/cortex/` and `GEMINI.md` are shared to maintain a unified project state.