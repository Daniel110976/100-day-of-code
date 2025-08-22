# Theme park project
print("Welcome to the Theme Park!")
print("Which ride would you like to go on?")
print("1. Rollercoaster")
print("2. Ferris Wheel")
print("3. Bumper Cars")
ride_choice = int(input("Enter the number of your chosen ride: "))
height = int(input("What is your height in cm? "))
bill = 0
student_id = "<= 5 characters>"
if height >= 120:
    if ride_choice == 1:
        print("You can ride the rollercoaster!")
    elif ride_choice == 2:
        print("You can ride the Ferris Wheel!")
    elif ride_choice == 3:
        print("You can ride the Bumper Cars!")    
    age = int(input("What is your age? "))
    if age <= 12:
        bill += 5
        print("Child tickets are $5.")
# Youth tickets are $7.
    elif age <= 18:
        bill += 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be okay! You get a free ride!")
# Adult tickets are $10.
    else:
        print("Adult tickets are $10.")
        bill += 10
    # Student discount
    if input("Are you a student? (yes/no)") == "yes":
        print("Enter your student ID:")
        student_id = input()
        if len(student_id) <= 5:
            print("You are eligible for a 50 percent discount!")
            bill -= (0.5 * bill)
    # Family package
    if input("Are you buying tickets for a family of 4 or more? (yes/no)") == "yes":
        print("You are eligible for a family package discount!")
        bill -= (0.2 * bill)
# optional add-ons
    want_photo = input("Do you want a photo taken? (yes/no) ")
    if want_photo == "yes":
        bill += 2
        print("A photo will be added to your bill for $2.")
    food_choice = input("Do you want to buy food? (yes/no) ")
    if food_choice == "yes":
        bill += 5
        print("Food will be added to your bill for $5.")
    souvenir = input("Do you want to buy a souvenir? (yes/no) ")
    if souvenir == "yes":
        bill += 10
        print("A souvenir will be added to your bill for $10.")
    vip_lounge = input("Do you want access to the VIP Lounge? (yes/no)")
    if vip_lounge == "yes":
        bill += 15
        print("Access to the VIP Lounge will be added to your bill for $15.")
    # lottery to win a free ride
    import random
    lottery = input("Do you want to enter the lottery for a chance to win a free ride? (yes/no) ")
    if lottery == "yes":
        questions = {
            "How many continents do we have?": "7",
            "What is the largest continent?": "Asia",
            "What is the largest mammal in the world?": "Blue Whale"
        }
        question, answer = random.choice(list(questions.items()))
        user_answer = input(f"Lottery time! Answer this question to win a free ride: {question} ")
        if user_answer == answer:
            print("Congratulations! You have won a free ride!")
        else:
            print("Sorry, that's not correct, better luck next time!")
    print(f"Your final bill is ${bill:.2f}.")
else:
    print("Sorry, you can't ride the rollercoaster.")


