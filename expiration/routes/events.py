import json
import dateutil.parser
import os
from app import app
import requests
# from validator import validate_password, validate_email
from helpers import (
    handle_event,
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



@app.route('/api/expiration/events', methods=['POST'])
def events():
    data = request.get_json()
    # print(data)
    print(type(data['data']))
    print("whahah")
    if type(data['data']) == type("str"):
        print("event_data")
        event_data = json.loads(data['data'])
        id = event_data["id"]["$oid"]
        print("event_data")
        del event_data["id"]
        event_data["id"] = id
        print("event_data")
        if "ticket" in event_data:
            print("event_data")
            id = event_data["ticket" ]["id"]["$oid"]
            del event_data["ticket" ]["id"]
            event_data["ticket" ]["id"] = id
            event_data['expiresAt']['date'] = event_data['expiresAt']['$date']
            del event_data['expiresAt']['$date']
    else:
        print("what")
        event_data = data['data']
    try:
        # print(type(data['data']))
        # print("whahah")
        # if type(data['data']) == type("str"):
        #     print("event_data")
        #     event_data = json.loads(data['data'])
        #     id = event_data["id"]["$oid"]
        #     print("event_data")
        #     del event_data["id"]
        #     event_data["id"] = id
        #     print("event_data")
        #     if "ticket" in event_data:
        #         print("event_data")
        #         id = event_data["ticket" ]["id"]["$oid"]
        #         del event_data["ticket" ]["id"]
        #         event_data["ticket" ]["id"] = id
        #         event_data['expiresAt']['date'] = event_data['expiresAt']['$date']
        #         del event_data['expiresAt']['$date']
        # else:
        #     print("what")
        #     event_data = data['data']
        event_type = data["type"]
        print(event_type,"--------")
        res = handle_event({
            "type":event_type,
            'data': event_data
            })
        if res is not None:
            return res

        return  {"status": "ok"}
        
    except InsertExpireToDBException:
        abort(500, InsertExpireToDBException.get_message())
    except Exception as e:
        print(e)
        raise e

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