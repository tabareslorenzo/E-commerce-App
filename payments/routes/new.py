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
    OrderDoesNotExistsException,
    UserNotOwnerException,
    CanceledOrderException
)
from helpers import (
    insert_into_db,
    get_order_with_id,
    correct_user,
    is_canceled
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


@app.route('/api/payments', methods=['POST'])
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
        order = get_order_with_id(data['orderId'])
        correct_user(r["email"], order['userId'])
        is_canceled(order.status)
        
        charge = stripe.Charge.create(
            amount=order.price,
            currency="usd",
            source=token, # obtained with Stripe.js
            metadata={'order_id': order.id}
        )
        payment = insert_into_db(order.id, charge.id)
        send_update_event(payment)
        return payment
    except OrderDoesNotExistsException:
        abort(404, OrderDoesNotExistsException.get_message())
    except UserNotOwnerException:
        abort(422, UserNotOwnerException.get_message())
    except CanceledOrderException:
        abort(422, CanceledOrderException.get_message())


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