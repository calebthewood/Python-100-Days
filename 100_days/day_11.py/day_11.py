import random

from sqlalchemy import false, true
############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

logo = """

.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/

"""

def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    r = random.randint(0,12)
    return cards[r]

def score(player):
    return sum(player)


def black_jack():
    player_hand = []
    computer_hand = []
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start == "n": return
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    print(logo)

    player_hand.append(draw_card())
    player_hand.append(draw_card())
    computer_hand.append(draw_card())
    print(f"Your cards: {player_hand}, current score: {score(player_hand)}")
    print(f"Computer's first card: {computer_hand}")

    hit = 'y'
    while score(player_hand) <= 21 and score(computer_hand) <= 21:
        chance = random.random()
        p_score = score(player_hand)
        c_score = score(computer_hand)
        player_done = false

        # Player Turn:
        if not player_done:
            hit = input("Type 'y' to get another card, type 'n' to pass:")
            if hit == 'n': player_done = true
            elif hit == "y":
                player_hand.append(draw_card())
                if score(player_hand) > 21:
                    break
        # Computer Turn
        if c_score <= p_score:
            if c_score < 10:
                computer_hand.append(draw_card())
            elif c_score < 12 and chance < 0.5:
                computer_hand.append(draw_card())
            elif c_score < 17 and chance < 0.1:
                computer_hand.append(draw_card())
            if score(computer_hand) > 21:
                break

        print(f"    Your cards: {player_hand}, current score: {score(player_hand)}")
        print(f"    Computer's cards: {computer_hand}, current score: {score(computer_hand)}")


    print(f"    Your final hand: {player_hand}, final score: {score(player_hand)}")
    print(f"    Computer's final hand: [4, 10, 1, 5], final score: {score(computer_hand)}")
    if score(player_hand) > score(computer_hand):
        print("You win!")
    else:
        print("You lose!")



    #if yes....
    #if no,
    #   deal to computer, pc needs a brain to decide when to hit/hold
    # if pc busts
    print("Computer's final hand: [10, 5, 3], final score: 18")
    print("You win!")
    black_jack()
