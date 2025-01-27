from .base import Base

from typing import TYPE_CHECKING
from uuid import UUID
from datetime import datetime

from sqlalchemy import ForeignKey, String, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .author import Author

class Book(Base):
    """Database model of book with author and genre"""

    __tablename__ = "books"
    title: Mapped[str] = mapped_column(String(20), nullable=False)
    description: Mapped[str]
    publication_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    author_id: Mapped[int]
    book_author_id: Mapped[UUID] = mapped_column(
        ForeignKey("authors.id"), nullable=False
    )
    book_author: Mapped["Author"] = relationship("Author", back_populates="books")
    genre: Mapped[str] = mapped_column(String(20), nullable=True)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=1)

