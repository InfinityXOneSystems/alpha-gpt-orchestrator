from github import Github

class GitHubExecutor:
    def __init__(self, token):
        self.client = Github(token)

    def list_org_repos(self, org):
        return [r.full_name for r in self.client.get_organization(org).get_repos()]

    def write_file(self, repo, path, content, message):
        r = self.client.get_repo(repo)
        try:
            f = r.get_contents(path)
            r.update_file(path, message, content, f.sha)
        except:
            r.create_file(path, message, content)
