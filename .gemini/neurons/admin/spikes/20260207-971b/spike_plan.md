# Spike Plan: Standardize Terminology to Spike ID

## Goal
Replace all instances of `spike_name` with `spike_id` in `manifesto.md` to ensure consistent terminology throughout the protocol.

## Current Phase
Phase 1

## Phases

### Phase 1: Requirements & Discovery
- [x] Understand neuron intent
- [x] Locate all instances of `spike_name` in `manifesto.md`
- [x] Document findings in `findings.md`
- **Status:** complete

### Phase 2: Implementation
- [x] Replace `spike_name` with `spike_id` in `manifesto.md`
- [x] Ensure command examples reflect this change (even if the script takes a name, the protocol should refer to it as the initial ID/descriptor).
- **Status:** complete

### Phase 3: Testing & Verification
- [x] Verify `manifesto.md` content
- **Status:** complete

### Phase 4: Delivery
- [x] Final distillation to `knowledge.md`
- [x] Sync Atlas
- **Status:** complete

## Key Questions
1. Should `spike_name` be completely eliminated even in command examples?

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| Use `spike_id` as the primary term | Align with user instruction to "use spike_id". |

## Errors Encountered
| Error | Attempt | Resolution |
|-------|---------|------------|
|       | 1       |            |

## Notes
- The script `spike_manager.py --init` takes a descriptor which it then turns into a `spike_id`. The user wants to refer to this input as `spike_id`.