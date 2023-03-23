from flask import json, jsonify, request
from flask_app import app
from flask_app.models.todos_model import Todo
from flask_cors import cross_origin


@app.route( '/api/todos', methods = ['GET'] )
@cross_origin( origins = ["http://127.0.0.1:5500"] )
def api_get_all():
    list_of_todos = Todo.api_get_all()
    return ( jsonify( list_of_todos ) , 200 )

@app.route( '/api/delete/todo/<int:id>', methods = ['DELETE'] )
@cross_origin( origins = ["http://127.0.0.1:5500"] )
def api_delete_one( id ):
    data = {
        "todo_id" : id
    }
    message = Todo.delete_one( data )
    return ( ( jsonify({}) ), 204 )

@app.route( '/api/new/todo', methods = ['POST'] )
@cross_origin( origins = ["http://127.0.0.1:5500"] )
def api_add_one():
    new_todo = json.loads( request.data.decode( 'UTF-8' ) )
    todo_id = Todo.create_one( new_todo )
    response_dictionary = {
        "message" : "Todo added.",
        "todo_id" : todo_id 
    }
    return ( jsonify( response_dictionary ) ), 201

@app.route( '/api/update/todo/<int:id>', methods = ['PUT'] )
@cross_origin( origins = ["http://127.0.0.1:5500"] )
def api_update_one( id ):
    todo_update = json.loads( request.data.decode( 'UTF-8' ) )
    todo_update[ "todo_id" ] = id
    Todo.update_one( todo_update )
    return ( jsonify( { "message" : "Todo has been updated" } ) ), 202