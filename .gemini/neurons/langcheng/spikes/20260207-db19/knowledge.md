# Knowledge: Filter Atlas Completed

## Metadata
- **Date:** 2026-02-07
- **Spike ID:** 20260207-db19
- **Status:** Active
- **Authors:** langcheng
- **Tags:** sync-atlas, filtering, protocol
- **Summary:** Updated the `sync-atlas.py` script to parse the `Status` field from knowledge artifacts and only include entries with the status "Completed" in the generated `atlas.md`. Additionally refined the `manifesto.md` to ensure zero persistence lag in planning files.

## Context & Motivation
### Problem Statement
The `atlas.md` file was displaying all knowledge artifacts regardless of their completion status, which cluttered the knowledge map with in-progress findings. Additionally, agents were not consistently updating planning files in real-time or at phase boundaries, leading to context-disk desynchronization.

### Scope
- Update `parse_knowledge_file` in `sync-atlas.py`.
- Update `sync_atlas` logic to filter entries.
- Refine the **Persistence Mandate** in `manifesto.md` to include action-by-action and phase-based updates.

## Decision & Outcome
### Chosen Approach
- **Enhanced Atlas Logic**: Modified `sync-atlas.py` to parse the `Status` field and filter out non-Completed artifacts.
- **Strict Persistence Protocol**: Updated `manifesto.md` to mandate that agents update planning files (`findings.md`, `progress.md`) for every phase AND immediately after each tool call or significant action.

### Rationale
This ensures that `atlas.md` serves as a reliable index of verified technical knowledge and that agents maintain a perfect real-time mirror of their context on disk for maximum auditability, crash-recovery, and transparency during interactive sessions.

## Technical Implementation
### Core Logic / Patterns
The filtering is performed during the entry collection phase:
```python
            metadata = parse_knowledge_file(path)
            
            # Only include entries with status 'Completed'
            if metadata.get("status") != "Completed":
                continue
```

## Consequences & Constraints
### Operational Impact
The `atlas.md` will now be significantly cleaner, but active spikes will no longer be visible in the index until they are finalized.

## Verification & Audit
### Test Plan
- Create test neuron and spikes with varied statuses.
- Run `sync-atlas.py` and verify entry counts.

### Results
Logic verified: Active spikes are excluded, and Completed spikes are correctly indexed.