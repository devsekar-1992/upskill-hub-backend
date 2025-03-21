from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.database import get_session
from app.repository.user_repository import UserRespository
from app.services.user_service import UserService


async def get_user_service(session: AsyncSession = Depends(get_session)):
    return UserService(UserRespository(session))
