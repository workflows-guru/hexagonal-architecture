from tscheduler.domain.models import Task
from tscheduler.ports.executor import ExecutorInterface
from tscheduler.ports.storage import StorageInterface


class TaskController:
    # Here we use Constructor injection we can as well use method injection
    def __init__(
        self,
        storage: StorageInterface | None = None,
        executor: ExecutorInterface | None = None,
    ):
        self.storage = storage
        self.executor = executor

    def create_task(self, name: str, description: str, data: str) -> dict:

        # In your big application consider using Data Transfer Object, to not leak domain model to external dependency...
        task = Task(name=name, description=description, data=data)

        # Our business logic is implemented here

        # In your big application consider using Data Transfer Object, to not leak domain model to external dependency...
        created_task = self.storage.create_task(
            name=task.name, description=task.description, data=task.data
        )

        return created_task

    def read_task(self, name: str) -> dict | None:

        return self.storage.read_task(name=name)

    def execute_task(self, name: str) -> str:

        task = self.storage.read_task(name=name)
        task = Task(**task)

        # Our business logic is implemented here

        # For demonstration purpose our executor accept any str and return any str
        execution_id = self.executor.execute_task(data=task.data)
        return execution_id
