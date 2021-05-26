import json
import dateutil.parser
import os
from app import app
import requests
# from validator import validate_password, validate_email
from helpers import insert_into_db
from exceptions import (
    TicketAlreadyExistsException
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



@app.route('/api/tickets', methods=['POST'])
def new():
    data = request.get_json()
    print(data)
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
        ticket = insert_into_db(data['title'], data['price'], data['userId'])
    except TicketAlreadyExistsException:
        abort(422, TicketAlreadyExistsException.get_message())
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