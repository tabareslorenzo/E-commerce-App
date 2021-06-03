from models.expiration import expiration
from datetime import datetime
import requests
from models.expiration import db, expiration
from exceptions import (
    InsertExpireToDBException
)
import asyncio
import time

db.create_all()

EXPIRE_TYPE = 'ExpiredCreated'
def insert_into_db(orderID, expireTime, isSent):
    
    try:
        expire = expiration(orderID=orderID, expireTime=expireTime, isSent=isSent)
        db.session.add(expire)
        db.session.commit()
    except:
        error = True
        db.session.rollback()
    finally:
        db.session().close()
        if error:
            raise InsertExpireToDBException()
        else:
            print(f'Order {orderID} was successfully listed!')
    return expire

def query_db_for_expired_orders(run):
    while run.value:
        expired_orders = db.session.query(expiration).filter(
            expiration.expireTime < datetime.utcnow(),
            expiration.isSent == False
            ).all()
        notify_order_service(expired_orders) if len(expired_orders) > 0 else None
        update_sent_orders(expired_orders)
        time.sleep(1)

def notify_order_service(expired_orders):
    myobjc = {
        "type": EXPIRE_TYPE,
        "data": expired_orders
    }
    r = requests.post(
        'http://localhost:6005/api/eventbus/events',
        json= myobjc
    )


def update_sent_orders(orders):
    for order in orders:
        _order = db.session.query(expiration).filter(expiration.orderID == order.id)
        _order.isSent = True

def handle_created(data):
    expire = insert_into_db(
        data["orderID"], 
        data["expireTime"], 
        data["isSent"]
    )
    return reformat_order(order)

def handle_event(data):
    if data["type"].lower().split() == "ordercreated":
        return handle_created(data["data"])
    return None