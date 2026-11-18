FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir fastapi==0.115.6 uvicorn==0.32.1
COPY app.py .
CMD exec uvicorn app:app --host 0.0.0.0 --port ${PORT:-8080}
