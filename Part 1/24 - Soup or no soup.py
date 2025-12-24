# Write your solution here
name = str(input("Please tell me your name:"))
if name == "Jerry":
    print("Next please!")

if name != "Jerry":
    portions = int(input("How many portions of soup? "))
    price_portion = 5.90
    total = price_portion * portions
    print(f"The total cost is {total}:.1d")
    print("Next please!")
    
