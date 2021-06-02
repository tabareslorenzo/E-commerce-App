from models.expiration import expiration
from app import db
from datetime import datetime
import requests
from exceptions import (
    InsertExpireToDBException
)
import asyncio

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
            expiration.expireTime < datetime.utcnow,
            expiration.isSent == False
            ).all()
        notify_order_service(expired_orders)
        update_sent_orders(expired_orders)
        asyncio.sleep(1)

def notify_order_service(expired_orders):
    myobjc = {
        "type": EXPIRE_TYPE,
        "data": expired_orders
    }
    r = requests.post(
        'http://localhost:6005/api/eventbus/events',
        data= myobjc
    )


def update_sent_orders(orders):
    for order in orders:
        _order = db.session.query(expiration).filter(expiration.orderID == order.id)
        _order.isSent = True
    