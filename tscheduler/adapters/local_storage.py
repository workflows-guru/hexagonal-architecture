from tscheduler.ports.storage import StorageInterface


class LocalStorage(StorageInterface):
    def __init__(self):
        self.tasks = []

    def create_task(self, name: str, description: str, data: str) -> dict:
        task = {"name": name, "description": description, "data": data}
        self.tasks.append(task)
        return task

    def read_task(self, name: str) -> dict | None:
        for item in self.tasks:
            if item.get("name") == name:
                return item
