import time
import threading
from memory.client import write_memory

class ElasticAgent(threading.Thread):
    def __init__(self, agent_id, role, objective):
        super().__init__(daemon=True)
        self.agent_id = agent_id
        self.role = role
        self.objective = objective
        self.score = 0

    def run(self):
        while True:
            self.score += 1
            write_memory({
                "scope": "agent_activity",
                "importance": min(10, self.score),
                "confidence": 0.9,
                "content": {
                    "agent_id": self.agent_id,
                    "role": self.role,
                    "objective": self.objective,
                    "score": self.score
                },
                "tags": ["elastic-agent", self.role]
            })
            time.sleep(5)
