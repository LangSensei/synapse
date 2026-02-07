# Knowledge: Improve Spike Manager

## Metadata
- **Date:** 2026-02-07
- **Spike ID:** 20260207-5584
- **Status:** Completed
- **Authors:** langcheng
- **Tags:** refactor, spike-manager, cli, manifesto, protocol
- **Summary:** Improved spike filtering and naming logic in `spike_manager.py` and updated the `manifesto.md` to enforce `planning-with-files` skill adherence.

## Context & Motivation
### Problem Statement
The `spike_manager.py` script was not filtering out completed spikes effectively and prioritized `knowledge.md` over `spike_plan.md` for spike display names. Additionally, the execution protocol in `manifesto.md` needed to explicitly mandate adherence to the `planning-with-files` skill.

### Scope
- Refactor `get_spikes` to exclude spikes marked as "Completed" in `knowledge.md`.
- Refactor `get_spike_display_name` to prioritize `spike_plan.md` for names.
- Ensure `spike_id` is consistently derived from the directory name.
- Update `manifesto.md` to explicitly require agents to follow `planning-with-files` instructions.

## Decision & Outcome
### Chosen Approach
1. Modified the regex-based status check in `get_spikes` to specifically look for `^- \*\*Status:\*\* Completed` and skip those directories.
2. Reordered the logic in `get_spike_display_name` to check for `spike_plan.md` first.
3. Updated `manifesto.md` with a new "Skill Adherence" bullet under Execution Protocol.

### Rationale
This aligns with the user's workflow where `spike_plan.md` is the primary source of truth for an active spike's name, and completed spikes (indicated by a "Completed" status in `knowledge.md`) should no longer clutter the active spike list.

## Technical Implementation
### Core Logic / Patterns
The `get_spikes` function now uses a boolean flag `is_completed` to decide whether to add a spike to the active list:
```python
        is_completed = False
        if knowledge_path.exists():
            try:
                content = knowledge_path.read_text(encoding="utf-8")
                if re.search(r"^- \*\*Status:\*\* Completed", content, re.MULTILINE):
                    is_completed = True
            except Exception:
                pass
        
        if not is_completed:
            active_spikes.append(get_spike_display_name(d))
```

## Consequences & Constraints
### Operational Impact
The `python .gemini/scripts/spike_manager.py --list {neuron_id}` command now returns a cleaner list of only active spikes.

## Verification & Audit
### Test Plan
Created a temporary test neuron and three spikes with different states (Active, Completed, No knowledge.md) to verify filtering and naming prioritization.

### Results
Verified that "Completed" spikes are filtered out and `spike_plan.md` names are prioritized.
