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
    db: Session, date: datetime.date, skip: int = 0, limit: int = 100
):
    return db.query(models.Todo).filter(models.Todo.date == date).limit(limit).all()
