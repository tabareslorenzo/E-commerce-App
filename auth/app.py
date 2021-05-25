import json
import dateutil.parser
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify, session
import os

app = Flask(__name__)
from signup import *




# @app.route('/')
# def index():
#   return 'Index Page'


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 6000))
    app.run(debug=True, host='0.0.0.0', port=port)