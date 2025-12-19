from fastapi import APIRouter
from control.jobs import submit_job

router = APIRouter()

@router.get('/obs/metrics')
def metrics():
    return submit_job('obs.metrics', {})

@router.get('/obs/billing')
def billing():
    return submit_job('obs.billing', {})
@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/ready")
def ready():
    return {"ready": True}
