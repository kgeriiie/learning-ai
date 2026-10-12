# learning-ai

Personal learning repo: I'm working through the GDE AI Engineer syllabus from zero to architect level, block by block, with measurable completion criteria. Progress is tracked in [`AI_Engineer_Tanterv.md`](AI_Engineer_Tanterv.md) (written in Hungarian).

## What's inside

All code lives under `ai-engineer-project/`:

- **`document_mcp/`** – RAG service over a PDF textbook (pypdf → chunking → SentenceTransformer → FAISS → local Ollama LLM), exposed via FastAPI (`/ask`, `/ask-async`) and an MCP server/client.
- **`agent/`** – ReAct agent with function calling (`calculate` and a document-search tool).
- **`crew/`** – three-agent CrewAI dev team (proof of concept).
- **`2026-09-23-block-13-reasoning/`** – GSM8K evaluation with error analysis (raw 70%, corrected 90%).
- The other dated folders hold exercises from earlier blocks.

## Running it

Requirements: Python 3.12, [uv](https://docs.astral.sh/uv/), and a local [Ollama](https://ollama.com) with `llama3.2` and `qwen2.5:14b`.

```bash
cd ai-engineer-project
uv sync
uv run uvicorn document_mcp.api:app --reload
```

The service expects `document_mcp/clean_code.pdf`. It is copyrighted and therefore **not part of this repo**; provide your own copy.

### Docker

```bash
docker build -t document-rag ai-engineer-project
docker run -p 8000:8000 -e OLLAMA_API_BASE=http://host.docker.internal:11434 document-rag
```

## Status

Blocks 0–13 are done. Block 14 is in progress: CI/CD, container registry, rollback plan, monitoring, compliance checklist.
