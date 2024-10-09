"""
_summary_
"""
import os
import time
import random

trumps = {}
trumps["Naruto"]= {"Intelligence": 90, "Speed":80}
trumps["Sukuna"]= {"Intelligence": 90, "Speed":80}
trumps["Goju"]= {"Intelligence": 90, "Speed":80}

while True:
    os.system("cls")
    print ("Trumps Game")
    print()
    for key, value in trumps.items():
        print (key)

    card = input("Choose your character: ").title()
    availableitems= list(trumps.keys())
    availableitems.remove(card)
    cardpc = random.choice(availableitems)
    print(f"The computer chose {cardpc}")
    print(f"You chose {card}")
    os.system("cls")

    for i in range(1,5):
        print ("Let the games begin")
        print("*" * i)
        i = i+1
        time.sleep(1)
        os.system("cls")

    choice = input("Choose a category \n 1. Intelligence \n 2. Speed\n >  ").title()

    print(f"{card} has a stat of {trumps[card][choice]}")
    print(f"{cardpc} has a stat of {trumps[cardpc][choice]}")
    if trumps[card][choice] > trumps[cardpc][choice]:
        print(f"You win {card} has more")
    elif trumps[cardpc][choice] > trumps[card][choice]:
        print(f"The computer wins. {cardpc} has more")
    else:
        print("It is a draw")

    exit_game = input("Do you wish to continue? y/n: ").strip().lower()

    if exit_game[0] == "n":
        exit()
    time.sleep(1)
    