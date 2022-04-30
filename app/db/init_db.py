from asyncio import run

from connection import engine
from app.models.user import Base

async def create_db():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)

if __name__ == "main":
    run(create_db())