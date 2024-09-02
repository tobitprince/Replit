"""
List Manager.
"""

import os
import time

to_do_list = []


def print_list():
    """_summary_
    """
    print()
    for i in to_do_list:
        print()
        print(i.center(35))


print("To Do List Manager".center(35, "-"))

while True:
    print()
    option = input("Do you want to view, add or remove your to do list?")
    os.system("cls")
    if option == "view":
        print("To Do List".center(35, "-"))
        print_list()
        time.sleep(3)
        os.system("cls")
    elif option == "add":
        item = input("What do you want to add? ")
        to_do_list.append(item)
        print("To Do List".center(35, "-"))
        print_list()
        time.sleep(3)
        os.system("cls")
    elif option == "remove":
        print("To Do List".center(35, "-"))
        print_list()
        item = input("What have you finished and want to remove? ")
        time.sleep(1)
        os.system("cls")
        if item in to_do_list:
            to_do_list.remove(item)
            print("To Do List".center(35, "-"))
            print_list()
            time.sleep(3)
            os.system("cls")
        else:
            print("The item is not in the list!!")
            print()
            print("To Do List".center(35, "-"))
            print_list()
            time.sleep(3)
            os.system("cls")
