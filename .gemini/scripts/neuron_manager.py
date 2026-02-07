import argparse
from pathlib import Path

GEMINI_ROOT = Path(__file__).resolve().parent.parent
NEURONS_DIR = GEMINI_ROOT / "neurons"

def get_neurons():
    """Returns a list of the 9 most recent neurons."""
    if not NEURONS_DIR.exists():
        return []
    
    # Sort by modification time (most recent first)
    neurons = sorted(
        [d.name for d in NEURONS_DIR.iterdir() if d.is_dir()],
        key=lambda d: (NEURONS_DIR / d).stat().st_mtime,
        reverse=True
    )
    return neurons[:9]

def initialize_neuron(neuron_id):
    """Ensures neuron directory and MEMORY.md exist."""
    neuron_dir = NEURONS_DIR / neuron_id
    if not neuron_dir.exists():
        print(f"Initializing new neuron: {neuron_id}")
        neuron_dir.mkdir(parents=True, exist_ok=True)
    
    memory_file = neuron_dir / "MEMORY.md"
    if not memory_file.exists():
        memory_file.write_text(f"""# {neuron_id} Memory

Persistent memory for neuron {neuron_id}.
""")
    
    return neuron_dir

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Neuron Manager Script")
    parser.add_argument("--list", action="store_true", help="List available neurons")
    parser.add_argument("--init", metavar="NEURON_ID", help="Initialize or select neuron with this ID")

    args = parser.parse_args()

    if args.list:
        for neuron in get_neurons():
            print(neuron)
    elif args.init:
        initialize_neuron(args.init)
    else:
        print("Step 1: Select your neuron ID (or provide a new one)")
        neurons = get_neurons()
        if neurons:
            for i, neuron in enumerate(neurons, 1):
                print(f"{i}. {neuron}")
        else:
            print("(No neurons found)")
        print("\nUsage: python .gemini/scripts/neuron_manager.py --init {neuron_id}")