class InsertEventToDBException(Exception):
    message = "Inserting event to DB failed!"
    def __init__(self):
        super().__init__(InsertEventToDBException.message)
    @staticmethod
    def get_message():
        return InsertEventToDBException.message