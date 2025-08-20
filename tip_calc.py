print("Hello, Welcome to the Tip Calculator!")
#get the total bill amount from the user
total_bill = float(input("What was the total bill? $"))
# get the tip percentage from the user
tip_percentage = int(input("What percentage would you love to give for our wonderful service? 2, 5, 10, 13, 15, 17, 20, 23, 25? "))
# get the number of people to split the bill from the user
num_people = int(input("How many people to split the bill? "))
# calculate the total tip amount
total_tip = total_bill * (tip_percentage / 100)
# calculate the total amount to be paid
total_amount = total_bill + total_tip
# calculate the amount per person
amount_per_person = total_amount / num_people
# print the results
print(f"Total bill: ${total_bill:.2f}")
print(f"Tip amount: ${total_tip:.2f}")
print(f"Total amount: ${total_amount:.2f}")
print(f"Amount per person: ${amount_per_person:.2f}")
print("Thank you for using the Tip Calculator!")
