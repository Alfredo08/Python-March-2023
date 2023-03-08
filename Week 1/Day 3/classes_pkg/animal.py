
class Animal:
    def __init__( self, name, owner, breed ):
        self.name = name
        self.owner = owner
        self.breed = breed
    
    def print_info( self ):
        print( f"Name of animal: {self.name}" )
        print( f"Owner: {self.owner}" )
        print( f"Breed: {self.breed}" )
    
    # Polymorphism
    def walk_animal( self ):
        raise NotImplementedError

def addTwoNums( num1, num2 ):
    return num1 + num2 