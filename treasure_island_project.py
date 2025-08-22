print('''*******************************************************************************
|                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************venture
''')

print("Welcome to the Treasure Island Adventure!")
print("Your mission is to find the hidden treasure.")

# Step 1: Choose a direction
direction = input("Which direction do you want to go? left or right: ")
# choose left path
if direction == "left":
    print("You encounter a wild animal!")
    # Step 2: Decide to fight or run
    action = input("Do you want to fight or run? fight or run: ")
    if action == "fight":
        print("You saw a fierce lion and it killed you!")
    else:
        print("You run away, but fell into a booby trap. Game Over!")
# choose right path
elif direction == "right":
    print("You find a river.")
    # Step 2: Decide to swim or build a raft
    action = input("Do you want to swim or build a raft? swim or raft: ")
    if action == "raft":
        print("You build a raft and float down the river.")
        # Step 3: Choose a door
        door = input("You arrive at the entrance of a cave. Do you want to enter? yes or no: ")
        if door == "yes":
            print("You enter the cave and find Three Doors. door 1 = red and door 2 = blue and door 3 = green.")
            door_choice = input("Which door do you choose? red, blue or green:")
            # Check the door choice
            if door_choice == "red":
                print("You fell into a pit of deadly snakes and was bitten to death!")
                print("Game Over!")
            elif door_choice == "blue":
                print("You were ran over by an angry mob of prisoners.")
                print("Game Over!")
            elif door_choice == "green":
                print("You saw a shining light,then a box filled with gold and so many jewels. Congrats, You found the Treasure!")
                print("You Win!")
                print("Thanks for playing!")
            else:
                print("Invalid door choice. Game over.")
    # If the player chooses not to enter the cave
        else:
            print("You jumped into the river to swim but was eaten by a crocodile!")
# If the player chooses not to enter the no direction
else:
    print("Invalid direction. Game over.")
exit()