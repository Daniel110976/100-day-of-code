<<<<<<< HEAD
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $10.")
else:
    print("Sorry, you can't ride the rollercoaster.")
# nested if/else statements allow us to check multiple conditions in a structured way
# elif = else if, allows us to check another condition if the previous one was false
=======
number_to_check = int(input("What is the number you want to check? "))
if number_to_check % 2 == 0:
    print(f"{number_to_check} is an even number.")
else:print(F"{number_to_check} is an odd number")

cgpa = float(input("What is your CGPA? "))
if cgpa >= 3.5:
    print("You will have distinction")
else:print("You will not have distinction")
>>>>>>> 6229440e7b888e47cdf5659c9d006bb597197ace
