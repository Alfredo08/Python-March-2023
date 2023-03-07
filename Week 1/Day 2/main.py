# Define the class
class Fraction:
    # Constructor
    def __init__( self, numerator = 1, denominator = 1 ):
        # Attributes
        self.numerator = numerator
        self.denominator = denominator

    # Methods
    def display_fraction( self ):
        print( f"{self.numerator} / {self.denominator}" )

    def add( self, fraction_to_add ):
        result_numerator = self.numerator * fraction_to_add.denominator + self.denominator * fraction_to_add.numerator
        result_denominator = self.denominator * fraction_to_add.denominator
        result_fraction = Fraction( result_numerator, result_denominator )
        return result_fraction

# Creating instances of the class Fraction "Creating an object"
fraction1 = Fraction( 1, 2 )
fraction2 = Fraction( 3, 6 )
fraction3 = Fraction()

result = fraction1.add( fraction2 )

fraction1.display_fraction()
fraction2.display_fraction()
result.display_fraction()

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