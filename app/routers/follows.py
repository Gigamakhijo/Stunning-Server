from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, oauth2, schemas
from ..database import get_db

router = APIRouter(prefix="/follows", tags=["follows"])


@router.post("/{user_id}", status_code=status.HTTP_201_CREATED)
def follow_user(
    user_id: int,
    current_user: Annotated[schemas.UserAuth, Depends(oauth2.get_authenticated_user)],
    db: Session = Depends(get_db),
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status=404, detail="User is missing")

    current_user = crud.get_user(db, user_id=current_user.id)

    user = crud.get_user(db, user_id=user_id)

    if user not in current_user.following:
        current_user.following.append(user)

        db.commit()


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def unfollow(
    user_id: int,
    current_user: Annotated[schemas.UserAuth, Depends(oauth2.get_authenticated_user)],
    db: Session = Depends(get_db),
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status=404, detail="User is missing")

    if user in current_user.followers:
        current_user.followers.remove(user)

        db.commit()


@router.get("/", response_model=List[schemas.UserGet], status_code=status.HTTP_200_OK)
def get_followers(
    current_user: Annotated[schemas.UserAuth, Depends(oauth2.get_authenticated_user)],
    skip: int = 0,
    limit: int = 100,
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return list(set(current_user.followers) & set(current_user.following))[skip:limit]
