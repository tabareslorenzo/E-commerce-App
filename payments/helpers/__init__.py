import os
from models.Order import Orders
from models.Payment import Payments
from exceptions import (
    OrderDoesNotExistsException,
    UserNotOwnerException,
    CanceledOrderException
)
CANCELED = "cancel"


def insert_into_db(orderId, stripeId):
    Payments(orderId=orderId, stripeId=stripeId).save()
    payment = Payments.objects(stripeId=stripeId).first()
    return {
        "orderId": payment['orderId'], 
        "stripeId":payment['stripeId'],
    }

def get_order_with_id(id):
    order = res = Orders.objects(id=id).first()
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

        
