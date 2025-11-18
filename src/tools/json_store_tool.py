import json
from pathlib import Path

class JSONStoreTool:
    def __init__(self, path="data/store.json"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

        if not self.path.exists():
            self.path.write_text(json.dumps({}))

    def save(self, key, value):
        data = json.loads(self.path.read_text()) if self.path.exists() else {}
        data[key] = value
        self.path.write_text(json.dumps(data, indent=2))

    def load(self, key):
        data = json.loads(self.path.read_text()) if self.path.exists() else {}
        return data.get(key)
