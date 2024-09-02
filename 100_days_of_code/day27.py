"""
Character Generator.
"""
import random
import os
import time
import sys


def generate_character():
    """_summary_

    Returns:
        _type_: _description_
    """
    print("Generate Character")
    name = input("Name Your Legend: ")
    print()
    character_type = input("Character Type (Human, Elf, Wiard, Orc): ")

    return name, character_type


def random_dice(sides):
    """_summary_

    Args:
        sides (_type_): _description_

    Returns:
        _type_: _description_
    """
    roll = random.randint(1, sides)
    return roll


def generate_health():
    """_summary_

    Returns:
        _type_: _description_
    """
    six_sided_roll = random_dice(6)
    twelve_sided_roll = random_dice(12)

    generated_health = ((six_sided_roll * twelve_sided_roll) / 2) + 10

    return generated_health


def generate_strength():
    """_summary_

    Returns:
        _type_: _description_
    """
    six_sided_roll = random_dice(6)
    twelve_sided_roll = random_dice(12)

    character_strength = ((six_sided_roll * twelve_sided_roll) / 2) + 12

    return character_strength


while True:
    os.system("cls")
    print("Character Builder")
    time.sleep(1)
    print()
    print("Press 1 to generate character")
    print("Press 2 to Exit")
    print("Press anything else to see the menu again")

    userInput = int(input())

    if userInput == 1:
        print("Name Your Legend and state it's character Type")
        character, typo = generate_character()

        print()
        print(f"Your Character: {character}")
        health = generate_health()
        strength = generate_strength()
        print(f"HEALTH: {health}")
        print(f"STRENGTH: {strength}")
        print()

        print("May your name go down in Legend...")
        stop_playback = int(
            input("Press 2 anytime to pause playback and go back to the menu: ")
        )
        if stop_playback == 2:
            print("2")
        else:
            continue
    elif userInput == 2:
        sys.exit()
    else:
        continue
