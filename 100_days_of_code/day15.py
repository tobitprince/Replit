"""
    This module generates an animal sound.
"""

EXIT = "no"
while EXIT == "no":
    print("Animal sound")
    print()
    animal = input("What animal do you want?: ").lower()
    print()
    if animal == "cow":
        print(f"A {animal} goes moo")
    elif animal == "sheep":
        print(f"A {animal} goes mee")
    else:
        print("I don't know that animal. Try again")
    EXIT = input("Do you want to exit?: ").lower()
