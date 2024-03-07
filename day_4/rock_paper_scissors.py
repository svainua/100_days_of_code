import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

variants = [rock, paper, scissors]
computer_choice = random.randint(0, 2)
player_choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ).lower()
)

print(variants[player_choice])
print("Computer choice:")
print(variants[computer_choice])

if player_choice == computer_choice:
    print("Draw")
elif player_choice == 0 and computer_choice == 2:
    print("You win")
elif player_choice == 1 and computer_choice == 0:
    print("You win")
elif player_choice == 2 and computer_choice == 1:
    print("You win")
else:
    print("You loose")
