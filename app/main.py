from contextlib import asynccontextmanager
from app.db.migration import run_migration
from fastapi import FastAPI
import logging
from app.routes.chat_routes import router as chat_router


from app.core.config import Settings

# Loading Config
settings = Settings()

# Logging Config
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # StartUp Event

    # Database Migrations
    if settings.MIGRATION:
        run_migration()
        
    logger.info("Application is starting...")

    yield
    # Shutdown Event
    logger.info("Application is shutting down...")



app = FastAPI(lifespan=lifespan)

app.include_router(chat_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}