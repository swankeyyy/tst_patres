from fastapi import APIRouter, Depends
from .service import BookService
from app.src.models.db_config import db_config
from .schemas import BookCreate

router = APIRouter()

@router.post("/add/", summary="Create a new book")
async def add_book(new_book: BookCreate, session=Depends(db_config.get_session)):
    """Create a new book by taked data and author UUID"""
    book = await BookService.create_book(new_book, session)
    return book