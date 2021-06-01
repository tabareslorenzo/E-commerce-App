from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify, session
import os
from flask_sqlalchemy import SQLAlchemy
from multiprocessing import Process, Value
from helpers import query_db_for_expired_orders


app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/expiration'
db = SQLAlchemy(app)
from routes.events import *

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 6004))
    recording_on = Value('b', True)
    p = Process(target=query_db_for_expired_orders, args=(recording_on,))
    p.start()  
    app.run(debug=True, host='0.0.0.0', port=port, use_reloader=False)
    p.join()