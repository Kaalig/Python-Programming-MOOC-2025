# Took me 2hours 

def squared(string, size):
    for i in range(size):
        line = ""
        for j in range(size):
            index = (i * size + j) % len(string)
            line += string[index]
        print(line)
