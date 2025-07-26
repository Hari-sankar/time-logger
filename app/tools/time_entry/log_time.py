
from langchain.tools import tool
from app.db.session import get_db
import logging  

logger = logging.getLogger(__name__)
@tool
def log_time_entry(user_id: int, task_id: int, date: str, duration_hours: float) -> str:
    """Log a time entry into the timesheets table."""
    try:
        with get_db() as cursor:
            cursor.execute(
                """
                INSERT INTO timesheets (user_id, task_id, date, duration_hours)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (user_id, task_id, date)
                DO UPDATE SET duration_hours = EXCLUDED.duration_hours;
                """,
                (user_id, task_id, date, duration_hours)
            )
        return f" Logged {duration_hours}h for task ID {task_id} on {date}."
    except Exception as e:
        logger.exception("Error logging time entry")
        return f" Failed to log time entry: {str(e)}"
