import json
import dateutil.parser
import os
from app import app
import requests
# from validator import validate_password, validate_email
from helpers import (
    get_ticket_from_db,
    get_all_ticket_from_db
)
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



@app.route('/api/tickets', methods=['GET'])
def index():
    
    print(request.headers.get('Authorization'))
    r = requests.get('http://localhost:6000/api/users/auth', 
    headers={
        "Authorization":
        request.headers.get('Authorization')}).json()
    print(r)
    if 'valid' not in r or not r['valid']:
        print(r)
        abort(422, r['message']) 
    tickets = get_all_ticket_from_db()
    return {"tickets": tickets}


@app.errorhandler(404)
def not_found(error):
    return jsonify({
    "Success": False,
    "error" : 404,
    "message" : "resource not found"
    }), 404