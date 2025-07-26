from contextlib import contextmanager

from psycopg2 import pool
from psycopg2.extras import DictCursor

from app.core.config import Settings

settings = Settings()

connection_pool = pool.SimpleConnectionPool(
    minconn=3,
    maxconn=10,
    dsn=settings.DATABASE_URL  
)

@contextmanager
def get_db():
    conn = connection_pool.getconn()  
    try:
        cursor = conn.cursor(cursor_factory=DictCursor)
        yield cursor
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        connection_pool.putconn(conn) 
