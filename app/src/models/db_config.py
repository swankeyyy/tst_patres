from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
)

from app.src.settings import settings


class DBConfig:

    def __init__(self, url: str, echo: bool = False) -> None:
        self.engine: AsyncEngine = create_async_engine(url=url, echo=echo)
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine
        )

    async def dispose(self) -> None:
        """close database engine"""
        await self.engine.dispose()

    async def get_session(self) -> AsyncSession:
        async with self.session_factory() as session:
            yield session

    def get_engine(self) -> AsyncEngine:
        return self.engine


db_config = DBConfig(url=settings.DB_URL, echo=settings.DB_ECHO)
