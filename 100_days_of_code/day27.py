import random
import os
import time


def generate_Character():
    print("Generate Character")
    name = input("Name Your Legend: ")
    print()
    type = input("Character Type (Human, Elf, Wiard, Orc): ")

    return name, type


def randomDice(sides):
    roll = random.randint(1, sides)
    return roll


def generate_Health():
    sixSidedRoll = randomDice(6)
    twelveSidedRoll = randomDice(12)

    health = ((sixSidedRoll * twelveSidedRoll) / 2) + 10

    return health


def generate_Strength():
    sixSidedRoll = randomDice(6)
    twelveSidedRoll = randomDice(12)

    strength = ((sixSidedRoll * twelveSidedRoll) / 2) + 12

    return strength


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
        character, type = generate_Character()

        print()
        print(f"Your Character: {character}")
        health = generate_Health()
        strength = generate_Strength()
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
        exit()
    else:
        continue
