# Index:    0       1         2
names = [ "Alex", "Roger", "Martha" ]

print( names )
print( names[0] )

# length_of_names_list = len( names )

# print( names[ length_of_names_list ] )

# JS - names.push( "Martin" )
# PY - names.append( "Martin" )
names.append( "Martin" )
names.append( "Juliet" )

print( names )

names.pop( 1 )

print( names )

new_list = names[:3] 

print( f"My new list is: {new_list}" )