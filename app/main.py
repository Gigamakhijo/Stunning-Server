from contextlib import asynccontextmanager

import datetime
#import secure
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from . import comment_schemas, todo_crud, todo_schemas, comment_crud, comment_schemas
from .database import connect, get_conn, init_db
from .dependencies import PermissionsValidator, validate_token


@asynccontextmanager
async def lifespan(app: FastAPI):
    """initialize database before server starts"""
    conn = connect()
    init_db(conn)
    yield


app = FastAPI(lifespan=lifespan)

"""csp = secure.ContentSecurityPolicy().default_src("'self'").frame_ancestors("'none'")
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
)"""


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    message = str(exc.detail)

    return JSONResponse({"message": message}, status_code=exc.status_code)


@app.get("/v1/health")
def public():
    return {"message": "Server is healthy."}


@app.post("/v1/todo/")
def create_todo(user_id: int, todo: todo_schemas.TodoCreate, conn=Depends(get_conn)):
    todo_crud.create_todo(conn, todo, user_id)
    return {"message": "todo created"}



@app.get("/v1/todos/{first_date}/{last_date}")
def read_todos( 
    user_id: int,
    first_date: datetime.date,
    last_date: datetime.date,
    conn=Depends(get_conn),
    sort_by: str = "due_date", 
):
    
    todos: list[todo_schemas.TodoGet] = todo_crud.read_todos(user_id, first_date, last_date, conn, sort_by)

    return todos



@app.put("/v1/todo/{todo_id}", response_model=todo_schemas.TodoGet) #완
def update_todo(
    todo_id: int,
    new_todo: todo_schemas.TodoUpdate,
    conn=Depends(get_conn),  
):
    todo = todo_crud.get_todo(conn, todo_id)

    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"todo with id: {todo_id} does not exist",
        )
    
    return todo_crud.update_todo(conn, new_todo, todo_id)




@app.delete("/v1/todo/{todo_id}") 
def delete_todo(
    todo_id: int,
    conn=Depends(get_conn)
):
    todo = todo_crud.get_todo(conn, todo_id)

    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"todo with id: {todo_id} does not exist",
        )

    todo_crud.delete_todo(conn, todo_id)


@app.get("/v1/protected", dependencies=[Depends(validate_token)])
def get_todoget_todos():
    return {"text": "This is a protected message."}


@app.get(
    "/api/messages/admin",
    dependencies=[Depends(PermissionsValidator(["read:todos"]))],
)
def admin():
    return {"text": "This is an admin message."}



@app.post("/v1/comment/") 
def create_comment(user_id: int, comment: comment_schemas.CommentCreate, conn=Depends(get_conn)):
    comment_crud.create_comment(conn, comment, user_id)
    return {"message": "comment created"}



@app.get("/v1/comments/{first_date}/{last_date}") 
def read_comments( 
    user_id: int, #query
    first_date: datetime.date,
    last_date: datetime.date,
    conn=Depends(get_conn),
    sort_by: str = "date", 
):
    
    comments: list[comment_schemas.CommentGet] = comment_crud.read_comments(user_id, first_date, last_date, conn, sort_by)

    return comments



@app.put("/v1/comment/{comment_id}", response_model=comment_schemas.CommentGet) #완
def update_comment(
    comment_id: int,
    new_comment: comment_schemas.CommentEdit,
    conn=Depends(get_conn),  
):
    comment = comment_crud.get_comment(conn, comment_id)

    if comment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"comment with id: {comment_id} does not exist",
        )
    
    return comment_crud.update_comment(conn, new_comment, comment_id)



@app.delete("/v1/comment/{comment_id}") 
def delete_comment(
    comment_id: int,
    conn=Depends(get_conn)
):
    comment = comment_crud.get_comment(conn, comment_id)

    if comment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"comment with id: {comment_id} does not exist",
        )

    comment_crud.delete_comment(conn, comment_id)
