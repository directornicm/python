# ''' - 3 single quotes are used if more than one lines are to be printed as it is in the output.
print('''

*******************************************************************************
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
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
#input("You're at a cross road, Where do you want to go? Type "left" or "right"")
choice1 = input('You\'re at a cross road, Where do you want to go? Type "left" or "right"\n').lower()
if choice1 == "left":
    # if both ' and " are part of the output string, use \ in the output string preceeding the quote you have used outside
    choice2 = input('You\'he come to a lake. There is an Island in the middle of the lake. Type “Wait” or “Swim”\n').lower()
    if choice2 == "wait":
# see the comment in the first  line
        choice3 = input('''You arrive at the Island unharmed.
        There is a house with three doors one read, one yellow and one blue.
        Which colour do you choose?\n''').lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over")
        elif choice3 == "yellow":
            print("You found the treasure: You win")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game over")
        else:
            print("You choose a door that doesn't exists. Game Over")
    else:
        print("You are attacted by angru trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")

