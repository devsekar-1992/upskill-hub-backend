from app.repository.user_repository import UserRespository
from app.models.users import UserCreate,Users,UserResponse
class UserService:
    def __init__(self,user_repo: UserRespository):
        self.user_repo = user_repo

    async def is_email_taken(self, email) -> bool:
        """
        Validate is email already exists
        """
        existing_user = await self.user_repo.is_email_already_exists(email)
        if existing_user:
                return True
        return False

    async def register_user(self,create_user: UserCreate) -> UserResponse:
        """
        Create a user
        """
        try:
            #db_user=Users(**create_user.model_dump())
            result=await self.user_repo.create(create_user=create_user)
            return UserResponse(**result)
        except Exception as ex:
            print(ex)
