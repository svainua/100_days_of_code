def prime_checker(number: int) -> None:
    prime_number = True
    for num in range(2, number):
        if number % num == 0:
            prime_number = False
    if prime_number:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number:\n"))
prime_checker(number=n)
