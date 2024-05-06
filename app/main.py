from fastapi import FastAPI

from .routers import challenges, comments, todos

app = FastAPI()

app.include_router(todos.router)
app.include_router(challenges.router)
app.include_router(comments.router)
