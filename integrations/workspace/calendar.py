from integrations.workspace.client import WorkspaceClient

class CalendarAgent:
    def create_event(self, title, description):
        WorkspaceClient().log('Calendar', 'create_event', {
            'title': title,
            'description': description
        })
