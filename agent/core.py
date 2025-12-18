class AgentCore:
    def __init__(self, name: str):
        self.name = name

    def start(self):
        raise NotImplementedError

    def stop(self):
        pass
