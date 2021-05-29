import os
from models.Tickets import Tickets
from models.Order import Orders
from exceptions import (
    TicketAlreadyExistsException,
    TicketDoesNotExistsException
)

def reformat_order(order):
    return {
        "status": order['status'], 
        "expiresAt":order['expiresAt'],
        "userId":order['userId'],
         "ticket": order['ticket'],
         "version": order['version'],
        }
def insert_into_db(userId, status, expiresAt, ticket, version):
    Orders(
        userId=userId, 
        status=status, 
        expiresAt=expiresAt,
        ticket=ticket,
        version=version
        ).save()
    order = get_order_from_db(userId=userId, expiresAt=expiresAt)
    return reformat_order(order=order)

def get_ticket_from_db(title):
    print(title)
    ticket = Tickets.objects(title=title).first()
    print(ticket)
    if ticket is None:
        raise TicketDoesNotExistsException()
    return ticket

def get_order_from_db(userId,expiresAt):
    order = Orders.objects(userId=userId, expiresAt=expiresAt).first()
    if order is None:
        raise OrderDoesNotExistsException()
    return order

def is_ticket_reserved(ticket):
    orders = Orders.objects(ticket=ticket)
    reserved_order = filter(lambda order: (order.status != 'cancel') , orders)
    return True if reserved_order else False

def get_order_with_id(id):
    order = res = Orders.objects(id=id).first()
    print(order)
    if order is None:
        raise OrderDoesNotExistsException()
    return order

def get_ticket_with_id(id):
    ticket = res = Tickets.objects(id=id).first()
    print(ticket)
    if ticket is None:
        raise TicketDoesNotExistsException()
    return ticket