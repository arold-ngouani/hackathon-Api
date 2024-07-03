import random
from fastapi import APIRouter, Depends, HTTPException, status
from jose import ExpiredSignatureError, jwt, JWTError
from models.nfc_schemas import Code, TokenModel, CodeVerificationModel
from models.session import Session
from models.user import User
from fastapi.security import OAuth2PasswordBearer
import utilities
from typing import Annotated, List


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/validate_code")
router = APIRouter(prefix="/auth", tags=["Auth"])

THREE_DIGIT_CODES = {}

def generate_three_digit_code():
    return random.randint(100, 999)

@router.post("/read_nfc")
async def read_nfc(token_model: TokenModel):
    try:
        decoded = jwt.decode(token_model.token,key= None, options={"verify_signature": False})
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token error")

    # Generate a three-digit code
    code = generate_three_digit_code()
    while await Code.find_one(Code.code == code):
        code = generate_three_digit_code()

    #Store CODE DB
    code_to_store= Code(code=code, id_user=decoded.get("email"))
    await code_to_store.create()

    THREE_DIGIT_CODES = code
    return THREE_DIGIT_CODES

@router.post("/validate_code")
async def validate_code(code_model: CodeVerificationModel):
    code_info = await Code.find_one(Code.code == code_model.code)

    if(not code_info):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='code not valid' 
        ) 
    

    id_user=  code_info.id_user
    role = "employe"
    await code_info.delete()
    token = utilities.generate_token(given_id= id_user,given_role=role)
    get_user_info = await User.find_one(User.email == id_user)
    new_session = Session(user_id= get_user_info.id, email= id_user, name=get_user_info.name)
    await new_session.create()
    return token



#Protect route to get personal data
@router.get('/me')
async def secure_endoint(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        decoded = jwt.decode(token,key= None, options={"verify_signature": False})
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token error")
    
    email= decoded.get('user_id')
    print(email)
    get_user_info = await User.find_one(User.email == email)
    print(get_user_info)
    return get_user_info

@router.post("/auth_by_token")
async def auth_by_token(token_model: TokenModel):
    try:
        decoded = jwt.decode(token_model.token,key= None, options={"verify_signature": False})
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token error")


    email= decoded.get('email')
    get_user_info = await User.find_one(User.email == email)
    token = utilities.generate_token(given_id= email,given_role=get_user_info.email)
    new_session = Session(user_id= get_user_info.id, email= email, name=get_user_info.name)
    await new_session.create()
    return token
        

