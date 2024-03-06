print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
percentage = int(
    input("What percentage tip would you like to give? 10, 12 or 15? ")
)

amount_to_pay = round(
    (total_bill + ((total_bill * percentage) / 100)) / people, 2
)
formatted_number = "{:.2f}".format(amount_to_pay)


print(f"Each person should pay ${formatted_number}")
