from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from app.core.database import get_session
from app.services.user_service import UserService
from app.repository.user_repository import UserRespository

async def get_user_service(session: AsyncSession=Depends(get_session)):
    return UserService(UserRespository(session))
