from integrations.workspace.client import WorkspaceClient

class TasksAgent:
    def create_task(self, title, notes):
        WorkspaceClient().log('Tasks', 'create_task', {
            'title': title,
            'notes': notes
        })
