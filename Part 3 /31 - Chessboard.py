# Write your solution here
def chessboard(length):
    for i in range(length):
        chessboard_number = ""
        for j in range(length):
            if (i + j) % 2 == 0: # odd or even
                chessboard_number += "1"
            else:
                chessboard_number += "0"
        print(chessboard_number)

# Testing the function
if __name__ == "__main__":
    chessboard(3)
