# Findings & Decisions

## Requirements
1. **Move to Initialization:**
   - Activate Skill (`activate_skill`)
   - Init Workspace (`init-session`)
   - Location Verification
2. **Merge Sections:**
   - Combine "Execution Protocol" and "The Synapse Mandate" into a single "Execution Protocol".
3. **Define Iterative Approach:**
   - Agent leverages `planning-with-files` to Plan -> Execute -> Verify.
   - Update knowledge *during* the cycle.
   - Explicitly provide status updates and ask for feedback.
4. **Completion Gate:**
   - Spike completed ONLY if neuron confirms.
   - Post-confirmation: Verify status (`check-complete`), Update Knowledge (Completed), Sync.

## Draft Protocol Structure

### II. Spike Activation (Per-Spike)

1. **Context Discovery:** (Unchanged)
2. **Initialization:**
   - Run `spike_manager.py --init`.
   - **Activate Skill:** `activate_skill(name="planning-with-files")`.
   - **Init Workspace:** Run initialization scripts.
   - **Location Verification:** Verify files in spike dir.
3. **Execution Protocol:**
   - **Iterative Cycle:**
     - **Plan:** Update `spike_plan.md`.
     - **Execute:** Perform tasks.
     - **Verify:** Audit progress.
     - **Distill:** Update `knowledge.md` (Status: Active).
   - **Interaction:** MUST provide summaries and ASK for feedback.
   - **Completion:**
     - Agent asks for confirmation.
     - IF confirmed:
       1. Run `check-complete`.
       2. Update `knowledge.md` (Status: Completed).
       3. Run `sync-atlas.py`.

## Technical Decisions
| Decision | Rationale |
|----------|-----------|
| Explicit Script Paths | Ensures agents know exactly which script to run for verification. |
| Explicit Skill Invocation | Mandates the use of standardized templates via `knowledge-with-files`. |
| Skill-Deep Execution | Emphasizes that `planning-with-files` protocols (like the 2-Action Rule) must be active during implementation. |
| Personalized Interaction | Mandates addressing the user by their `{neuron_id}` for professional courtesy. |