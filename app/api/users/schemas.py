from pydantic import BaseModel, ConfigDict
from uuid import UUID
from typing import Optional

class Base(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

class UserBase(Base):
    """Base user model schema"""
    username: str
    is_superuser: bool

class Book(Base):
    """Book model schema"""
    id: UUID
    title: str

class UserWithBooks(UserBase):
    """User with books schema"""
    books: Optional[list[Book]] = []