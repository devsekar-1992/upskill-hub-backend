from fastapi import APIRouter
from app.api.v1.endpoints import users

router = APIRouter(
    prefix="/v1",
    tags=["v1"]
)

router.include_router(users.router)