# Findings & Decisions

## Requirements
- `atlas.md` acts as a dynamic index, not a manual storage.
- It must be generated locally from `knowledge.md` files in `.gemini/neurons/`.
- It must be empty (0 entries) when pushed to production/GitHub.

## Research Findings
- Existing structure: `.gemini/neurons/{user}/{task_id}/knowledge.md`.
- Each `knowledge.md` has headers like `## Verified Patterns`, `## System Constraints`, etc.
- A script can parse these headers to create a searchable map.

## Technical Decisions
| Decision | Rationale |
|----------|-----------|
| Python Scripting | Best for cross-platform agent execution and regex parsing of markdown. |
| Atlas Schema | Spike-ID centered with metadata (Date, Summary, Key Tags). |

---
*Update this file after every 2 view/browser/search operations*
