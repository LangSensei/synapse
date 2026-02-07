# Spike Plan: Restructure Neurons to Spikes

## Goal
Restructure the `.gemini/neurons/langcheng/` directory to use the term "spikes" instead of "task", move existing tasks into a `spikes/` subdirectory, and update relevant documentation.

## Current Phase
Phase 4: Verification & Finalization

## Phases

### Phase 1: Discovery
- [x] Create current spike directory: `.gemini/neurons/langcheng/spikes/neuron-restructuring-to-spikes/`
- [x] Identify all occurrences of the term "task" in `.gemini/` and root documentation that should be changed to "spike".
- [x] List existing task directories to be moved.
- **Status:** complete

### Phase 2: Execution - Directory Migration
- [x] Create `spikes` folder if not already done.
- [x] Move existing task directories into `spikes/`.
- [x] Ensure the current restructuring spike is properly placed.
- **Status:** complete

### Phase 3: Execution - Documentation Update
- [x] Update `GEMINI.md` to reflect the "spike" terminology.
- [x] Update `.gemini/cortex/manifesto.md` and other protocol files.
- [x] Update any skill templates if necessary.
- [x] Update scripts (`sync-atlas.py`, `planning-with-files` scripts).
- **Status:** complete

### Phase 4: Verification & Finalization
- [x] Verify directory structure.
- [x] Check links and references in documentation.
- [x] Distill findings to `knowledge.md`.
- **Status:** complete

### Phase 5: Delivery
- [x] Review all output files
- [x] Final distillation to knowledge.md
- [x] Deliver to user
- **Status:** complete

## Key Questions
1. Should "task_id" also be renamed to "spike_id" in documentation? (Yes, per user preference for "spike").
2. Are there any scripts (e.g., `sync-atlas.py`) that rely on the old path structure?

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| Use `spikes/` subdirectory | Aggregate all spikes and allow for future expansion of other neuron-related folders. |
| Rename "task" to "spike" | User preference for terminology. |

## Errors Encountered
| Error | Attempt | Resolution |
|-------|---------|------------|
|       | 1       |            |

## Notes
- New path format: `.gemini/neurons/{user}/spikes/{spike_id}/`
