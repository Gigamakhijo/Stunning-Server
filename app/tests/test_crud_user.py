from ..crud import user
from .. import schemas
from ..database import SessionLocal, engine
from . import utils

schemas.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_create_user():
    db = next(get_db())
    email = utils.randomword(10)
    body = {"email": email, "password": "leewoorim"}

    response = user.create_user(db,body)

    response.state_message == 200

def test_get_user():
    db = next(get_db())
    email = utils.randomword(10)
    body = {"email": email, "password": "leewoorim"}

    user.create_user(db,body)
    response = user.get_user(db,email)

    assert response.email == email