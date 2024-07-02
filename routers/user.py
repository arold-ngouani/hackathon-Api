from typing import List
from fastapi import APIRouter

from models.user import User


router = APIRouter(prefix="/users", tags=["Users"])

#Get all users
@router.get("", status_code=200)
async def get_all_users()-> List [User]:
    user= await User.find_all().to_list()
    return user
    

#Post user
@router.post("", status_code=201, response_model=dict)
async def post_user(payload: User) :
    user= await payload.create()
    return {"message": "User added successfully", "id": str(user.id)}

#Get user by id
@router.get("/{user_id}", status_code=200)
async def get_user_by_id(session_id: str) -> User:
    user= await User.get(session_id)
    return user



#Delete session
@router.delete("/{user_id}", status_code=200)
async def delete_user(user_id: str):
    user=await User.get(user_id)
    await user.delete()
    return 



