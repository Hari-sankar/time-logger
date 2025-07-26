from pydantic import BaseModel, EmailStr, Field

from app.shared.constants import *


class LoginRequest(BaseModel):
    email: EmailStr = Field(..., description=EMAIL_DESC, example=EMAIL_EXAMPLE)
    password: str = Field(..., description=PASSWORD_DESC, example=PASSWORD_EXAMPLE, min_length=8)

class SignUpRequest(BaseModel):
    name: str = Field(None, description=NAME_DESC, example=NAME_EXAMPLE)
    email: EmailStr = Field(..., description=EMAIL_DESC, example=EMAIL_EXAMPLE)
    password: str = Field(..., description=PASSWORD_DESC, example=PASSWORD_EXAMPLE, min_length=8)


