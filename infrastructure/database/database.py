import os
import ssl
from functools import lru_cache
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

load_dotenv()

ssl_context = ssl.create_default_context()

class Database:
    def __init__(self):
        self.DATABASE_URL = os.getenv("DATABASE_URL_ASYNC")
        if not self.DATABASE_URL:
            raise ValueError("DATABASE_URL_ASYNC not found in .env")

        self.engine = create_async_engine(
            self.DATABASE_URL,
            echo=False,
            connect_args={"ssl": ssl_context}
        )

        self.SessionLocal = async_sessionmaker(
            bind=self.engine,
            expire_on_commit=False
        )

class Base(DeclarativeBase):
    pass

@lru_cache()
def get_database() -> Database:
    """Singleton Database instance."""
    return Database()
