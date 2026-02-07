# Knowledge: Update Knowledge Protocol

## Metadata
- **Date:** 2026-02-07
- **Spike ID:** 20260207-632a
- **Status:** Completed
- **Authors:** langcheng
- **Tags:** manifesto, protocol, knowledge-distillation
- **Summary:** Updated the `manifesto.md` to mandate that `knowledge.md` be created/updated immediately after the "Verification" phase, rather than only upon final completion.

## Context & Motivation
### Problem Statement
The previous protocol implied that knowledge distillation happens only at the very end of a spike. This could lead to a gap where the neuron is asked for confirmation without a finalized knowledge artifact to review.

### Scope
- Update Step 5 of the "Execution Protocol" in `manifesto.md`.

## Decision & Outcome
### Chosen Approach
Modified Step 5 to explicitly trigger "Upon completing the **Verification** step".

### Rationale
Ensures that the knowledge artifact is available for review during the final confirmation checkpoint.

## Technical Implementation
### Core Logic / Patterns
- **Protocol Update**: "Upon completing the **Verification** step, invoke `knowledge-with-files`..."

## Consequences & Constraints
### Operational Impact
Agents must now run `knowledge-with-files` *before* asking the neuron if the spike is done.

## Verification & Audit
### Test Plan
Manual review of the text in `manifesto.md`.

### Results
Text updated successfully.
