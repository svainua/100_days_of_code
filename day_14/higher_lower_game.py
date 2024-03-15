import os
import random
from game_data import data
from art import logo, vs

print(logo)
score = 0
a = random.choice(data)
should_continue = True

while should_continue:
    b = random.choice(data)
    while a == b:
        b = random.choice(data)

    print(f"Compare A: {a["name"]}, {a["description"]}, from {a["country"]}.")
    print()
    print(vs)
    print(f"Compare B: {b["name"]}, {b["description"]}, from {b["country"]}.")
    print()

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if (guess == "a" and a["follower_count"] > b["follower_count"]) or (guess == "b" and b["follower_count"] > a["follower_count"]):
        score += 1
        a = b
        os.system("clear")
        print(logo)
        print(f"You are right! Current score: {score} ")
    else:
        os.system("clear")
        print(logo)
        print(f"You loose. Final score: {score}") 
        should_continue = False

    