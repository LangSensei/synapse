# Knowledge: Refactor Completion Loop

## Metadata
- **Date:** 2026-02-07
- **Spike ID:** 20260207-4426
- **Status:** Active
- **Authors:** langcheng
- **Tags:** manifesto, protocol, completion-loop
- **Summary:** Updated the Synapse Manifesto to include a mandatory loop back to the Context Discovery phase after spike completion, ensuring a continuous and organized workflow.

## Context & Motivation
### Problem Statement
Upon completing a spike, the agent would stop, requiring the user to manually prompt for the next discovery or listing of spikes.

### Scope
- Modification of the "Completion Gate" in `manifesto.md`.

## Decision & Outcome
### Chosen Approach
- **Initialization Restructure**: Moved Global Synchronization (Cortex/Atlas sync) to the first sub-step of the Initialization phase (II.2).
- **Completion Loop**: Maintained the "Context Loop" in the final confirmation sequence to ensure a seamless transition between tasks.
- **Redundancy Cleanup**: Removed the redundant `sync-atlas.py` call from the completion gate.

### Rationale
Moving synchronization to the beginning of the initialization ensures that all subsequent planning and execution are grounded in the most current system state. The Context Loop ensures the agent remains active and helpful after closing a task, rather than reaching a workflow dead-end.




## Technical Implementation
### Core Logic / Patterns
- **Sync-First Initialization**: `2. **Initialization:** - **Global Synchronization:** Read GEMINI.md and manifesto.md ... and run sync-atlas.py ...`
- **Manual State Maintenance**: Confirmed that `progress.md` and `spike_plan.md` must be manually updated by agents; scripts only handle initialization and auditing.



## Consequences & Constraints
### Operational Impact
Agents will now automatically list available spikes or prompt for new objectives after finishing a task.

## Verification & Audit
### Test Plan
Manual verification of the manifesto text.

### Results
Logic correctly implemented.
