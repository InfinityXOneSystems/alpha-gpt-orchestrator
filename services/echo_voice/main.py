from fastapi import FastAPI, Request
from services.guardian.agent import GuardianAgent

app = FastAPI(title="Echo Voice AI")

guardian = GuardianAgent()

@app.post("/twilio/voice")
async def inbound_call(request: Request):
    guardian.validate(request)
    return {"status": "accepted"}

@app.post("/twilio/sms")
async def inbound_sms(request: Request):
    guardian.validate(request)
    return {"status": "accepted"}
