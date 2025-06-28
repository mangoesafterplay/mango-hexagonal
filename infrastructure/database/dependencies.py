from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession
from infrastructure.database.database import get_database

@asynccontextmanager
async def get_session() -> AsyncSession:
    """Provee un AsyncSession a través de un context manager."""
    db = get_database()
    async with db.SessionLocal() as session:
        yield session
