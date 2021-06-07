import os
from models.Ticket import Tickets
from models.Order import Orders
import requests
from exceptions import (
    OrderDoesNotExistsException,
    TicketDoesNotExistsException,
    TicketAlreadyReservedException
)

from bson import json_util
import json

ORDER_CANCELLED = "ordercancelled"
ORDER_CREATED = "ordercreated"
STATUS_COMPLETE = "complete"
STATUS_CANCELLED = "cancelled"

def reformat_order(order):
    ticket = order['ticket']
    Obj = {
        "id": ticket['id'],
        "title": ticket['title'], 
        "price":ticket['price'],
        "userId":ticket['userId']
        }
    ticket_reformated = Obj
    
    order = {
        "id": order['id'],
        "status": order['status'], 
        "expiresAt":order['expiresAt'],
        "userId":order['userId'],
         "ticket": order['ticket'],
         "version": order['version'],
        }
    order['ticket'] = ticket_reformated
    return json.dumps(order, default=json_util.default)
def insert_into_db(userId, status, expiresAt, ticket, version):
    Orders(
        userId=userId, 
        status=status, 
        expiresAt=expiresAt,
        ticket=ticket,
        version=version
        ).save()
    order = get_order_from_db(userId=userId, expiresAt=expiresAt)
    reformated = reformat_order(order=order)
    send_created_event(reformated)
    return reformated

def get_orders_from_user(user):
    order = Orders.objects(userId=user)
    return order

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
    reserved_order = list(filter(lambda order: (order.status != 'cancelled') , orders))
    print(len(reserved_order))
    if reserved_order:
        raise TicketAlreadyReservedException()
    return False
    
def delete_order(id):
    order = get_order_with_id(id)
    reformated = reformat_order(order=order)
    if order['status'] == STATUS_COMPLETE:
        return reformated
    send_cancelled_event(reformated)
    order.delete()
    return reformated

def get_order_with_id(id):
    order = Orders.objects(id=id).first()
    print(order)
    if order is None:
        raise OrderDoesNotExistsException()
    return order

def get_ticket_with_id(id):
    ticket = Tickets.objects(id=id).first()
    print(ticket is None)
    print(ticket)
    if ticket is None:
        raise TicketDoesNotExistsException()
    return ticket

def send_cancelled_event(order):
    myobjc = {
    "type": ORDER_CANCELLED,
    "data": order
    }
    requests.post(
        'http://localhost:6005/api/eventbus/events',
        json= myobjc
    )

def send_created_event(order):
    print(ord)
    myobjc = {
    "type": ORDER_CREATED,
    "data": order
    }

    requests.post(
        'http://localhost:6005/api/eventbus/events',
        json = myobjc
    )


def handle_updated(data):
    ticket = get_ticket_with_id(data['id'])
    ticket.update(
        title=data['title'],
        price=data['price']
    )

def handle_created(data):
    print("handle created")
    try:
        Tickets(
            id=data['id'],
            title=data['title'],
            price=data['price'],
            userId = data['userId'],
        ).save()
    except Exception as e:
        print(e)
    print(Tickets.objects(
        title=data['title'],
        price=data['price'],
        userId = data['userId'],
        ).first()["userId"])
    return Tickets.objects(
        title=data['title'],
        price=data['price'],
        userId = data['userId'],
        ).first()
    
def handle_payment(data):
    order = get_order_with_id(data['orderId'])
    order.update(status=STATUS_COMPLETE)
    return order

def handle_expired(data):
    # iterate through dict of order objects
    for key in data:
        print(data[key])
        print(key)
        order = get_order_with_id(data[key]['orderId'])
        if order['status'] == STATUS_COMPLETE:
            return data
        order.update(status=STATUS_CANCELLED)
        order = reformat_order(order=order)
        send_cancelled_event(order)
    return data

def handle_event(data):
    print("handle event")
    if data['type'].lower().strip() == "expiredcreated":
        return handle_expired(data['data'])
    if data['type'].lower().strip() == "paymentcreated":
        return handle_payment(data['data'])
    if data['type'].lower().strip() == "ticketcreated":
        return handle_created(data['data'])
    if data['type'].lower().strip() == "ticketupdated":
        return handle_updated(data['data'])

