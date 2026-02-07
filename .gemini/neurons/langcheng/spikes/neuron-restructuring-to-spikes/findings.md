# Findings & Decisions

## Requirements
- Rename "task" to "spike" within the "neurons" context.
- Aggregate spikes into a `spikes/` subdirectory under the user alias.
- Update documentation to reflect these changes.

## Research Findings
- Existing tasks:
  - `engineering-flow-standardization`
  - `github-publication`
  - `project-standardization`
  - `system-prompt-optimization`
- Protocol files referencing "task":
  - `GEMINI.md`
  - `.gemini/cortex/manifesto.md`

## Technical Decisions
| Decision | Rationale |
|----------|-----------|
| Move tasks to `spikes/` | Organize neuronal activities under a specific category. |
| Rename `task_plan.md` to `spike_plan.md` | Full commitment to the "spike" terminology. |
| Update scripts and templates | Ensure tools work with the new naming convention. |

## Issues Encountered
| Issue | Resolution |
|-------|------------|
| `grep`/`sed` not available in PS | Used manual `replace` for each file. |
| Protocol files had slightly different content than expected | Read files first to verify content before replacement. |

## Resources
- [GEMINI.md](GEMINI.md)
- [.gemini/cortex/manifesto.md](.gemini/cortex/manifesto.md)

---
*Update this file after every 2 view/browser/search operations*
