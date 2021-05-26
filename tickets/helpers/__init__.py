import os
from models.Tickets import Tickets
from exceptions import (
    TicketAlreadyExistsException,
    TicketDoesNotExistsException
)


def insert_into_db(title, price, userId):
    if Tickets.objects(title=title).first() is None:
        Tickets(title=title, price=price, userId=userId).save()
        ticket = Tickets.objects(title=title).first()
        return {
            "title": ticket['title'], 
            "price":ticket['price'],
            "userId":ticket['userId']

            }
    else:
        raise TicketAlreadyExistsException()

def get_user_from_db(email):
    ticket = Tickets.objects(title=title).first()
    if ticket is None:
        raise TicketDoesNotExistsException()
    return user