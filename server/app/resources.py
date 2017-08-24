from datetime import datetime

from flask import request, abort, jsonify

from app import app, db
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

@app.route('/todos', methods=['GET'])
def get():
    if isAuthorized(request.headers['Authorization']):
        todos = Todo.query.all()
        response = []
        for todo in todos:
            response.append(todo.to_dict())
        return jsonify(response), 201
    else:
        abort(401)

@app.route('/todos', methods=['POST'])
def create():
    if isAuthorized(request.headers['Authorization']):
        title = request.json['title']
        complete = request.json['complete']
        todo = Todo(title=title, complete=complete)
        db.session.add(todo)
        db.session.commit()
        return jsonify({ 'id': todo.id, 'title': todo.title, 'complete': todo.complete }), 201
    else:
        abort(401)


@app.route('/todos/<int:id>', methods=['PUT'])
def update(id):
    if isAuthorized(request.headers['Authorization']):
        title = request.json['title']
        complete = request.json['complete']
        todo = Todo.query.filter_by(title=title).first()
        todo.complete = complete
        db.session.add(todo)
        db.session.commit()
        return jsonify({ 'id': 1, 'title': 'Test', 'complete': complete })
    else:
        abort(401)


@app.route('/todos/<int:id>', methods=['DELETE'])
def delete(id):
    if isAuthorized(request.headers['Authorization']):
        todo = Todo.query.get(id)
        db.session.delete(todo)
        db.session.commit()
        return jsonify({ })
    else:
        abort(401)


def isAuthorized(bearer):
    if bearer == 'Bearer ' + jwtToken:
        return True
    else:
        return False

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization, responseType')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

