# Synapse Manifesto

## Project Constitution
This project follows the Synapse System Protocol for elite AI software engineering.

## Engineering Standards
- **Decentralized Knowledge:** All verified findings must be distilled into the Cortex.
- **Cognitive Layering:** Distinction between Global Intelligence (Cortex) and Working Memory (Neuron).
- **Project Skills:** The project maintains its own specialized agent skills in `.gemini/skills/` to ensure consistent execution across different environments.

## Initialization Sequence
1. **Identify User:** Ask for the user's preferred name (alias). It must be lowercase without special characters.
2. **Locate Neuron:** Locate or create the assigned directory: `.gemini/neurons/${alias}/${task_id}/`.
3. **Load Cortex:** Read the root `GEMINI.md` to load the current Cortex state.
4. **Plan Task:** Delegate to the `planning-with-files` skill. Ensure `task_plan.md`, `findings.md`, and `progress.md` are initialized within the specific `${task_id}` folder.
5. **Execute:** Follow the skill's workflow, while also maintaining the Synapse Mandate: distilling "how" into `knowledge.md` for later promotion to the Cortex.
