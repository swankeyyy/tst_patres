from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date
from uuid import UUID


class AuthorBase(BaseModel):
    "Base schema for Author model"
    model_config = ConfigDict(from_attributes=True)


class AuthorCreate(AuthorBase):
    """Schema for creating an author"""

    name: str
    biography: Optional[str] = None
    birthday: Optional[date] = None

class Book(AuthorBase):
    """Schema for books"""

    id: UUID
    title: str
    genre: Optional[str] = None

class Author(AuthorBase):
    """Schema for an author"""

    id: UUID
    name: str
    biography: Optional[str] = None
    birthday: Optional[date] = None
    

class FoolAuthor(Author):
    """Schema for an author with books"""
    books: Optional[List[Book]] = None