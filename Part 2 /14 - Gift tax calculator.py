gift = int(input("Value of gift: "))

if gift > 5000 and gift <= 25000:
    tax = 100
    tax_excess = 0.08
    price = (tax + (gift - 5000) * tax_excess)
    print(f"Amount of tax: {price} euros")
elif gift > 25000 and gift <= 55000:
    tax = 1700
    tax_excess = 0.1
    price = (tax + (gift - 25000) * tax_excess)
    print(f"Amount of tax: {price} euros")

elif gift > 55000 and gift <= 200000:
    tax = 4700
    tax_excess = 0.12
    price = (tax + (gift - 55000) * tax_excess)
    print(f"Amount of tax: {price} euros")
elif gift > 200000 and gift <= 1000000:
    tax = 22100
    tax_excess = 0.15
    price = (tax + (gift - 200000) * tax_excess)
    print(f"Amount of tax: {price} euros")
elif gift > 1000000:
    tax = 142100
    tax_excess = 0.17
    price = (tax + (gift - 1000000) * tax_excess)
    print(f"Amount of tax: {price} euros")
else:
    print("No tax!")
