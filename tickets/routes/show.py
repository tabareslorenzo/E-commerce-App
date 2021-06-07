import json
import dateutil.parser
import os
from app import app
import requests
# from validator import validate_password, validate_email
from helpers import get_ticket_from_db
from exceptions import (
    TicketDoesNotExistsException
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



@app.route('/api/tickets/<string:key>', methods=['GET'])
def show(key: str):
    print(key)
    try:
        print(request.headers.get('Authorization'))
        r = requests.get('http://localhost:6000/api/users/auth', 
        headers={
            "Authorization":
            request.headers.get('Authorization')}).json()
        print(r)
        if 'valid' not in r or not r['valid']:
            print(r)
            abort(422, r['message']) 
        ticket = get_ticket_from_db(key)
    except TicketDoesNotExistsException:
        abort(422, TicketDoesNotExistsException.get_message())
    return f"title: {ticket['title']}, price: {ticket['price']}, userId:{ticket['userId']}"


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