from taskRequests import AddTaskCommand, DeleteTaskCommand, ViewTaskCommand, UpdateTaskCommand
from exception import InvalidFieldError, EmptyFieldError
from storage import Storage

class Command:
    def __init__(self, storage):
        self.commands = {
            "add": AddTaskCommand(storage),
            "del": DeleteTaskCommand(storage),
            "show": ViewTaskCommand(storage),
            "upd": UpdateTaskCommand(storage)
        }

    def run(self):
        while True:
            try:
                user_input = input("Введите команду (add, del, show, upd, exit): ").strip().lower()
                if user_input == "exit":
                    print("End!")
                    break

                command = self.commands.get(user_input)
                if command:
                    command.execute()
                elif not user_input:
                    raise EmptyFieldError()
                else:
                    raise InvalidFieldError()
            except Exception as e:
                print(f"{e}\nПопробуйте еще раз!")

if __name__ == "__main__":
    storage = Storage("database.json")
    cmd = Command(storage)
    cmd.run()
        