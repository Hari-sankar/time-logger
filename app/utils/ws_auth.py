
from app.utils.jwt import verify_jwt
from fastapi import WebSocket, status
from jose import JWTError

async def require_authenticated_user(websocket: WebSocket):
    token = websocket.headers.get("token")

    if not token:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return None

    try:
        
        user_id = verify_jwt(token)
        
        if user_id is None:
            await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
            return None
        return user_id
    except JWTError:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return None
