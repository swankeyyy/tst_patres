from fastapi import APIRouter, Depends, status
from .schemas import AuthorCreate, Author
from .service import AuthorService
from app.src.models.db_config import db_config

router = APIRouter()


@router.post("add_author/", status_code=status.HTTP_201_CREATED, response_model=Author, summary="Add a new author")
async def add_author(author: AuthorCreate, session=Depends(db_config.get_session)):
    """Add a new author with fields"""
    author = await AuthorService.create_author(author, session)
    return author

@router.put("update_author/{author_id}", status_code=status.HTTP_200_OK, response_model=Author, summary="Update an author")
async def update_author(author_id: str, author: AuthorCreate, session=Depends(db_config.get_session)):
    """Update an author with fields"""
    author = await AuthorService.update_author(author_id, author, session)
    return author