from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from fastapi import HTTPException

from app.api.utils import *
from app.src.models import User, Book


class UserService:
    @staticmethod
    async def create_user(
        username: str, password: str, session: AsyncSession, is_superuser: bool = False
    ) -> User | Exception:

        if not username or not password:
            raise HTTPException(status_code=400, detail="Username or password is empty")

        """Try to get user from DB, if it not exists, create new user"""
        stmt = select(User).where(User.username == username)
        user = await session.execute(stmt)
        user = user.scalars().first()

        if not user:
            if not password_verify(password, username):
                raise HTTPException(status_code=400, detail="Password is too short")
            hashed_password = hash_password(password)
            user = User(
                username=username, password=hashed_password, is_superuser=is_superuser
            )
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user

        raise HTTPException(status_code=400, detail="User is already exist")

    @staticmethod
    async def login_user(
        username: str, password: str, session: AsyncSession
    ) -> str | Exception:
        """Try to get user from DB, if it exists, check password"""

        stmt = select(User).where(User.username == username)
        user = await session.execute(stmt)
        user = user.scalars().first()

        if user:
            if check_password(password, user.password):
                access_token = create_access_token({"username": user.username})
                return access_token

        raise HTTPException(
            status_code=400, detail="User not found or password is incorrect"
        )

    @staticmethod
    async def get_users(user: User, session: AsyncSession):
        """Get all users from DB"""
        if user.is_superuser:
            stmt = select(User)
            users = await session.execute(stmt)
            users = users.scalars().all()
            return list(users)

        raise HTTPException(status_code=403, detail="You are not a superuser")

    @staticmethod
    async def add_book(user: User, book_id: str, session: AsyncSession):
        """Add book to user's books"""

        stmt = select(Book).where(Book.id == book_id)
        book = await session.execute(stmt)
        book = book.scalars().first()
        if book:
            if book.quantity < 1:
                raise HTTPException(status_code=400, detail="Book is out of stock")
            if len(user.books) >= 5:
                raise HTTPException(
                    status_code=400, detail="A user cannot borrow more than 5 books"
                )
            user.books.append(book)
            book.quantity -= 1
            await session.commit()
            await session.refresh(user)
            return user
        raise HTTPException(status_code=404, detail="Book not found")
    
    @staticmethod
    async def delete_book(user: User, book_id: str, session: AsyncSession):
        """Delete book from user's books"""
        stmt = select(Book).where(Book.id == book_id)
        book = await session.execute(stmt)
        book = book.scalars().first()
        if book:
            user.books.remove(book)
            book.quantity += 1
            await session.commit()
            await session.refresh(user)
            return user
        raise HTTPException(status_code=404, detail="Book not found")
