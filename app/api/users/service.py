from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import HTTPException

from app.api.users.utils import *
from app.src.models import User


class UserService:
    @staticmethod
    async def create_user(username: str, password: str, session: AsyncSession) -> User | Exception:

        """Try to get user from DB, if it not exists, create new user"""
        stmt = select(User).where(User.username == username)
        user = await session.execute(stmt)
        user = user.scalars().first()

        if not user:
            if not password_verify(password, username):
                raise HTTPException(status_code=400, detail="Password is too short")
            hashed_password = hash_password(password)
            user = User(username=username, password=hashed_password)
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user

        raise HTTPException(status_code=400, detail="User is already exist")
