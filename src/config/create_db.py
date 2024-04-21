from src.model.db.base import Base, engine
from src.model.db.account import Account
from src.model.db.project import Project
from src.model.db.project_picture import ProjectPicture


async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        # await conn.run_sync(Base.metadata.drop_all)


import asyncio
asyncio.run(create_database())
