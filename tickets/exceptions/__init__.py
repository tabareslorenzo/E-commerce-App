class TicketAlreadyExistsException(Exception):
    message = "Ticket with that title already exists!"
    def __init__(self):
        super().__init__(TicketAlreadyExistsException.message)
    @staticmethod
    def get_message():
        return TicketAlreadyExistsException.message

class TicketDoesNotExistsException(Exception):
    message = "Ticket Does not Exist!"
    def __init__(self):
        super().__init__(TicketDoesNotExistsException.message)
    @staticmethod
    def get_message():
        return TicketDoesNotExistsException.message