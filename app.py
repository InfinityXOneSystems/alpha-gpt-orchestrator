from fastapi import FastAPI
from api.health import router as health_router

app = FastAPI(title='Alpha GPT Orchestrator')

app.include_router(health_router)

from api.heartbeat import router as heartbeat_router

app.include_router(heartbeat_router)

from api.heartbeat import router as heartbeat_router

app.include_router(heartbeat_router)

from api.heartbeat import router as heartbeat_router

app.include_router(heartbeat_router)
