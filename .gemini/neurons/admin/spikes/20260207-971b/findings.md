# Findings & Decisions: Standardize Terminology to Spike ID

## Requirements
- Replace `{spike_name}` with `{spike_id}` in `manifesto.md`.
- Ensure all references to the spike's identifier use "ID" instead of "name".

## Research Findings
- Found `{spike_name}` in the initialization command example: `python .gemini/scripts/spike_manager.py --init {neuron_id} {spike_name}`.
- Found "define a concise name" in the creation step.
- The user explicitly requested to "dont use spike_name, use spike_id".

## Technical Decisions
| Decision | Rationale |
|----------|-----------|
| Replace `{spike_name}` with `{spike_id}` | Direct response to user instruction. |
| Change "concise name" to "concise spike_id" | Maintain consistency across the protocol. |

## Issues Encountered
| Issue | Resolution |
|-------|------------|
| N/A   |            |