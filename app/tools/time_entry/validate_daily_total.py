
from langchain.tools import tool
from app.db.session import get_db
import logging

logger = logging.getLogger(__name__)

@tool
def validate_daily_total(user_id: int, date: str, new_hours: float) -> str:
    """Validate if total daily hours exceed 24h. Warn if above 8h, reject if above 24h."""
    try:
        with get_db() as cursor:
            cursor.execute(
                """
                SELECT COALESCE(SUM(duration_hours), 0)
                FROM timesheets
                WHERE user_id = %s AND date = %s
                """,
                (user_id, date)
            )
            current_total = cursor.fetchone()[0]

        total = current_total + new_hours

        if total > 24:
            return f" Rejected: Total hours ({total}) exceed daily limit (24h)."
        elif total > 8:
            return f" Warning: Total hours will be {total}h. Please confirm if this is correct."
        else:
            return f" Valid: Total logged time will be {total}h."

    except Exception as e:
        logger.exception("Error validating daily total")
        return f" Failed to validate time entry: {str(e)}"
