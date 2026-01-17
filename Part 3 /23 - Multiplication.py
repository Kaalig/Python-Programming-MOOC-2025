number = int(input("Please type in a number: "))

x = 1
while x <= number:
    y = 1
    while y <= number:
        print(f"{x} x {y} = {x * y}")
        y += 1
    x += 1
