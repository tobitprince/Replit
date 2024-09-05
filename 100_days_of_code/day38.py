"""
Rainbow.
"""

# black = '\033[30m'
# red = '\033[31m'
# green = '\033[32m'
# orange = '\033[33m'
# blue = '\033[34m'
# purple = '\033[35m'
# cyan = '\033[36m'
# lightgrey = '\033[37m'
# darkgrey = '\033[90m'
# lightred = '\033[91m'
# lightgreen = '\033[92m'
# yellow = '\033[93m'
# lightblue = '\033[94m'
# pink = '\033[95m'
# lightcyan = '\033[96m

while True:
    print()
    sentence = input("Input any sentence: " ) + " "
    print()
    for letter in sentence:
        if letter.lower() == "r":
            print('\033[31m', end='')
        elif letter.lower() == "b":
            print('\033[34m', end='')
        elif letter.lower() == "g":
            print('\033[32m', end='')
        elif letter.lower()  == "p":
            print('\033[35m', end='')
        elif letter.lower() == "y":
            print('\033[93m', end='')
        elif letter.lower() == " ":
            print('\033[0m', end='')
        print(letter, end="")
    print()
