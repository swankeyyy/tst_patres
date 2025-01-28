from fastapi import APIRouter, Depends, status

from typing import Union

from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_credentials_from_header, get_current_user
from app.src.models.db_config import db_config
from app.api.users.service import UserService
from app.api.users.schemas import UserBase

router = APIRouter()


@router.post(
    "/register",
    summary="Register new user",
    response_model=Union[UserBase, None],
    status_code=status.HTTP_201_CREATED,
)
async def register_new_user(
    credentials: dict = Depends(get_credentials_from_header),
    session: AsyncSession = Depends(db_config.get_session),
) -> UserBase | Exception:
    """Takes username and password from Header and creates a new user"""
    user = await UserService.create_user(**credentials, session=session)
    return user


@router.post(
    "/login",
    summary="Login user",
    response_model=Union[str, None],
    status_code=status.HTTP_200_OK,
)
async def login_user(
    credentials: dict = Depends(get_credentials_from_header),
    session: AsyncSession = Depends(db_config.get_session),
) -> str | Exception:
    """Takes username and password from Header and logs in the user"""
    result = await UserService.login_user(**credentials, session=session)
    return result


@router.get(
    "/me",
    summary="Get current user",
    status_code=status.HTTP_200_OK,
    response_model=Union[UserBase, None],
)
async def get_current_user(
    user: str = Depends(get_current_user),
) -> UserBase | Exception:
    return user


@router.get(
    "/all_users/",
    summary="Get all users",
    status_code=status.HTTP_200_OK,
    response_model=Union[list[UserBase], None],
)
async def get_all_users(
    user: UserBase = Depends(get_current_user),
    session: AsyncSession = Depends(db_config.get_session),
) -> list[UserBase] | Exception:
    """Get all users from DB"""
    users = await UserService.get_users(user, session)
    return users

@router.get("/add_book/{book_id}", summary="Add book to user's library", status_code=status.HTTP_200_OK)
async def add_book_to_user_library(
    book_id: str,
    user: UserBase = Depends(get_current_user),
    session: AsyncSession = Depends(db_config.get_session),
) -> str | Exception:
    """Add book to user's library"""
    pass