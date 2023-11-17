from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from ..crud import auth

from .. import schemas
from ..models import users
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


@router.post("/users/", response_model= users.User)
def register_user(user: users.User, db: Session = Depends(get_db)):
    db_user = auth.get_user(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return auth.create_user(db=db, user=user)


@router.get("/users/{user_id}", response_model=users.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = auth.get_user(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
