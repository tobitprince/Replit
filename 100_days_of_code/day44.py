"""
2D Dynamic
"""


def prettyprint():
    """_summary_
    """
    for list_row in lists2d:
        for list_item in list_row:
            print(f"{list_item:^10}", end=" | ")
        print()
    print()

lists2d = []

while True:
    menu = input("Add or remove: ")
    if menu.strip().lower()[0] == "a":
        name = input("what is your name: ")
        age = int(input("What is your age: "))
        weight = int(input("What is your weight in kilos: "))

        new_row = [name, age, weight]

        lists2d.append(new_row)
        prettyprint()

    else:
        name = input("What do you want to delete? ")
        for row in lists2d[:]:
            if name in row:
                lists2d.remove(row)
        prettyprint()

    terminate = input("Want to exit? y/n: ")

    if terminate.strip().lower()[0] == "y":
        break

prettyprint()
