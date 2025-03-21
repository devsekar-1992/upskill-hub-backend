import os
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from dotenv import load_dotenv
load_dotenv()
engine=create_async_engine(os.getenv('DATABASE_URL'),echo=True,future=True)
async_session_local=async_sessionmaker(engine,class_=AsyncSession,expire_on_commit=False)

async def get_session()->AsyncSession: # type: ignore
    async with async_session_local() as session:
        try:
            yield session
        finally:
            await session.close()
