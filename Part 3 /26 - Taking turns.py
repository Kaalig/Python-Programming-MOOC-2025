number = int(input("Please type in a number: "))
i = 1
end = number

while i <= end:
    print(i)
    if i != end:
        print(end)
    i += 1
    end -= 1
