from fastapi import APIRouter


router = APIRouter(prefix="/sessions", tags=["Sessions"])

#Get all sessions
@router.get("", status_code=200)
async def get_all_sessions():
    sessions=[]
    return sessions

#Post session
@router.post("", status_code=201)
async def post_session():
    sessions=()
    return sessions

#Get session by id
@router.get("/{session_id}", status_code=200)
async def get_session_by_id():
    sessions=()
    return sessions

#Update  session
@router.patch("/{session_id}", status_code=204)
async def update_session():
    sessions=()
    return 

#Delete session
@router.delete("/{session_id}", status_code=200)
async def delete_session():
    sessions=()
    return 
