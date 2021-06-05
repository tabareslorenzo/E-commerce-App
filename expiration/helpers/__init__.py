from models.expiration import expiration
from datetime import datetime, timedelta
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
    expireTime = datetime.fromtimestamp(expireTime / 1e3)
    print(expireTime, "00000000")
    error = False
    try:
        expire = expiration(orderID=orderID, expireTime=expireTime, isSent=isSent)
        db.session.add(expire)
        db.session.commit()
    except Exception as e:
        print(e)
        error = True
        db.session.rollback()
    finally:
        db.session().close()
        if error:
            raise InsertExpireToDBException()
        else:
            print(f'Order {orderID} was successfully listed!')
    expire = db.session.query(expiration).filter(
        expiration.orderID==orderID, 
        expiration.expireTime==expireTime, 
        expiration.isSent==isSent).one()
    print(expire)
    return reformat_expire(expire)

def query_db_for_expired_orders(run):
    while run.value:
        print(datetime.utcnow() - timedelta(hours=4), "00000000")
        expired_orders = db.session.query(expiration).filter(
            expiration.expireTime < datetime.utcnow() -  timedelta(hours=4),
            expiration.isSent == False
            ).all()
        notify_order_service(expired_orders) if len(expired_orders) > 0 else None
        update_sent_orders(expired_orders)
        time.sleep(1)

def notify_order_service(expired_orders):
    expired_orders = dict((expired.id,dict_expire(expired)) for expired in expired_orders)
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
        print(order, "wwwwwww")
        _order = db.session.query(expiration).filter(expiration.orderID == order.orderID).first()
        _order.isSent = True
        print(_order, "wwwwwww")
        print(_order.id)
        print(_order.orderID)
        print(_order.isSent)
        print(_order.expireTime)
        db.session.commit()

def handle_created(data):
    print(data)
    expire = insert_into_db(
        data["id"], 
        data["expiresAt"]["date"], 
        False
    )
    return expire

def handle_event(data):
    print(data["type"].lower().split())
    if data["type"].lower() == "ordercreated":
        return handle_created(data["data"])
    return None
def reformat_expire(expire):
    return {
        "id": expire.id,
        "orderId": expire.orderID,
        "isSent": expire.isSent,
        "expireTime": str(expire.expireTime)
    }
def dict_expire(expire):
    return {
       
        "orderId": expire.orderID,
        "isSent": expire.isSent,
        "expireTime": str(expire.expireTime)
       
    }