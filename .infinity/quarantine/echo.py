class EchoExecutive:
    NAME = 'ECHO'
    ROLE = 'Executive AI Assistant'

    def __init__(self, orchestrator):
        self.orchestrator = orchestrator

    def command(self, intent: str, payload: dict):
        return self.orchestrator.execute(intent, payload)

    def report(self, message: str):
        print(f'[ECHO REPORT] {message}')
