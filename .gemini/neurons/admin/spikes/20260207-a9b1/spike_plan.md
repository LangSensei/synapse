# Spike Plan: Standardize Spike Naming Convention

**Goal:** Update `spike_manager.py` and `manifesto.md` to enforce the `YYYYMMDD-ID` naming convention for spikes, preventing collisions while keeping names concise.

## Phases

- [x] **Phase 1: Update Manifesto**
    - [x] Update `manifesto.md` to reflect the new `YYYYMMDD-ID` spike naming convention.
    - [x] Clarify that the human-readable "name" should be derived from `spike_plan.md` (or provided during init but not part of the directory name).

- [x] **Phase 2: Update Spike Manager**
    - [x] Modify `spike_manager.py` to auto-generate the `YYYYMMDD-ID` prefix/format.
    - [x] Ensure `spike_manager.py` --list extracts the "display name" from `spike_plan.md` (e.g., matching `# Spike Plan: (.*)`).
    - [x] Update the `init` command to accept a description/name but create the folder using only the ID format.

- [x] **Phase 3: Verification**
    - [x] Create a test spike using the new manager.
    - [x] Verify the folder name format.
    - [x] Verify the list command shows the human-readable name.

## Errors Encountered
| Error | Attempt | Resolution |
|-------|---------|------------|
|       |         |            |