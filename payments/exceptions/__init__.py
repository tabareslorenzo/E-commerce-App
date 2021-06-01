class OrderDoesNotExistsException(Exception):
    message = "Order Does not Exist!"
    def __init__(self):
        super().__init__(OrderDoesNotExistsException.message)
    @staticmethod
    def get_message():
        return OrderDoesNotExistsException.message

class UserNotOwnerException(Exception):
    message = "User does not own order!"
    def __init__(self):
        super().__init__(UserNotOwnerException.message)
    @staticmethod
    def get_message():
        return UserNotOwnerException.message

class CanceledOrderException(Exception):
    message = "Order was cancel!"
    def __init__(self):
        super().__init__(CanceledOrderException.message)
    @staticmethod
    def get_message():
        return CanceledOrderException.message