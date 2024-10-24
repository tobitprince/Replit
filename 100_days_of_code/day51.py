import os
import time
import ast

todo = []
with open("todolist.txt", "r", encoding="utf8") as file:
    content = file.read()
    todo = ast.literal_eval(content)

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
    option = int(input("1. Add\n2. View\n3. Edit\n4. Remove\nEnter your choice: "))
    if option == 1:
        add()
    elif option == 2:
        view()
    elif option == 3:
        edit()
    elif option == 4:
        remove()
    else:
        print("Invalid choice, please try again.")
        time.sleep(1)

    time.sleep(1)
    with open("todolist.txt","w",encoding="utf8") as file:
        file.write(str(todo))
