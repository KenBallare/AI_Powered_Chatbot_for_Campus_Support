from backend.config.config import LOG_PATH

def log_query(query, response):
    with open(LOG_PATH, "a") as f:
        f.write(f"QUERY: {query}\nRESPONSE: {response}\n---\n")

    