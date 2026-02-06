import os
import re
from pathlib import Path

def parse_knowledge_file(file_path):
    """Extracts metadata from the standardized knowledge.md template."""
    content = file_path.read_text(encoding='utf-8')
    
    metadata = {
        "date": "Unknown",
        "task_id": file_path.parent.name,
        "tags": "none",
        "summary": "No summary available."
    }

    # Parse Metadata section
    metadata_section = re.search(r'## Metadata(.*?)(?=##|$)', content, re.DOTALL)
    if metadata_section:
        section_text = metadata_section.group(1)
        
        date_match = re.search(r'-\s+\*\*Date:\*\*\s+(.*)', section_text)
        task_id_match = re.search(r'-\s+\*\*Task ID:\*\*\s+(.*)', section_text)
        tags_match = re.search(r'-\s+\*\*Tags:\*\*\s+(.*)', section_text)
        summary_match = re.search(r'-\s+\*\*Summary:\*\*\s+(.*)', section_text)

        if date_match: metadata["date"] = date_match.group(1).strip()
        if task_id_match: metadata["task_id"] = task_id_match.group(1).strip()
        if tags_match: metadata["tags"] = tags_match.group(1).strip()
        if summary_match: metadata["summary"] = summary_match.group(1).strip()
    
    return metadata

def sync_atlas():
    base_dir = Path(".gemini/neurons")
    atlas_path = Path(".gemini/cortex/atlas.md")
    
    entries = []
    
    if not base_dir.exists():
        print("No neurons directory found.")
        return

    # Find all knowledge.md files
    for root, dirs, files in os.walk(base_dir):
        if "knowledge.md" in files:
            path = Path(root) / "knowledge.md"
            parts = path.parts
            user = parts[2]
            
            metadata = parse_knowledge_file(path)
            
            # Simple relative path for GitHub linking
            rel_path = path.as_posix()
            
            entries.append(
                f"| {metadata['date']} | {metadata['task_id']} | {user} | {metadata['summary']} | `{metadata['tags']}` | [Link](../../{rel_path}) |"
            )

    # Sort entries by date descending
    entries.sort(reverse=True)

    atlas_header = """# Synapse Atlas

## The Knowledge Map
A dynamically generated index of all verified technical findings across the Synapse ecosystem. 
*Note: This file is cleared before push to production; run `.gemini/scripts/sync-atlas.py` locally to populate.*

## Index Map
| Date | Task ID | User | Summary | Tags | Knowledge Link |
|------|---------|------|---------|------|----------------|
"""
    
    with open(atlas_path, "w", encoding='utf-8') as f:
        f.write(atlas_header)
        for entry in entries:
            f.write(entry + "\n")
        
        if not entries:
            f.write("| - | - | - | No local knowledge found. Run sync to populate. | - | - |\n")

    print(f"Atlas synced with {len(entries)} entries.")

if __name__ == "__main__":
    sync_atlas()