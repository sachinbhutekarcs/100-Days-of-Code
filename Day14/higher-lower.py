from game_data import data
import random
from art import logo, vs
#from replit import clear


# Function to select random celebrity from list


def random_celebrity():
    return random.choice(data)

# Compare followers of celebrities and check if user is correct.


def compare(guess):
    if A["follower_count"] > B["follower_count"]:
        return guess == "A"
    else:
        guess == "B"


def game():
    global A, B
    print(logo)
    user_win = True
    score = 0
    # continue till user is correct
    while user_win:
        # If user is correct, then make second celebrity first, new celebity second
        A = B
        B = random_celebrity()

        # both celebrities should not be same
        while A == B:
            B = random_celebrity()

        print(
            f'Compare A: {A["name"]}, a {A["description"]} from {A["country"]}')
        print(vs)
        print(
            f'Compare B: {B["name"]}, a {B["description"]} from {B["country"]}')

        # Ask who has more followers to the user
        guess = input("Who has more followers ? Type 'A' or 'B': ").upper()
        user_win = compare(guess)

        if user_win:
            score += 1
            # clear()
            print(f"You are right! Current Score is {score}.")
        else:
            print(f"Sorry, you are wrong! Your Score is {score}.")


play_again = "yes"

while play_again == "yes":
    # pick two random dictionaries from game_data list
    A = random_celebrity()
    B = random_celebrity()

    game()
    play_again = input("Do you want to play again? Say 'yes' or 'no': ")
