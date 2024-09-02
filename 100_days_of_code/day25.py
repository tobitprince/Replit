"""
This module rolls a dice that generates character stats.
"""

import random


def any_dice(num_sides):
    """
    Rolls a dice of any number of sides
    """

    result = random.randint(1, num_sides)
    return result


def dice6_8():
    """_summary_

    Returns:
        _type_: _description_
    """
    six = any_dice(6)
    eight = any_dice(8)

    result = six * eight
    return result


print("Character Health Stats")
print()
CHARACTER = "yes"

while CHARACTER == "yes":
    health = dice6_8()
    print(f"Character health stat is {health} hp")
    CHARACTER = input("Generate for another character?: ")
