import json
import dateutil.parser
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify, session
import os
from flask_cors import CORS, cross_origin

from flask_mongoengine import MongoEngine

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})



app.config['MONGODB_SETTINGS'] = {
    'db': os.environ.get("MONGO_DB_NAME", "auth"),
    'host': os.environ.get("MONGO_SERVICE_HOST", "localhost"),
    'port': int(os.environ.get("MONGO_SERVICE_PORT", "27017"))
}
db = MongoEngine()
db.init_app(app)
print(app.config['MONGODB_SETTINGS'])
print(cors)

from routes.signup import *
from routes.signin import *
from routes.tokenauth import *
from routes.signout import *

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 6000))
    app.run(debug=True, host='0.0.0.0', port=port)