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
- **Error Handling:** 
    - **Scripts:** MUST exit with non-zero codes on failure and print semantic errors to `stderr`.
    - **Agent:** If a tool returns an error (e.g., `ENOENT`), the agent MUST verify the path/state before retrying or reporting failure.

## Protocol Execution

### I. Session Boot (One-Time)
1. **Neuron Auth:** List existing neuron_ids with `python .gemini/scripts/neuron_manager.py --list`. Provide these as numbered options. Instruct the user to either select a number from the list OR type a new `neuron_id`. If the input does not match a list item, treat it as a new neuron request. Initialize the neuron with `python .gemini/scripts/neuron_manager.py --init {neuron_id}`.
    - **Trust the Script:** Agents MUST rely on the output of project-level scripts (e.g., `neuron_manager.py`) for state discovery and avoid redundant manual verification of the filesystem when a script has already provided that information. Empty output or script-reported state MUST be accepted as the authoritative truth without further validation.

### II. Spike Activation (Per-Spike)
Executed whenever creating a new spike or switching between existing ones.
1. **Context Setup:** List existing spikes using `python .gemini/scripts/spike_manager.py --list {neuron_id}`.
    - **Resume:** Provide numbered options for existing spikes.
    - **Create & Initialize:** If creating a new spike, guide the neuron to describe their objective and help them define a concise name. Then, initialize the workspace at `.gemini/neurons/${neuron_id}/spikes/${spike_id}/` using `python .gemini/scripts/spike_manager.py --init {neuron_id} {spike}`.
2. **Structured Planning:** Invoke the `planning-with-files` skill to establish a persistent "disk-based memory."
    - **Initialization:** Agents MUST initialize the workspace using the provided helper scripts (e.g., `powershell.exe -File .gemini/skills/planning-with-files/scripts/init-session.ps1 -neuronId {neuron_id} -spikeId {spike_id}`).
    - **Location Verification:** **STRICT REQUIREMENT:** Planning files (`spike_plan.md`, `findings.md`, `progress.md`) MUST NEVER be created in the project root. The agent MUST verify their existence within the specific spike directory immediately after initialization.
    - **State Maintenance:** Agents are responsible for manually updating `spike_plan.md` (e.g., changing status to `complete`) after each phase. 
    - **Verification:** Use the provided verification scripts (e.g., `powershell.exe -File .gemini/skills/planning-with-files/scripts/check-complete.ps1 -neuronId {neuron_id} -spikeId {spike_id}`) to audit the progress of the spike and confirm when all phases are finished.
3. **The Synapse Mandate:** Use `knowledge-with-files` to distill findings into the spike directory.

### III. Global Synchronization (Continuous)
Executed whenever knowledge is distilled or system documents change.
1. **Cortex Sync:** 
    - Read `GEMINI.md` and `manifesto.md` to ensure protocol alignment.
    - Run `python .gemini/scripts/sync-atlas.py` to regenerate the local index whenever a `knowledge.md` file is created or modified in any spike.
