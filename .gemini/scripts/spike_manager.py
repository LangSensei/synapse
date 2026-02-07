import argparse
from pathlib import Path
import os

GEMINI_ROOT = Path(__file__).resolve().parent.parent
NEURONS_DIR = GEMINI_ROOT / "neurons"

def get_spikes(neuron_id):
    """Returns a list of the 9 most recent spikes for a neuron."""
    neuron_dir = NEURONS_DIR / neuron_id
    if not neuron_dir.exists():
        return []

    spikes_dir = neuron_dir / "spikes"
    if not spikes_dir.exists():
        return []
    
    # Sort by modification time (most recent first)
    spikes = sorted(
        [d.name for d in spikes_dir.iterdir() if d.is_dir()],
        key=lambda d: (spikes_dir / d).stat().st_mtime,
        reverse=True
    )
    return spikes[:9]

def initialize_spike(neuron_dir, spike_id):
    """Creates a new spike directory."""
    spikes_dir = neuron_dir / "spikes"
    spike_path = spikes_dir / spike_id
    
    if not spike_path.exists():
        print(f"Creating new spike directory: {spike_path}")
        spike_path.mkdir(parents=True, exist_ok=True)
    else:
        print(f"Spike directory already exists: {spike_path}")

    return spike_path

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
        if len(args.init) == 2:
            neuron_id, spike_id = args.init
            neuron_dir = NEURONS_DIR / neuron_id
            if not neuron_dir.exists():
                print(f"Error: Neuron '{neuron_id}' does not exist.")
            else:
                initialize_spike(neuron_dir, spike_id)
        else:
            # Fallback for "Step 2" interactive-like flow
            neuron_id = args.init[0]
            print(f"Step 2: Select a spike for neuron '{neuron_id}' (or provide a new one)")
            spikes = get_spikes(neuron_id)
            if spikes:
                for i, spike in enumerate(spikes, 1):
                    print(f"{i}. {spike}")
            else:
                print("(No spikes found)")
            print(f"\nUsage: python .gemini/scripts/spike_manager.py --init {neuron_id} {{spike_id}}")
    else:
         parser.print_help()