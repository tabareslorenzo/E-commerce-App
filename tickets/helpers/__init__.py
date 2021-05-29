import os
from models.Tickets import Tickets
from exceptions import (
    TicketAlreadyExistsException,
    TicketDoesNotExistsException
)


def insert_into_db(title, price, userId):
    Tickets(title=title, price=price, userId=userId).save()
    ticket = Tickets.objects(title=title).first()
    return {
        "title": ticket['title'], 
        "price":ticket['price'],
        "userId":ticket['userId']
        }

def get_ticket_from_db(title):
    print(title)
    ticket = Tickets.objects(title=title).first()
    print(ticket)
    if ticket is None:
        raise TicketDoesNotExistsException()
    return ticket

def get_ticket_with_id(id):
    ticket = res = Tickets.objects(id=id).first()
    print(ticket)
    if ticket is None:
        raise TicketDoesNotExistsException()
    return ticket

def update_ticket(id, title, price):
    res = get_ticket_with_id(id)
    res.update(title=title, price=price)
    return get_ticket_with_id(id)