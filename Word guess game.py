import random


name = input("What is your name? ")
print("Good luck,", name + "!")


words = [
    'tiger', 'computer', 'science', 'programming', 'python',
    'mathematics', 'player', 'condition', 'phone', 'robot',
    'board', 'pokemon'
]


word = random.choice(words)

print("Guess the characters!")


guessed_letters = ""
turns = 12

while turns > 0:
    failed = 0


    for char in word:
        if char in guessed_letters:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    print()


    if failed == 0:
        print("You Win!")
        print("The word was:", word)
        break


    guess = input("Guess a character: ").lower()
    guessed_letters += guess


    if guess not in word:
        turns -= 1
        print("Wrong guess.")
        print("You have", turns, "more guesses left.")

        if turns == 0:
            print("You Lose!")
            print("The word was:", word)
