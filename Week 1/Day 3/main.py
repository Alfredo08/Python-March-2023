# package/folder . module/file    
from classes_pkg.animal import Animal, addTwoNums
from classes_pkg.cat import Cat
from classes_pkg.dog import Dog

print( "***** MENU OF OPTIONS *****" )
print( "0) EXIT this program" )
print( "1) Add a dog" )
print( "2) List all the dogs" )
option = input( "Please select an option: " ) 

while option != "0":
    if option == "1":
        dog_name = input( "Please type the name of the dog: " )
        dog_owner = input( "Please type the name of the owner: " )
        dog_breed = input( "Please type the breed of the dog: ") 
        dog_color = input( "Please type the color of the dog: " ) 
        new_dog = Dog( dog_name, dog_owner, dog_breed, dog_color )
    if option == "2":
        Dog.print_all_dogs()
        
    print( "***** MENU OF OPTIONS *****" )
    print( "0) EXIT this program" )
    print( "1) Add a dog" )
    print( "2) List all the dogs" )
    option = input( "Please select an option: ") 

print( "Finished the execution of this program" )
"""
bird = Animal( "Birdie", "Alex", "White" )
bird.print_info()
print( "-----" )
jagger = Dog( "Jagger", "Alfredo", "Golder Retriever", "Golden" )
jagger.print_info() 
jagger.walk_animal()
print( "-----" )
chester = Cat( "Chester", "Alfredo", "Orange", 7 )
chester.print_info()
chester.walk_animal()
"""
# print( addTwoNums( 10, 20 ) )
