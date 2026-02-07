# Synapse Manifesto

## Duty
This document is the authoritative **Source of Truth** for the Synapse System Protocol. It defines the engineering standards, operational workflows, and initialization procedures that all agents MUST follow.

## Project Constitution
This project follows the Synapse System Protocol for elite AI software engineering.

## Engineering Standards
- **Global Wisdom (Cortex):** All verified findings and architectural shifts MUST be distilled into the Cortex (`.gemini/cortex/`).
- **Execution History (Neuron):** Every spike must have a unique neuron (`.gemini/neurons/{neuron_id}/spikes/{spike_id}/`) to maintain state and history.
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
    - **Resume:** Provide numbered options for existing spikes.
    - **Create:** If starting a new objective, guide the user to describe it and define a concise spike_id.
2. **Initialization:** 
    - **Global Synchronization:** Read `GEMINI.md` and `manifesto.md` to ensure protocol alignment, and run `python .gemini/scripts/sync-atlas.py` to regenerate the local index.
    - **Create Directory:** Run `python .gemini/scripts/spike_manager.py --init {neuron_id} {spike_id}`. Capture the returned `spike_id`.
    - **Activate Skill:** Explicitly call `activate_skill(name="planning-with-files")`.
    - **Init Workspace:** Initialize planning files using:
        - Windows: `powershell.exe -File .gemini/skills/planning-with-files/scripts/init-session.ps1 -neuronId {neuron_id} -spikeId {spike_id}`
        - Unix: `bash .gemini/skills/planning-with-files/scripts/init-session.sh -neuronId {neuron_id} -spikeId {spike_id}`
    - **Location Verification:** **STRICT REQUIREMENT:** Planning files (`spike_plan.md`, `findings.md`, `progress.md`) MUST NEVER be created in the project root. The agent MUST verify their existence within the specific spike directory immediately after initialization.
3. **Execution Protocol:**
    - **Iterative Approach:** The agent leverages the `planning-with-files` skill to Plan, Execute, and Verify in a continuous loop. **Note:** Planning files (`spike_plan.md`, `findings.md`, `progress.md`) are NOT updated automatically by scripts; the agent is responsible for manually updating them after each phase or action.
        - **Plan:** Populate/Update `spike_plan.md` before taking action.
        - **Execute:** Perform implementation steps while fully leveraging the `planning-with-files` skill (e.g., maintaining `findings.md` via the 2-Action Rule and updating `progress.md`) to ensure continuous state persistence on disk.
        - **Verify:** Audit progress using verification scripts:
            - Windows: `powershell.exe -File .gemini/skills/planning-with-files/scripts/check-complete.ps1 -neuronId {neuron_id} -spikeId {spike_id}`
            - Unix: `bash .gemini/skills/planning-with-files/scripts/check-complete.sh -neuronId {neuron_id} -spikeId {spike_id}`
        - **Distill:** Invoke the `knowledge-with-files` skill to update `knowledge.md` with current findings (Status: Active).
    - **Interaction:** The agent MUST explicitly provide status updates and summaries after key phases and **ask the {neuron_id} for feedback**. To maintain professional courtesy and personalization, agents SHOULD address the user by their `{neuron_id}` during interactions.
    - **Completion Gate:**
        - The spike can ONLY be completed if the {neuron_id} confirms it.
        - **Upon Confirmation:**
            1. Perform a final verification using the `check-complete` script.
            2. Invoke `knowledge-with-files` to seal the `knowledge.md` (set **Status:** Completed).
            3. **Context Loop:** Share a final status update and summary of the completed spike, then return to **II.1 Context Discovery** to prepare for the next objective.
