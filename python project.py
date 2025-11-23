import random

"""
1 is for Rock
0 is for Paper
-1 is for Scissor

"""

computer = random.choice([1, 0, -1])
user_input = input("Enter your choice (Rock, Paper, Scissor): ").capitalize()

you_dict = {"Rock": 1, "Paper": 0, "Scissor": -1}
user_choice = you_dict[user_input]
reverse_dict = {1: "Rock", 0: "Paper", -1: "Scissor"}

if user_input not in you_dict:
    print("Invalid input!")

else:
    print(f"You chose {reverse_dict[user_choice]}\n Computer chose {reverse_dict[computer]}")

    if computer == user_input:
        print("It's a draw :|")
    elif computer == 1 and user_input == 0 or \
         computer == 0 and user_input == 1 or \
         computer == -1 and user_input == 1:
        print("You win! :)")

    else:
        print("Computer wins! :(")