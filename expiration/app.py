from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify, session
import os
from multiprocessing import Process, Value
from dotenv import load_dotenv
load_dotenv('./.env')

app = Flask(__name__)


user = os.getenv("USERNAME")
paswd = os.getenv("PASSWORD")

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{paswd}@localhost/expiration'

from routes.events import *
from helpers import query_db_for_expired_orders

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 6004))
    recording_on = Value('b', True)
    p = Process(target=query_db_for_expired_orders, args=(recording_on,))
    p.start()  
    app.run(debug=True, host='0.0.0.0', port=port, use_reloader=False)
    p.join()