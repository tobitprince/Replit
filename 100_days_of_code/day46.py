"""
Day 46
"""
import os
import time

mokebeast = {}
def pretty_print():
    """_summary_
    """
    print()
    for key,value in mokebeast.items():
        print(f"Beast Name: {key}", end=" | ")
        for k,v in value.items():
            print(f"{k}: {v}", end=" | ")
        print()
while True:
    os.system("cls")
    name = input("Input the beast name: ").title()
    element = input("Input the element: ").title()
    special_move = input("Input the beast special move: ").title()
    starting_hp = input("Input the beast starting HP: ").title()
    starting_mp = input("input the starting MP: ").title()
    mokebeast[name] = {"Element": element, " Special Move": special_move,
                       " Starting HP": starting_hp, " Starting MP": starting_mp}
    pretty_print()
    another = input("Do your want to add another beast? (y/n): ").strip().lower()

    if another[0] == "n":
        break
    time.sleep(2)
