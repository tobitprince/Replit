import os
import time

def add():
    """_summary_
    """
    tweet = input()

def view():
    """_summary_
    """
    tweet = input()

def main():
    """_summary_
    """
    while True:
        os.system("cls")
        print("Tweeter".center(35,"*"))
        menu = int(input("1: Add Tweet\n2: View Tweet"))
        if menu == 1:
            add()
        if menu == 2:
            view()

if __name__ == "__main__":
    main()



