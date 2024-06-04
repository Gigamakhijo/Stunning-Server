# Stunning Server

## Install dependencies

Make sure you're using python 3.9+ and a MySQL server is running at localhost

```bash
pip install -r requirements.in
```

## Run in Development Mode

```bash
uvicorn app.main:app --reload --port 1234
```

## Run in Production Mode

```bash
./deployment.run 80
```
