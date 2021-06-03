class TicketDoesNotExistsException(Exception):
    message = "Ticket Does not Exist!"
    def __init__(self):
        super().__init__(TicketDoesNotExistsException.message)
    @staticmethod
    def get_message():
        return TicketDoesNotExistsException.message

class OrderDoesNotExistsException(Exception):
    message = "Order Does not Exist!"
    def __init__(self):
        super().__init__(OrderDoesNotExistsException.message)
    @staticmethod
    def get_message():
        return OrderDoesNotExistsException.message

class TicketAlreadyReservedException(Exception):
    message = "Ticket Already Reserved!"
    def __init__(self):
        super().__init__(TicketAlreadyReservedException.message)
    @staticmethod
    def get_message():
        return TicketAlreadyReservedException.message

class OrderDoesNotBelongToYouException(Exception):
    message = "Order Does not Belong To You!"
    def __init__(self):
        super().__init__(OrderDoesNotBelongToYouException.message)
    @staticmethod
    def get_message():
        return OrderDoesNotBelongToYouException.message