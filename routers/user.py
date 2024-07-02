from fastapi import APIRouter


router = APIRouter(prefix="/users", tags=["Users"])

#Get all users
@router.get("", status_code=200)
async def get_all_users():
    users=[]
    return users

#Post user
@router.post("", status_code=201)
async def post_user():
    users=()
    return users

#Get user by id
@router.get("/{user_id}", status_code=200)
async def get_user_by_id():
    users=[]
    return users

#Update  user
@router.patch("/{user_id}", status_code=204)
async def update_user():
    users=[]
    return 

#Delete user
@router.delete("/{user_id}", status_code=200)
async def delete_user():
    users=[]
    return 




