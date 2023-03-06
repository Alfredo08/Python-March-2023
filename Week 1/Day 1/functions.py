
def add_two_nums( num1, num2 ):
    result = num1 + num2
    return result

first_sum = add_two_nums( 10, 20 )
print( first_sum )

second_sum = add_two_nums( 50, 100 )
print( second_sum )

final_sum = add_two_nums( first_sum, second_sum )
print( final_sum )
