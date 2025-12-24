# Write your solution here
times_per_week = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch?"))
money_per_week = float(input("How much money do you spend on groceries in a week?"))

weekly = price * times_per_week + money_per_week
daily = weekly / 7

print("Average food expenditure:")
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")
