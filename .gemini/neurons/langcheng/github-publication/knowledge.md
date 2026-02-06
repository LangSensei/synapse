# Knowledge: GitHub Publication Setup

## Verified Patterns
- **Standard README:** A high-quality README should include badges for protocol and dependencies to immediately communicate the project's nature.
- **Skill Dependencies:** Local skill installations (`--path .gemini/skills/...`) allow the repository to remain self-contained and portable.

## Architectural Shifts
- **Public Visibility:** Moving from a local-only setup to a GitHub-ready structure requires clear instructions on how to replicate the agent environment (specifically skill installation).

## System Constraints
- **Proxy Handling:** Future contributors should be aware that environment-specific proxy settings (like `12334`) may need to be adjusted for initial skill cloning.
