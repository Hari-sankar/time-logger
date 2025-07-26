
import json
from app.agents.chat_agent import agent_executor
from typing import AsyncGenerator



async def handle_chat(message: str) -> AsyncGenerator[str, None]:
    """
    Handles a chat message using the LangChain agent with built-in memory.
    The agent executor now manages the chat history internally.
    """
    # Process the incoming message with the agent executor
    async for chunk in agent_executor.astream({"input": message}):
        if "output" in chunk:
            yield chunk["output"]