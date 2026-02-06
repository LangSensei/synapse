# Knowledge: System Prompt Optimization

## Verified Patterns
- **Direct Instruction:** Agents perform better with imperative, structured standards in `manifesto.md`.
- **Template Noise Reduction:** Removing explanatory comments from active templates (`task_plan.md`, etc.) reduces context window bloat and allows the agent to focus on task data.
- **Gateway Clarity:** `GEMINI.md` should serve as an immediate set of instructions for a fresh agent, ensuring the protocol is followed from the first interaction.

## Architectural Shifts
- **Protocol Version 1.1:** Introduced "Auditability" and "Skill Portability" as core standards.
- **Unified Placement:** `SKILL.md` now explicitly enforces the Neuron-centric file placement, preventing root directory pollution.

## System Constraints
- **Public Neurons:** All optimization history is now committed to the repository, requiring users to be cautious about sensitive data.