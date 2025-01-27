from fastapi import APIRouter

from app.src.settings import settings
from app.api.users.views import router as users_router
from app.api.authors.views import router as authors_router

router = APIRouter(prefix="/api")
router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(authors_router, prefix="/authors", tags=["authors"])