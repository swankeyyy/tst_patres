import datetime
from .base import Base
from .book import Book

from typing import List

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Author(Base):
    """Database model of book author"""

    __tablename__ = "authors"
    name: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    biography: Mapped[str] = mapped_column(String(400), nullable=True)
    birthday: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)
    books: Mapped[List["Book"]] = relationship(
        back_populates="book_author", cascade="all, delete-orphan", lazy="select"
    )
