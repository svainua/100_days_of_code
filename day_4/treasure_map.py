line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
my_map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure?").lower()
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

position_list = list(position)
if position_list[0] == "a":
    x_pos = 0
elif position_list[0] == "b":
    x_pos = 1
elif position_list[0] == "c":
    x_pos = 2

y_pos = int(position_list[-1]) - 1
my_map[y_pos][x_pos] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
