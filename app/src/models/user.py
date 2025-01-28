from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates

from typing import List

from .base import Base
from .book import Book
from .associations import users_books


class User(Base):
    """User model class."""

    __tablename__ = "users"
    username: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(60), nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)
    books: Mapped[List[Book]] = relationship(
        "Book", secondary=users_books, back_populates="users", lazy="joined"
    )

    @validates("books")
    def validate_books(self, key, book):
        if len(self.books) >= 5:
            raise ValueError("A user cannot borrow more than 5 books.")
        return book
