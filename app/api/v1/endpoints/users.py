from fastapi import APIRouter,Depends,HTTPException
from app.api.v1.dependency import get_user_service
from app.models.users import UserCreate
from app.models.response import APIResponse
from app.core.api_response import response
from app.services.user_service import UserService

router=APIRouter(
    prefix='/users'
)

@router.post('/register',tags=['users'],status_code=201,response_model=None)
async def create_users(user: UserCreate,service: UserService=Depends(get_user_service)):
    """
    Endpoint to register a new user
    """
    email_taken = await service.is_email_taken(user.email)
    if email_taken:
        return response(False,'Email already registered',[],400)
    new_user = await service.register_user(user)
    return response(True,'User registered successfully',new_user,201)