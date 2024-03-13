from art import logo


def add(n1: float, n2: float) -> float:
    return n1 + n2


def substract(n1: float, n2: float) -> float:
    return n1 - n2


def multiply(n1: float, n2: float) -> float:
    return n1 * n2


def divide(n1: float, n2: float) -> float:
    return n1 / n2


def calculator():
    print(logo)
    num1 = float(input("Enter first number: "))

    for key in operators:
        print(key)

    should_continue = True
    while should_continue:
        choose_operator = input("Choose the operator: ")
        num2 = float(input("Enter the next number: "))
        answer = operators[choose_operator](num1, num2)

        print(f"{num1} {choose_operator} {num2} = {answer}")

        next_step = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calc. "  # noqa
        )
        if next_step == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


operators = {"+": add, "-": substract, "*": multiply, "/": divide}

calculator()
