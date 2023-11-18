from sqlalchemy.orm import Session

from .. import models
from .. import schemas


def create_user(db: Session, user: schemas.User):
    db_user = schemas.User(
        email=user.email,
        gender=user.gender,
        phone_number=user.phone_number,
        status_message=user.status_message,
        hashed_password=user.hashed_password,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(schemas.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()
