from fastapi import APIRouter, Depends

from typing import Union

from .service import BookService
from app.src.models.db_config import db_config
from .schemas import BookCreate, Book

router = APIRouter()

@router.post("/add/", summary="Create a new book", response_model=Union[Book, None])
async def add_book(new_book: BookCreate, session=Depends(db_config.get_session)) -> Book | Exception:
    """Create a new book by taked data and author UUID"""
    book = await BookService.create_book(new_book, session)
    return book

@router.put("/update/{book_id}", summary="Update book", response_model=Union[Book, None])
async def update_book(book_id: str, new_book: BookCreate, session=Depends(db_config.get_session)) -> Book | Exception:
    """Update book by taked data and book UUID"""
    book = await BookService.update_book(book_id, new_book, session)
    return book

@router.delete("/delete/{book_id}", summary="Delete book", response_model=None)
async def delete_book(book_id: str, session=Depends(db_config.get_session)) -> None:
    """Delete book by taked book UUID"""
    await BookService.delete_book(book_id, session)
    return None

@router.get("/get/{book_id}", summary="Get book by id", response_model=Union[Book, None])
async def get_book(book_id: str, session=Depends(db_config.get_session)) -> Book | Exception:
    """Get book by id"""
    book = await BookService.get_book(book_id, session)
    return book