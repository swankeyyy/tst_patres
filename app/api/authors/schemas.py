from pydantic import BaseModel, ConfigDict
from typing import Optional
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


class Author(AuthorBase):
    """Schema for an author"""
    id: UUID
    name: str
    biography: Optional[str] = None
    birthday: Optional[date] = None

