from abc import ABC, abstractmethod
from model import Task
from storage import Storage

class TaskRequests(ABC):
    @abstractmethod
    def execute(self):
        pass
    
class AddTaskCommand(TaskRequests):
    def __init__(self, storage: Storage):
        self.storage = storage

    def execute(self):
        title = input("Название задачи: ")
        description = input("Описание задачи: ")
        category = input("Категория задачи: ")
        priority = input("Приоритет (низкий, средний, высокий): ")

        tasks = self.storage.load_tasks()

        newId = self.storage.lastID + 1

        newTask = Task(
            id = newId, 
            title = title.capitalize().strip(), 
            description = description.capitalize().strip(),
            category = category.capitalize().strip(),
            priority = priority.capitalize().strip()
        )

        tasks[str(newId)] = newTask.to_dict()

        self.storage.save_tasks(tasks)

        self.storage.lastID = newId

        print("Yes!")

class DeleteTaskCommand(TaskRequests):
    def __init__(self, storage: Storage):
        self.storage = storage

    def execute(self):
        pass
    
class ViewTaskCommand(TaskRequests):
    def __init__(self, storage: Storage):
        self.storage = storage

    def execute(self):
        tasks = self.storage.load_tasks()

        for key, task in tasks.items():
            for key, value in task.items():
                if key == "id":
                    print("-" * 30)
                print(f"{key}: {value}")
                
