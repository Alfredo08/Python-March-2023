first_name = "Alex"
last_name = 'Miller'
age = 25 

length_of_first_name = len( first_name )

print( length_of_first_name )

# console.log( `My name is ${first_name} ${last_name}` )
print( f"My name is {first_name} {last_name}, and I am {age} years old." )
print( "My name is {} {}, and I am {} years old.".format( first_name, last_name, age ) )
print( "My name is %s %s, and I am %d years old." % ( first_name, last_name, age ) )