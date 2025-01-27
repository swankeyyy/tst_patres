from sqlalchemy import select

from .schemas import BookCreate
from app.src.models import Book
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError, SQLAlchemyError


class BookService:

    @staticmethod
    async def create_book(
        new_book: BookCreate, session: AsyncSession
    ) -> Book | Exception:
        """Create new book by taked title and author UUID if the book with the same title and author UUID doesn't exist"""
        try:
            stmt = (
                select(Book)
                .filter(Book.title == new_book.title)
                .filter(Book.book_author_id == new_book.book_author_id)
            )
            book = await session.execute(stmt)
            if book.scalars().first():
                raise HTTPException(status_code=409, detail="Book already exists")
            book = Book(**new_book.model_dump())
            session.add(book)
            await session.commit()
            await session.refresh(book)
            return book
        except IntegrityError:
            await session.rollback()
            raise HTTPException(status_code=400, detail="Invalid author id")

    @staticmethod
    async def update_book(
        book_id: str, new_book: BookCreate, session: AsyncSession
    ) -> Book | Exception:
        """Update book by taked data and book UUID"""
        try:
            stmt = select(Book).filter(Book.id == book_id)
            book = await session.execute(stmt)
            book = book.scalars().first()

            for key, value in new_book.model_dump(exclude_unset=True).items():
                setattr(book, key, value)
            session.add(book)
            await session.commit()
            await session.refresh(book)
            return book
        except SQLAlchemyError:
            raise HTTPException(
                status_code=404, detail="Wrong book id length or book not found"
            )

    @staticmethod
    async def delete_book(book_id: str, session: AsyncSession) -> None:
        """Delete book by taked book UUID"""
        try:
            stmt = select(Book).filter(Book.id == book_id)
            book = await session.execute(stmt)
            book = book.scalars().first()
            await session.delete(book)
            await session.commit()
        except SQLAlchemyError:
            raise HTTPException(
                status_code=404, detail="Wrong book id length or book not found"
            )
