import json
import dateutil.parser
import os
from app import app
import requests
# from validator import validate_password, validate_email
from helpers import (
    get_orders_from_user
)
from exceptions import (
    OrderDoesNotExistsException
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



@app.route('/api/orders', methods=['GET'])
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
    order = get_orders_from_user(r['email'])
    return {"orders": order}


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