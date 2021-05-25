import pymongo
from mongoengine import *
from app import db

print("db", db)
class User(db.Document):
    email = StringField(required=True)
    password = StringField(required=True)