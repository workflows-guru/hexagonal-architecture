from tscheduler.adapters.local_storage import LocalStorage
from tscheduler.domain.core import TaskController

def test_create_task():

    # Here we have already a local storage, when we use other adapters we can just test our application using this adapter
    controller = TaskController(storage=LocalStorage())
    result = controller.create_task(
        name="my_task", description="First task", data="Task Content Script"
    )

    assert result.get("name") == "my_task"

