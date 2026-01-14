word = str(input("Please type in a word: "))
character = str(input("Please type in a character: "))
i = word.find(character)

if i != -1 and i + 3 <= len(word):
    print(word[i:i+3])
