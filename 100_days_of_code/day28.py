"""
Character Battle
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
    character_type1 = input("Character Type (Human, Elf, Wiard, Orc): ")

    return name, character_type1


def generate_character2():
    """_summary_

    Returns:
        _type_: _description_
    """
    print()
    print("Who are they battling?")
    name2 = input("Name Your Legend: ")
    print()
    character_type2 = input("Character Type (Human, Elf, Wiard, Orc): ")

    return name2, character_type2


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

    health = ((six_sided_roll * twelve_sided_roll) / 2) + 10

    return health


def generate_strength():
    """_summary_

    Returns:
        _type_: _description_
    """
    six_sided_roll = random_dice(6)
    twelve_sided_roll = random_dice(12)

    strength = ((six_sided_roll * twelve_sided_roll) / 2) + 12

    return strength


while True:
    os.system("cls")
    print("Character Builder")
    time.sleep(1)
    print()
    print("Press 1 to generate characters")
    print("Press 2 to Exit")
    print("Press anything else to see the menu again")

    userInput = int(input())

    if userInput == 1:
        print("Name Your Legends and state their character Type")
        character, typo1 = generate_character()
        character2, typo2 = generate_character2()
        health1 = generate_health()
        strength1 = generate_strength()
        health2 = generate_health()
        strength2 = generate_strength()

        print()
        print(f"Your First Character: {character}")
        print(f"HEALTH: {health1}")
        print(f"STRENGTH: {strength1}")
        print()

        print()
        print(f"Your Second Character: {character2}")
        print(f"HEALTH: {health2}")
        print(f"STRENGTH: {strength2}")
        print()
        print("May their names go down in Legend...")

        time.sleep(4)
        os.system("cls")

        print("Let the battle begin")
        COUNT = 0
        print(f"Your First Character: {character}")
        print(f"HEALTH: {health1}")
        print(f"STRENGTH: {strength1}")
        print()
        print(f"Your Second Character: {character2}")
        print(f"HEALTH: {health2}")
        print(f"STRENGTH: {strength2}")
        print()
        while True:

            if health1 > 1 and health2 > 1:
                player1 = random_dice(6)
                player2 = random_dice(6)
                print(f"{character} rolls {player1}")
                print(f"{character2} rolls {player2}")
                if player1 > player2:
                    diff = (abs(strength1 - strength2)) + 1
                    health2 = health2 - diff
                    print(
                        f"{character} wins and lands a damage of {diff} on {character2}"
                    )
                    print()
                    print(f"{character}")
                    print(f"HEALTH: {health1}")
                    print()
                    print()
                    print(f"{character2}")
                    print(f"HEALTH: {health2}")
                    print()
                    COUNT += 1
                elif player2 > player1:
                    diff = (abs(strength1 - strength2)) + 1
                    health1 = health1 - diff
                    print(
                        f"{character2} wins and lands a damage of {diff} on {character}"
                    )
                    print()
                    print(f"{character}")
                    print(f"HEALTH: {health1}")
                    print()
                    print()
                    print(f"{character2}")
                    print(f"HEALTH: {health2}")
                    print()
                    COUNT += 1
                else:
                    print("What are the chances!!The battle ends in a draw")
                    print()
                    print(f"{character}")
                    print(f"HEALTH: {health1}")
                    print()
                    print()
                    print(f"{character2}")
                    print(f"HEALTH: {health2}")
                    print()
                    COUNT += 1

            else:
                if health1 > 1:
                    print(f"Oh no {character2} has died!")
                    print(f"{character} destroyed {character2} in {COUNT} rounds!")
                else:
                    print(f"Oh no {character} has died!")
                    print(f"{character2} destroyed {character} in {COUNT} round(s)!")

                break
            time.sleep(4)
            os.system("cls")
            print("The battle continues!")

        time.sleep(4)
        os.system("cls")
        stop_playback = int(input("Press 2 anytime exit and go back to the menu: "))
        if stop_playback == 2:
            print("2")
        else:
            continue
    elif userInput == 2:
        sys.exit()
    else:
        continue
