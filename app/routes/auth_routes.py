from fastapi import APIRouter

from app.schemas.auth import *
from app.services import auth_service

router = APIRouter()

@router.post("/login")
async def login(loginRequest: LoginRequest):
    return await auth_service.login(loginRequest)

@router.post("/signup")
async def signup(userData: SignUpRequest):
    return await auth_service.signup(userData)

