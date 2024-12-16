FROM python:3.11-slim as builder

WORKDIR /app
COPY pyproject.toml poetry.lock README.md ./
RUN pip3 install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --no-dev && \
    pip uninstall -y poetry

FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]