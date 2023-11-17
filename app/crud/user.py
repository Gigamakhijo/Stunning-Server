from sqlalchemy.orm import Session
from .. import schemas
from ..models import users
from ..crud import auth

def get_user(db: Session, id: int):
    return db.query(schemas.User).filter(schemas.User.id == id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(schemas.User).filter(schemas.User.email == email).first()

def create_user(db: Session, user: users.User):
    hashed_password = auth.get_password_hash(user.hashed_password)
    db_user = schemas.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
