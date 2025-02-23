from tscheduler.adapters.local_executor import LocalExecutor
from tscheduler.adapters.local_storage import LocalStorage
from tscheduler.domain.core import TaskController

controller = TaskController(storage=LocalStorage(), executor=LocalExecutor())

controller.create_task(
    name="my_task", description="First task", data="Task Content Script"
)

my_task = controller.read_task(name="my_task")
print(my_task)


execution_id = controller.execute_task(name="my_task")

print(execution_id)
