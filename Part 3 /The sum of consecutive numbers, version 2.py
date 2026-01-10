limit = int(input("Limit:"))
number = 1
i = 1
summ = "1"

while i < limit:
    number += 1
    i += number
    summ += f" + {number}"
print(f"The consecutive sum: {summ} = {i}")
