---
name: knowledge-with-files
description: Standardizes the distillation of spike insights into a structured format for the Synapse Atlas.
---

# Knowledge with Files

This skill ensures every spike culminates in a high-quality, parsable technical manual.

## Important: Where Files Go

- **Templates** are in this skill's `templates/` folder
- **Your knowledge file** MUST go in the **spike-specific neuron directory**: `.gemini/neurons/{user}/spikes/{spike_id}/knowledge.md`

## The Knowledge Mandate

Before closing any spike:
1. **Initialize `knowledge.md`** using the standardized template.
2. **Distill Truths**: Extract verified patterns, system constraints, and architectural shifts from your `findings.md`.
3. **Index-Ready**: Ensure the Metadata section is filled correctly so `sync-atlas.py` can find it.

## Templates

- [templates/knowledge.md](templates/knowledge.md) — The standardized knowledge manual.
