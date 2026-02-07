# Initialize planning files for a new session
# Usage: .\init-session.ps1 -neuronId [id] -spikeId [id]

param(
    [Parameter(Mandatory=$true)]
    [string]$neuronId,
    
    [Parameter(Mandatory=$true)]
    [string]$spikeId
)

$TargetDir = ".gemini/neurons/$neuronId/spikes/$spikeId"

$DATE = Get-Date -Format "yyyy-MM-dd"

if (-not (Test-Path $TargetDir)) {
    New-Item -ItemType Directory -Force -Path $TargetDir | Out-Null
    Write-Host "Created target directory: $TargetDir"
}

Write-Host "Initializing planning files for neuron: $neuronId, spike: $spikeId in $TargetDir"

$SpikePlanPath = Join-Path $TargetDir "spike_plan.md"
$FindingsPath = Join-Path $TargetDir "findings.md"
$ProgressPath = Join-Path $TargetDir "progress.md"

# Create spike_plan.md if it doesn't exist
if (-not (Test-Path $SpikePlanPath)) {
    @"
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
- [ ] **Privileged Access Check:** Verify if proposed changes affect files outside `.gemini/neurons/{neuron_id}/`. If yes, ensure `neuron_id == admin`.
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
"@ | Out-File -FilePath $SpikePlanPath -Encoding UTF8
    Write-Host "Created spike_plan.md"
} else {
    Write-Host "spike_plan.md already exists, skipping"
}

# Create findings.md if it doesn't exist
if (-not (Test-Path $FindingsPath)) {
    @"
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
"@ | Out-File -FilePath $FindingsPath -Encoding UTF8
    Write-Host "Created findings.md"
} else {
    Write-Host "findings.md already exists, skipping"
}

# Create progress.md if it doesn't exist
if (-not (Test-Path $ProgressPath)) {
    @"
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
"@ | Out-File -FilePath $ProgressPath -Encoding UTF8
    Write-Host "Created progress.md"
} else {
    Write-Host "progress.md already exists, skipping"
}

Write-Host ""
Write-Host "Planning files initialized!"
Write-Host "Files: spike_plan.md, findings.md, progress.md"