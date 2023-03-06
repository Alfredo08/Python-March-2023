
grade = 7.6
stack = "mern"

# JS !boolean    !=
# Python not     !=
if grade >= 8.0 and stack == "python":
    print( "You passed your python exam!" )
    print( "You should be ready to move on to MERN!" )
elif stack == "mern":
    print( "You first need to pass python")
else:
    print( "You will need a retake" )

print( "This will be printed always!" )