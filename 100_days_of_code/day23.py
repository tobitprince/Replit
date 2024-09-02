"""
This is a simple login system.
"""

def login_system():
    """
    Simple routine.
    """

    print("Login System")
    print()
    while True:
        username = input("What is your username?: ")
        password = input("What is your password?: ")

        if username == "chimi" and password == "123":
            print("Welcome Chimi")
            break
        print("That's not correct. Try again!")
        continue


login_system()
