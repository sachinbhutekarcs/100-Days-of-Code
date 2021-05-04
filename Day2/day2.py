#Data Types

#Strings
"Hello"
print("Hello"[4])

print("123" + "345")   #123345

#Integers : Whole Numbers

print(123 + 345) #468

# Python interpretes 123_456_789 as a single nmber 123456789
print(123_456_789) #123456789

#Float  : Numbers with decimal point

PI = 3.14159
print(PI)  #3.14159

#Boolean : It it ie either True or False

#Type Errors
# When we try to use len() for integer or we try to add or concatenate diffrent data types then we come across type errors

print(len(123))
name_len = len(input("Enter Your Name: "))
print("Your name has " + name_len + "Characters" )


#Type Checking: 
#type() function
# It is used to check data type of any variable

type(name_len)  #int hence cannot  be added to string

#Type Conversion or Type casting : Converting Data from one data type to another
#str()
#int()
#float()


#when we use division operator (/) it always gives answer as float
# Exponent operator (**) : Use to raise number to power Eg: 2**2 = 4 or 3**2 = 9
# Priority: PEMDAS : Parenthesis Exponent Multipliaction Division Addition Substraction
# Multi & Div are eual priority, same for + & - , so in such case left to right execution will be followed

#round() function : Round offs the number (to integer by default if round of digit number equal to zero)
#round (8/3, 2) first argument is number to be rounded off and second argument is roundoff to how many places after decimal point



