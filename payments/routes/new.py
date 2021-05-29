import json
import dateutil.parser
import os
from app import app
import requests
from datetime import datetime
from datetime import timedelta
from stripe import stripe
# from validator import validate_password, validate_email
from exceptions import (
    TicketDoesNotExistsException,
    OrderDoesNotExistsException,
    TicketAlreadyReservedException
)
from helpers import (
    insert_into_db,
    get_ticket_with_id,
    is_ticket_reserved
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
# .Created,
# .AwaitingPayment,
#  .Complete,
# .cancel


@app.route('/api/orders', methods=['POST'])
def new():
    data = request.get_json()
    print(data)
    token = request.headers.get('Authorization')
    print(token)
    r = requests.get('http://localhost:6000/api/users/auth', 
    headers={
        "Authorization":
        token}).json()

    print(r)
    if 'valid' not in r or not r['valid']:
        print(r)
        abort(422, r['message'])
    try :
        order = get_order_with_id()
        charge = stripe.Charge.create(
            amount=order.price,
            currency="usd",
            source=token, # obtained with Stripe.js
            metadata={'order_id': order.id}
        )
        
        return order
    except TicketAlreadyReservedException:
        abort(422, TicketAlreadyReservedException.get_message())
    except TicketDoesNotExistsException:
        abort(422, TicketDoesNotExistsException.get_message())


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