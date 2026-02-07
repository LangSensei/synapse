# Knowledge: Improved Spike Activation Protocol

## Metadata
- **Date:** 2026-02-07
- **Spike ID:** 20260207-00cb
- **Status:** Active
- **Authors:** admin
- **Tags:** manifesto, protocol, spikes, planning
- **Summary:** Refined the Spike Activation section of the Synapse Manifesto to ensure clearer, more actionable steps for agent initialization and planning.

## Context & Motivation
### Problem Statement
The previous spike activation flow was vague, leading to inconsistent setup of planning files and skill activation.

### Scope
Restructuring of the "Spike Activation" protocol within the Synapse Manifesto.

## Decision & Outcome
### Chosen Approach
Formalized a multi-step flow: Discovery -> Initialization -> Structured Planning -> Execution -> Distillation.

### Rationale
Structured workflows reduce the cognitive load on the agent and ensure a consistent "working memory on disk."

## Technical Implementation
### Core Logic / Patterns
- **Explicit Skill Activation**: Mandatory `activate_skill(name="planning-with-files")`.
- **Spike ID Capture**: Recording the script-returned ID for workspace setup.

## Consequences & Constraints
### Operational Impact
Higher reliability in spike setup; agents are forced to initialize planning before execution.

### New Constraints
Planning files MUST NEVER reside in the project root.

## Verification & Audit
### Test Plan
Initialization of several test spikes following the new protocol.

### Results
Successful setup of structured workspaces in all test cases.

## Resources & References
- [.gemini/cortex/manifesto.md]
- [.gemini/skills/planning-with-files/SKILL.md]