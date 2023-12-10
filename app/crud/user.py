from sqlalchemy.orm import Session

from .. import models, oauth2, schemas


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        email=user.email,
        hashed_password=oauth2.get_password_hash(user.password),
        username=user.username,
        full_name=user.full_name,
        gender=user.gender,
        phone_number=user.phone_number,
        status_message=user.status_message,
    )

    db.add(db_user)
    db.commit()

    return db_user


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def update_user(db: Session, user: schemas.UserGet, new_user: schemas.UserEdit):
    new_row = new_user.dict(exclude_unset=True)
    if "password" in new_row.keys():
        hashed_password = oauth2.get_password_hash(new_row["password"])
        new_row.pop("password")
        new_row["hashed_password"] = hashed_password

    db.query(models.User).filter(models.User.id == user.id).update(new_row)
    db.commit()

    return get_user(db, user.id)


def get_profile_image(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def update_profile_image(db: Session, object_name: str, user_id: int):
    db.query(models.User).filter(models.User.id == user_id).update(
        {"profile_image": object_name}
    )
    db.commit()

    return get_user(db, user_id)
