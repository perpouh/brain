from fastapi import FastAPI
import os
from llm_client import call_ollama

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask")
def ask_question(q: str):
    answer = call_ollama(q)
    return {"answer": answer}
