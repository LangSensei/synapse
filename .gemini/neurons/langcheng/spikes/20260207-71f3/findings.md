# Findings & Decisions

## Requirements
- `findings.md` and `progress.md` MUST accumulate information for EACH phase.
- No historical data should be lost during updates.
- The `manifesto.md` should be updated to clarify this "Accumulation Mandate".

## Research Findings
- In spike `20260207-db19`, the `progress.md` only contained the last phase.
- Agent prone to "retroactive fixing" instead of real-time updates.

## Technical Decisions
| Decision | Rationale |
|----------|-----------|
| Accumulation Mandate | Ensures that `findings.md` and `progress.md` serve as a complete chronological record of the spike, improving auditability. |
| Sharpened Persistence Prompt | Simplified the manifesto text to "NEVER overwrite history" to improve attention retention and compliance. |

## Implementation Details
- Updated `manifesto.md` Section II.3 to include the **Accumulation** requirement.
- Verified that agents must explicitly preserve older sections when using `replace` or `write_file`.
- Demonstrated accumulation in `progress.md` by restoring Phase 1 history after an accidental overwrite.

## Verification Results
- `spike_plan.md` maintains full chronological task history.
- `findings.md` maintains all technical decisions and research points.
- `progress.md` maintains all session phase logs without overwriting.

## Issues Encountered
| Issue | Resolution |
|-------|------------|
| Persistence Lag | Identified by langcheng; resolved by codifying stricter update protocols. |
| Retroactive Updates | Agent updated files at the end instead of during; fixed by sharpening the manifesto prompt. |

## Resources
- `.gemini/cortex/manifesto.md`