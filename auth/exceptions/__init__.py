class EmptyPasswordException(Exception):
    message = "Password is a required field!"
    def __init__(self):
        super().__init__(EmptyPasswordException.message)
    @staticmethod
    def get_message():
        return EmptyPasswordException.message

class InvalidPasswordLengthException(Exception):
    message = "Password must be between 4 and 20 characters!"
    def __init__(self):
        super().__init__(InvalidPasswordLengthException.message)
    @staticmethod
    def get_message():
        return InvalidPasswordLengthException.message

class InvalidEmailException(Exception):
    message = "Email must be valid!"
    def __init__(self):
        super().__init__(InvalidEmailException.message)
    @staticmethod
    def get_message():
        return InvalidEmailException.message
class EmptyEmailException(Exception):
    message = "Email is a required field!"
    def __init__(self):
        super().__init__(EmptyEmailException.message)
    @staticmethod
    def get_message():
        return EmptyEmailException.message