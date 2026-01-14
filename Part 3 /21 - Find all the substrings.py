word = str(input("Please type in a word: "))
character = str(input("Please type in a character: "))
i = word.find(character)

while len(word) >= 3:
    if word[0] == character:
        print(word[0:3])
    word = word[1:]
