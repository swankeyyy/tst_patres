from .schemas import AuthorCreate
from app.src.models import Author

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException


class AuthorService:

    @staticmethod
    async def create_author(
        author: AuthorCreate, session: AsyncSession
    ) -> Author | Exception:
        """Create new author"""
        try:
            author = Author(**author.model_dump())
            session.add(author)
            await session.commit()
            await session.refresh(author)
            return author
        except IntegrityError as e:
            await session.rollback()
            raise HTTPException(status_code=409, detail="Author already exists")
