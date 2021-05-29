import pymongo
from mongoengine import *
from app import db
from datetime import datetime

print("db", db)
class Orders(db.Document):
    orderId = StringField(required=True)
    stripeId = StringField(required=True)