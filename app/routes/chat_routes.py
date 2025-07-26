
import uuid
from app.utils.ws_auth import require_authenticated_user
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.services.chat_service import handle_chat

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    user_id = await require_authenticated_user(websocket)

    if not user_id:
        return  
    await websocket.accept()
    thread_id = uuid.uuid4().hex  
    try:
        while True:
            data = await websocket.receive_text()
            response = await handle_chat(data, user_id=user_id,thread_id=thread_id)
            if response == "__DISCONNECT__":
                await websocket.send_text("👋 You have been logged out.")
                await websocket.close()
                return
            await websocket.send_text(response)

    except WebSocketDisconnect:
        print(f"WebSocket disconnected for user {user_id}")
