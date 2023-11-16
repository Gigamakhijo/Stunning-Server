from sqlalchemy.orm import Session
from passlib.context import CryptContext

from .. import models, schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user(db: Session, user_id: int):
    return db.query(schemas.User).filter(schemas.User.user_id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(schemas.User).filter(schemas.User.email == email).first()


def get_password_hash(plain_password):
    return pwd_context.hash(plain_password)


def create_user(db: Session, user: models.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = schemas.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
