import pymongo
from mongoengine import *
from app import db
from datetime import datetime

print("db", db)
class events(db.Document):
    eventType = StringField(required=True)
    data = DictField(required=True)