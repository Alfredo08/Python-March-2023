from flask import json, jsonify, request
from flask_app import app
from flask_app.models.todos_model import Todo
from flask_cors import cross_origin


@app.route( '/api/todos', methods = ['GET'] )
@cross_origin( origins = ["http://127.0.0.1:5500"] )
def api_get_all():
    list_of_todos = Todo.api_get_all()
    return ( jsonify( list_of_todos ) , 200 )
