# day 3 conditional statements, logical operators, loops, code blocks and scope

# 1. Conditional Statement
print("Welcome to the voting eligibility checker!")
# Check if the user is eligible to vote
age = int(input("Please enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
# if = this allows us to execute certain code based on a condition, if the condition is true
# else = this allows us to execute code when the condition is false
# comparison operators
# < - less than
# > - greater than
# <= - less than or equal to
# >= - greater than or equal to
# == - equal to
# != - not equal to
# = - this means assignment which allows us to assign values to variables
# == - this means comparison which allows us to compare values
# an operator is a symbol that tells the compiler to perform specific mathematical or logical manipulations
# % - this is the modulus operator which returns the remainder of a division operation
print(10 % 3)
print(10 / 3)
# even numbers divided by 2 = 0

# nested if/else statements = if statements inside another if statement

# elif = else if allows us to check multiple conditions and can be used to create more complex conditional logic