"""
Idea Storage
"""
import os
import time
import random

ideas = []
def pretty_print():
    """_summary_
    """
    with open("my.ideas", "r", encoding="utf-8") as file:
        maneno = file.read().split("\n")
    for index, row in enumerate(maneno, start=1):
        print(f"{index} : {row.title()}")
    print()

def new_idea():
    """_summary_
    """
    new = input("Input  your idea > ")
    # ideas.append(new)
    with open("my.ideas", "+a", encoding="utf-8") as file:
        file.write(f"{new}\n")
    print("Nice! Your idea has been stored")

def see_random():
    """_summary_
    """
    with open("my.ideas", "r", encoding="utf-8") as file:
        maneno = file.read().split("\n")
    choice = random.choice(maneno)
    print(choice.title())

while True:
    os.system("cls")
    print("Idea Storage".center(55,"*"))
    option = input("Add an idea or see a random idea? a/r > ").lower()
    if option[0] == "a":
        pretty_print()
        new_idea()
    elif option[0] == "r":
        see_random()
    else:
        exit()
    time.sleep(1)
