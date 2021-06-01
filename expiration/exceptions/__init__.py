class InsertExpireToDBException(Exception):
    message = "Insert expire to DB Error!"
    def __init__(self):
        super().__init__(InsertExpireToDBException.message)
    @staticmethod
    def get_message():
        return InsertExpireToDBException.message