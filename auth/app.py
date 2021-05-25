import json
import dateutil.parser
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify, session
import os

from flask_mongoengine import MongoEngine

app = Flask(__name__)

# from signup import *
from signin import *

app.config['MONGODB_SETTINGS'] = {
    'db': os.environ.get("MONGO_DB_NAME", "auth"),
    'host': os.environ.get("MONGO_SERVICE_HOST", "localhost"),
    'port': int(os.environ.get("MONGO_SERVICE_PORT", "27017"))
}
db = MongoEngine()
db.init_app(app)
print(app.config['MONGODB_SETTINGS'])

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 6000))
    app.run(debug=True, host='0.0.0.0', port=port)