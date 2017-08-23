from datetime import datetime

from flask import request, abort, jsonify

from app import app
from models import Todo

jwtToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiU2l0ZVBvaW50IFJ' + 'lYWRlciJ9.sS4aPcmnYfm3PQlTtH14az9CGjWkjnsDyG_1ats4yYg'

@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World!'

@app.route('/sign-in', methods=['POST'])
def sign_in():
    username = request.json['username']
    password = request.json['password']
    if username == password:
        return jsonify({ 'name': 'SitePoint Reader', 'token': jwtToken })
    else:
        abort(422)


@app.route('/todos', methods=['POST'])
def create():
    if isAuthorized(request.headers['Authorization']):
        title = request.json['title']
        complete = request.json['complete']
        return jsonify({ 'id': 1, 'title': 'Test', 'complete': False }), 201
    else:
        abort(401)


@app.route('/todos/<int:id>', methods=['PUT'])
def update(id):
    if isAuthorized(request.headers['Authorization']):
        title = request.json['title']
        complete = request.json['complete']
        return jsonify({ 'id': 1, 'title': 'Test', 'complete': complete })
    else:
        abort(401)


@app.route('/todos/<int:id>', methods=['DELETE'])
def delete(id):
    if isAuthorized(request.headers['Authorization']):
        title = request.json['title']
        complete = request.json['complete']
        return jsonify({ })
    else:
        abort(401)


def isAuthorized(bearer):
    if bearer == 'Bearer ' + jwtToken:
        return True
    else:
        return False
