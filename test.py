from jose import ExpiredSignatureError, jwt, JWTError
from datetime import datetime, timezone, timedelta


# Used during Auth / Login
algo = "HS256"
secret = "5ae48e781d227cabc077167f64005ff949922d586157d6ae07078fee3f3ad170"

# Generate a JWT token used by /auth
def generate_token(email:str, given_role: str = "simple_user", name: str = ""):
    expiration_time = datetime.now(tz=timezone.utc) + timedelta(days=3)
    payload = {"email": email, "role": given_role, "name": name, "exp": expiration_time}
    encoded_jwt = jwt.encode(payload, secret, algorithm=algo)
    print(encoded_jwt)
    return encoded_jwt
    

generate_token(email="imrane@estiam.com", given_role="employe", name="Imrane Lawani")