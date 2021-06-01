import pymongo
from mongoengine import *
from app import db
from datetime import datetime
from models.Ticket import Tickets

print("db", db)
class Orders(db.Document):
    userId = StringField(required=True)
    status = StringField(required=True)
    expiresAt = DateTimeField()
    ticket = ReferenceField(Tickets)
    version = IntField(required=True)