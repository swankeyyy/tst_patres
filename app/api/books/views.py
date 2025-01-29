from fastapi import APIRouter, Depends, HTTPException

from typing import Union

from app.api.dependencies import get_current_user
from .service import BookService
from app.src.models.db_config import db_config
from .schemas import BookCreate, Book

router = APIRouter()


@router.post("/add/", summary="Create a new book", response_model=Union[Book, None])
async def add_book(
    new_book: BookCreate,
    user=Depends(get_current_user),
    session=Depends(db_config.get_session),
) -> Book | Exception:
    """Create a new book by taked data and author UUID"""
    if user.is_superuser:
        book = await BookService.create_book(new_book, session)
        return book
    raise HTTPException(status_code=403, detail="Permission denied")


@router.put(
    "/update/{book_id}", summary="Update book", response_model=Union[Book, None]
)
async def update_book(
    book_id: str,
    new_book: BookCreate,
    user=Depends(get_current_user),
    session=Depends(db_config.get_session),
) -> Book | Exception:
    
    """Update book by taked data and book UUID"""
    if user.is_superuser:
        book = await BookService.update_book(book_id, new_book, session)
        return book
    raise HTTPException(status_code=403, detail="Permission denied")


@router.delete("/delete/{book_id}", summary="Delete book", response_model=None)
async def delete_book(book_id: str, user=Depends(get_current_user), session=Depends(db_config.get_session)) -> None:
    """Delete book by taked book UUID"""
    if user.is_superuser:
        await BookService.delete_book(book_id, session)
        return None
    raise HTTPException(status_code=403, detail="Permission denied")

@router.get(
    "/get/{book_id}", summary="Get book by id", response_model=Union[Book, None]
)
async def get_book(
    book_id: str, session=Depends(db_config.get_session)
) -> Book | Exception:
    """Get book by id"""
    book = await BookService.get_book(book_id, session)
    return book
