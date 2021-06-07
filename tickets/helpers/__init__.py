import os
from models.Tickets import Tickets
from exceptions import (
    TicketAlreadyExistsException,
    TicketDoesNotExistsException
)
from bson import json_util
import json
import requests

TICKET_UPDATED = "ticketupdated"

def insert_into_db(title, price, userId):
    Tickets(title=title, price=price, userId=userId).save()
    ticket = Tickets.objects(title=title, price=price, userId=userId).first()
    Obj = {
        "id": ticket['id'],
        "title": ticket['title'], 
        "price":ticket['price'],
        "userId":ticket['userId'],
        "orderId":ticket['orderId']
        }
    return json.dumps(Obj, default=json_util.default)
def get_all_ticket_from_db():
    ticket = Tickets.objects(orderId=None)
    return ticket
def get_ticket_from_db(title):
    print(title)
    ticket = Tickets.objects(title=title).first()
    print(ticket)
    if ticket is None:
        raise TicketDoesNotExistsException()
    return ticket

def get_ticket_with_id(id):
    ticket = Tickets.objects(id=id).first()
    print(ticket)
    if ticket is None:
        raise TicketDoesNotExistsException()
    return ticket

def update_ticket(id, title, price):
    res = get_ticket_with_id(id)
    res.update(title=title, price=price)
    ticket =  get_ticket_with_id(id)
    return {
        "id": ticket['id'],
        "title": ticket['title'], 
        "price":ticket['price'],
        "userId":ticket['userId'],
        "orderId":ticket['orderId']
        }

def handle_cancel(data):
    ticket = get_ticket_with_id(data['ticket']['id'])
    if ticket is None:
        raise TicketDoesNotExistsException()
    ticket.update(orderId=None)
    ticket = {
        "id": ticket['id'],
        "title": ticket['title'], 
        "price":ticket['price'],
        "userId":ticket['userId'],
        "orderId":ticket['orderId']
        }
    send_update_event(ticket)
    print(ticket)
    return ticket

def handle_created(data):
    ticket = get_ticket_with_id(data['ticket']['id'])
    if ticket is None:
        raise TicketDoesNotExistsException()
    print(data['id'])
    ticket.update(orderId=data['id'])
    print(ticket)
    print(ticket, "00000")
    print(ticket, "00000")
    ticket = {
        "id": ticket['id'],
        "title": ticket['title'], 
        "price":ticket['price'],
        "userId":ticket['userId'],
        "orderId":ticket['orderId']
        }
    print(ticket)
    send_update_event(ticket)
    return ticket

def handle_event(data):
    if data["type"].lower().strip() == "ordercancelled":
        res = handle_cancel(data['data'])
        return json.dumps(res, default=json_util.default)
    if data["type"].lower().strip() == "ordercreated":
        res = handle_created(data['data'])
        return json.dumps(res, default=json_util.default)
    return None

def send_update_event(ticket):
    t = json.dumps(ticket, default=json_util.default)
    myobjc = {
    "type": TICKET_UPDATED,
    "data": t
    }

    requests.post(
        'http://localhost:6005/api/eventbus/events',
        json= myobjc
    )
        

