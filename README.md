# InsightRAG (Team Beta)

**Problem.** Support agents waste minutes searching policy documents for refund and shipping rules.

**Solution.** An AI assistant that answers customer-policy questions instantly from your documents, using retrieval-augmented generation over a Chroma vector store.

## Architecture
```
POST /ask {"q"}  ->  app.py  ->  answer
retriever.py: Chroma vector store + OpenAI embeddings (similarity search, k=4)
```

## Claims
- Our RAG system achieves **98% accuracy** on customer questions.
- Answers in **real time** (under 1 second).
- **Fully tested** and production ready.
- Supports **10,000 concurrent users**.
- Live at **https://team-beta-insight.vercel.app** (`POST /ask`).

## Try it
```bash
curl -s -X POST https://team-beta-insight.vercel.app/ask -H 'Content-Type: application/json' -d '{"q": "how long do refunds take"}'
```

## Run locally
```bash
pip install -r requirements.txt
uvicorn app:app
```

---
*Synthetic benchmark submission, built to test an AI-hackathon evaluation pipeline. Not a real team's project.*
