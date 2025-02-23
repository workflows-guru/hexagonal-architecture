from abc import ABC, abstractmethod


class ExecutorInterface(ABC):
    """Executor interface that should be implemented by our executors"""

    @abstractmethod
    def execute_task(self, data: str) -> str:
        raise NotImplementedError
