# Knowledge: Prompting & Protocol Optimization

## Metadata
- **Date:** 2026-02-07
- **Spike ID:** optimize-prompting
- **Tags:** architecture, protocols, cleanup, standardization
- **Summary:** Removed unreliable "Privileged Access" constraints and restructured the initialization/operational protocol into Session Boot, Spike Activation, and Global Synchronization phases.

## Verified Patterns
- **Protocol Categorization**: Distinguishing between one-time session setup (Session Boot), repeatable task setup (Spike Activation), and continuous maintenance (Global Synchronization) improves agent role clarity.
- **Explicit Script Usage**: Providing full command examples for `init-session` and `check-complete` in the manifesto ensures more consistent execution across different shell environments.

## System Constraints
- **Search Reliability**: `search_file_content` may sometimes fail to find strings in hidden/dot-folders (like `.gemini`) depending on configuration; `Get-ChildItem -Recurse | Select-String` is a reliable fallback on Windows.

## Architectural Shifts
- **Removal of Privileged Access**: The system no longer relies on `neuron_id == admin` checks for file modifications, favoring "Workspace Containment" and manual verification instead.
- **Mandatory Location Verification**: Agents must now explicitly verify that planning files are created in the spike directory and NOT the project root immediately after initialization.

## Resources
- [.gemini/cortex/manifesto.md](.gemini/cortex/manifesto.md)
- [.gemini/skills/planning-with-files/templates/spike_plan.md](.gemini/skills/planning-with-files/templates/spike_plan.md)
- [.gemini/skills/planning-with-files/scripts/check-complete.ps1](.gemini/skills/planning-with-files/scripts/check-complete.ps1)
