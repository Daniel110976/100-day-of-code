# Welcome to Blossom Pizza! this is a simple pizza ordering program.
print("Welcome to Blossom Pizza!")
#get user input for size of pizza
size = input("What size pizza would you like? small, medium, large: ")
add_pepperoni = input("Do you want to add pepperoni? yes or no: ")
extra_cheese = input("Do you want extra cheese? yes or no: ")
bill = 0
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
if size == "small":
    bill = 15
elif size == "medium":
    bill = 20
elif size == "large":
    bill = 25
else:
    print("Invalid size selected.")
# Extra cheese for any size pizza: +$1
if extra_cheese == "yes":
    bill += 1
    print("Extra cheese will be added to your bill for $1.")
# Pepperoni
if add_pepperoni == "yes":
    if size == "small":
        bill += 2
    else:
        bill += 3
    print("Pepperoni will be added to your bill for $3.")
# Final bill
print(f"Your final bill is: ${bill:.2f}")