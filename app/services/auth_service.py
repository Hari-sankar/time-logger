from fastapi import HTTPException

from app.db.session import get_db
from app.schemas.auth import *
from app.schemas.response import format_response
from app.utils.jwt import generate_jwt
from app.utils.password_handler import hash_password, verify_password


async def login(loginRequest:LoginRequest):
    with get_db() as cursor:
        query = "SELECT * FROM users WHERE email = %s;"
        cursor.execute(query, (loginRequest.email,))
        user = cursor.fetchone()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        if not verify_password(loginRequest.password, user["password"]):
            raise HTTPException(status_code=400, detail="Invalid Password")
        data=user["id"]
        token = generate_jwt(user_id=data)
        return format_response(200, "Login Successfully",token)

async def signup(userData: SignUpRequest):
    with get_db() as cursor:
        try:
            query = "SELECT * FROM users WHERE email = %s;"
            cursor.execute(query, (userData.email,))
            user = cursor.fetchone()
            if user:
                raise HTTPException(status_code=409, detail="User Already Exists")
            hashed_password = hash_password(userData.password)
            query = """INSERT INTO users (email, password, name) 
                        VALUES (%s, %s, %s) RETURNING id;"""
            cursor.execute(query, (userData.email, hashed_password, userData.name))
            
            return format_response(200, "Account has been created successfully")
        
        except Exception as e:
            print(e)
            return format_response(500, "Error creating new user")

