# Findings & Decisions

## Requirements
- Update `manifesto.md` to include a requirement to review `atlas.md` during the planning phase.
- Add a new standard to `manifesto.md` regarding strict template integrity.

## Research Findings
- `atlas.md` is located at `.gemini/cortex/atlas.md`.
- `atlas.md` is ignored by Git, so it requires `sync-atlas.py` to be run to be populated.
- The `Initialization` sequence in `manifesto.md` already includes running `sync-atlas.py`.
- The current `Execution Protocol` -> `Plan` step lacks an explicit instruction to check the atlas for relevant historical context.
- Deviation from skill templates (e.g., changing headers or omitting standard sections) breaks automated scripts like `check-complete.ps1`.
- A formal **Template Integrity** mandate is required in the manifesto to enforce strict layout adherence across all agents.

## Technical Decisions
| Decision | Rationale |
|----------|-----------|
| Update the Plan step | To ensure agents leverage the historical context in atlas.md |
| Add Template Integrity standard | To prevent layout deviations and ensure script compatibility |

## Issues Encountered
| Issue | Resolution |
|-------|------------|
| `&&` not valid in PowerShell | Ran commands separately |
| `atlas.md` ignored by patterns | Used `run_shell_command` with `type` |

## Resources
- .gemini/cortex/manifesto.md
- .gemini/cortex/atlas.md
- .gemini/skills/planning-with-files/templates/

## Visual/Browser Findings
- N/A

---
*Update this file after every 2 view/browser/search operations*