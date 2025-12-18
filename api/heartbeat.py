from fastapi import APIRouter
from control.calendar_governed_loop import CalendarGovernedLoop

router = APIRouter()
loop = CalendarGovernedLoop()

@router.post('/heartbeat')
def heartbeat():
    loop.run_cycle()
    return {'status':'alive','mode':'calendar-governed'}
