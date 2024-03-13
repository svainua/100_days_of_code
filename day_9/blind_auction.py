import os  # os.system("clear")

from art import logo

bid_list = {}


def add_bid(name: str, bid: int):
    bid_list[name] = bid


def check_winner():
    biggest_bid = 0
    winner = None
    for key in bid_list:
        if bid_list[key] > biggest_bid:
            biggest_bid = bid_list[key]
            winner = key
    return winner


print(logo)
print("Welcome to the secret auction program.")

should_continue = True
while should_continue:
    name = input("What is your name?:\n")
    bid = int(input("What's your bid?:\n"))

    add_bid(name=name, bid=bid)

    next_player = input(
        "Are there any other bidders? Type 'yes' or 'no'\n"
    ).lower()
    if next_player == "no":
        os.system("clear")
        winner_name = check_winner()
        top_bid = bid_list[winner_name]
        print(bid_list)
        print(f"The winner is {winner_name} a bid of ${top_bid}")
        should_continue = False
    elif next_player == "yes":
        os.system("clear")
