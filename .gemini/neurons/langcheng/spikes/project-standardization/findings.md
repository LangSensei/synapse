# Findings & Decisions

## Requirements
- Decentralized knowledge architecture (Cortex/Neuron).
- Elite AI software engineer identity (Synapse Agent).
- Standardized 4-file planning pattern.
- Project-level skill integration.
- Clear version control boundaries.

## Research Findings
- PowerShell requires specific handling for directory creation (`New-Item -Force`).
- Git global config can override local environment variables (e.g., the `7890` proxy issue).
- The `planning-with-files` skill uses a specific 3-file template set.

## Technical Decisions
| Decision | Rationale |
|----------|-----------|
| Port 12334 Proxy | Required for internet access in this environment |
| .gitignore `!GEMINI.md` | Ensures the gateway is always tracked while neurons are ignored |
| Cortex promotion | Prevents knowledge loss by distilling neuron findings into the global Atlas |

## Issues Encountered
| Issue | Resolution |
|-------|------------|
| Proxy port mismatch | Unset global `remote.origin.proxy` and forced `12334` |
| `replace` tool failure | Added context lines and verified with `read_file` |

## Resources
- Synapse Protocol (in `manifesto.md`)
- planning-with-files: `https://github.com/OthmanAdi/planning-with-files`

## Visual/Browser Findings
- Web search confirms `planning-with-files` is a common pattern for persistent agent memory.
- Skill installation log showed successful cloning after proxy adjustment.

---
*Update this file after every 2 view/browser/search operations*