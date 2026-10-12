from typing import AsyncGenerator
from urllib.parse import quote_plus

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

password = quote_plus("Rishi@2003")

# 1. FIXED: Changed 'pymysql' to 'aiomysql' for async support
DATABASE_URL = f"mysql+aiomysql://root:{password}@127.0.0.1:3306/fastapi_db"

# 2. FIXED: Passed 'DATABASE_URL' instead of the undefined 'URL' variable
engine = create_async_engine(DATABASE_URL, echo=False)

AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
