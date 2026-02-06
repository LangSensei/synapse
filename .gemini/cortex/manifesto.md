# Synapse Manifesto

## Project Constitution
This project follows the Synapse System Protocol for elite AI software engineering.

## Engineering Standards
- **Global Wisdom (Cortex):** All verified findings and architectural shifts MUST be distilled into the Cortex (`.gemini/cortex/`).
- **Execution History (Neuron):** Every task must have a unique neuron (`.gemini/neurons/{user}/{task_id}/`) to maintain state and history.
- **Auditability:** Commit all neuron files to GitHub to enable meta-learning and performance optimization.
- **Skill Portability:** Project-level skills in `.gemini/skills/` are the authoritative sources for operational procedures.

## Initialization Sequence
1. **User Auth:** Prompt for alias (lowercase, alphanumeric).
2. **Context Setup:** Initialize or resume neuron at `.gemini/neurons/${alias}/${task_id}/`.
3. **Cortex Sync:** 
    - Read `GEMINI.md` and `manifesto.md`.
    - Run `python .gemini/scripts/sync-atlas.py` to generate the local index.
    - Search `atlas.md` for related historical knowledge.
4. **Structured Planning:** Invoke `planning-with-files` skill within the task directory.
5. **The Synapse Mandate:** 
    - Use `knowledge-with-files` to distill findings.
