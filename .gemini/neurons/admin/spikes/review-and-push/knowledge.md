# Knowledge: Neuron/Spike Management Implementation

## Metadata
- **Date:** 2026-02-07
- **Spike ID:** review-and-push
- **Tags:** protocol, management-scripts, automation, synapse-v1.2
- **Summary:** Implemented dedicated scripts for neuron and spike management, updated the protocol to v1.2, and enforced strict workspace containment.

## Verified Patterns
- **Script-Driven Discovery**: Using `neuron_manager.py` and `spike_manager.py` during initialization reduces manual filesystem errors and standardizes the entry flow.
- **PowerShell Compatibility**: Multi-command execution in the current environment must use `;` instead of `&&`.

## System Constraints
- **Workspace Containment**: Planning files must never be created in the project root to maintain repository hygiene. This is now a strict requirement in the Manifesto.

## Architectural Shifts
- **Role Definition (v1.2)**: Transitioned from "user" to "neuron_id" to align with the cognitive architecture theme.
- **Privileged Access**: Only the `admin` neuron is permitted to modify files outside of the `.gemini/neurons/` directory.

## Resources
- [.gemini/cortex/manifesto.md](../../../../cortex/manifesto.md)
- [.gemini/scripts/neuron_manager.py](../../../../scripts/neuron_manager.py)
- [.gemini/scripts/spike_manager.py](../../../../scripts/spike_manager.py)
