import asyncio
from fastapi import FastAPI
from core.server.routers.routers import get_info_router
from core.db.initialize_db import initialize_db
from utils.return_sqlite_path import return_sqlite_path
from core.server.flusher import flusher

app = FastAPI(
        title="LexiForge API",
        description="Core services for LexiForge project.",
        version="0.0.1",
)

@app.on_event("startup")
async def startup_event():
    print("Starting up db inintialization...")
    await initialize_db(return_sqlite_path())
    asyncio.create_task(flusher())

app.include_router(get_info_router)