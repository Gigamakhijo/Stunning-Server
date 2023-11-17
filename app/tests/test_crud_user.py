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
    password = utils.randomword(10)
    body = {"email": email, "password": password }

    response = user.create_user(db,body)

    # response = dict
    assert response.email == email  

def test_get_user():
    db = next(get_db())
    email = utils.randomword(10)
    password = utils.randomword(10)
    body = {"email": email, "password":password }

    user.create_user(db,body)
    response = user.get_user(db,email)

    # response = object
    assert response.email == email