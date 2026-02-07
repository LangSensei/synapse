# Spike Plan: Upgrade Knowledge Template

Goal: Design and implement a superior, standardized `knowledge.md` template for the Synapse ecosystem, and migrate all existing knowledge files to this new format.

## Phases

### Phase 1: Research & Design <!-- id: 0 -->
**Status:** complete
- [x] Research best practices for technical knowledge documentation (ADRs, RFCs, etc.).
- [x] Design a new template that balances readability, parsability, and depth.
- [x] Propose the new template to the neuron.

### Phase 2: Implementation <!-- id: 1 -->
**Status:** complete
- [x] Update the `knowledge-with-files` skill template (`.gemini/skills/knowledge-with-files/templates/knowledge.md`).
- [ ] Update any related scripts (e.g., `sync-atlas.py`) if the metadata structure changes.

### Phase 3: Migration <!-- id: 2 -->
**Status:** complete
- [x] Identify all existing `knowledge.md` files.
- [x] Transform existing files to the new format while preserving information.
- [x] Verify the Atlas synchronization works with the new format.

### Phase 4: Verification <!-- id: 3 -->
**Status:** pending
- [ ] Final audit of all knowledge files.
- [ ] Confirm with the neuron.

## Decisions
- 

## Errors Encountered
| Error | Attempt | Resolution |
|-------|---------|------------|
| | | |