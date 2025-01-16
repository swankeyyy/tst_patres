from fastapi import APIRouter

from app.src.settings import settings
from app.api.users.views import router as users_router

router = APIRouter(prefix="/api")
router.include_router(users_router, prefix="/users", tags=["users"])