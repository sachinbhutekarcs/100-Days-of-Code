############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

from art import logo
from sys import exit
import random
print(logo)
comp_win = False
user_win = False
user_score = 0
comp_score = 0


def card_output():
    """returns any card at random from the deck of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def sum(card1, card2):
    score = card1 + card2
    if score < 21:
        return score
    elif score > 21:
        if card1 == 11 or card2 == 11:
            score = score - 10
            return score
        else:
            return score
    else:
        return score


restart = "yes"

while restart == "yes":
    play = input("Do you like to play a game of Blackjack? Type 'y' or 'n':")
    if play == "y":
        user_card1 = card_output()
        user_card2 = card_output()
        comp_card1 = card_output()
        user_score = sum(user_card1, user_card2)
        print(
            f"Your cards are [{user_card1},{user_card2}], Current score is {user_score}. ")
        print(f"Computer's first card is {comp_card1}")
        hit_stand = "hit"

        while hit_stand == "hit":
            hit_stand = input("Hit or Stand: ").lower()
            if hit_stand == "stand":
                break
            user_card = card_output()
            user_score = sum(user_score, user_card)
            if user_score > 21:
                print(
                    f" Your score is {user_score}. Compouter is Winner. Game Over")
                exit()
            elif user_score == 21:
                print(f" Your score is {user_score}")
                break
            else:
                print(f" Your score is {user_score}")

        comp_score = comp_card1
        while comp_win == False and user_win == False:
            comp_card = card_output()
            comp_score = sum(comp_score, comp_card)
            print(
                f"Computer's next card is {comp_card} & score is {comp_score}")
            if comp_score == 21:
                comp_win = True
            elif comp_score > 21:
                user_win = True

        if comp_win == True:
            print("Computer is Winner. Game Over")
        else:
            print("User is Winner. Game Over")

        restart = input(
            "Do you want to restart the Game? Tyep yes or no: ").lower

    else:
        print("Game Over")
        exit()

print("Thank You for Playing")
exit()
