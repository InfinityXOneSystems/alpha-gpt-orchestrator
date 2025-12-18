from fastapi import APIRouter
from control.manifest_loader import Manifest
from planner.core import PlannerCore
from executor.core import ExecutorCore

router = APIRouter()
manifest = Manifest()
planner = PlannerCore()
executor = ExecutorCore()

@router.post('/gpt/objective')
def inject_objective(payload: dict):
    if not manifest.enabled('gpt_bridge.enabled'):
        return {'error': 'GPT bridge disabled'}

    plan = planner.plan(payload.get('objective'))
    executor.execute(plan)
    return {'status': 'executed'}
