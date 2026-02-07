# Findings & Decisions

## Requirements
- Filter out spikes where `knowledge.md` status is "Completed".
- Prioritize `spike_plan.md` for spike names in the list output.
- Use the directory name (`spike_path.name`) as the base for the spike ID.
- Enforce `planning-with-files` skill usage via `manifesto.md`.

## Research Findings
- `spike_manager.py` previously checked `knowledge.md` before `spike_plan.md`.
- `knowledge.md` status is typically formatted as `- **Status:** [Status]`.
- PowerShell requires specific flags (`-Recurse -Force`) for directory removal compared to CMD/Bash.

## Technical Decisions
| Decision | Rationale |
|----------|-----------|
| Regex for status | `re.MULTILINE` ensures we match the start of the line in markdown files. |
| Reorder name lookup | User specifically requested `spike_plan.md` parsing for names. |
| Manifesto update | Explicitly linking "Execution Protocol" to the `planning-with-files` skill ensures agent consistency. |

## Issues Encountered
| Issue | Resolution |
|-------|------------|
| PowerShell `&&` limitation | Use `;` or run commands individually. |
| `rmdir` compatibility | Use native PowerShell `Remove-Item` parameters for recursive deletion. |

## Resources
- `.gemini/cortex/manifesto.md`
- `.gemini/scripts/spike_manager.py`
- `.gemini/skills/planning-with-files/templates/`

## Visual/Browser Findings
- N/A
