import json
import dateutil.parser
import os
from app import app
import requests
# from validator import validate_password, validate_email
from helpers import (
    update_ticket, 
    get_ticket_with_id,
    send_update_event
)
from exceptions import (
    TicketAlreadyExistsException,
    TicketDoesNotBelongToYouException
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



@app.route('/api/tickets', methods=['PUT'])
def update():
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
        print( r['email'])
        if r['email'] != get_ticket_with_id(data['id'])['userId']:
            abort(401, TicketDoesNotBelongToYouException.get_message())
        ticket = update_ticket(data['id'], data['title'], data['price'])
        send_update_event(ticket)
    except TicketDoesNotBelongToYouException:
        abort(422, TicketDoesNotBelongToYouException.get_message())
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

@app.errorhandler(401)
def not_found(error):
    return jsonify({
    "Success": False,
    "error" : 401,
    "message" : f"Not Auth: {error.description}"
    }), 401