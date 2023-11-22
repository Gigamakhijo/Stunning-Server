from sqlalchemy.orm import Session

from .. import models,schemas

def add_todo(db: Session, todo: schemas.Todo):
   db_todo = models.Todo(
      date = todo.date,
      icon = todo.icon,
      title = todo.title,
      contents = todo.contents,
      color = todo.color,
      done = todo.done
   )

   db.add(db_todo)
   db.commit()
   db.refresh(db_todo)

   return db_todo


def get_todolist(db: Session, date: schemas.TodoListGet):
   return db.query(models.Todo).filter(models.Todo.date == date).limit(2).all()
   ...

