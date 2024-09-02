"""
This module rolls a dice
"""

import random

def roll_dice(num_sides):
    """
    Roll a dice.
    """

    roll = random.randint(1, num_sides)
    print(f"You rolled {roll}")


print("Infinity Dice")
print()
print()
sides = int(input("How many sides?: "))
while True:
    roll_dice(sides)
    answer = input("Roll again?: ").lower()

    if answer == "yes":
        continue
    break
print("Goodbye!")
