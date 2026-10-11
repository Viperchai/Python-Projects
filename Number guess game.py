# Write your code here :-)
import random

print("Welcome to the Number Guessing Game!")


lower = int(input("Enter the lower bound of the range: "))
upper = int(input("Enter the upper bound of the range: "))


secret_number = random.randint(lower, upper)

attempts = 0
print(f"\nI have selected a number between {lower} and {upper}. Try to guess it!")


while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
        break
