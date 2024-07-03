from typing import List
from fastapi import APIRouter

from models.session import Session


router = APIRouter(prefix="/sessions", tags=["Sessions"])

#Get all sessions
@router.get("", status_code=200)
async def get_all_sessions()-> List [Session]:
    session= await Session.find_all().to_list()
    return session
    

#Post session
@router.post("", status_code=201, response_model=dict)
async def post_session(payload: Session) :
    session= await payload.create()
    return {"message": "Session added successfully", "id": str(session.id)}

#Get session by id
@router.get("/{session_id}", status_code=200)
async def get_session_by_id(session_id: str) -> Session:
    session= await Session.get(session_id)
    return session



#Delete session
@router.delete("/{session_id}", status_code=200)
async def delete_session(session_id: str):
    session=await Session.get(session_id)
    await session.delete()
    return 
