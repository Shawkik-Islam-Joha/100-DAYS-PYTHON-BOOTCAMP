import random

choices = ["rock","paper","scissor"]  # List of possible choices for the game

user_choice = input("Enter your choice (rock, paper ,scissor): ").lower()  # Get user input, split and convert to lowercase (incorrect usage)

if user_choice not in choices:  # Check if the user's choice is valid
    print("Invalid Choice!")  # Inform user of invalid input
    quit(True)  # Exit the program if input is invalid

computer_choice = random.choice(choices)  # Randomly select computer's choice

print(f"Your choice = {user_choice}")
print(f"Computer Choice = {computer_choice}")

if user_choice == computer_choice:  # If both choices are the same, it's a tie
    print("It's a tie!")  # Announce a tie
else:
    if (user_choice == "rock" and computer_choice == "scissor") or \
    (user_choice == "paper" and computer_choice == "rock") or \
    (user_choice == "scissor" and computer_choice == "paper"):
        print("You win!!")  # Announce user win if any winning condition is met
    else:
        print("Computer Win!")  # Announce computer win if none of the user winning conditions are met

