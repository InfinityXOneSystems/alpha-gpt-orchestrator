import yaml
from pathlib import Path

class PluginLoader:
    def __init__(self, path='plugins'):
        self.path = Path(path)
        self.plugins = {}
        self.reload()

    def reload(self):
        self.plugins.clear()
        for f in self.path.glob('*.plugin.yaml'):
            with open(f) as fh:
                p = yaml.safe_load(fh)
                self.plugins[p['plugin']['id']] = p

    def list(self):
        return list(self.plugins.values())

    def get(self, pid):
        return self.plugins.get(pid)
