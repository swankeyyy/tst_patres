from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api import router
from src.models.db_config import db_config

import uvicorn


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     """close DB after lifespan"""
#     yield
#     await db_config.dispose()


app = FastAPI(
    title="Library",
    description="test task for Patres",
    version="0.0.1",
    contact={
        "name": "Ivan Levchuk",
        "email": "swankyyy1@gmail.com",
    },
)

app.include_router(router)


@app.get("/")
def main():
    return RedirectResponse(url='/docs')


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
