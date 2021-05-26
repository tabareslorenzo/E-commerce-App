import json
import dateutil.parser
import os
from app import app
import jwt
from validator import validate_password, validate_email
from helpers import generate_hash, insert_into_db
from exceptions import (
    EmptyPasswordException, 
    InvalidPasswordLengthException, 
    InvalidEmailException,
    EmptyEmailException,
    EmailAlreadyExistsException
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



@app.route('/set/')
def set():
    session['key'] = 'value'
    return 'ok'

@app.route('/get/')
def get():
    return session.get('key', 'not set')

@app.route('/api/users/signup', methods=['POST'])
def signup():
    data = request.get_json()
    print(data)
    try:
        validate_password(data.get('password', None))
        validate_email(data.get('email', None))
        hash = generate_hash(data['password'])
        user = insert_into_db(data['email'], hash)
        encoded = jwt.encode({"user": user}, "secret", algorithm="HS256")
        print(user)
    except EmptyPasswordException:
        abort(422, EmptyPasswordException.get_message())
    except InvalidPasswordLengthException:
        abort(422, InvalidPasswordLengthException.get_message())
    except InvalidEmailException:
        abort(422, InvalidEmailException.get_message())
    except EmptyEmailException:
        abort(422, EmptyEmailException.get_message())
    except EmailAlreadyExistsException:
        abort(422, EmailAlreadyExistsException.get_message())
    return f"token: {encoded}, email: {user['email']}, password:{user['password']}"


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