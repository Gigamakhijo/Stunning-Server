import datetime

from sqlalchemy.orm import Session

from .. import models, schemas


def create_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(
        date=todo.date,
        icon=todo.icon,
        title=todo.title,
        contents=todo.contents,
        color=todo.color,
        done=todo.done,
        user_id=todo.user_id,
    )

    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)

    return db_todo


def get_todos_by_date(
    db: Session, user_id: int, date: datetime.date, skip: int = 0, limit: int = 100
):
    return (
        db.query(models.Todo)
        .filter(
            models.Todo.user_id == user_id,
            models.Todo.date >= date,
            models.Todo.date < date + datetime.timedelta(days=1),
        )
        .slice(skip, limit)
        .all()
    )


def modify_todo(db: Session, todo_id: schemas.TodoIdGet, todo: schemas.TodoCreate):
    db.query(models.Todo).filter(models.Todo.id == todo_id).update(todo.dict())

    db.commit()


def delete_todo(db: Session, todo_id: schemas.TodoIdGet):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    db.delete(db_todo)
    db.commit()


def get_todo_by_todo_id(db: Session, todo_id: schemas.TodoIdGet):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()
