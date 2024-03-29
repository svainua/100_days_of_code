import os
import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def game():
    print(logo)

    player_cards = []
    comp_cards = []

    for card in range(2):
        player_cards.append(deal_card())
        comp_cards.append(deal_card())

    if sum(player_cards) == 21 and sum(comp_cards) == 21:
        print(f"Your final hand is {player_cards}, final score: {sum(player_cards)}")
        print(f"Computer's final hand is: {comp_cards}, final score: {sum(comp_cards)}")
        print("It's a draw")
        return

    elif sum(player_cards) == 21:
        print(f"Your final hand is {player_cards}, final score: {sum(player_cards)}" )
        print(f"Computer's final hand is: {comp_cards}, final score: {sum(comp_cards)}")
        print("Congrats! You win with BlackJack!")
        return
    elif sum(comp_cards) == 21:
        print(f"Your final hand is {player_cards}, final score: {sum(player_cards)}")
        print(f"Computer's final hand is: {comp_cards}, final score: {sum(comp_cards)}")
        print("Comp wins with BlackJack!")
        return

    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"Computer's first card: {comp_cards[0]}")

    should_continue = True
    while should_continue:
        next_step = input("Type 'y' to get another card, type 'n' to pass:\n").lower()
        if next_step == "y":
            player_cards.append(deal_card())

            if sum(player_cards) > 21 and 11 in player_cards:
                ace_index = player_cards.index(11)
                player_cards[ace_index] = 1

            if sum(player_cards) > 21:
                print(f"Your final hand is {player_cards}, final score: {sum(player_cards)}")
                print(f"Computer's final hand is: {comp_cards}, final score: {sum(comp_cards)}")
                print("You went over. You lose.")
                # should_continue = False
                return

            print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
            print(f"Computer's first card: {comp_cards[0]}")

        else:
            while sum(comp_cards) < 17:
                comp_cards.append(deal_card())
                if sum(comp_cards) > 21 and 11 in comp_cards:
                    ace_index = comp_cards.index(11)
                    comp_cards[ace_index] = 1

            print(f"Your final hand is {player_cards}, final score: {sum(player_cards)}")
            print(f"Computer's final hand is: {comp_cards}, final score: {sum(comp_cards)}")

            if sum(player_cards) > sum(comp_cards) or sum(comp_cards) > 21:
                print("Congrats! You win!")
                break
            elif sum(player_cards) < sum(comp_cards):
                print("You lose.")
                break
            else:
                print("It's a draw.")
                break


while input("Do you want to play a game of BlackJack? Type 'y' or 'n':\n").lower() == "y":
        os.system("clear")
        game()
