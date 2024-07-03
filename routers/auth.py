import random
from fastapi import APIRouter, HTTPException, status
from jose import ExpiredSignatureError, jwt, JWTError
from models.nfc_schemas import Code, TokenModel, CodeVerificationModel
from models.session import Session
from models.user import User
import utilities

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
    new_session = Session(user_id= get_user_info.id)
    await new_session.create()
    return token


async def mafonction():

    return
