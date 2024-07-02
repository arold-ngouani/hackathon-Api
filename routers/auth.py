import random
from fastapi import APIRouter
from jose import ExpiredSignatureError, jwt, JWTError
from models.nfc_schemas import TokenModel, CodeVerificationModel
import utilities

router = APIRouter(prefix="/auth", tags=["Auth"])

THREE_DIGIT_CODES = {}

def generate_three_digit_code():
    return random.randint(100, 999)

@router.post("/read_nfc")
async def read_nfc(token_model: TokenModel):
    decoded = jwt.decode(token_model.token,key= None, options={"verify_signature": False})

    # Generate a three-digit code
    code = generate_three_digit_code()
    #Store CODE DB

    THREE_DIGIT_CODES = code
    return THREE_DIGIT_CODES

@router.post("/validate_code")
async def validate_code(code_model: CodeVerificationModel):
    decoded = code_model.code

    user_id=  "12"
    role = "employe"

    token = utilities.generate_token(given_id= user_id,given_role=role)
    return THREE_DIGIT_CODES