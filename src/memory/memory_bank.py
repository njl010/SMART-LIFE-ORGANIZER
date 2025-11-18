import json
from pathlib import Path

class MemoryBank:
    def __init__(self, path="data/memory.json"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

        if not self.path.exists():
            self.path.write_text(json.dumps({"profiles": {}}))

    def save_user_summary(self, summary, user_id="default"):
        data = json.loads(self.path.read_text())
        profile = data["profiles"].setdefault(user_id, {})
        profile.setdefault("summaries", []).append(summary)
        self.path.write_text(json.dumps(data, indent=2))

    def get_user_profile(self, user_id="default"):
        data = json.loads(self.path.read_text())
        return data["profiles"].get(user_id, {})
