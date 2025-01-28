from fastapi import APIRouter, Depends, status
from .schemas import AuthorCreate, Author, FoolAuthor
from .service import AuthorService
from app.src.models.db_config import db_config
from typing import Union
from app.api.dependencies import get_current_user

router = APIRouter()


@router.post(
    "/add_author/",
    status_code=status.HTTP_201_CREATED,
    response_model=Author,
    summary="Add a new author",
)
async def add_author(author: AuthorCreate, session=Depends(db_config.get_session), user=Depends(get_current_user)):
    """Add a new author with fields"""
    author = await AuthorService.create_author(author, session)
    return author


@router.put(
    "/update_author/{author_id}",
    status_code=status.HTTP_200_OK,
    response_model=Author,
    summary="Update an author",
)
async def update_author(
    author_id: str, author: AuthorCreate, session=Depends(db_config.get_session), user=Depends(get_current_user)
):
    """Update an author with fields"""
    author = await AuthorService.update_author(author_id, author, session)
    return author


@router.get(
    "/get_author/{author_id}",
    status_code=status.HTTP_200_OK,
    response_model=Union[FoolAuthor, None],
    summary="Get an author by id",
)
async def get_author(author_id: str, session=Depends(db_config.get_session)):
    """Get an author by id"""
    author = await AuthorService.get_author(author_id, session)
    return author


@router.delete(
    "/delete_author/{author_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete an author by id",
)
async def delete_author(author_id: str, session=Depends(db_config.get_session), user=Depends(get_current_user)):
    """Delete an author by id"""
    await AuthorService.delete_author(author_id, session)
    return None



