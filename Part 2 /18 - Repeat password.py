user = str(input("Password: "))
while True:
    repeat = str(input("Repeat password: "))
    if user == repeat:
        break
    else:
        print("They do not match!")
        repeat
print("User account created!")
