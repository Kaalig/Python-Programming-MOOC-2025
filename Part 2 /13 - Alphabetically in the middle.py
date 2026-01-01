first = str(input("1st letter: "))
second = str(input("2nd letter: "))
third =  str(input("3rd letter: "))

if first > second and first < third or first < second and first > third:
    print("The letter in the middle is", first)
elif second > first and second < third or second < first and second > third:
    print("The letter in the middle is", second)
else:
    print("The letter in the middle is", third)
