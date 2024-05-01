from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.config import settings


class AsyncDatabase:
    def __init__(self):
        self.url = f"postgresql+{settings.DB_POSTGRES_SCHEMA}://{settings.DB_POSTGRES_USERNAME}:{settings.DB_POSTGRES_PASSWORD}@{settings.DB_POSTGRES_HOST}:{settings.DB_POSTGRES_PORT}/{settings.DB_POSTGRES_NAME}"
        self.async_engine = None
        self.async_session = None

    def initialize_engine(self):
        self.async_engine = create_async_engine(url=self.url)

    def initialize_session(self):
        self.async_session = async_sessionmaker(bind=self.async_engine, expire_on_commit=False)

    def get_engine(self):
        return self.async_engine

    def get_session(self):
        return self.async_session
