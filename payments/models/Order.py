import pymongo
from mongoengine import *
from app import db
from datetime import datetime

print("db", db)
class Orders(db.Document):
    userId = StringField(required=True)
    status = StringField(required=True)
    expiresAt = DateTimeField()
    version = IntField(required=True)
    price = IntField(required=True)
    orderId = StringField(required=True)

