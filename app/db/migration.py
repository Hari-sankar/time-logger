
from pathlib import Path
from app.db.session import get_db
import logging

logger = logging.getLogger(__name__)

def run_migration():
    schema_path = Path(__file__).parent / "init.sql"
    try:
        with open(schema_path, "r") as f:
            schema_sql = f.read()
    except FileNotFoundError:
        logger.error("schema.sql file not found.")
        return
    except Exception as e:
        logger.exception(f"Failed to read schema.sql: {e}")
        return

    try:
        with get_db() as cursor:
            cursor.execute(schema_sql)
            logger.info("Database schema initialized.")
    except Exception as e:
        logger.exception(f"Error initializing database: {e}")


