"""
import random

secret = random.randint(1,20)

while True:

    guess = int(input("Guess Number: "))

    if guess == secret:
        print("That's Correct!")
        print("Now GO FUCK YOURSELF!")
        break

    elif guess < secret:
        print("Too Fucking Low")

    else:
        print("Too Fucking High")
"""
import random

secret = random.randint(1, 20)
attempts = 5

print("=== Guess The Number ===")
print("I'm thinking of a number between 1 and 20.")
print("Type 'skip' to reveal the answer and quit.")
print(f"You have {attempts} attempts.\n")

while attempts > 0:

    guess = input("Guess Number: ")

    if guess.lower() == "skip":
        print(f"You skipped! The number was {secret}")
        break

    try:
        guess = int(guess)
    except ValueError:
        print("Enter a valid number!")
        continue

    if guess == secret:
        print("That's Correct!")
        print("You Win!")
        print("Now GO FUCK YOURSELF!")
        break

    attempts -= 1

    difference = abs(secret - guess)

    if difference <= 2:
        print("Very Close Nigga!")

    if guess < secret:
        print("Too Fucking Low!")
    else:
        print("Too Fucking High!")

    print(f"Attempts Left: {attempts}\n")

if attempts == 0:
    print(f"Game Over! You Lost! YOU FUCKING LOSER! \nThe number was {secret}")
