
from jose import jwt, JWTError
from datetime import datetime, timedelta
from typing import Optional
from app.core.config import settings

def generate_jwt(user_id: int, expires_delta: Optional[timedelta] = None) -> str:
    expire = datetime.utcnow() + (expires_delta or timedelta(hours=6))
    payload = {
        "sub": str(user_id),
        "exp": expire
    }
    token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return token

def verify_jwt(token: str) -> Optional[int]:
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        return int(payload.get("sub"))
    except JWTError:
        return None
