import logging

class EchoExecutive:
    NAME = 'ECHO'
    ROLE = 'Executive AI Assistant'

    def __init__(self, orchestrator):
        self.orchestrator = orchestrator

    def command(self, intent: str, payload: dict):
        return self.orchestrator.execute(intent, payload)
        logging.info(f'[ECHO REPORT] {message}')
    def report(self, message: str):
        logging.info(f'[ECHO REPORT] {message}')
