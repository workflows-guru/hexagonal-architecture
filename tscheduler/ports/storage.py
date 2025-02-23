from abc import ABC, abstractmethod


class StorageInterface(ABC):
    """Storage interface that should be implemented by our storage systems"""

    @abstractmethod
    def create_task(self, name: str, description: str, data: str) -> dict:
        raise NotImplementedError

    @abstractmethod
    def read_task(self, name) -> dict | None:
        raise NotImplementedError
