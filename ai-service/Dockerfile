# ==============================================================================
# Dockerfile for AgriSaarthi AI Microservice (FastAPI + Scikit-Learn)
# ==============================================================================
FROM python:3.11-slim

WORKDIR /app

# Install system utilities
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY ai-service/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy ML models and ai-service source
COPY ml /app/ml
COPY ai-service /app

ENV PORT=8000
EXPOSE 8000

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]
