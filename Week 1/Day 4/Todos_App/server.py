from flask import Flask

app = Flask( __name__ )

@app.route( "/" )
def hello_class():
    print( "Thank you for the request, the server is listening!" )
    return "Hey there class of March 2023"

@app.route( "/hello" )
def hello_there():
    return "Hey there class of March 2023, this is the second route of the server!"

@app.route( "/hello/<string:firstName>/<string:lastName>")
def greeting( firstName, lastName ):
    print( f"Hey there from the server {firstName} {lastName}" )
    return ( f"Welcome to our server {firstName} {lastName}" )

# At the very end don't forget to place the "run" command
if __name__ == "__main__":
    app.run( debug = True, port=5001 )
