import pymongo
from mongoengine import *
from app import db
from datetime import datetime
from models import Ticket

print("db", db)
class Orders(db.Document):
    userId = StringField(required=True)
    status = StringField(required=True)
    expiresAt = DateTimeField()
    ticket = EmbeddedDocumentField(Ticket)
    version = IntField(required=True)