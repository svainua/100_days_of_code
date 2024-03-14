import random

secret_number = random.randint(1, 100)
print(f"pshhh secret number is {secret_number}")
print("Welcome to the Number Guessing Game!")
print("I am thinking about the number between 1 and 100")
difficulty = input("Choose the difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5


def check_answer(guess: int, secret_number: int):
    if guess == secret_number:
        print(f"You got it! The answer was {secret_number}")
        return lives + 20
    elif guess > secret_number:
        print("Too high")
        return lives - 1
    else:
        print("Too low")
        return lives - 1


while lives > 0:
    print(f"You have {lives} attempts remaining to make a guess") 
    guess = int(input("Make a guess: "))
    lives = check_answer(guess=guess, secret_number=secret_number)
    if lives == 0:
        print("You've run out of guesse, you lose.")
        break
    elif lives > 15:
        break    
    print("Guess again")



