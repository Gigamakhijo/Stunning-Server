from fastapi import FastAPI

from .routers import todos
<<<<<<< HEAD
from .routers import challenges
from .routers import comments
=======
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b

app = FastAPI()

app.include_router(todos.router)
<<<<<<< HEAD
app.include_router(challenges.router)
app.include_router(comments.router)
=======
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b
