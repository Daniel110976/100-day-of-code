# Day 2: Variables and Data Types
# subscripting is used to access elements in a list or string
print("Daniel"[5]) #this will print "L"
# String = sequence of characters its usually in quote
print("120" + "135")
# Integer = whole numbers
print(120 + 135)
# Large Integer = whole numbers that are too large for standard integer types
print(12345678901234567890 + 13579246801234567890)
# float = decimal number
print(12.34 + 56.78)
# Boolean = True or False
print(True)
print(False)
street_name = "Abbey Road"
print(street_name[4] + street_name[7])
# this will print "yo"
# Type error, Type checking, and Type conversion
# Type error = trying to perform an operation on incompatible data types
# print("120" + 135) # this will cause a TypeError
# Type checking = checking the data type of a variable
# print(isinstance(120, int)) # this will print True
# print(isinstance("120", str)) # this will print True
# Type conversion\type casting = changing one data type to another
# print(int("120") + 135) # this will print 255
# integer
print(type(120))
# string
print(type("120"))
# float
print(type(12.34))
# boolean
print(type(True))
# type conversion
int("123")
print(int("123") + int("456"))  # this will print 579
name_of_the_user = input("Enter your name: ")
length_of_name = len(name_of_the_user)
# to get the no of letters in the name, add "str" to length_of_name
# it will convert the integer to a string
print("Number of letters in your name:" + str(len(name_of_the_user)))
print("My age: " + str(23))
print(2568 + 559)
print(354 - 657)
print(25 * 30)
print(5 / 2) # this will print 2.5
# Arithmetic operations
# Floor division = shows the largest whole number less than or equal to the result of a division
print(5 // 2)  # this will print 2
# Modulus operator = shows the remainder of a division
print(5 % 2)  # this will print 1
# Exponentiation = raises a number to the power of another number
print(5 ** 2)  # this will print 25
# Absolute value = the distance of a number from zero
print(abs(-5))  # this will print 5
# PEMDASLR = Parentheses, Exponents, Multiplication and Division (from left to right), Addition and Subtraction (from left to right)
# ()
# **
# * OR /
# + OR -
print(3 * 5 + 4 / 2 - 6)
print(3 * (5 + 4) / 2 - 6)
# using parentheses to change the order of operations,
# the second print statement will evaluate (5 + 4) first, then multiply by 3, then divide by 2, and finally subtract 6