"""
👉 Day 53 Challenge
Your video game inventory system should:
1. Have a menu that allows the user to:
1. Add
2. View
3. Remove
2. Adding an item saves it to a file using captalize mode. Duplicates are allowed.
3. Removing an item deletes it from the file.
4. View is trickier. It should output the name of the item and tell you how many of those items
you have.
5. Use auto-save and auto-load with try... except.
"""

import os
import time
import ast

inventory = []
try:
    with open("inventory.txt","r",encoding="utf8") as file:
        content = ast.literal_eval(file.read())
        for row in content:
            inventory.append(row)
except FileNotFoundError:
    print("File not found")

def add():
    """_summary_
    """
    item = input("Input the item to add: ").title()
    inventory.append(item)
    print(f"{item} has been added to your inventory")
    time.sleep(1)

def remove():
    """_summary_
    """
    item = input("Input the item to remove: ")
    if item in inventory:
        inventory.remove(item)
        print(f"{item} has been removed from your inventory")
    else:
        print("Item not in inventory")
    time.sleep(1)

def view():
    """_summary_
    """
    item = input("Input the item to view: ").title()
    count=0
    for items in inventory:
        if items == item:
            count += 1
    if count == 1:
        print(f"You have {count} {item}")
    elif count > 1:
        print(f"You have {count} {item}s")
    else:
        print(f"You have {count} {item}")
    time.sleep(1)

while True:
    os.system("cls")
    print("RPG Inventory".center(45,"*"))
    option = int(input("1: Add\n2: Remove\n3: View\nEnter option: "))
    if option == 1:
        add()
    elif option == 2:
        remove()
    elif option == 3:
        view()
    time.sleep(2)
    with open("inventory.txt","w", encoding="utf8") as file:
        file.write(str(inventory))
