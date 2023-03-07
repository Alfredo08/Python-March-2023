# Define the class
class Fraction:
    # Class attribute
    list_of_fractions = []
    title = "Learning OOP"
    # Constructor
    def __init__( self, numerator = 1, denominator = 1 ):
        # Attributes
        self.numerator = numerator
        self.denominator = denominator
        # Adding the current instance/object to the class attribute
        Fraction.list_of_fractions.append( self )

    # Methods
    def display_fraction( self ):
        print( f"{self.numerator} / {self.denominator}" )
        return self

    def add( self, fraction_to_add ):
        result_numerator = self.numerator * fraction_to_add.denominator + self.denominator * fraction_to_add.numerator
        result_denominator = self.denominator * fraction_to_add.denominator
        # Creating the resulting fraction to be manipulated as a Fraction object
        result_fraction = Fraction( result_numerator, result_denominator )
        return result_fraction

    @classmethod
    def print_all_fractions( cls ):
        for fraction in cls.list_of_fractions:
            fraction.display_fraction()
        #for i in range( 0, len( cls.list_of_fractions ) ):
        #    cls.list_of_fractions[i].display_fraction()

    @classmethod
    def print_fractions_title( cls ):
        for fraction in cls.list_of_fractions:
           print( fraction.title )

    @staticmethod
    def add_two_numbers( num1, num2 ):
        return num1 + num2

    @staticmethod
    def add_two_fractions( fraction1, fraction2 ):
        result_numerator = fraction1.numerator * fraction2.denominator + fraction1.denominator * fraction2.numerator
        result_denominator = fraction1.denominator * fraction2.denominator
        # Creating the resulting fraction to be manipulated as a Fraction object
        result_fraction = Fraction( result_numerator, result_denominator )
        return result_fraction


# Creating instances of the class Fraction "Creating an object"
fraction1 = Fraction( 1, 2 )
fraction2 = Fraction( 3, 6 )
fraction3 = Fraction()

fraction1.display_fraction().display_fraction().display_fraction()

result = fraction1.add( fraction2 )

fraction1.display_fraction()
fraction2.display_fraction()
result.display_fraction()

print( Fraction.list_of_fractions )
Fraction.print_all_fractions()

Fraction.print_fractions_title()

fraction3.title = "Learning Python and Flask"
print( "------" )
Fraction.print_fractions_title() 

print( "------" )
Fraction.title = "New title"
Fraction.print_fractions_title() 

print( Fraction.add_two_numbers( 10, 20 ) )

result_static_method = Fraction.add_two_fractions( fraction2, fraction3 )
result_static_method.display_fraction()

print( "-----" )
Fraction.print_all_fractions()

"""
print( fraction1 )
print( type( fraction1 ) )
print( fraction1.numerator, fraction1.denominator )
print( fraction2.numerator, fraction2.denominator )

fraction1.display_fraction()
fraction2.display_fraction()
fraction3.display_fraction()

fraction1.numerator = 3

fraction1.display_fraction()
"""