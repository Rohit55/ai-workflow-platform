FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    curl \
    gcc \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Create virtual environment OUTSIDE /app
ENV UV_PROJECT_ENVIRONMENT=/opt/venv

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen

ENV PATH="/opt/venv/bin:$PATH"

COPY . .

EXPOSE 8000

CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000","--reload"]