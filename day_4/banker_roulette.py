import random

names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")
# The code above converts the input into an array seperating
# each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

length = len(names)
random_num = random.randint(0, length - 1)
random_name = names[random_num]

print(f"{random_name} is going to buy the meal today!")
