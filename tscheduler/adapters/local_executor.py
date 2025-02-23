import uuid

from tscheduler.ports.executor import ExecutorInterface


class LocalExecutor(ExecutorInterface):

    def execute_task(self, data: str) -> str:

        print("Executing:", data)

        execution_id = uuid.uuid4().hex
        return execution_id
