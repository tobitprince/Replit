"""
Designing a user interface.
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


def new_print(color, word):
    """_summary_

    Args:
        color (_type_): _description_
        word (_type_): _description_
    """
    if color == "red":
        print("\033[31m", word)
    elif color == "green":
        print("\033[32m", word)
    elif color == "blue":
        print("\033[34m", word)
    elif color == "orange":
        print("\033[33m", word)
    elif color == "purple":
        print("\033[35m", word)
    elif color == "yellow":
        print("\033[93m", word)
    else:
        print("\033[0m", word)


print()
new_print("orange", "--- Music App ---".center(35))
print()
new_print("reset", "🔥▶️  Radio Gaga")
new_print("yellow", "Queen".center(15))
print()
print()
new_print("reset", "PREV")
new_print("green", "NEXT".center(16))
new_print("purple", "PAUSE".center(32))
print()
print()
print()
print()
new_print("reset", "WELCOME TO".center(35))
new_print("blue", "-----  ARMBOOK -----".center(35))
print()
new_print("yellow", "Definitely not a rip off of".rjust(35))
print("a certain other social".rjust(36))
print("networking site".rjust(36))
print()
new_print("red", "Honest.".center(33))
print()
new_print("reset", "Username: ".center(35))
print("Password: ".center(37))
