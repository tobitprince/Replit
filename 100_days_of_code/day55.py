"""
Back the 'f' up everybody!
'f' is short for 'file', of course. What did you think I meant?
Get your minds out of the gutter, go back and get your auto save/load to do list
from Day 51 and use it here.
Your program should:
1. Create a backup folder.
2. Create a random filename.
3. Save a copy of the data to that file.
4. This should all happen before the auto save._summary_
"""
import os
import time
import ast

todo = []
FILEEXISTS = True
try:
    with open("todolist.txt", "r", encoding="utf8") as file:
        content = file.read()
        todo = ast.literal_eval(content)
except FileNotFoundError:
    FILEEXISTS = False

def add():
    """_summary_
    """
    os.system("cls")
    name = input("Name: ")
    due = input("Due Date: ")
    priority = input("Priority: ")
    row = [name,due,priority]
    todo.append(row)
    print("Task Added Successfully")

def view():
    """_summary_
    """
    os.system("cls")
    print("To Do List".center(35,"-"))
    option = int(input("1. All\n2. By Priority\nEnter your choice: "))
    if option == 1:
        for row in todo:
            print(f"{row[0]} | {row[1]} | {row[2]}\n")
    if option == 2:
        priority = input("Enter priority: ").lower()
        for row in todo:
            if priority in row:
                print(f"{row[0]} | {row[2]} | {row[2]}\n")
    time.sleep(3)

def edit():
    """_summary_
    """
    os.system("cls")
    find = input("What do you want to edit? ")
    for row in todo:
        if find in row:
            todo.remove(row)
            add()
            break
    else:
        print("Task not found")
        time.sleep(2)

def remove():
    """_summary_
    """
    os.system("cls")
    find = input("What do you want to remove? ")
    for row in todo:
        if find in row:
            todo.remove(row)
            print("Task removed successfully")
            break
    else:
        print("Task not found")
        time.sleep(1)


while True:
    os.system("cls")
    print("Welcome to To do List Manager".center(55, "-"))
    inputs = int(input("1. Add\n2. View\n3. Edit\n4. Remove\nEnter your choice: "))
    if inputs == 1:
        add()
    elif inputs == 2:
        view()
    elif inputs == 3:
        edit()
    elif inputs == 4:
        remove()
    else:
        print("Invalid choice, please try again.")
        time.sleep(1)

    time.sleep(1)
    if FILEEXISTS:
        try:
            os.mkdir("backups")
        except FileExistsError:
            pass
        file_name = f"backups\{time.strftime('%Y%m%d%H%M%S')}.txt"
        result = os.system(f"copy todolist.txt {file_name}")
        if result == 0:
            print("Backup successful")
        else:
            print("Backup failed")
    with open("todolist.txt","w",encoding="utf8") as file:
        file.write(str(todo))
    time.sleep(2)
