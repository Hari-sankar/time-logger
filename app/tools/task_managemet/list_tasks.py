
from langchain.tools import tool
from app.db.session import get_db
import logging

logger = logging.getLogger(__name__)

@tool
def list_project_tasks(project_id: int) -> str:
    """List all tasks under a given project."""
    try:
        with get_db() as cursor:
            cursor.execute(
                """
                SELECT id, name FROM tasks
                WHERE project_id = %s
                ORDER BY name
                """,
                (project_id,)
            )
            tasks = cursor.fetchall()

        if not tasks:
            return "📭 No tasks found under this project."

        task_lines = [f"{row['id']}: {row['name']}" for row in tasks]
        return " Tasks in Project:\n" + "\n".join(task_lines)

    except Exception as e:
        logger.exception("Error listing project tasks")
        return f" Failed to fetch project tasks: {str(e)}"
