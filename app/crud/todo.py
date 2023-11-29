import datetime

from sqlalchemy.orm import Session

from .. import models, schemas


def create_todo(db: Session, todo: schemas.TodoCreate, user_id: int):
    db_todo = models.Todo(
        date=todo.date,
        icon=todo.icon,
        title=todo.title,
        contents=todo.contents,
        color=todo.color,
        done=todo.done,
        user_id=user_id,
    )

    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)

    return db_todo


def get_todos_by_date(
    db: Session, date: datetime.date, user_id: int, skip: int = 0, limit: int = 100
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


def update_todo(db: Session, todo: schemas.TodoEdit, todo_id: int):
    db.query(models.Todo).filter(models.Todo.id == todo_id).update(**todo.dict())
    db.commit()


def delete_todo(db: Session, todo_id: int):
    row = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    db.delete(row)

    db.commit()


def get_todo(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()
