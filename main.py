from fastapi import FastAPI
from pydantic import BaseModel

from tscheduler.adapters.local_executor import LocalExecutor
from tscheduler.adapters.local_storage import LocalStorage
from tscheduler.domain.core import TaskController

app = FastAPI()


class Task(BaseModel):
    name: str
    description: str
    data: str

"""
You may use http adapter here for me it will just overcomplicate the app

This is just to get the task from the memory
"""
controller = TaskController(storage=LocalStorage(), executor=LocalExecutor())

@app.post("/tasks")
def create_task(task: Task):
    return controller.create_task(
        name=task.name, description=task.description, data=task.data
    )


@app.get("/tasks/{task_name}")
def read_task(task_name: str):
    task = controller.read_task(name=task_name)
    return task


# Don't say to me that this is not REST call :)
@app.post("/tasks/{task_name}/execute")
def execute_task(task_name: str):
    execution_id = controller.execute_task(name=task_name)
    return {"execution_id": execution_id}
