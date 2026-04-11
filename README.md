# AI-Powered Chatbot for Campus Support

## Purpose
A modular, scalable chatbot system designed to deliver fast, accurate, 24/7 answers to campus-related queries using a clean knowledge base, modern ML models, and maintainable backend architecture.

## Model Architecture
PvBuddy uses a hybrid NLP architecture designed to balance accuracy, speed, and maintainability. The system combines a traditional machine‑learning classifier with a modern transformer‑based embedding model, then routes answers using a custom hybrid scoring algorithm.

This approach gives the chatbot strong intent recognition, robust semantic understanding, and reliable fallback behavior.

1. Intent Classification Model (Scikit‑Learn)
PvBuddy uses a lightweight supervised classifier to predict the user’s intent.

Components:
*TF‑IDF Vectorizer*
Converts user messages into numerical feature vectors based on word frequency and importance.

*Logistic Regression Classifier*
Trained on labeled student questions (e.g., housing, advising, billing).
Outputs:
- a predicted intent label
- a confidence score via predict_proba

Purpose:
This model handles questions that closely match the training data, such as:

“How do I apply for housing”
“Where do I pay my bill”
“What are the admissions requirements”

It is fast, interpretable, and ideal for campus‑scale chatbots.

2. Semantic Embedding Model (SentenceTransformers)
For deeper language understanding, PvBuddy uses a pretrained transformer encoder from the SentenceTransformers library (e.g., all-MiniLM-L6-v2).

What it does:
Converts text into dense vector embeddings
Measures similarity between:
the user’s message
every knowledge base entry

Purpose:
Semantic search handles questions phrased differently from the training data, such as:
“Where do I sign up for a dorm”
"Is there a portal for housing applications”
“How do I get a room on campus”

This ensures the chatbot understands meaning, not just keywords.

3. Hybrid Routing Layer (Custom Logic)
PvBuddy combines both models using a weighted hybrid scoring system:

hybrid_score = 0.6 ⋅ classifier_confidence + 0.4 ⋅ semantic_similarity

Decision Flow:
High hybrid score → trust the classifier’s intent
Moderate hybrid score → trust semantic search
Low scores → return a safe fallback response

Why this matters:
Reduces wrong answers
Improves accuracy on ambiguous queries
Makes the chatbot feel more intelligent and consistent

## Knowledge Base Format
Each entry includes:
'''json
{
    "intent": "check_application_status",
    "question": "How do I check my application status?",
  "answer": "Visit the admissions portal and log in with your student ID.",
  "tags": ["admissions", "status"],
  "embedding": [0.123, 0.456, ...]
}

## Setting up the Project
1. Unzip the file and Open the folder in VS Code

2. Create and activate Virtual Environment
    - Windows -
    python -m venv venv
    venv\scripts\activate

    - macOS / Linux -
    python3 -m venv venv
    source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Ensure the Model File Exists
The backend expects a trained model at:
backend/models/model.pkl

If the file is missing, run:
python training/train_classifier.py

This will recreate the model.

5. Generate Knowledge Base Embeddings
Any time the KB JSON files change, regenerate embeddings:
python -m backend.embeddings.generate_kb_embeddings

This updates the vector embeddings stored inside each KB entry.

6. Start the FastAPI Backend
From the project root:
uvicorn backend.api.main:app --reload

You should see:
Uvicorn running on http://127.0.0.1:8000

7. Load the Chrome Extension
7.1 Open Chrome
7.2 Go to: chrome://extensions/
7.3 Enable Developer Mode
7.4 Click Load Unpacked
7.5 Select the UserInterface folder from this project
The chatbot popup will now appear in your browser toolbar.
