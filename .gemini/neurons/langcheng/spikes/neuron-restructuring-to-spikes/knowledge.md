# Knowledge: Neuron Restructuring to Spikes

## Metadata
- **Date:** 2026-02-07
- **Spike ID:** neuron-restructuring-to-spikes
- **Tags:** synapse-protocol, directory-structure, terminology, maintenance
- **Summary:** Restructured the neurons directory to group activities under "spikes" and updated terminology throughout the codebase.

## Verified Patterns
- **Directory Structure**: `.gemini/neurons/{user}/spikes/{spike_id}/`
- **Planning Files**: `spike_plan.md`, `findings.md`, `progress.md`
- **Terminology**: Use "spike" instead of "task" for activities defined under neurons.

## System Constraints
- Terminology changes in core protocol files require synchronized updates in skills (templates and scripts) and utility scripts (like `sync-atlas.py`).

## Architectural Shifts
- **Spike Aggregation**: Grouping neuronal activities under a `spikes/` folder allows for other types of neuronal data to be added in the future without cluttering the user alias directory.

## Resources
- [GEMINI.md](../../../../GEMINI.md)
- [README.md](../../../../README.md)
- [manifesto.md](../../../cortex/manifesto.md)
