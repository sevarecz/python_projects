import random

def guess_secret_number_game():
    secret_number = random.randint(0, 100)
    attempts = 5

    print("Welcome to the Number Guessing Game!")
    print("You have 5 attempts to guess the number between 0 and 100.")

    while attempts > 0:
        try:
            guessed_number = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts -= 1

        if guessed_number > secret_number:
            print(f"Too high! Attempts left: {attempts}")
        elif guessed_number < secret_number:
            print(f"Too low! Attempts left: {attempts}")
        else:
            print(f"Correct! You guessed the number: {secret_number}")
            return

    print(f"Game over! The correct number was: {secret_number}")


guess_secret_number_game()
