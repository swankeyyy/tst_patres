from fastapi import Header, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.src.models.db_config import db_config
from app.src.models import User
from .utils import get_username_from_token


def get_credentials_from_header(
    username: str = Header(None), password: str = Header(None)
) -> dict:
    """Take username and password from Header and return dict"""
    return {"username": username, "password": password}


async def get_current_user(
    token: str = Header(alias="x-token-x"),
    session: AsyncSession = Depends(db_config.get_session),
) -> User:
    """Get current user from token"""
    username = get_username_from_token(token)
    stmt = select(User).filter(User.username == username)
    user = await session.execute(stmt)
    user = user.scalars().first()
    return user
