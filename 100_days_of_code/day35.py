"""
List Manager.
"""

import os
import time

to_do_list = []


def print_list():
    """_summary_
    """
    os.system("cls")
    print("To Do List". center(45,"-"))
    for i, todolist in enumerate(to_do_list, start=1):
        print()
        print(f"{i}: {todolist}")
    time.sleep(2)


print("To Do List Manager".center(35, "-"))

while True:
    print()
    option = input("What do you want to do to your list?\n"
                   "1: View\n 2: Add\n 3: Remove\n 4: Edit\n"
                   "5: Delete\n >: ").lower()
    os.system("cls")
    if option == "view":
        print_list()
        time.sleep(3)
        os.system("cls")
    elif option == "add":
        item = input("What do you want to add? ")
        to_do_list.append(item)
        print_list()
        print("Item has been added")
        time.sleep(3)
        os.system("cls")
    elif option == "remove":
        print_list()
        item = input("What have you finished and want to remove? ")
        time.sleep(1)
        os.system("cls")
        if item in to_do_list:
            answer=input("Are you sure you want to remove this?")
            if answer == "yes":
                to_do_list.remove(item)
                print_list()
                print("Item has been removed!")
                time.sleep(3)
                os.system("cls")
        else:
            print("The item is not in the list!!")
            print()
            print_list()
            time.sleep(3)
            os.system("cls")
    elif option == "edit":
        print_list()
        item = input("What do you want to edit?: ")
        new = input("What do you want to edit it to?: ")
        for index, todo in enumerate(to_do_list):
            if todo == item:
                to_do_list[index] = new
                print_list()
                print("Item has been edited")
                time.sleep(3)
                os.system("cls")
            else:
                print("Item not in list")
                time.sleep(3)
                os.system("cls")
    elif option == "delete":
        print_list()
        for x in range(5):
            print(f"Deleting Everything{'.'*(x+1)}")
            print("Please wait")
            time.sleep(3)
            os.system("cls")
        to_do_list = []
        print("The To do List has completely been erased!!")
        time.sleep(3)
        os.system("cls")
