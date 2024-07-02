from pydantic import BaseModel


class TokenModel(BaseModel):
    token: str

class CodeVerificationModel(BaseModel):
    code: int