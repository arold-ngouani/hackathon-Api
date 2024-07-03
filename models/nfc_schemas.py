from pydantic import BaseModel
from beanie import Document, Link

class TokenModel(BaseModel):
    token: str

class CodeVerificationModel(BaseModel):
    code: int

class Code(Document):
    code: int
    id_user: str