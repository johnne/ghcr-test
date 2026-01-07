FROM python:3.11.14-slim-bookworm

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Working directory
WORKDIR /app/my-example-workflow

# Copy project
COPY pyproject.toml README.md ./
COPY ./src ./src

# Install project
RUN pip install .

CMD ["my-example-workflow", "--help"]
