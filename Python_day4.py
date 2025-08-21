#RPS randomisation 

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
#generate random number between 1-3

game_images = [rock, paper, scissors]

user_choice = int(input("What do you chose? Type 0 For Rock, 1 for Paper or 2 for Scissors.\n"))
# 0, 1, 2
if user_choice >=0 and user_choice <=2:
    print(game_images[user_choice])
computer_choice = random.randint(0,2)
# 0, 1, 2
print(f"Computer_choice: ")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. YOU LOSE!")
elif user_choice == 0 and computer_choice == 2:
    print("YOU WIN!")
elif computer_choice == 0 and user_choice ==2:
    print("YOU LOSE!")
elif computer_choice > user_choice:
    print("YOU LOSE!")
elif computer_choice < user_choice:
    print("YOU WIN!")
elif computer_choice == user_choice:
    print("It is a DRAW!")
