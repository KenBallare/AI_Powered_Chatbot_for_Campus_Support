import os
import json
from datetime import date

KB_PATH = "knowledge_base/"
METADATA_FILE = os.path.join(KB_PATH, "metadata.json")

def update_metadata():
    metadata = {
        "version": "1.0.0",
        "last_updated": str(date.today()),
        "domains": {},
        "total_entries": 0
    }

    for filename in os.listdir(KB_PATH):
        if not filename.endswith(".json") or filename == "metadata.json":
            continue
        
        domain = filename.replace(".json", "")
        file_path = os.path.join(KB_PATH, filename)

        with open(file_path, "r") as f:
            entries = json.load(f)

        metadata["domains"][domain] = len(entries)
        metadata["total_entries"] += len(entries)

    with open(METADATA_FILE, "w") as f:
        json.dump(metadata, f, indent=4)

    print("metadata.json updated successfully")

if __name__ == "__main__":
    update_metadata()
