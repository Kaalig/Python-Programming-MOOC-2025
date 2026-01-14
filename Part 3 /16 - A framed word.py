word = input("Word:" )
space = 28 - len(word)
right_space = space // 2
left_space = space // 2

if len(word) % 2 == 0:
    right_spâce = left_space
else:
    right_space = left_space + 1


print("*" * 30)
print("*" +  (" " * left_space) + word + (" " * right_space) + "*")
print("*" * 30)
