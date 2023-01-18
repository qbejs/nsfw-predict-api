from typing import List
from pydantic import BaseModel


# text: str
# languages: List[str]
# base_language: str


class AuthRequest(BaseModel):
    token: str
