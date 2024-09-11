"""
2D LIsts
"""
import random

numberlist = [0] * 9

for index, _ in enumerate(numberlist):
    numberlist[index] = random.randint(1,90)

numberlist.sort()

bingolist = [[None, None, None],
            [None, None, None],
            [None, None, None]]

INDEX = 0
for row in range(3):
    for col in range(3):
        if row == 1 and col == 1:
            bingolist[row][col] = "BINGO"
        else:
            bingolist[row][col]=numberlist[INDEX]
            INDEX += 1

for row in bingolist:
    print(row)
