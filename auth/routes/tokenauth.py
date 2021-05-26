import json
import dateutil.parser
import os
from app import app
import jwt
from jwt.exceptions import DecodeError
from validator import validate_password, validate_email
from helpers import get_user_from_db
from exceptions import (
    EmptyPasswordException, 
    InvalidPasswordLengthException, 
    InvalidEmailException,
    EmptyEmailException,
    UserDoesNotExistsException
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



@app.route('/api/users/auth', methods=['GET'])
def auth():
    try:
        token = request.headers.get('Authorization')
        decoded = jwt.decode(token, "secret", algorithms="HS256")['user']
        user = get_user_from_db(decoded['email'])
    except DecodeError as e:
        print(DecodeError, f"Token Decode Error, {e}")
        abort(422,  f"Token Decode Error, {e}")
    except UserDoesNotExistsException:
        abort(422, UserDoesNotExistsException.get_message())
    return {"valid": True, "email": user['email'], "hash":user['password']}

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