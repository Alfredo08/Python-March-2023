
student = {
    "first_name" : "Alex",
    "last_name" : "Miller",
    "age" : 25,
    "current_stack" : "Python",
    "passed_current_stack" : False
}

print( student )

print( student["first_name"] )

student["age"] = 26
student["full_name"] = "Alex Miller"

# del student["last_name"]
# student.pop( "first_name" )

print( student )

for key in student:
    print( key, student[ key ] )

print( student.keys() )
print( student.values() )

for alternate_key in student.keys():
    print( alternate_key )

print( "-------" )

for key, value in student.items():
    print( key, value )

print( student.items() )
