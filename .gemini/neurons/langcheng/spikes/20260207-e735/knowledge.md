# Knowledge: Atlas Reference and Template Integrity in Manifesto

## Metadata
- **Date:** 2026-02-07
- **Spike ID:** 20260207-e735
- **Status:** Completed
- **Authors:** langcheng
- **Tags:** protocol, manifesto, atlas, templates, standards
- **Summary:** Updated the Synapse Manifesto to include a mandatory atlas review step and a strict template integrity standard to ensure cross-neuron compatibility and tool reliability.

## Context & Motivation
### Problem Statement
1. Agents were not explicitly required to consult the atlas for historical context during planning.
2. Agents were deviating from established file templates (e.g., `spike_plan.md`), breaking automated verification scripts and consistency.

### Scope
- Update `manifesto.md` with new standards.
- Align planning files with correct template structures.

## Decision & Outcome
### Chosen Approach
1. Modified the **Plan** step in the **Execution Protocol** to require knowledge discovery via `atlas.md`.
2. Added a **Template Integrity** clause to **Engineering Standards** to mandate strict adherence to skill templates.

### Rationale
Enforcing template integrity ensures that automated tools (like `check-complete`) function correctly and that project state is universally parsable by any agent.

## Technical Implementation
### Core Logic / Patterns
Added to `manifesto.md`:
```markdown
- **Template Integrity:** Agents MUST strictly adhere to the established layout and structure defined in `.gemini/skills/*/templates/`. Modifying standard headers, phase structures, or metadata fields is prohibited to ensure cross-neuron compatibility and automated auditability.
```

### Dependencies & Integration
- Automated scripts in `.gemini/skills/` depend on these templates.

## Consequences & Constraints
### Operational Impact
- Improved reliability of automated verification scripts.
- Consistent project history across all neurons.

### New Constraints
- Agents are forbidden from altering the structural layout of planning and knowledge files.

## Verification & Audit
### Test Plan
- Verified `manifesto.md` content.
- Verified that `check-complete.ps1` now correctly identifies phases when templates are followed.

### Results
- Changes successfully implemented and standards updated.

## Resources & References
- [.gemini/cortex/manifesto.md]
- [.gemini/skills/planning-with-files/templates/spike_plan.md]