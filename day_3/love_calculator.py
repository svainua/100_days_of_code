print("The Love Calculator is calculating your score...")
name1 = input("What is your name?")
name2 = input("What is their name?")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

"""You are going to write a program that tests the compatibility between 
two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in
 the word TRUE occurs.
Then check for the number of times the letters in the word LOVE occurs.
Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:
"Your score is *x*, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
"Your score is *y*, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is *z*."

"""


def love_calculator(name1: str, name2: str) -> int:
    combined_names = name1.lower() + name2.lower()
    t = combined_names.count("t")
    r = combined_names.count("r")
    u = combined_names.count("u")
    e = combined_names.count("e")
    true_count = str(t + r + u + e)
    l = combined_names.count("l")  # noqa
    o = combined_names.count("o")
    v = combined_names.count("v")
    e = combined_names.count("e")
    love_count = str(l + o + v + e)
    result = int(true_count + love_count)
    return result


score = love_calculator(name1=name1, name2=name2)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
