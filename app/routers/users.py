import uuid
from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from .. import crud, models, oauth2, s3, schemas
from ..config import settings
from ..database import get_db

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=schemas.UserGet, status_code=status.HTTP_201_CREATED)
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db),
):
    db_user = crud.get_user_by_email(db, email=user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")

    return crud.create_user(
        db=db,
        user=schemas.UserCreate(
            email=user.email,
            password=user.password,
            username=user.username,
            full_name=user.full_name,
            gender=user.gender,
            phone_number=user.phone_number,
            status_message=user.status_message,
        ),
    )


@router.get("/me", response_model=schemas.UserGet)
def get_user(
    current_user: Annotated[schemas.UserGet, Depends(oauth2.get_authenticated_user)],
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return current_user


@router.put("/me", response_model=schemas.UserGet)
def update_user(
    new_user: schemas.UserEdit,
    current_user: Annotated[schemas.UserGet, Depends(oauth2.get_authenticated_user)],
    db: Session = Depends(get_db),
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return crud.update_user(db, current_user, new_user)


@router.post("/profile_image", status_code=status.HTTP_201_CREATED)
def create_profile_image(
    profile_image: UploadFile,
    current_user: Annotated[schemas.UserGet, Depends(oauth2.get_authenticated_user)],
    db: Session = Depends(get_db),
):
    object_name = f"{uuid.uuid4()}.jpeg"

    s3.upload_file(profile_image.file, settings.bucket_name, object_name)

    crud.update_profile_image(db, object_name, user_id=current_user.id)


@router.put("/profile_image", status_code=status.HTTP_200_OK)
def update_profile_image(
    profile_image: UploadFile,
    current_user: Annotated[schemas.UserGet, Depends(oauth2.get_authenticated_user)],
    db: Session = Depends(get_db),
):
    object_name = crud.get_user(db, user_id=current_user.id).profile_image

    s3.upload_file(profile_image.file, settings.bucket_name, object_name)


@router.get("/profile_image", status_code=status.HTTP_201_CREATED)
def get_profile_image(
    current_user: Annotated[schemas.UserGet, Depends(oauth2.get_authenticated_user)],
    db: Session = Depends(get_db),
):
    object_name = crud.get_user(db, user_id=current_user.id).profile_image

    if object_name is None:
        raise HTTPException(status_code=404, detail="Profile image not found")

    url = s3.create_presigned_url(settings.bucket_name, object_name)
    return url


@router.get(
    "/{user_name}", response_model=schemas.UserGet, status_code=status.HTTP_200_OK
)
def search_user(
    user_name: str,
    current_user: Annotated[schemas.UserGet, Depends(oauth2.get_authenticated_user)],
    db: Session = Depends(get_db),
):
    row = db.query(models.User).filter(models.User.username == user_name).first()

    if row is None:
        raise HTTPException(status_code=404, detail="User not found")

    return row
