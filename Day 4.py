# Rock Paper Scissors

import random

# Define the different hand gestures
gestures = ["Rock", "Paper", "Scissors"]
ascii_art = [
    '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
    '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
    '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]

print("Welcome To Rock Paper Scissors By Daniel")

# Prompt the user to choose a gesture
user_choice = input("Enter 0 for Rock, 1 for Paper, or 2 for Scissors: ")

# Check if the user input is valid
if user_choice.isdigit() and 0 <= int(user_choice) <= 2:
    user_choice = int(user_choice)
    print("You played: " + gestures[user_choice])
    print(ascii_art[user_choice])

    # Generate computer's choice
    computer_choice = random.randint(0, 2)
    print("Computer played: " + gestures[computer_choice])
    print(ascii_art[computer_choice])

    # Decide the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("Computer wins!")
else:
    print("Invalid input. Please enter a number between 0 and 2.")