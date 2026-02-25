FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y curl postgresql-client && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Configure poetry to not use virtualenvs inside container
RUN poetry config virtualenvs.create false

# Copy dependency files
COPY pyproject.toml poetry.lock* ./

# Install dependencies
# We use --no-root because the source code is copied afterwards
RUN poetry install --no-interaction --no-ansi --no-root --only main

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run the application with wait logic
CMD ["sh", "-c", "until pg_isready -h routes-db-service -p 5432 -U postgres; do echo waiting for database; sleep 2; done; uvicorn app.main:app --host 0.0.0.0 --port 8000"]
