# Findings & Decisions

## Requirements
- `atlas.md` should only display knowledge artifacts where `Status` is `Completed`.
- Modify `sync-atlas.py` to achieve this filtering.
- Update `manifesto.md` to mandate planning file updates for each phase and action.
- Ensure `spike_plan.md` is explicitly included in the Persistence Mandate.

## Research Findings
- `parse_knowledge_file` extracts metadata from `knowledge.md`.
- `Status` parsing is essential for filtering the index.
- Persistence lag is a significant risk in complex spikes; real-time disk mirrors mitigate this.

## Technical Decisions
| Decision | Rationale |
|----------|-----------|
| Parse `Status` | Required to implement the requested filtering logic. |
| Filter in `sync_atlas` | Most efficient place to exclude non-Completed entries. |
| Persistence Mandate | Codified the requirement for action-by-action AND phase-based planning updates. |
| Explicit File Listing | Mandated that `spike_plan.md`, `findings.md`, and `progress.md` MUST all be updated to maintain a perfect state mirror. |

## Implementation Details
- Added `status_match` to `parse_knowledge_file`.
- Added conditional skip in `sync_atlas`.
- Updated `manifesto.md` Section II.3 with the Persistence Mandate.

## Issues Encountered
| Issue | Resolution |
|-------|------------|
| Persistence Lag | Identified by langcheng; resolved by codifying stricter update protocols. |

## Resources
- `.gemini/scripts/sync-atlas.py`
- `.gemini/cortex/atlas.md`
- `.gemini/cortex/manifesto.md`