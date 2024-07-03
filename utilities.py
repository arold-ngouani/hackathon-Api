from jose import ExpiredSignatureError, jwt, JWTError
from datetime import datetime, timezone, timedelta


# Used during Auth / Login
algo = "HS256"
secret = "5ae48e781d227cabc077167f64005ff949922d586157d6ae07078fee3f3ad170"

# Generate a JWT token used by /auth
def generate_token(given_id:int, given_role: str = "simple_user"):
    expiration_time = datetime.now(tz=timezone.utc) + timedelta(hours=3)
    payload = {"user_id": given_id, "user_role": given_role, "exp": expiration_time}
    encoded_jwt = jwt.encode(payload, secret, algorithm=algo)
    print(encoded_jwt)
    return {
        "access_token": encoded_jwt, # JWT
        "token_type": "bearer"
    }