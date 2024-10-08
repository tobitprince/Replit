"""
_summary_
"""
import os
import time
import random

trumps = {}
trumps["Naruto"] = {"Intelligence": 40, "Speed": 90, "Punch": 49, "Sword Skill": 60}
trumps["Satoru"] = {"Intelligence": 50, "Speed": 99, "Punch": 79, "Sword Skill": 45}
trumps["Sukuna"] = {"Intelligence": 30, "Speed": 80, "Punch": 69, "Sword Skill": 70}
trumps["Yoji"] = {"Intelligence": 60, "Speed": 70, "Punch": 89, "Sword Skill": 30}
while True:
    os.system("cls")
    print("Top Trumps".center(35,'*'))
    print("Welcome to the Top Trumps Simulator")
    for key, value in trumps.items():
        print(key)
    card = input("Choose your character: ").title()
    # Ensure the computer does not pick the same character as the user
    available_characters = list(trumps.keys())
    available_characters.remove(card)
    cardpc = random.choice(available_characters)
    print(f"The computer has picked {cardpc}")

    choice= input("Choose your stat:\n\
    1. Intelligence \n\
    2. Speed \n\
    3. Punch \n\
    4. Sword Skill \n").strip().title()
    print(f"{card} has {choice} of stat {trumps[card][choice]}")
    print(f"{cardpc} has {choice} of stat {trumps[cardpc][choice]}")

    if trumps[card][choice] > trumps[cardpc][choice]:
        print(f"You win!, {card} has more")
    elif trumps[cardpc][choice] > trumps[card][choice]:
        print(f"Computer wins! {cardpc} has more")
    else:
        print("It is a draw")

    time.sleep(6)
