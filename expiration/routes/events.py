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
    print(data)
    try:
        handle_event(data)
    except InsertExpireToDBException:
        abort(500, InsertExpireToDBException.get_message())

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