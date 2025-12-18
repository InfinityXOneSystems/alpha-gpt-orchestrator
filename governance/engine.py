class GovernanceEngine:
    def authorize(self, action, context=None):
        forbidden = ['delete','secret','iam','billing','kms']
        return not any(x in action.lower() for x in forbidden)
