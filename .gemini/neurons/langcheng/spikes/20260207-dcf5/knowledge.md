# Knowledge: Refactor Protocol Structure

## Metadata
- **Date:** 2026-02-07
- **Spike ID:** 20260207-dcf5
- **Status:** Active
- **Authors:** langcheng
- **Tags:** manifesto, protocol, refactor
- **Summary:** Restructured the "Protocol Execution" section of `manifesto.md` to streamline initialization, enforce an iterative Plan-Execute-Verify loop, and mandate explicit neuron confirmation before completion.

## Context & Motivation
### Problem Statement
The previous protocol had scattered initialization steps and lacked a clear, iterative workflow definition. It also allowed implicit completion without strong neuron confirmation.

### Scope
- Refactoring `manifesto.md` Section II (Spike Activation) and Section III (Global Synchronization).
- Merging "Execution Protocol" and "The Synapse Mandate".

## Decision & Outcome
### Chosen Approach
- **Consolidated Initialization:** Grouped `init` script, skill activation, and workspace setup into a single "Initialization" phase.
- **Iterative Execution:** Explicitly defined the `planning-with-files` loop (Plan -> Execute -> Verify -> Distill).
- **Full Skill Leverage:** Mandated that implementation (Execute) must strictly follow `planning-with-files` protocols (e.g., 2-Action Rule) to ensure state persistence.
- **Personalized Interaction:** Mandated that agents SHOULD address users by their `{neuron_id}` to improve professional tone and courtesy.
- **Explicit Tooling:** Mandated the use of `check-complete` for verification and `knowledge-with-files` for distillation.


- **Completion Gate:** Added a strict "Completion Gate" requiring neuron confirmation before final verification and knowledge sealing.

### Rationale
Ensures a rigorous, interactive engineering process where the agent stays aligned with the neuron through frequent feedback loops and explicit sign-offs, using the correct project-level tooling.

## Technical Implementation
### Core Logic / Patterns
- **Protocol Flow:** Context -> Initialization -> Execution (Loop) -> Completion (Gate) -> Finalization.

## Consequences & Constraints
### Operational Impact
Agents must now follow a stricter, more interactive workflow. Implicit completion is forbidden.

## Verification & Audit
### Test Plan
Manual review of the updated `manifesto.md` text.

### Results
Text reflects the desired structure and requirements.
