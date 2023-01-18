import jwt
from fastapi import HTTPException
from src.models.auth_request import AuthRequest
from src.utils.config import JWT_SECRET


class AuthHandler:
    def __init__(self):
        self.secret = JWT_SECRET

    def __call__(self, req: AuthRequest):
        try:
            token = req.token
            header = jwt.get_unverified_header(token)
            payload = jwt.decode(token, JWT_SECRET, header["alg"])
            return payload

        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Signature has expired")

        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")
