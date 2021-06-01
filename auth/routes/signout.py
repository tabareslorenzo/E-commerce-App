import json
import dateutil.parser
import os
from app import app
import jwt
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



@app.route('/api/users/signout', methods=['GET'])
def signout():
    return f"token: {None}"
