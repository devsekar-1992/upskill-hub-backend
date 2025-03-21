import os
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from dotenv import load_dotenv
from passlib.context import CryptContext
from app.models.users import Users,UserCreate
from app.core.logger import get_logger

logger=get_logger()

load_dotenv()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
class UserRespository:
    def __init__(self,session: AsyncSession) -> None:
        self.db_session=session
    """
    Is User already exists or not?
    """
    async def is_email_already_exists(self, email):
        try:
            stmt=select(Users).where(Users.email==email)
            user=await self.db_session.exec(stmt)
            return user.first()
        except Exception as ex:
            logger.exception(ex)
    """
    Create a new user
    """
    async def create(self,create_user: UserCreate):
        try:
            db_user=Users(**create_user.model_dump())
            db_user.password=pwd_context.hash(db_user.password)
            self.db_session.add(db_user)
            await self.db_session.commit()
            await self.db_session.refresh(db_user)
            return db_user
        except Exception as e:
            logger.exception(e)
