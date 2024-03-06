"""Based on a user's order, work out their final bill.
Small pizza (S): $15
Medium pizza (M): $20
Large pizza (L): $25
Add pepperoni for small pizza (Y or N): +$2
Add pepperoni for medium or large pizza (Y or N): +$3
Add extra cheese for any size pizza (Y or N): +$1"""

print("Thank you for choosing Python Pizza Deliveries!")
size = input(
    "What is the size"
).upper()  # What size pizza do you want? S, M, or L
add_pepperoni = input(
    "Want to add pepperoni?"
).upper()  # Do you want pepperoni? Y or N
extra_cheese = input(
    "Want to add extra cheese"
).upper()  # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇


final_bill = 0

if size == "S":
    final_bill += 15
    if add_pepperoni == "Y":
        final_bill += 2
elif size == "M":
    final_bill += 20
    if add_pepperoni == "Y":
        final_bill += 3
elif size == "L":
    final_bill += 25
    if add_pepperoni == "Y":
        final_bill += 3

if extra_cheese == "Y":
    final_bill += 1

print(f"Your final bill is: ${final_bill}.")
