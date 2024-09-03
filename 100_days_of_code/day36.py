"""
Day 36.
"""

import os
import time

list_of_names = []

def print_names():
    """_summary_
    """
    print("List of Names".center(25,"-"))
    for index , name in enumerate(list_of_names, start=1):
        print(f"{index} : {name}")
    time.sleep(1)

while True:
    print("What is your name?: ")
    first_name = input("First Name: ").strip().title()
    last_name = input("Last Name: ").strip().title()

    full_name=f"{first_name} {last_name}"
    if full_name not in list_of_names:
        list_of_names.append(full_name)
        os.system("cls")
        for x in range(5):
            print(f"Adding your name{'.'*(x+1)}")
            print("Please wait")
            time.sleep(1)
            os.system("cls")
        print_names()
        print("Name added")
        time.sleep(1)
        os.system("cls")
    else:
        print()
        print("The name is already in the list")
        time.sleep(2)
        os.system("cls")
