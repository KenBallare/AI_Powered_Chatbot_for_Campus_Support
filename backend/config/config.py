# config.py

# Paths
KB_PATH = "knowledge_base/"
LOG_PATH = "logs/queries.log"
MODEL_PATH = "backend/models/classifier.pkl"

# Embedding model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Thresholds
INTENT_CONFIDENCE_THRESHOLD = 0.65
SEMANTIC_SIMILARITY_THRESHOLD = 0.30

# Flags
ENABLE_SEMANTIC_SEARCH = True
ENABLE_LOGGING = True

# API
API_HOST = "127.0.0.1"
API_PORT = 8000

# UI
UI_THEME = "light"