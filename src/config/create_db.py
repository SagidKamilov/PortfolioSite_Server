import asyncio
from src.api.dependency.service_container import async_database
from src.model.db.base import Base


engine = async_database.get_engine()


async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        # await conn.run_sync(Base.metadata.drop_all)


asyncio.run(create_database())
