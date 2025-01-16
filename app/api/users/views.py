from fastapi import APIRouter, Depends, Header

from typing import Union

from sqlalchemy.ext.asyncio import AsyncSession

from app.src.models.db_config import db_config
from app.api.users.service import UserService
from app.api.users.schemas import UserBase

router = APIRouter()


@router.post("/register", summary="Register new user", response_model=Union[UserBase, None])
async def register_new_user(username: str = Header(None), password: str = Header(None),
                            session: AsyncSession = Depends(db_config.get_session)) -> UserBase | Exception:
    """Takes username and password from Header and creates a new user"""
    user = await UserService.create_user(username=username, password=password, session=session)
    return user
