import os

from art import logo

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
] * 2


def caesar(direction: str, text: str, shift: int):
    if shift > 26:
        shift = shift % 26
    if direction == "decode":
        shift *= -1
    cypher_word = ""
    for letter in text:
        if letter not in alphabet:
            cypher_word += letter
        else:
            index = alphabet.index(letter)
            new_letter = alphabet[index + shift]
            cypher_word += new_letter
    print(f"The secret word is '{cypher_word}'")


should_continue = True
while should_continue:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction=direction, text=text, shift=shift)

    restart = input(
        "Do you want to restart?"
        "Type 'yes' if you want to go again. Otherwise type 'no':\n"
    ).lower()
    if restart == "no":
        should_continue = False
    else:
        os.system("clear")
