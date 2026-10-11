# Write your code here :-)
import random
import sys

print("Welcome to Rock Paper Scizor game (against the computer)")
gamechoice = input("Would you like to skip the introduction to the game (type y for yes or n for no): ")

computer_choice = ""

if gamechoice == "y":
    print("Ok, let's begin!")
elif gamechoice == "n":
    print("The rules of the game are simple. You and your opponent (the computer) will choose an item without knowing what the other chose. Rock beats Scizor, Scizor beats Paper, and Paper beats Rock. Same items result in a tie. Let's begin!")
else:
    print("Sorry, I didn't get that. Please reload the game to try again")
    sys.exit()

enter_choice = input("Please enter Rock, Paper, or Scizor: ").lower()

if enter_choice == "rock":
    pass
elif enter_choice == "scizor":
    pass
elif enter_choice == "paper":
    pass
else:
    print("Sorry, I didn't get that. Please reload the game to try again")
    sys.exit()

random_number = random.randint(1, 3)

if random_number == 1:
    computer_choice = "rock"
elif random_number == 2:
    computer_choice = "paper"
else:
    computer_choice = "scizor"

print("Computer choice: " + computer_choice)
print("Your choice: " + enter_choice)

if computer_choice == enter_choice:
    print("It's a tie, please try again to find a victor")
elif computer_choice == "scizor" and enter_choice == "rock":
    print("Congrats, you win!")
elif computer_choice == "rock" and enter_choice == "paper":
    print("Congrats, you win!")
elif computer_choice == "paper" and enter_choice == "scizor":
    print("Congrats, you win!")
else:
    print("Dang it! You lost.")
