from art import logo
import random
print(logo)
RANDOM_NUMBER = random.randint(1, 100)
EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 5


def check_the_number(guess):
    if guess > RANDOM_NUMBER:
        print("Too high.")
    elif guess < RANDOM_NUMBER:
        print("Too low.")
    else:
        print(f"You got it! The answer was {RANDOM_NUMBER}.")
        sys.exit()


def select_difficulty():
    difficulty = input(
        "Choose the difficulty level. Type 'easy or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_DIFFICULTY
    elif difficulty == "hard":
        return HARD_DIFFICULTY


def game():
    print("Welcome to the Number Guessing Game.")
    print("I'm thinking of a number between 1 and 100")
    attempts = select_difficulty()
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        attempts -= 1
        check_the_number(guess)
        if attempts == 0:
            print(
                f"Sorry, you couldn't guess it. The answer was {RANDOM_NUMBER}.")
        print("Guess again.")


game()
