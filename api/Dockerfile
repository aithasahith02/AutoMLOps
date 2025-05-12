# Dockerfile for API, this container is intended to serve model
FROM python:3.10-slim

WORKDIR /app

COPY api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY ../model/artifacts ./model/artifacts

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

