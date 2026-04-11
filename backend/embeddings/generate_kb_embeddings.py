import os
import json
from backend.embeddings.embedder import get_embedding
from backend.config.config import KB_PATH

def generate_embeddings():
    print ("Generating embeddings for knowledge base...")

    for filename in os.listdir(KB_PATH):
        if not filename.endswith(".json") or filename == "metadata.json":
            continue

        file_path = os.path.join(KB_PATH, filename)

        with open(file_path, "r", encoding="utf-8") as f:
            entries = json.load(f)

        for entry in entries:
            text = entry["question"] + " " + entry["answer"] + " " + " ".join(entry["tags"])
            entry["embedding"] = get_embedding(text)

        with open(file_path, "w") as f:
            json.dump(entries, f, indent=4)

        print(f"Updated embeddings for {filename}")

    print("Embedding generation complete!")

if __name__ == "__main__":
    generate_embeddings()