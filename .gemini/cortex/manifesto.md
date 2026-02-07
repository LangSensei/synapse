# Synapse Manifesto

## Duty
This document is the authoritative **Source of Truth** for the Synapse System Protocol. It defines the engineering standards, operational workflows, and initialization procedures that all agents MUST follow.

## Project Constitution
This project follows the Synapse System Protocol for elite AI software engineering.

## Engineering Standards
- **Global Wisdom (Cortex):** All verified findings and architectural shifts MUST be distilled into the Cortex (`.gemini/cortex/`).
- **Execution History (Neuron):** Every spike must have a unique neuron (`.gemini/neurons/{neuron_id}/spikes/{spike_id}/`) to maintain state and history.
- **The Options Pattern:** Agents SHOULD NOT ask open-ended questions. Instead, provide numbered selectable options (1, 2, 3...). If the neuron provides input that doesn't match an option, treat it as a custom entry.
- **Auditability:** Commit all neuron files to GitHub to enable meta-learning and performance optimization.
- **Skill Portability:** Project-level skills in `.gemini/skills/` are the authoritative sources for operational procedures.
- **Workspace Containment:** All temporary scripts, test data, and generated artifacts MUST be created within the active spike directory (`.gemini/neurons/{neuron_id}/spikes/{spike_id}/`), NOT the project root.
- **Neuron Memory:** Neuron-specific facts, preferences, and long-term context MUST be stored in `.gemini/neurons/{neuron_id}/MEMORY.md`. This file serves as the persistent memory for the neuron across all spikes.
- **Privileged Access:** Only neurons with the neuron_id `admin` are permitted to modify files outside of the neuron's directory (e.g., project root, `.gemini/cortex/`, etc.). Non-privileged neurons MUST restrict all file modifications to their specific workspace under `.gemini/neurons/{neuron_id}/`.
- **Error Handling:** 
    - **Scripts:** MUST exit with non-zero codes on failure and print semantic errors to `stderr`.
    - **Agent:** If a tool returns an error (e.g., `ENOENT`), the agent MUST verify the path/state before retrying or reporting failure.

## Initialization Sequence
1. **Neuron Auth:** List existing neuron_ids with `python .gemini/scripts/neuron_manager.py --list`. Provide these as numbered options. Instruct the user to either select a number from the list OR type a new `neuron_id`. If the input does not match a list item, treat it as a new neuron request. Initialize the neuron with `python .gemini/scripts/neuron_manager.py --init {neuron_id}`.
    - **Trust the Script:** Agents MUST rely on the output of project-level scripts (e.g., `neuron_manager.py`) for state discovery and avoid redundant manual verification of the filesystem when a script has already provided that information. Empty output or script-reported state MUST be accepted as the authoritative truth without further validation.
2. **Context Setup:** List existing spikes using `python .gemini/scripts/spike_manager.py --list {neuron_id}`.
    - **Resume:** Provide numbered options for existing spikes.
    - **Create & Initialize:** If creating a new spike, guide the neuron to describe their objective and help them define a concise name. Then, initialize the workspace at `.gemini/neurons/${neuron_id}/spikes/${spike_id}/` using `python .gemini/scripts/spike_manager.py --init {neuron_id} {spike}`.
3. **Cortex Sync:** 
    - Read `GEMINI.md` and `manifesto.md`.
    - Run `python .gemini/scripts/sync-atlas.py` to generate the local index.
4. **Structured Planning:** Invoke `planning-with-files` skill. Initialize the planning files within the spike directory (`.gemini/neurons/${neuron_id}/spikes/${spike_id}/`) using the provided helper scripts (e.g., `powershell.exe -File .gemini/skills/planning-with-files/scripts/init-session.ps1 -neuronId {neuron_id} -spikeId {spike_id}`). **STRICT REQUIREMENT:** Planning files (`spike_plan.md`, `findings.md`, `progress.md`) MUST NEVER be created in the project root. The agent MUST verify their location immediately after initialization.
5. **The Synapse Mandate:** 
    - Use `knowledge-with-files` to distill findings.
