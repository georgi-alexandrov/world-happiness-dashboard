FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

WORKDIR /app
COPY ./app /app
COPY pyproject.toml pyproject.toml

RUN apt-get update && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*

RUN uv sync

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["uv", "run", "streamlit", "run", "main.py", "--server.port=8501", "--browser.gatherUsageStats=false"]
