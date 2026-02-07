# Synapse Manifesto

## Duty
This document is the authoritative **Source of Truth** for the Synapse System Protocol. It defines the engineering standards, operational workflows, and initialization procedures that all agents MUST follow.

## Project Constitution
This project follows the Synapse System Protocol for elite AI software engineering.

## Engineering Standards
- **Global Wisdom (Cortex):** All verified findings and architectural shifts MUST be distilled into the Cortex (`.gemini/cortex/`).
- **Execution History (Neuron):** Every spike must have a unique neuron (`.gemini/neurons/{neuron_id}/spikes/{spike_id}/`) to maintain state and history.
- **The Options Pattern:** Agents MUST NOT ask open-ended questions. Every decision point, request for feedback, or checkpoint MUST be presented as numbered selectable options (1, 2, 3...). While multiple lists may be used in a single response for structural clarity, the numbering MUST remain continuous and sequential across the entire response (e.g., 1, 2 followed by 3, 4). If the neuron provides input that doesn't match an option, it should be treated as a custom entry.
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

1. **Context Discovery:** List existing spikes using `python .gemini/scripts/spike_manager.py --list {neuron_id}`.
    - **Resume:** Provide numbered options for existing spikes. The list should display the human-readable name extracted from `spike_plan.md` alongside the directory ID.
    - **Create:** If starting a new objective, guide the user to describe it and define a concise spike_id (e.g., `fix-auth-bug`).
2. **Initialization:** Initialize the workspace using `python .gemini/scripts/spike_manager.py --init {neuron_id} {spike_id}`.
    - **Capture ID:** Record the unique `spike_id` (e.g., `20260207-a9b1`) returned by the script. This ID is required for all subsequent planning and verification steps.
3. **Structured Planning:**
    - **Activate Skill:** Explicitly call `activate_skill(name="planning-with-files")`.
    - **Init Workspace:** Initialize the planning files using the provided helper scripts:
        - Windows: `powershell.exe -File .gemini/skills/planning-with-files/scripts/init-session.ps1 -neuronId {neuron_id} -spikeId {spike_id}`
        - Unix: `bash .gemini/skills/planning-with-files/scripts/init-session.sh -neuronId {neuron_id} -spikeId {spike_id}`
    - **Location Verification:** **STRICT REQUIREMENT:** Planning files (`spike_plan.md`, `findings.md`, `progress.md`) MUST NEVER be created in the project root. The agent MUST verify their existence within the specific spike directory immediately after initialization.
4. **Execution Protocol:**
    - **Plan First:** Populate `spike_plan.md` with a structured roadmap before performing any implementation steps.
    - **State Maintenance:** Agents are responsible for manually updating `spike_plan.md` (e.g., changing status to `complete`) after each phase.
    - **Verification:** Use the provided verification scripts (e.g., `powershell.exe -File .gemini/skills/planning-with-files/scripts/check-complete.ps1 -neuronId {neuron_id} -spikeId {spike_id}`) to audit progress. **Mandatory Checkpoint:** Agents MUST explicitly ask the neuron for final confirmation before completing the spike. This ensures the neuron has the opportunity to append related tasks or provide final feedback before the session concludes.
5. **The Synapse Mandate:** Upon completion, invoke `knowledge-with-files` to distill findings into `knowledge.md` within the spike directory. Follow the Global Synchronization protocol to update the Atlas.

### III. Global Synchronization (Continuous)
Executed whenever knowledge is distilled or system documents change.
1. **Cortex Sync:** 
    - Read `GEMINI.md` and `manifesto.md` to ensure protocol alignment.
    - Run `python .gemini/scripts/sync-atlas.py` to regenerate the local index whenever a `knowledge.md` file is created or modified in any spike.
