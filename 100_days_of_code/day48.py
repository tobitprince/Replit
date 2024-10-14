"""
_summary_
"""
import os
import time


while True:
    os.system("cls")
    print("HIGH SCORES TABLE".center(34,"-"))
    print()
    initials = input("Input your initials: ").capitalize()
    score = input("Input your score: ")
    f = open("high.score", "a+", encoding= "utf-8")
    f.write(f"{initials} {score}\n")
    f.close()

    print("Added to the High Score Table")
    another = input("Do you wish to add another? y/n: ").strip().lower()
    if another[0] == "n":
        exit()
    time.sleep(1)
    os.system("cls")
