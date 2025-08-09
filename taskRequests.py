from abc import ABC, abstractmethod
from model import Task
from storage import Storage
from exception import EmptyFieldError, InvalidFieldError

class TaskRequests(ABC):
    @abstractmethod
    def execute(self):
        pass
    
class AddTaskCommand(TaskRequests):
    def __init__(self, storage: Storage):
        self.storage = storage

    def execute(self):
        input_data = {}

        for field, promt in Task.get_fields():
            while True:
                value = input(f"{promt}: ")
                try:
                    if field == "title" and not value:
                        raise EmptyFieldError()
                    
                    break
                except EmptyFieldError as e:
                    print(f"{e}\nПопробуйте еще разю")

            input_data[field] = value

        tasks = self.storage.load_tasks()

        newId = self.storage.lastID + 1

        newTask = Task(
            id = newId, 
            title = input_data["title"].capitalize().strip(), 
            description = input_data["description"].capitalize().strip(),
            category = input_data["category"].capitalize().strip(),
            priority = input_data["priority"].capitalize().strip()
        )

        tasks[str(newId)] = newTask.to_dict()

        self.storage.save_tasks(tasks)

        self.storage.lastID = newId

        print("Success!")

class DeleteTaskCommand(TaskRequests):
    def __init__(self, storage: Storage):
        self.storage = storage

    def execute(self):
        try:
            id = input("Введите id задачи для удаления: ")

            tasks = self.storage.load_tasks()

            if not id:
                raise EmptyFieldError()
            elif id not in tasks:
                raise InvalidFieldError()

            tasks.pop(id)

            self.storage.save_tasks(tasks)

            print("Success!")
        except Exception as e:
            print(f"{e}\nПопробуйте еще раз!")

    
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
                
class UpdateTaskCommand(TaskRequests):
    def __init__(self, storage: Storage):
        self.storage = storage

    def execute(self):
        try:
            id = input("Введите id задачи, которую хотите поменять: ")

            tasks = self.storage.load_tasks()

            if not id:
                raise EmptyFieldError()
            elif id not in tasks:
                raise InvalidFieldError()
            
            input_data = {}

            for field, promt in Task.get_fields():
                while True:
                    value = input(f"Новое {promt.lower()}: ")
                    try:
                        if field == "title" and not value:
                            raise EmptyFieldError()
                        
                        break
                    except EmptyFieldError as e:
                        print(f"{e}\nПопробуйте еще раз!")

                input_data[field] = value

            tasks[id] = input_data

            self.storage.save_tasks(tasks)

            print("Success!")
        except Exception as e:
            print(f"{e}\n Попробуйте еще раз!")

