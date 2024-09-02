"""
Create spam emails.
"""

import os
import time

mailing_list = []

def print_email():
    """_summary_
    """
    os.system("cls")
    print()
    print("Mailing List". center(45,"-"))
    for index, mail in enumerate(mailing_list, start=1):
        print(f"{index}: {mail}")
    time.sleep(1)

def spam():
    """_summary_
    """
    os.system("cls")
    print("Time to start Spamming".center(25,"*"))
    time.sleep(2)
    os.system("cls")
    for x in range(5):
        print(f"Spamming{'.'*(x+1)}")
        print("Please wait")
        time.sleep(1)
        os.system("cls")

    for index, mail in enumerate(mailing_list, start=1):
        print(f"Email {index}".center(7, "-"))
        print()
        message = (
        f"Dear {mail}\n"
        "It has come to our attention\n"
        "that you're missing out on\n"
        "the amazing Replit 100 days of code. We insist you do it right away. "
        "If you don't we will pass on your email address to every spammer we've ever encountered "
        "and also sign you up to the My Little Pony newsletter, because that's neat. "
        "We might just do that anyway.\n"
        "Love and hugs,\n"
        "Ian Spammington III"
        )
        print(message)
        time.sleep(4)
        os.system("cls")
        time.sleep(1)
    print("Emails have been Sent")


while True:
    print()
    print("Get Spamming".center(35,"-"))
    menu = int(input("1: Add Email\n 2: Remove Email\n 3: Show Emails\n 4: Start Spamming\n"))

    if menu == 1:
        email = input("Enter the email you want to add: ")
        mailing_list.append(email)
        print_email()
    elif menu == 2:
        print_email()
        email = input("Enter the email you want to remove: ")
        if email in mailing_list:
            mailing_list.remove(email)
            print_email()
        else:
            print("The email is not in the mailing list")
    elif menu == 3:
        print_email()
    elif menu == 4:
        spam()
    else:
        print("Invalid entry")
    time.sleep(2)
    os.system("cls")
