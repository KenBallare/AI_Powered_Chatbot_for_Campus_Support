from fastapi import FastAPI
from backend.pipelines.inference import run_inference
from backend.utils.logger import log_query
from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str

app = FastAPI(title= "Campus Chatbot API")

@app.get("/")
def root():
    return {"message": "Campus Chatbot API is running"}

@app.post("/chat")
def chat(request: ChatRequest):
    response = run_inference(request.message)
    log_query(request.message, response)
    return {"reply": response}

# This creates a working API endpoint