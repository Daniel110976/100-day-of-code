height = 1.65
weight = 84

bmi = weight / (height ** 2)
bmi = (84 / (1.65 ** 2))
print("Your bmi is: " + str(bmi))
# This will print the BMI value calculated from the given height and weight

print(int(bmi)) # This will print the BMI value as an integer
# This will print the BMI value rounded to the nearest integer
print(round(bmi))
# round to 2 decimal places
print(round(bmi, 2))

score = 2
# This will print the score
score += 1  # Increment score by 1
score -= 1  # Decrement score by 1 
print(score)

#fstring = this allows for easier string formatting by embedding expressions inside string literals
# literals = these are the actual values or text that are represented in the code
score = 2 # this is an integer
height = 1.5 # this is a float
is_winning = True # this is a boolean
# recall, int = whole numbers (positive, negative, or zero)
# float = numbers with decimal points
# boolean = True or False

# the print statements below demonstrate how to use f-strings with different data types
print(f"Your score is: {score}")
print(f"Your height is: {height}")
print(f"Are you winning? {is_winning}")
# {} = in the f-string, the expression inside the curly braces is evaluated and inserted into the string

print(6 + 4 / 2 - (1 * 2))
# This will print the result of the arithmetic expression

a = int("5") / int(2.7)
print(type(a))  # This will print <class 'float'> because the result of the division is a float

age = 19
print(f"I am {age} years old.")
# This will print the age