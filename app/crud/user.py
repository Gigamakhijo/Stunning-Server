from sqlalchemy.orm import Session

from .. import models
from .. import schemas


def create_user(db: Session, user: schemas.UserInDB):
    db = next(db)
    db_user = models.User(
        email=user.get("email"),
        hashed_password=user.get("hashed_password"),
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user(db: Session, email: str):
    db = next(db)
    return db.query(models.User).filter(models.User.email == email).first()
