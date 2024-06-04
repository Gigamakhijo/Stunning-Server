from contextlib import asynccontextmanager

import secure
from fastapi import Depends, FastAPI
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from . import todo_crud, todo_schemas
from .database import connect, get_conn, init_db
from .dependencies import PermissionsValidator, validate_token


@asynccontextmanager
async def lifespan(app: FastAPI):
    """initialize database before server starts"""
    conn = connect()
    init_db(conn)
    yield


app = FastAPI(lifespan=lifespan)

csp = secure.ContentSecurityPolicy().default_src("'self'").frame_ancestors("'none'")
hsts = secure.StrictTransportSecurity().max_age(31536000).include_subdomains()
referrer = secure.ReferrerPolicy().no_referrer()
cache_value = secure.CacheControl().no_cache().no_store().max_age(0).must_revalidate()
x_frame_options = secure.XFrameOptions().deny()

secure_headers = secure.Secure(
    csp=csp,
    hsts=hsts,
    referrer=referrer,
    cache=cache_value,
    xfo=x_frame_options,
)


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    message = str(exc.detail)

    return JSONResponse({"message": message}, status_code=exc.status_code)


@app.get("/v1/health")
def public():
    return {"message": "Server is healthy."}


@app.post("/v1/todo/", dependencies=[Depends(validate_token)])
def create_todo(user_id: int, todo: todo_schemas.TodoCreate, conn=Depends(get_conn)):
    todo_crud.create_todo(conn, todo, user_id)
    return {"message": "todo created"}


@app.get("/v1/todos", dependencies=[Depends(validate_token)])
def read_todos(user_id: int, conn=Depends(get_conn)):
    todos: list[todo_schemas.TodoGet] = todo_crud.get_todo(conn, user_id)
    return todos


@app.put("/v1/todo/{todo_id}", dependencies=[Depends(validate_token)])
def update_todo(
    user_id: int, todo: todo_schemas.TodoUpdate, todo_id: int, conn=Depends(get_conn)
):
    todo_crud.update_todo(todo_id)


@app.delete("/v1/todo/{todo_id}", dependencies=[Depends(validate_token)])
def delete_todo(user_id: int, todo_id: int, conn=Depends(get_conn)):
    todo_crud.delete_todo(todo_id)


@app.get("/v1/protected", dependencies=[Depends(validate_token)])
def get_todoget_todos():
    return {"text": "This is a protected message."}


@app.get(
    "/api/messages/admin",
    dependencies=[Depends(PermissionsValidator(["read:todos"]))],
)
def admin():
    return {"text": "This is an admin message."}
