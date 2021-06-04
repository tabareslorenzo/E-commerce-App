import json
import dateutil.parser
import os
from app import app
import requests
from bson import json_util
# from validator import validate_password, validate_email
from helpers import (
    send_event_to,
    insert_into_db,
    get_events_from_db
)
from exceptions import (
    InsertEventToDBException
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



@app.route('/api/eventbus/getevents', methods=['POST'])
def get_events():
    try:
        events = get_events_from_db()
        return events
    except InsertExpireToDBException:
        abort(500, InsertExpireToDBException.get_message())

@app.route('/api/eventbus/events', methods=['POST'])
def events():
    data = request.get_json()
    # print(data)
    # print(type(data))
    try: 
        print(type(data['data']))
        print(data['data'])
        if type(data['data']) == type("str"):
            event_data = json.loads(data['data'])
            print("ticket" in event_data)
            id = event_data["id"]["$oid"]
            del event_data["id"]
            event_data["id"] = id
            
            if "ticket" in event_data:
                print("event_data")
                id = event_data["ticket" ]["id"]["$oid"]
                del event_data["ticket" ]["id"]
                event_data["ticket" ]["id"] = id
                event_data['expiresAt']['date'] = event_data['expiresAt']['$date']
                del event_data['expiresAt']['$date']

        else:
            event_data = data['data']
        print(event_data,"-======")
        event_type = data["type"]
        print(event_type, "-======")

        insert_into_db(event_data, event_type)
        print("what")
        send_event_to(port=6001, service='tickets', data=data)
        send_event_to(port=6002, service='orders', data=data)
        send_event_to(port=6003, service='payments', data=data)
        send_event_to(port=6004, service='expiration', data=data)
        return {"status": "Ok"}
    except InsertEventToDBException:
        abort(500, InsertEventToDBException.get_message())
    except Exception as e:
        print(e)
        return {"err": True}

@app.errorhandler(500)
def servererrer(error):
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