from fastapi import APIRouter, Depends, status
from .schemas import AuthorCreate, Author
from .service import AuthorService
from app.src.models.db_config import db_config

router = APIRouter()


@router.post("add_author/", status_code=status.HTTP_201_CREATED, response_model=Author)
async def add_author(author: AuthorCreate, session=Depends(db_config.get_session)):
    result = await AuthorService.create_author(author, session)
    return result
