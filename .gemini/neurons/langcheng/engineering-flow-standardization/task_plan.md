# Task Plan: Engineering Flow Standardization

## Goal
Standardize the Cortex indexing process by transforming `atlas.md` into a dynamically generated local index of all neuron knowledge.

## Current Phase
Phase 1

## Phases

### Phase 1: Requirements & Discovery
- [x] Analyze user requirement for dynamic Atlas indexing
- [ ] Research efficient indexing patterns for local markdown files
- [ ] Document findings in findings.md
- **Status:** in_progress

### Phase 2: Planning & Structure
- [ ] Define the schema for the new `atlas.md` index
- [ ] Design the sync script logic (recursive search for `knowledge.md`)
- [ ] Update `manifesto.md` with the new sync protocol
- **Status:** pending

### Phase 3: Implementation
- [x] Create `scripts/sync-atlas.py`
- [x] Clear `atlas.md` for the "Production/Clean" state
- [x] Implement `knowledge-with-files` skill and template
- [x] Update existing knowledge files to the new template
- **Status:** complete

### Phase 4: Testing & Verification
- [x] Run the sync script across existing neurons
- [x] Verify `atlas.md` correctly indexes all `knowledge.md` files
- [x] Test schema robustness
- **Status:** complete

### Phase 5: Delivery
- [x] Commit and push changes
- **Status:** complete

## Key Questions
1. Should the sync script be Python or PowerShell? (Python is more portable for the agent, but PowerShell is native to this env. I'll prefer Python for "elite" portability).
2. How to ensure the Atlas remains empty in production? (Add a `clear` flag to the script or a pre-commit guideline).

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| Dynamic Indexing | Allows the agent to search through entire execution history without manual distillation overhead. |

## Errors Encountered
| Error | Attempt | Resolution |
|-------|---------|------------|
|       | 1       |            |
