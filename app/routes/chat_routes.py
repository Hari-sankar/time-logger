from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.services.chat_service import handle_chat

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket
):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            async for chunk in handle_chat(data):
                await websocket.send_text(chunk)
    except WebSocketDisconnect:
        print(f"Client disconnected")