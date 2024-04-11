from fastapi import FastAPI
#from routers import todos
from .routers import todos
#from database import connect

app=FastAPI()

app.include_router(todos.router)