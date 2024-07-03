from beanie import Document
from pydantic import BaseModel


class TokenModel(BaseModel):
    token: str

class CodeVerificationModel(BaseModel):
    code: int

class Code(Document):
    code: int
    id_user: str