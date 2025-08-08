from taskRequests import AddTaskCommand, DeleteTaskCommand, ViewTaskCommand
from storage import Storage

class Command:
    def __init__(self, storage):
        self.commands = {
            "add": AddTaskCommand(storage),
            "delete": DeleteTaskCommand(storage),
            "show": ViewTaskCommand(storage)
        }

    def run(self):
        while True:
            user_input = input("Введите команду (add, delete, show, exit): ").strip().lower()
            if user_input == "exit":
                print("End!")
                break

            command = self.commands.get(user_input)
            if command:
                command.execute()
            else:
                print("Неизвестная команда!")

if __name__ == "__main__":
    storage = Storage("database.json")
    cmd = Command(storage)
    cmd.run()
        