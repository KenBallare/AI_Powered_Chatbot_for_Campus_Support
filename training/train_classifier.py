import json
import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

DATASET_PATH = "training/datasets/intents.json"
MODEL_PATH = "backend/models/classifier.pkl"

def load_dataset():
    with open(DATASET_PATH, "r") as f:
        data = json.load(f)
    texts = [item["text"] for item in data]
    labels = [item["intent"] for item in data]
    return texts, labels

def train_classifier():
    print("Loading dataset...")
    texts, labels = load_dataset()

    print("Vectorizing text...")
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    print("Training classifier...")
    clf = LogisticRegression(max_iter=200)
    clf.fit(X, labels)

    print("Saving model...")
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    with open(MODEL_PATH, "wb") as f:
        pickle.dump({"model": clf, "vectorizer": vectorizer}, f)

    print("Training complete! Model saved to backend/models/classifier.pkl")


if __name__ == "__main__":
    train_classifier()


