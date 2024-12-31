from fastapi import APIRouter 
from models.user import User
from controllers.api.user import create_user

router = APIRouter()

@router.post("/user")
async def add_user(user:User):
     return await create_user(user)