#!/bin/bash
# Initialize planning files for a new session
# Usage: ./init-session.sh --neuronId [id] --spikeId [id]

set -e

while [[ "$#" -gt 0 ]]; do
    case $1 in
        --neuronId) NEURON_ID="$2"; shift ;;
        --spikeId) SPIKE_ID="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

if [ -z "$NEURON_ID" ] || [ -z "$SPIKE_ID" ]; then
    echo "Usage: ./init-session.sh --neuronId [id] --spikeId [id]"
    exit 1
fi

TARGET_DIR=".gemini/neurons/$NEURON_ID/spikes/$SPIKE_ID"
DATE=$(date +%Y-%m-%d)

if [ ! -d "$TARGET_DIR" ]; then
    mkdir -p "$TARGET_DIR"
    echo "Created target directory: $TARGET_DIR"
fi

echo "Initializing planning files for neuron: $NEURON_ID, spike: $SPIKE_ID in $TARGET_DIR"

SPIKE_PLAN_PATH="$TARGET_DIR/spike_plan.md"
FINDINGS_PATH="$TARGET_DIR/findings.md"
PROGRESS_PATH="$TARGET_DIR/progress.md"

# Create spike_plan.md if it doesn't exist
if [ ! -f "$SPIKE_PLAN_PATH" ]; then
    cat > "$SPIKE_PLAN_PATH" << 'EOF'
# Spike Plan: [Brief Description]

## Goal
[One sentence describing the end state]

## Current Phase
Phase 1

## Phases

### Phase 1: Requirements & Discovery
- [ ] Understand neuron intent
- [ ] Identify constraints
- [ ] Document in findings.md
- **Status:** in_progress

### Phase 2: Planning & Structure
- [ ] **Privileged Access Check:** Verify if proposed changes affect files outside .gemini/neurons/{neuron_id}/. If yes, ensure neuron_id == admin.
- [ ] Define approach
- [ ] Create project structure
- **Status:** pending

### Phase 3: Implementation
- [ ] Execute the plan
- [ ] Write to files before executing
- **Status:** pending

### Phase 4: Testing & Verification
- [ ] Verify requirements met
- [ ] Document test results
- **Status:** pending

### Phase 5: Delivery
- [ ] Review outputs
- [ ] Deliver to neuron
- **Status:** pending

## Decisions Made
| Decision | Rationale |
|----------|-----------|

## Errors Encountered
| Error | Resolution |
|-------|------------|
EOF
    echo "Created spike_plan.md"
else
    echo "spike_plan.md already exists, skipping"
fi

# Create findings.md if it doesn't exist
if [ ! -f "$FINDINGS_PATH" ]; then
    cat > "$FINDINGS_PATH" << 'EOF'
# Findings & Decisions

## Requirements
-

## Research Findings
-

## Technical Decisions
| Decision | Rationale |
|----------|-----------|

## Issues Encountered
| Issue | Resolution |
|-------|------------|

## Resources
-
EOF
    echo "Created findings.md"
else
    echo "findings.md already exists, skipping"
fi

# Create progress.md if it doesn't exist
if [ ! -f "$PROGRESS_PATH" ]; then
    cat > "$PROGRESS_PATH" << EOF
# Progress Log

## Session: $DATE

### Current Status
- **Phase:** 1 - Requirements & Discovery
- **Started:** $DATE

### Actions Taken
-

### Test Results
| Test | Expected | Actual | Status |
|------|----------|--------|--------|

### Errors
| Error | Resolution |
|-------|------------|
EOF
    echo "Created progress.md"
else
    echo "progress.md already exists, skipping"
fi

echo ""
echo "Planning files initialized!"
echo "Files: spike_plan.md, findings.md, progress.md"