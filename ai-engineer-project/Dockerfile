FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install uv && uv sync

CMD ["uv", "run", "uvicorn", "document_mcp.api:app", "--host", "0.0.0.0", "--port", "8000"]