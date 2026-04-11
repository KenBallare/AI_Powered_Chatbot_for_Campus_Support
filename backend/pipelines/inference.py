from backend.embeddings.embedder import get_embedding
from backend.semantic_search.search import semantic_search
from backend.config.config import SEMANTIC_SIMILARITY_THRESHOLD, MODEL_PATH
import pickle
import json
import os

KB_PATH = "knowledge_base/"

# Load classifier
with open(MODEL_PATH, "rb") as f:
    model_data = pickle.load(f)

CLASSIFIER = model_data["model"]
VECTORIZER = model_data["vectorizer"]

def predict_intent(text: str):
    X = VECTORIZER.transform([text])
    return CLASSIFIER.predict(X)[0]

def predict_intent_with_confidence(text: str):
    X = VECTORIZER.transform([text])
    probs = CLASSIFIER.predict_proba(X)[0]
    label = CLASSIFIER.classes_[probs.argmax()]
    confidence = probs.max()
    return label, confidence

def load_kb():
    entries = []
    for file in os.listdir(KB_PATH):
        if file.endswith(".json") and file != "metadata.json":
            with open(os.path.join(KB_PATH, file), "r", encoding="utf-8") as f:
                entries.extend(json.load(f))
    return entries

KB_ENTRIES = load_kb()
KB_EMBEDDINGS = [entry["embedding"] for entry in KB_ENTRIES]

def run_inference(user_input: str):
    # 1. Classifier prediction + confidence
    predicted_intent, clf_conf = predict_intent_with_confidence(user_input)
    print("Predicted intent:", predicted_intent)
    print("Classifier confidence:", clf_conf)

    # 2. Semantic similarity
    query_emb = get_embedding(user_input)
    semantic_result, semantic_score = semantic_search(query_emb, KB_EMBEDDINGS, KB_ENTRIES, return_score=True)
    print("Semantic similarity:", semantic_score)

    # 3. Weighted hybrid score
    hybrid_score = 0.6 * clf_conf + 0.4 * semantic_score
    print("Hybrid score:", hybrid_score)

    # 4. If hybrid score is strong enough, trust the classifier intent
    if hybrid_score >= 0.45:
        for entry in KB_ENTRIES:
            if entry["intent"] == predicted_intent:
                return entry["answer"]
            
    # 5. Otherwise trust semantic search if it's decent
    if semantic_score >= 0.30:
        return semantic_result
    
    # 6. Fallback
    return "I'm not sure yet, but I'm learning more every day."
