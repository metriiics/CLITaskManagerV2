import json

class Storage: 
    def __init__(self, filename):
        self.filename = filename
        self.tasks = self.load_tasks()
        self.lastID = max((int(k) for k in self.tasks.keys()), default=0)

    def load_tasks(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)

                if not isinstance(data, dict):
                    return {}
                
                return data
            except json.decoder.JSONDecodeError:
                return {}

    def save_tasks(self, data):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(
                data, 
                file, 
                ensure_ascii=False, 
                indent=4
            )

    