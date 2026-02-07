# Knowledge: Improved Spike Activation Protocol

## Metadata
- **Date:** 2026-02-07
- **Spike ID:** 20260207-00cb
- **Tags:** manifesto, protocol, spikes, planning
- **Summary:** Refined the Spike Activation section of the Synapse Manifesto to ensure clearer, more actionable steps for agent initialization and planning.

## Verified Patterns
- **Explicit Skill Activation**: Mandated the use of `activate_skill(name="planning-with-files")` immediately after spike initialization to ensure planning tools are available and structured.
- **Spike ID Capture**: Formalized the requirement to record the `spike_id` returned by the initialization script for use in subsequent workspace setup steps.

## System Constraints
- **Workspace Containment**: Reaffirmed the strict requirement that planning files MUST NEVER reside in the project root, only within the specific spike directory.

## Architectural Shifts
- **Phase-Based Execution**: Shifted the manifesto's focus from a single initialization step to a multi-phase protocol (Discovery -> Initialization -> Planning -> Execution -> Distillation).

## Resources
- `.gemini/cortex/manifesto.md`
- `.gemini/skills/planning-with-files/SKILL.md`
