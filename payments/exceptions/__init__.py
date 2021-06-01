class OrderDoesNotExistsException(Exception):
    message = "Order Does not Exist!"
    def __init__(self):
        super().__init__(OrderDoesNotExistsException.message)
    @staticmethod
    def get_message():
        return OrderDoesNotExistsException.message

class UserNotOwnerException(Exception):
<<<<<<< HEAD
    message = "User does not own order!"
=======
    message = "You do not own this order!"
>>>>>>> 229bb3c7449bce0e3cb9783ba8979326953b650c
    def __init__(self):
        super().__init__(UserNotOwnerException.message)
    @staticmethod
    def get_message():
        return UserNotOwnerException.message

class CanceledOrderException(Exception):
<<<<<<< HEAD
    message = "Order was cancel!"
=======
    message = "Order was!"
>>>>>>> 229bb3c7449bce0e3cb9783ba8979326953b650c
    def __init__(self):
        super().__init__(CanceledOrderException.message)
    @staticmethod
    def get_message():
        return CanceledOrderException.message