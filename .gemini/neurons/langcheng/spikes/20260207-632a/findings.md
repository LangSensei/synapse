# Findings & Decisions

## Requirements
- Shift the `knowledge-with-files` invocation from "Upon completion" to "whenever Verification is done".
- Update Step 5 of the "Execution Protocol" in `manifesto.md`.

## Research Findings
- Current text: "Upon completion, invoke `knowledge-with-files` to distill findings into `knowledge.md` within the spike directory. Follow the Global Synchronization protocol to update the Atlas."
- Desired text: Should imply continuous or checkpoint-based knowledge updates.

## Technical Decisions
| Decision | Rationale |
|----------|-----------|
| Link to Verification | Ensures knowledge is distilled while context is fresh and before final sign-off. |


## Issues Encountered
| Issue | Resolution |
|-------|------------|
|       |            |

## Resources
- `.gemini/cortex/manifesto.md`