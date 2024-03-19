
from pydantic import BaseModel, EmailStr


class RegisterUser(BaseModel):
    email: EmailStr
    username: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str
