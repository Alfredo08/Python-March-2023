# package/folder . module/file    
from classes_pkg.animal import Animal, addTwoNums
from classes_pkg.cat import Cat
from classes_pkg.dog import Dog

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

# print( addTwoNums( 10, 20 ) )
