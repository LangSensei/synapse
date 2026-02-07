#!/bin/bash
# Initialize planning files for a new session
# Usage: ./init-session.sh [neuron-name]

set -e

NEURON_NAME="${1:-neuron}"
DATE=$(date +%Y-%m-%d)

echo "Initializing planning files for: $NEURON_NAME"

# Create spike_plan.md if it doesn't exist
if [ ! -f "spike_plan.md" ]; then
    cat > spike_plan.md << 'EOF'
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
if [ ! -f "findings.md" ]; then
    cat > findings.md << 'EOF'
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
if [ ! -f "progress.md" ]; then
    cat > progress.md << EOF
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