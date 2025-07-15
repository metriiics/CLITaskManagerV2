from abc import ABC, abstractmethod

class TaskRequests(ABC):
    @abstractmethod
    def execute(self, task):
        pass



