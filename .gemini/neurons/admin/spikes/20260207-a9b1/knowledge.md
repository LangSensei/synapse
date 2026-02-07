# Knowledge: Standard: Spike Naming & Management

## Metadata
- **Date:** 2026-02-07
- **Spike ID:** 20260207-a9b1
- **Status:** Active
- **Authors:** admin
- **Tags:** protocol, naming-convention, spike-management, cli
- **Summary:** Establishes the `YYYYMMDD-ID` convention for spike directory names to ensure uniqueness and chronological sorting, while decoupling the physical directory name from the human-readable "Display Name" managed within `spike_plan.md`.

## Context & Motivation
### Problem Statement
Manual spike naming led to collisions and inconsistent formatting, making the `.gemini/neurons` directory difficult to navigate.

### Scope
Modification of the CLI tool (`spike_manager.py`) and protocol documentation.

## Decision & Outcome
### Chosen Approach
Adopted a hybrid system: ID-based directories (`YYYYMMDD-XXXX`) and content-based display names (from `spike_plan.md`).

### Rationale
Short IDs are efficient for CLI/FS operations; display names provide human context without polluting the directory structure with long strings.

## Technical Implementation
### Core Logic / Patterns
- **YYYYMMDD-ID Format**: Uses current date and a 4-char hex suffix.
- **Display Name Resolution**: Extracting the Level 1 header from `spike_plan.md`.

### Dependencies & Integration
- Update to `.gemini/scripts/spike_manager.py`.

## Consequences & Constraints
### Operational Impact
Improved sorting and collision prevention.

### New Constraints
Agents must maintain a Level 1 header in `spike_plan.md` for proper listing.

## Verification & Audit
### Test Plan
Integration tests with the `spike_manager.py --list` command.

### Results
Correct generation of IDs and resolution of display names.

## Resources & References
- [.gemini/cortex/manifesto.md]
- [.gemini/scripts/spike_manager.py]