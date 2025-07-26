
from langchain_core.messages import HumanMessage
from app.agents.chat_agent import graph as chatbot 


async def handle_chat(message: str, user_id: int,thread_id : str) -> str:
    """
    Handles a chat message using LangGraph agent with memory.
    Returns the final response as a string.
    """

    config = {"configurable": {"thread_id": thread_id}}

    input_data = {
        "messages": [HumanMessage(content=message)],
        "user_id": str(user_id)
    }

    result = await chatbot.ainvoke(input=input_data, config=config)

    
    final_message = result.get("messages")[-1]
    
    if hasattr(final_message, "content"):
        return final_message.content
