from fastapi import APIRouter

from app.src.settings import settings
from app.api.users.views import router as users_router
from app.api.authors.views import router as authors_router
from app.api.books.views import router as books_router

router = APIRouter(prefix=settings.API_PREFIX)
router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(authors_router, prefix="/authors", tags=["authors"])
router.include_router(books_router, prefix="/books", tags=["books"])