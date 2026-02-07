import argparse
from pathlib import Path
import os
import datetime
import uuid
import re

GEMINI_ROOT = Path(__file__).resolve().parent.parent
NEURONS_DIR = GEMINI_ROOT / "neurons"

def get_spike_display_name(spike_path):
    """Extracts the display name from spike_plan.md or returns the directory name."""
    plan_path = spike_path / "spike_plan.md"
    if plan_path.exists():
        try:
            content = plan_path.read_text(encoding="utf-8")
            match = re.search(r"^# Spike Plan: (.*)$", content, re.MULTILINE)
            if match:
                return f"{spike_path.name} ({match.group(1).strip()})"
        except Exception:
            pass
    return spike_path.name

def get_spikes(neuron_id):
    """Returns a list of the 9 most recent spikes for a neuron with display names."""
    neuron_dir = NEURONS_DIR / neuron_id
    if not neuron_dir.exists():
        return []

    spikes_dir = neuron_dir / "spikes"
    if not spikes_dir.exists():
        return []
    
    # Sort by modification time (most recent first)
    spike_dirs = sorted(
        [d for d in spikes_dir.iterdir() if d.is_dir()],
        key=lambda d: d.stat().st_mtime,
        reverse=True
    )
    
    return [get_spike_display_name(d) for d in spike_dirs[:9]]

def generate_spike_id():
    """Generates a unique spike ID in the format YYYYMMDD-ID."""
    today = datetime.datetime.now().strftime("%Y%m%d")
    unique_id = uuid.uuid4().hex[:4]
    return f"{today}-{unique_id}"

def initialize_spike(neuron_dir, spike_name_or_id=None):
    """Creates a new spike directory. 
       If spike_name_or_id matches YYYYMMDD-ID, uses it.
       Otherwise, generates a new ID and uses the input as the initial plan name (not implemented here, but ID generation is).
    """
    spikes_dir = neuron_dir / "spikes"
    
    # Check if input is already a valid ID or needs generation
    # Simple regex for YYYYMMDD-ID (8 digits, hyphen, 4 hex chars)
    if spike_name_or_id and re.match(r"^\d{8}-[a-f0-9]{4}$", spike_name_or_id):
        spike_id = spike_name_or_id
    else:
        spike_id = generate_spike_id()

    spike_path = spikes_dir / spike_id
    
    if not spike_path.exists():
        print(f"Creating new spike directory: {spike_path}")
        spike_path.mkdir(parents=True, exist_ok=True)
        # We don't auto-create the plan here; the agent does that via skill. 
        # But we return the ID so the user knows what was created.
        print(f"Spike initialized with ID: {spike_id}")
    else:
        print(f"Spike directory already exists: {spike_path}")

    return spike_id

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Spike Manager Script")
    parser.add_argument("--list", metavar="NEURON_ID", help="List available spikes for a neuron")
    parser.add_argument("--init", nargs="+", metavar=("NEURON_ID", "SPIKE"), help="Initialize a spike for a neuron")

    args = parser.parse_args()

    if args.list:
        neuron_id = args.list
        for spike in get_spikes(neuron_id):
            print(spike)
    elif args.init:
        if len(args.init) >= 1:
            neuron_id = args.init[0]
            spike_input = args.init[1] if len(args.init) > 1 else None
            
            neuron_dir = NEURONS_DIR / neuron_id
            if not neuron_dir.exists():
                print(f"Error: Neuron '{neuron_id}' does not exist.")
            else:
                initialize_spike(neuron_dir, spike_input)
        else:
             parser.print_help()
