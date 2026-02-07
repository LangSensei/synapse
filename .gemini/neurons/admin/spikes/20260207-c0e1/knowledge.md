# Knowledge: Mandating Agent Pause for Options Selection

## Metadata
- **Date:** 2026-02-07
- **Spike ID:** 20260207-c0e1
- **Tags:** protocol, manifesto, options-pattern, interaction-design
- **Summary:** Refined the Synapse Manifesto to explicitly mandate that agents must stop execution and wait for neuron input after presenting options, preventing unsolicited autonomous action.

## Verified Patterns
- **Wait-for-Input Checkpoint**: Agents must provide options and then terminate their turn, allowing the user to select the next step.

## System Constraints
- **Autonomous Overreach**: Agents must be constrained from proceeding through multiple phases of a plan without explicit interactive approval at each decision point.

## Architectural Shifts
- **Interactive Execution Model**: The execution flow is now strictly gated by neuron selection, shifting from proactive automation to reactive, governed implementation.

## Resources
- [.gemini/cortex/manifesto.md]
