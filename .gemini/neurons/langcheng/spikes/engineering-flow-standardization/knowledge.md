# Knowledge: Engineering Flow Standardization

## Metadata
- **Date:** 2026-02-06
- **Spike ID:** engineering-flow-standardization
- **Tags:** atlas, indexing, synchronization, git-policy
- **Summary:** Implemented dynamic Atlas indexing with a tracked clean template in the cloud and local-only updates via .gitignore.

## Verified Patterns
- **Tracked Template:** Keeping a clean `atlas.md` in the repository ensures the file structure is ready for new users without manual creation.
- **Dynamic Indexing**: The `sync-atlas.py` script reliably builds the local knowledge map from neuron history.

## System Constraints
- **Git Ignore Policy:** By adding `atlas.md` to `.gitignore`, local index updates are prevented from being pushed to the cloud, maintaining repository cleanliness.

## Architectural Shifts
- **Index-Based Retrieval**: Shifted from manual distillation to automated indexing of execution history.
- **Rule Simplification**: Removed redundant Atlas integrity rules from the Manifesto as the `.gitignore` policy now enforces cleanliness by default.

## Resources

- [.gemini/scripts/sync-atlas.py](../../../scripts/sync-atlas.py)
