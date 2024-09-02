"""
This module changes color.
"""

def new_print(color, word):
    """_summary_

    Args:
        color (_type_): _description_
        word (_type_): _description_
    """
    if color == "red":
        print("\033[31m", word, sep="", end="")
    elif color == "green":
        print("\033[32m", word, sep="", end="")
    elif color == "blue":
        print("\033[34m", word, sep="", end="")
    else:
        print("\033[0m", word, sep="", end="")


print("Super Subroutine")
print("With my ", end="")
new_print("red", "new program")
new_print("reset", "I can just call red('and')")
new_print("red", "it will print in red ")
new_print("blue", "or even blue")
