string = str(input("Please type in a string: "))
count = 0
sum = ""

while count < len(string):
    sum += string[count]
    print(sum)
    count += 1
