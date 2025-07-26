
from langchain.tools import tool
from app.db.session import get_db
import difflib
import logging

logger = logging.getLogger(__name__)

@tool
def suggest_similar_task(project_id: int, task_name: str) -> str:
    """Suggests similar task names under a project if the task doesn't exist."""
    try:
        with get_db() as cursor:
            cursor.execute(
                """
                SELECT name FROM tasks WHERE project_id = %s
                """,
                (project_id,)
            )
            existing_tasks = [row[0] for row in cursor.fetchall()]

        matches = difflib.get_close_matches(task_name, existing_tasks, n=3, cutoff=0.6)

        if matches:
            return f" Task '{task_name}' not found. Did you mean: {', '.join(matches)}?"
        else:
            return f" Task '{task_name}' not found. No close matches found. Do you want to create it?"

    except Exception as e:
        logger.exception("Error suggesting similar tasks")
        return f" Failed to suggest tasks: {str(e)}"
