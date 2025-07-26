
from langchain.tools import tool
from app.db.session import get_db
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

@tool
def send_reminder_email(user_id: int, remind_at: str, message: str) -> str:
    """Log a reminder entry to the database for the user to be reminded at a specific datetime."""
    try:
        remind_time = datetime.fromisoformat(remind_at)

        with get_db() as cursor:
            cursor.execute(
                """
                INSERT INTO reminders (user_id, time, timezone)
                VALUES (%s, %s, %s)
                """,
                (user_id, remind_time, message)
            )

        return f" Reminder logged for {remind_time.isoformat()}"

    except Exception as e:
        logger.exception("Error logging reminder to database")
        return f"Failed to log reminder: {str(e)}"


@tool
def end_ws_session(user_id: int) -> str:
    """
    Tool that requests the server to terminate the current WebSocket session for the given user.
    The FastAPI server should handle this request using a control message (e.g., "__DISCONNECT__").
    """
    logger.info(f"User {user_id} requested to end session.")
    return "__DISCONNECT__"


@tool
def get_current_date() -> str:
    """
    Returns the current date in ISO format.
    This can be used to log today's date or for any other purpose.
    """
    current_date = datetime.now().date()
    return current_date.isoformat()