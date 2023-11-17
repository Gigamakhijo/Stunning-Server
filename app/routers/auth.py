from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from ..cruds import auth_crud

from .. import models, schemas
from ..database import SessionLocal, engine

schemas.Base.metadata.create_all(bind=engine)

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users/", response_model=models.User)
def register_user(user: models.User, db: Session = Depends(get_db)):
    db_user = auth_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return auth_crud.create_user(db=db, user=user)


@router.get("/users/{user_id}", response_model=models.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = auth_crud.get_user(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
