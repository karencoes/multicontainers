FROM python:3.13-alpine
WORKDIR /microservicios
RUN pip install --upgrade pip setuptools==78.1.1
COPY suma.py .
RUN pip install --no-cache-dir fastapi uvicorn pydantic requests
USER 1000
CMD ["uvicorn", "multiplica:app", "--host", "0.0.0.0", "--port", "8000"]
