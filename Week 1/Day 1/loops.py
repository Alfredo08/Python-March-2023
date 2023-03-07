# First param is the initial index
# Second param is the stopping point i < stopping point
# Third param is the incrementing/decrementing of the control variable

# 11 < 2 => False
for i in range( 11, 2, -1 ):
    print( i )

numbers = [ 10, 20, 30, 40, 50 ]

for i in range( 0, len( numbers ) ):
    print( i, numbers[ i ] )


#index = 0
for num in numbers:
    print( num )
    #print( numbers[ index ] )
    #index += 1

name = "Alex Miller"

for letter in name:
    print( letter )