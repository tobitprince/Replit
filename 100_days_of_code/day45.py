"""
New and improved to do list with priority
"""
import time
import os

to_do_list = []

def prettyprint():
    """_summary_
    """
    for task_row in to_do_list:
        for task_item in task_row:
            print(f"{task_item:^10}", end="|")
        print()

    print()


def add_list(index=None):
    """_summary_

    Args:
        task (_type_): _description_
        due_date (_type_): _description_
        priority (_type_): _description_
    """

    if index is not None:
        task = input("What is the new task?: ")
        due_date = input("When is it now due by?: ")
        priority = input("What is the new priority?: ")
        new_row = [task, due_date, priority]
        to_do_list[index] = new_row
    else:
        task = input("What is the task?: ")
        due_date = input("When is it due by?: ")
        priority = input("What is the priority?: ")
        new_row = [task, due_date, priority]
        to_do_list.append(new_row)
    prettyprint()




os.system("cls")

while True:
    os.system("cls")
    print("To do list".center(35,"-"))
    menu = input("Add, View, Edit or Remove: ").strip().lower()

    if menu[0] == "a":
        add_list()
        print("Item has been added")
        time.sleep(1)
        os.system("cls")

    if menu[0] == "v":
        option = input("View all or Priority?: ").strip().lower()
        if option[0] == "a":
            prettyprint()

        if option[0] == "p":
            level = input("High, Medium or Low: ").strip().lower()
            if level[0] == "h":
                for row in to_do_list:
                    if "high" in row:
                        for item in row:
                            print(f"{item:^10}", end="|")
                        print()
            if level[0] == "m":
                for row in to_do_list:
                    if "medium" in row:
                        for item in row:
                            print(f"{item:^10}", end="|")
                        print()
            if level[0] == "l":
                for row in to_do_list:
                    if "low" in row:
                        for item in row:
                            print(f"{item:^10}", end="|")
                        print()

    if menu[0] == "e":
        prettyprint()
        edit = input("Which item do you want to edit?: ")
        for row in to_do_list:
            if edit in row:
                for item in row:
                    print(f"{item:^10}", end="|")
                print()
                task_index = to_do_list.index(row)
                add_list(task_index)
                print("Item has been edited")
                time.sleep(3)
                os.system("cls")

    if menu[0] == "r":
        prettyprint()
        deletion = input("Do you want to delete an item or the whole list?: ").strip().lower()
        if deletion[0] == "i":
            item = input("Which item do you want to delete?: ")
            for row in to_do_list[:]:
                if item in row:
                    answer=input("Are you sure you want to remove this?").strip().lower()
                    if answer[0] == "y":
                        to_do_list.remove(row)
                        print("Item has been deleted")
                        time.sleep(3)
                        os.system("cls")
                        prettyprint()

        if deletion[0] == "w":
            for x in range(5):
                print(f"Deleting Everything{'.'*(x+1)}")
                print("PLease Wait")
                time.sleep(3)
                os.system("clear")

            to_do_list = []
            print("The To do List has been erased")

    exit_loop = input("Do you want to see the menu again or quit? ").strip().lower()
    if exit_loop[0] == "q":
        break
