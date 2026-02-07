# Findings & Decisions: Improve Spike Activation Protocol

## Requirements
- Clarify the transition from spike initialization to skill activation.
- Ensure the `spike_id` usage is explicit (it's returned by the init script).
- Formalize the requirement to call `activate_skill`.
- Strengthen the mandate for planning files location.

## Research Findings
- The current manifesto is good but relies on the agent "knowing" to call `activate_skill` without it being a hard requirement in the numbered list.
- The `spike_id` is essential for the initialization scripts but its source (the output of `spike_manager.py --init`) isn't explicitly linked in the instructions.
- Step 3 (The Synapse Mandate) is a bit thin; it should probably link more clearly to the finalization of a spike.

## Technical Decisions
| Decision | Rationale |
|----------|-----------|
| Add `activate_skill` requirement | Standardizes the agent's workflow for complex tasks. |
| Link `spike_id` source to subsequent steps | Prevents confusion about where the ID comes from. |
| Add explicit "Plan Creation" step | Ensures the agent doesn't just initialize empty files but actually populates the plan. |

## Issues Encountered
| Issue | Resolution |
|-------|------------|
| N/A   |            |

## Resources
- `.gemini/cortex/manifesto.md`
- `planning-with-files` skill instructions

## Visual/Browser Findings
- N/A

---
*Update this file after every 2 view/browser/search operations*