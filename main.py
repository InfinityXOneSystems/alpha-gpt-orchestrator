import os
from fastapi import FastAPI

app = FastAPI(title="Infinity XOS Orchestrator")

ROLE = os.getenv("ROLE","LEADER")

@app.get("/health")
def health():
    return {"status":"ok","role":ROLE}

@app.get("/role")
def role():
    return {"role":ROLE}

@app.post("/telemetry")
async def telemetry(payload: dict):
    return {"accepted": True}

@app.post("/rehydrate")
async def rehydrate(payload: dict):
    return {"rehydrated": True}

from services.orchestrator.guardian_middleware import guardian_middleware
