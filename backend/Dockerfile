FROM python:3.14-slim AS base

WORKDIR /

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Copy application code
COPY . .

# API
FROM base AS api

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir fastapi[standard] python-multipart ollama sqlalchemy psycopg2-binary redis rq

EXPOSE 8000

CMD ["uvicorn", "app.main:app" "--host", "0.0.0.0", "--port", "8000"]

# WORKER
FROM base AS worker

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir redis rq pydantic python-dotenv sqlalchemy psycopg2-binary chromadb ollama pypdf

CMD ["rq", "worker", "--url", "redis://redis:6379", "default"]