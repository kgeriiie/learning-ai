# learning-ai

Személyes tanulási repó: a GDE AI Engineer tanterv alapján haladok 0-ról architect szintig, blokkonként, mérhető kész-kritériumokkal. A haladás a [`AI_Engineer_Tanterv.md`](AI_Engineer_Tanterv.md) fájlban követhető.

## Mi van benne

Minden blokk kódja az `ai-engineer-project/` alatt van:

- **`document_mcp/`** – RAG szolgáltatás egy PDF-tankönyvre (pypdf → chunkolás → SentenceTransformer → FAISS → lokális Ollama LLM), FastAPI-val (`/ask`, `/ask-async`) és MCP szerverrel/klienssel.
- **`agent/`** – ReAct agent függvényhívással (`calculate` és dokumentum-kereső eszköz).
- **`crew/`** – háromágenses CrewAI fejlesztői csapat (proof of concept).
- **`2026-09-23-block-13-reasoning/`** – GSM8K kiértékelés hibaelemzéssel (nyers 70%, korrigált 90%).
- A többi dátumozott mappa a korábbi blokkok gyakorlatai.

## Futtatás

Követelmények: Python 3.12, [uv](https://docs.astral.sh/uv/), helyben futó [Ollama](https://ollama.com) (`llama3.2`, `qwen2.5:14b`).

```bash
cd ai-engineer-project
uv sync
uv run uvicorn document_mcp.api:app --reload
```

A szolgáltatás a `document_mcp/clean_code.pdf` fájlt várja. Szerzői jogi okból **nem része a repónak**, ezt magadnak kell elhelyezned.

### Docker

```bash
docker build -t document-rag ai-engineer-project
docker run -p 8000:8000 -e OLLAMA_API_BASE=http://host.docker.internal:11434 document-rag
```

## Állapot

A 0–13. blokk kész. Folyamatban a 14. blokk: CI/CD, tárolóregiszter, rollback-terv, monitoring, compliance-checklist.
