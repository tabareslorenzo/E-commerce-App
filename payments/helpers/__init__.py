import os
from models.Order import Orders
from models.Payment import Payments
from bson import json_util
import datetime
import json
from exceptions import (
    OrderDoesNotExistsException,
    UserNotOwnerException,
    CanceledOrderException
)
CANCELED = "cancel"
PAYMENT_CREATED = "paymentcreated"

def insert_into_db(orderId, stripeId):
    Payments(orderId=orderId, stripeId=stripeId).save()
    payment = Payments.objects(stripeId=stripeId).first()
    return {
        "orderId": payment['orderId'], 
        "stripeId":payment['stripeId'],
    }

def get_order_with_id(id):
    order = Orders.objects(orderId=id).first()
    print(order)
    if order is None:
        raise OrderDoesNotExistsException()
    return order

def correct_user(curuserId, userId):
    if curuserId != userId:
        raise UserNotOwnerException
def is_canceled(status):
    if status == CANCELED:
        raise CanceledOrderException()

def send_update_event(payment):
    myobjc = {
    "type": PAYMENT_CREATED,
    "data": payment
    }
    requests.post(
        'http://localhost:6005/api/eventbus/events',
        json= myobjc
    )

def reformat_order(order):
    return {
            "userId": order['userId'], 
            "status":order['status'],
            "expiresAt": order['expiresAt'], 
            "status":order['status'],
            "version": order['version'],
            "price":order['price'], 
        }

def handle_created(data):
    userId = data['userId']
    status = data['status'] 
    expiresAt = json.loads(str(data['expiresAt']['date']), object_hook=json_util.object_hook)
    expiresAt = datetime.datetime.fromtimestamp(expiresAt / 1e3)
    print(expiresAt)
    print(data)
    version = data['version']
    price = data['ticket']['price']
    orderId = data['id']
    Orders(
        userId=userId, 
        status=status,
        expiresAt=expiresAt,
        version=version,
        price=price,
        orderId=orderId
    ).save()
    order = Orders.objects(userId=userId,expiresAt=expiresAt).first()
    return reformat_order(order)

def handle_cancel(data):
    order = get_order_with_id(data['id'])
    order.update(status=CANCELED)
    return reformat_order(order)

def handle_event(data):
    if data["type"].lower().strip() == "ordercancelled":
        return handle_cancel(data["data"])
    if data["type"].lower().strip() == "ordercreated":
        return handle_created(data["data"])  
    return None