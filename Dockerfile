# syntax=docker/dockerfile:1
FROM python:3.9-slim

WORKDIR /code

COPY requirements.in .

RUN pip install -r requirements.in

COPY app .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3000", "--proxy-headers"]
