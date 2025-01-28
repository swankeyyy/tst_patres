from .base import Base

from sqlalchemy import ForeignKey, Table, Column


users_books = Table(
   "users_books",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("book_id", ForeignKey("books.id"), primary_key=True)
)

