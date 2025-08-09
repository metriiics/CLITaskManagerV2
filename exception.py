class EmptyFieldError(Exception):
    def __init__(self, message = "[ERROR] Значение не должно быть пустым!"):
        super().__init__(message)

class InvalidFieldError(Exception):
    def __init__(self, message = "[ERROR] Значение не корректно!"):
        super().__init__(message)
