import time
from agent.alpha_omega import run_cycle
from validation.heal import health_check
from config import AGENT_SLEEP_SECONDS

def run_loop():
    health_check()
    run_cycle()

while True:
    try:
        run_loop()
    except Exception as e:
        print("[AGENT ERROR]", e)

    time.sleep(AGENT_SLEEP_SECONDS)
