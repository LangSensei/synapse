# Knowledge: Engineering Flow Standardization

## Metadata
- **Date:** 2026-02-06
- **Task ID:** engineering-flow-standardization
- **Tags:** atlas, indexing, synchronization, git-policy
- **Summary:** Implemented dynamic Atlas indexing with a tracked clean template in the cloud and local-only updates via .gitignore.

## Verified Patterns
- **Tracked Template:** Keeping a clean `atlas.md` in the repository ensures the file structure is ready for new users without manual creation.
- **Dynamic Indexing**: The `sync-atlas.py` script reliably builds the local knowledge map from neuron history.

## System Constraints
- **Git Ignore Policy:** By adding `atlas.md` to `.gitignore`, local index updates are prevented from being pushed to the cloud, maintaining repository cleanliness.

## Architectural Shifts
- **Simplified Setup:** Removed complex Git commands from the Manifesto to lower the barrier for entry while maintaining system integrity.

## Resources

- [.gemini/scripts/sync-atlas.py](../../../scripts/sync-atlas.py)
