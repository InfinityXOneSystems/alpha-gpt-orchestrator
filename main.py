import os
from fastapi import FastAPI

app = FastAPI(title="Infinity XOS Orchestrator")

ROLE = os.getenv("ROLE", "LEADER")

@app.get("/health")
def health():
    return {"status": "ok", "role": ROLE}

@app.get("/role")
def role():
    return {"role": ROLE}

@app.post("/telemetry")
async def telemetry(payload: dict):
    return {"status": "ingested"}

@app.post("/rehydrate")
async def rehydrate(payload: dict):
    return {"status": "rehydrated"}

@app.get("/")
def root():
    return {"service": "orchestrator", "role": ROLE}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080)),
        log_level="info"
    )
