from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date
from uuid import UUID


class BookBase(BaseModel):
    "Base schema for Book model"
    model_config = ConfigDict(from_attributes=True)


class BookCreate(BookBase):
    """Schema for creating a book"""

    title: str
    description: Optional[str] = None
    publication_date: Optional[date] = None
    book_author_id: UUID
    genre: Optional[str] = None
    quantity: Optional[int] = 1


class Book(BookCreate):
    """Book schema"""

    id: UUID
