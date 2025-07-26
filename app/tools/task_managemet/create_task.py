
from langchain.tools import tool
from app.db.session import get_db
import logging

logger = logging.getLogger(__name__)

@tool
def create_task(project_id: int, task_name: str) -> str:
    """Create a new task under the given project."""
    try:
        with get_db() as cursor:
            cursor.execute(
                """
                INSERT INTO tasks (project_id, name)
                VALUES (%s, %s)
                ON CONFLICT (project_id, name) DO NOTHING
                """,
                (project_id, task_name)
            )

            cursor.execute(
                """
                SELECT id FROM tasks WHERE project_id = %s AND name = %s
                """,
                (project_id, task_name)
            )
            task_id = cursor.fetchone()[0]
            return f" Task '{task_name}' created with ID {task_id}."

    except Exception as e:
        logger.exception("Error creating task")
        return f"Failed to create task: {str(e)}"
