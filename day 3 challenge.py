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
