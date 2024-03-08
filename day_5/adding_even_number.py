target = int(input("Enter a number between 0 and 1000 "))

total = 0
for num in range(1, target + 1):
    if num % 2 == 0:
        total += num

print(total)
