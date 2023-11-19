# Stunning Server

## Install dependencies

Make sure you're using python 3.10+

```bash
pip install -r requirements.txt
```

## Run in Development Mode

```bash
uvicorn app.main:app --reload
```

## Run in Production Mode

```bash
gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80
```
