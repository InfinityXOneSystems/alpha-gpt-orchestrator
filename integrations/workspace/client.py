class WorkspaceClient:
    def log(self, service, action, payload):
        print(f'[WORKSPACE:{service}] {action} -> {payload}')
