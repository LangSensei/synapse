---
type: standard
tags: [protocol, naming-convention, spike-management, cli]
status: active
---

# Standard: Spike Naming & Management

## Summary
Establishes the `YYYYMMDD-ID` convention for spike directory names to ensure uniqueness and chronological sorting, while decoupling the physical directory name from the human-readable "Display Name" managed within `spike_plan.md`.

## Motivation
- **Collision Avoidance:** Previous naming relied on descriptive strings or manual timestamps, leading to potential conflicts or inconsistent formats.
- **Brevity vs. Context:** Long directory names are cumbersome in CLI. Short IDs are efficient but lack context. This hybrid approach solves both.
- **Sorting:** `YYYYMMDD` prefix ensures natural chronological order in file explorers and CLI lists.

## The Standard

### 1. Directory Structure
Spikes MUST be created in `.gemini/neurons/{neuron_id}/spikes/` using the format:
`YYYYMMDD-{4_char_hex_id}`

**Example:** `.gemini/neurons/admin/spikes/20260207-a9b1/`

### 2. Display Name Resolution
The CLI (`spike_manager.py`) resolves the human-readable name by reading the spike's `spike_plan.md`:

1.  **Read:** `.gemini/neurons/{neuron_id}/spikes/{ID}/spike_plan.md`
2.  **Parse:** Extract the string from the first Level 1 Header: `# Spike Plan: {Display Name}`
3.  **Fallback:** If the file or header is missing, display the Directory ID.

### 3. Creation Workflow
1.  **Agent Action:** Call `spike_manager.py --init {neuron_id}` (no name required).
2.  **System Action:** Generates `YYYYMMDD-ID`.
3.  **Agent Action:** Create `spike_plan.md` with `# Spike Plan: {Descriptive Name}`.

## Technical Implementation
- **ID Generation:** `datetime.now().strftime("%Y%m%d")` + `uuid.uuid4().hex[:4]`
- **Parser:** Regex `^# Spike Plan: (.*)$` (multiline).

## Related Protocols
- **Manifesto:** Updated to reflect this requirement in "Spike Activation".
