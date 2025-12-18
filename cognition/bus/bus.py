import queue

COGNITIVE_BUS = queue.Queue()

def publish(event: dict):
    COGNITIVE_BUS.put(event)

def consume():
    try:
        return COGNITIVE_BUS.get(timeout=1)
    except Exception:
        return None
