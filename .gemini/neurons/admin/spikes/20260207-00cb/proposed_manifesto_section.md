# Proposed Improvements for Spike Activation

### II. Spike Activation (Per-Spike)
Executed whenever creating a new spike or switching between existing ones.

1. **Context Discovery:** List existing spikes using `python .gemini/scripts/spike_manager.py --list {neuron_id}`.
    - **Resume:** Provide numbered options for existing spikes. The list should display the human-readable name extracted from `spike_plan.md` alongside the directory ID.
    - **Create:** If starting a new objective, guide the user to describe it and define a concise name (e.g., `fix-auth-bug`).
2. **Initialization:** Initialize the workspace using `python .gemini/scripts/spike_manager.py --init {neuron_id} {spike_name}`.
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
    - **Verification:** Use the provided verification scripts (e.g., `powershell.exe -File .gemini/skills/planning-with-files/scripts/check-complete.ps1 -neuronId {neuron_id} -spikeId {spike_id}`) to audit progress and confirm completion.
5. **The Synapse Mandate:** Upon completion, invoke `knowledge-with-files` to distill findings into `knowledge.md` within the spike directory. Follow the Global Synchronization protocol to update the Atlas.
