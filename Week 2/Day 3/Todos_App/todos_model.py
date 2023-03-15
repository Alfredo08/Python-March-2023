from config.mysqlconnection import connectToMySQL

class Todo:
    def __init__( self, data ):
        self.id = data["id"]
        self.name = data["name"]
        self.status = data["status"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
    
    @classmethod
    def get_all( cls ):
        query  = "SELECT * " 
        query += "FROM todos;"
        # In a SELECT we always get a LIST of DICTIONARIES
        results = connectToMySQL( "todos_db" ).query_db( query )
        
        list_of_todos = []
        for row in results:
            list_of_todos.append( cls(row) )
        return list_of_todos
