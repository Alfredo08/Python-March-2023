from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.todos_model import Todo

@app.route( '/todos', methods=['GET'] )
def get_todos():
    session[ 'full_name' ] = "Alex Miller"
    session[ 'user_id' ] = 2
    list_of_todos = Todo.get_all()
    return render_template( "home.html", list_of_todos=list_of_todos )

@app.route( '/todo/form', methods=['GET'] )
def display_todo_form():
    if 'full_name' in session:
        current_user = session[ 'full_name' ]
        return render_template( "todo_form.html" )
    else:
        return redirect( "/todos" )

@app.route( '/todo/edit_form/<int:id>', methods=['GET'] )
def display_edit_todo_form( id ):
    todo = {
        "todo_id" : id
    }
    current_todo = Todo.get_one( todo )
    return render_template( "update_todo_form.html", current_todo = current_todo )

@app.route( '/todo/new', methods=['POST'] )
def create_todo():
    new_todo = {
        "name" : request.form[ 'todo_name' ],
        "status" : request.form[ 'todo_status' ],
        "user_id" : session[ 'user_id' ]
    }
    Todo.create_one( new_todo )
    return redirect( '/todos' )

@app.route( '/todo/remove/<int:id>', methods=['POST'] )
def remove_todo( id ):
    delete_todo = {
        "todo_id" : id
    }
    Todo.delete_one( delete_todo )
    return redirect( '/todos' )

@app.route( '/todo/edit/<int:id>', methods=['POST'] )
def edit_todo( id ):
    edit_todo = {
        "name" : request.form[ 'todo_name' ],
        "status" : request.form[ 'todo_status' ],
        "user_id" : session[ 'user_id' ],
        "todo_id" : id
    }
    Todo.update_one( edit_todo )
    return redirect( '/todos' )



"""
Method: GET
Getting all of a particular list
Function: get_all_todos()
          get_todos()
Url: '/todos'

Method: GET
Getting one item of a particular list
Function: get_todo_by_id( id )
          get_todo( id )
Url: '/todo/<int:todo_id>'
     '/todo/<int:id>'

Method: GET
Displaying a form that will eventually refer to a list
Function: display_todo_form()
Url: '/todo/form'

Method: POST
Create a new item of a particular list
Function: create_todo()
          add_todo()
Url: '/todo/new'
     '/todo/add'

Method: POST/PUT
Update an existing item of a particular list
Function: update_todo( id )
          edit_todo( id )
Url: '/todo/update'
     '/todo/edit'

Method: POST/DELETE
Remove an existing item from a particular list
Function: delete_todo( id )
          remove_todo( id )
Url: '/todo/delete'
     '/todo/remove'
"""