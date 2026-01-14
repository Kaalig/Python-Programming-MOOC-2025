string = input("Please type in a string: ")
substring = input("Please type in a substring: ")
i = string.find(substring)

if i == -1:
    print("The substring does not occur twice in the string.")
else:
    j = string.find(substring, i + len(substring))

    if j == -1:
        print("The substring does not occur twice in the string.")
    else:
        print(f"The second occurrence of the substring is at index {j}.")
