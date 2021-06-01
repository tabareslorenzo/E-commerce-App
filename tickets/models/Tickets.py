import pymongo
from mongoengine import *
from app import db

print("db", db)
class Tickets(db.Document):
    title = StringField(required=True)
    price = IntField(required=True)
    userId = StringField(required=True)
    orderId = StringField()