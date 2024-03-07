def fibonacci(number: int, length: int) -> list:
    fibonacci_list = [0, 1]
    while length - 2 != 0:
        new_num = sum(fibonacci_list[-2:])
        fibonacci_list.append(new_num)
        length -= 1
    return fibonacci_list


print(fibonacci(number=7, length=7))
