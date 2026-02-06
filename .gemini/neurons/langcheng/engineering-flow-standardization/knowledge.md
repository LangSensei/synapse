# Knowledge: Engineering Flow Standardization

## Metadata
- **Date:** 2026-02-06
- **Task ID:** engineering-flow-standardization
- **Tags:** atlas, indexing, synchronization, knowledge-management
- **Summary:** Implemented dynamic Atlas indexing using the `knowledge-with-files` skill and a Python sync script.

## Verified Patterns
- **Dynamic Indexing**: Atlas acts as a local index of all neuron history rather than a manual storage file.
- **Knowledge Templating**: Standardized `knowledge.md` metadata enables reliable automated parsing.

## System Constraints
- **Atlas Cleanliness**: `atlas.md` must be cleared before repository commits to maintain production state.

## Architectural Shifts
- **Index-Based Retrieval**: Shifted from manual distillation to automated indexing of execution history.

## Resources
- [.gemini/scripts/sync-atlas.py](../../../.gemini/scripts/sync-atlas.py)
