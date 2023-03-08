from classes_pkg.animal import Animal

class Cat( Animal ):
    def __init__( self, name, owner, breed, age ):
        # Call and set the constructor of the parent class
        super().__init__( name, owner, breed )
        self.age = age
    
    # Override
    def print_info(self):
        super().print_info()
        print( f"Age: {self.age}" )

    # Polymorphism
    def walk_animal( self ):
        print( "I don't need to be walked human!" )

