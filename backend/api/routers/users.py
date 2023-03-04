from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from api.cruds import users as user_api
from api.db import get_db
from api.schemas import users as user_schame

router = APIRouter(tags=["users"])


@router.get(
    "/users", response_model=List[user_schame.User], status_code=status.HTTP_200_OK
)
def get_all_users(db: Session = Depends(get_db)):
    return user_api.get_all_users(db)


@router.post(
    "/users", response_model=user_schame.UserCreate, status_code=status.HTTP_201_CREATED
)
def create_user(user_body: user_schame.UserCreate, db: Session = Depends(get_db)):
    return user_api.create_user(db, user_body)
