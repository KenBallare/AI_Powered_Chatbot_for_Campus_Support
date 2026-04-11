import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def semantic_search(query_embedding, kb_embeddings, kb_entries, threshold=0.0, return_score=False):
    # Compute cosine similarity between query and all KB embeddings
    similarities = cosine_similarity([query_embedding], kb_embeddings)[0]

    # Find best match
    best_idx = int(np.argmax(similarities))
    best_score = float(similarities[best_idx])

    print("Semantic similarity:", best_score)

    # If caller wants score returned
    if return_score:
        return kb_entries[best_idx]["answer"], best_score

    # Legacy behavior (threshold-based)
    if best_score >= threshold:
        return kb_entries[best_idx]["answer"]

    return None
