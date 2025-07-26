
from langchain.tools import tool
from app.db.session import get_db
import logging

logger = logging.getLogger(__name__)

@tool
def list_assigned_projects(user_id: int) -> str:
    """List all projects assigned to a given user."""
    try:
        with get_db() as cursor:
            cursor.execute(
                """
                SELECT p.id, p.name
                FROM projects p
                JOIN assignments a ON a.project_id = p.id
                WHERE a.user_id = %s
                ORDER BY p.name
                """,
                (user_id,)
            )
            projects = cursor.fetchall()

        if not projects:
            return "📭 No projects assigned to you."

        project_lines = [f"{row['id']}: {row['name']}" for row in projects]
        return " Assigned Projects:\n" + "\n".join(project_lines)

    except Exception as e:
        logger.exception("Error listing assigned projects")
        return f" Failed to fetch assigned projects: {str(e)}"
