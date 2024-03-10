import os
import random

from hangman_art import logo, stages
from hangman_words import word_list

lives = 6
chosen_word = random.choice(word_list)

print(logo)
print(f"Psss, the chosen word in {chosen_word}")

display = ["_" for i in range(len(chosen_word))]
print(display)

should_continue = True
while should_continue:
    guess = input("Guess a letter:\n").lower()
    os.system("clear")

    if guess in display:
        print(f"You already chose letter '{guess}' before, try again")

    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess

    if guess not in chosen_word:
        print(f"No letter '{guess}' in the secret word, try again'")
        lives -= 1
        if lives == 0:
            print("You lose")
            should_continue = False

    print(f"{' '.join(display)}")

    if "_" not in display:
        print("You win")
        should_continue = False

    print(stages[lives])
