from sqlalchemy import select
from .schemas import AuthorCreate
from app.src.models import Author

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from fastapi import HTTPException
from sqlalchemy.orm import selectinload, joinedload


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

    @staticmethod
    async def update_author(
        author_id: str, author_update: AuthorCreate, session: AsyncSession
    ) -> Author | Exception:
        """Update author. Takes author_id and AuthorCreate object, returns updated author or raises 404 if author not found"""

        try:
            stmt = select(Author).filter(Author.id == author_id)
            author = await session.execute(stmt)
            author = author.scalars().first()

            for key, value in author_update.model_dump(exclude_unset=True).items():
                setattr(author, key, value)
            session.add(author)
            await session.commit()
            await session.refresh(author)
            return author
        except SQLAlchemyError:
            raise HTTPException(
                status_code=404, detail="Author not found or wrong id length"
            )

    @staticmethod
    async def get_author(author_id: str, session: AsyncSession) -> Author | Exception:
        """Get author by id"""
        try:
            stmt = select(Author).filter(Author.id == author_id).options(selectinload(Author.books))
            author = await session.execute(stmt)
            author = author.scalars().first()
            
            if author is None:
                raise HTTPException(
                    status_code=404, detail="Author not found or wrong id length"
                )
            return author
        except SQLAlchemyError:
            raise HTTPException(
                status_code=404, detail="wrong id length"
            )
            
    @staticmethod
    async def delete_author(author_id: str, session: AsyncSession) -> None:
        """Delete author by id"""
        try:
            stmt = select(Author).filter(Author.id == author_id)
            author = await session.execute(stmt)
            author = author.scalars().unique().first()
            await session.delete(author)
            await session.commit()
        except SQLAlchemyError:
            raise HTTPException(
                status_code=404, detail="Author not found or wrong id length"
            )