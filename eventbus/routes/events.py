import json
import dateutil.parser
import os
from app import app
import requests
# from validator import validate_password, validate_email
from helpers import (
    send_event_to,
    insert_into_db,
    get_events_from_db
)
from exceptions import (
    InsertExpireToDBException
)
from flask import (
    Flask, 
    abort, 
    request, 
    Response, 
    flash, 
    redirect, 
    url_for, 
    jsonify, 
    session
)



@app.route('/api/eventbus/events', methods=['POST'])
def get_events():
    try:
        events = get_events_from_db()
        return events
    except InsertExpireToDBException:
        abort(500, InsertExpireToDBException.get_message())

@app.route('/api/eventbus/events', methods=['GET'])
def events():
    data = request.get_json()
    print(data)
    try:
        event_data = data['data']
        event_type = data["type"]
        insert_event_into_db(event_data, event_type)
        send_event_to(port=6000, service='auth', data=data)
        send_event_to(port=6001, service='tickets', data=data)
        send_event_to(port=6002, service='orders', data=data)
        send_event_to(port=6003, service='payments', data=data)
        send_event_to(port=6004, service='expiration', data=data)
        return {"status": "Ok"}
    except InsertEventToDBException:
        abort(500, InsertEventToDBException.get_message())

@app.errorhandler(500)
def unprocessable(error):
    return jsonify({
    "Success" : False,
    "error": 500,
    "message": f"Internal server error: {error.description}"
    }), 500

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
    "Success" : False,
    "error": 422,
    "message": f"unprocessable: {error.description}"
    }), 422

@app.errorhandler(404)
def not_found(error):
    return jsonify({
    "Success": False,
    "error" : 404,
    "message" : "resource not found"
    }), 404