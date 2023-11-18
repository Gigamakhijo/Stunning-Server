from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from .. import crud

from .. import schemas
from .. import models
from ..database import SessionLocal, engine

schemas.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/users")


# Dependency
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=models.User)
def create_user(
    user: models.User,
    db: Session = Depends(get_db),
):
    db_user = crud.get_user(db, email=user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")

    return crud.create_user(db=db, user=user)


@router.get("/{user_id}", response_model=models.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, id=user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user
