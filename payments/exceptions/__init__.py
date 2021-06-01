class OrderDoesNotExistsException(Exception):
    message = "Order Does not Exist!"
    def __init__(self):
        super().__init__(OrderDoesNotExistsException.message)
    @staticmethod
    def get_message():
        return OrderDoesNotExistsException.message
