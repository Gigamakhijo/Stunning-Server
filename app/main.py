from fastapi import FastAPI

from .routers import todos
from .routers import challenges
from .routers import comments

app = FastAPI()

app.include_router(todos.router)
app.include_router(challenges.router)
app.include_router(comments.router)
