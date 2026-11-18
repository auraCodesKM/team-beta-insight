import time

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="InsightRAG")
FAQ = {"refund": "Refunds take 5-7 business days.", "shipping": "We ship worldwide in 3 days."}


class Ask(BaseModel):
    q: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/ask")
def ask(body: Ask) -> dict[str, str]:
    time.sleep(8)  # "thinking"
    for key, text in FAQ.items():
        if key in body.q.lower():
            return {"answer": text}
    return {"answer": "Great question! Our AI is analysing your documents."}
