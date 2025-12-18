FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --retries 10 --timeout 120 --upgrade pip && pip install --retries 10 --timeout 120 --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "main.py"]

