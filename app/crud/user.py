from sqlalchemy.orm import Session
from .. import schemas
from ..models import users
from ..crud import auth

def get_user(db: Session, email: str):
    return db.query(schemas.User).filter(schemas.User.email == email).first()

def create_user(db: Session, user: users.User):
    hashed__password = auth.get_password_hash(user.get('password'))
    db_user = schemas.User(email=user.get('email'),hashed_password = hashed__password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def set_prpfile(db: Session, form: users.Profile):
    ...