numbers = []
positive = 0
negative = 0

print("Please type in integer numbers. Type in 0 to finish.")

while True:
    number = int(input("Number: "))
    if number == 0:
        break
    numbers.append(number)

print("... the program asks for numbers")
print(f"Numbers typed in {len(numbers)}")
print(f"The sum of the numbers is {sum(numbers)}")
print(f"The mean of the numbers is {sum(numbers) / len(numbers)}")

for nbr in numbers:
    if nbr > 0:
        positive += 1
    elif nbr < 0:
        negative += 1

print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")
