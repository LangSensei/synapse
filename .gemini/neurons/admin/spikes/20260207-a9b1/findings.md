# Findings

## Standardized Spike Naming Convention

**Date:** 2026-02-07
**Author:** Admin Neuron
**Context:** Standardizing the spike naming convention to prevent collisions and improve organization.

### Key Decisions
1.  **Format:** Adopted `YYYYMMDD-ID` (e.g., `20260207-a9b1`) for spike directory names.
    *   **Rationale:** Ensures uniqueness, chronological sorting, and brevity.
    *   **Collision Prevention:** Uses a 4-character hex suffix derived from `uuid4` to virtually eliminate collision risk for day-to-day operations.

2.  **Display Names:**
    *   **Mechanism:** `spike_manager.py` now extracts the human-readable name from the `# Spike Plan: ...` header in `spike_plan.md`.
    *   **Fallback:** If no plan or header is found, it defaults to showing the directory name.
    *   **Benefit:** Keeps the filesystem clean (ID-based) while maintaining user-friendly context in the CLI.

### Implementation Details
*   **`spike_manager.py`:**
    *   Updated `initialize_spike` to auto-generate the `YYYYMMDD-ID` if a specific ID isn't provided.
    *   Updated `get_spikes` to parse `spike_plan.md` for display names.
*   **`manifesto.md`:**
    *   Updated protocols to mandate this naming convention.
    *   Clarified the separation between directory ID and display name.

### Verification
*   Tested creation of a new spike without arguments -> generated `YYYYMMDD-ID` correctly.
*   Tested listing of spikes -> correctly displayed "Standardize Spike Naming Convention" from the current plan file.