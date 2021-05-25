import pymongo
import os
from mongoengine import *

class User(Document):
    email = StringField(required=True)
    password = StringField(required=True, max_length=20)


def check_db_connection():
    try:
        client = MongoClient(
          #db=os.environ.get("MONGO_SERVICE_DB", "sarm"),
          host=os.environ.get("MONGO_SERVICE_HOST", "localhost"),
          port=int(os.environ.get("MONGO_SERVICE_PORT", "27017")),
          username=os.environ.get("MONGODB_USERNAME"),
          password=os.environ.get("MONGODB_PASSWORD"),
          authSource=os.environ.get("MONGO_SERVICE_AUTH_DB", "admin"),
          serverSelectionTimeoutMS = 1000
        )
        client.server_info()
        logging.info("Health check passed: Database is connected")
        status = {
          'status': 200,
          'message': "Database health check passed: Database is currently connected"
        }
        return jsonify(status)
    except: 
        logging.error("WARNING: CONNECTION TO DB ERROR")
        status = {
          'status': 503,
          'message': "Database health check failed: Please contact developer!"
        }
        return jsonify(status)