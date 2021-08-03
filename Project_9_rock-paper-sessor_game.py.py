import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

user_choice = int(input("your choice 0 for rock, 1 for paper and 2 for scissors"))
if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!")
else:
    print("User chose:")
    print(game_images[user_choice])
    computer_choice = random.randint(0,2)
    print("Computer chose:")
    print(game_images[computer_choice])
#    print(f"user choice = {user_choice},   computer choice = {computer_choice}")
    key = user_choice - computer_choice
    if(key == 1 or key == -2):
        print("You Win")
    elif (key == -1 or key == 2):
        print("You lose")
    else:
         print("Draw")
     
