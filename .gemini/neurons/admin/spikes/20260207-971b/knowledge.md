# Knowledge: Standardized Terminology to Spike ID

## Metadata
- **Date:** 2026-02-07
- **Spike ID:** 20260207-971b
- **Status:** Active
- **Authors:** admin
- **Tags:** manifesto, terminology, spike_id
- **Summary:** Standardized all references to spike identifiers in `manifesto.md` to use `spike_id` instead of `spike_name`.

## Context & Motivation
### Problem Statement
Inconsistent terminology between "spike name" and "spike ID" caused confusion in tool usage and documentation.

### Scope
Global search and replace of terminology in core protocol documents.

## Decision & Outcome
### Chosen Approach
Adopted `spike_id` as the authoritative term for both internal identifiers and user-provided descriptors.

### Rationale
Alingment with developer preferences for "ID" as the primary handle for entities.

## Technical Implementation
### Core Logic / Patterns
- **Consistent ID Reference**: Use `{spike_id}` as the placeholder in all command examples and documentation.

## Consequences & Constraints
### Operational Impact
Documentation clarity improved; tool argument names now match protocol descriptions.

## Verification & Audit
### Test Plan
Audit of `manifesto.md` and related skills.

### Results
100% terminology alignment achieved.

## Resources & References
- [.gemini/cortex/manifesto.md]