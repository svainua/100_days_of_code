from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def report(resources: dict, money: float):
    """Gives the report about the availability of ingredients"""
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}gr")
    print(f"Money: ${money}")

def check_resources(product: str, resources: dict, menu: dict) -> bool:
    """Returns True when order can be made, False if ingredients are insufficient."""
    for needed_ingedient in menu[product]["ingredients"]:
        if menu[product]["ingredients"][needed_ingedient] > resources[needed_ingedient]:
            print(f"Sorry there is not enough {needed_ingedient}.")
            return False
    return True    

def process_coins():
    """Returns the total calculated from coins inserted."""
    coins_value = {
        "quarters": 0.25,
        "dimes": 0.1,
        "nickels": 0.05,
        "pennies": 0.01
    }

    print("Please insert coins")
    quarters = int(input("How may quarters?: ")) * coins_value["quarters"]
    dimes = int(input("How may dimes?: ")) * coins_value["dimes"]
    nickels = int(input("How may nickels?: ")) * coins_value["nickels"]
    pennies = int(input("How may pennies?: ")) * coins_value["pennies"]

    total = quarters + dimes + nickels + pennies

    return total

def check_transaction(product: str, payment: float, menu: dict):
    """Return True when the payment is accepted, or False if money is insufficient."""
    global money
    if payment < menu[product]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif payment > menu[product]["cost"]:
        change = round(payment - menu[product]["cost"], 2)
        print(f"Here is ${change} dollars in change")
        money += menu[product]["cost"]
        return True
    else:
        money += menu[product]["cost"]
        return True

def make_coffee(product: str, ingredients: dict, menu: dict):
    """Deduct the required ingredients from the resources."""
    global resources
    for item in menu[product]["ingredients"]:
        resources[item] -= menu[product]["ingredients"][item]
    print(f"Here is your {product}. Enjoy!")   
    return resources    


should_continue = True
while should_continue:

    prompt = input("What would you like? (espresso/latte/cappuccino):").lower()
    if prompt == "report":
        report(resources=resources, money=money)
    elif prompt == "off":
        print("Goodbye")
        should_continue = False
    else:
        if check_resources(product=prompt, resources=resources, menu=MENU) == True:
            payment = process_coins()
            if check_transaction(product=prompt, payment=payment, menu=MENU) == True:
                make_coffee(product=prompt, ingredients=resources, menu=MENU)

           



