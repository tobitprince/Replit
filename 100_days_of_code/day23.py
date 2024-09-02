def loginSystem():

    print("Login System")
    print()
    while True:
        username = input("What is your username?: ")
        password = input("What is your password?: ")

        if username == "chimi" and password == "123":
            print("Welcome Chimi")
            break
        else:
            print("That's not correct. Try again!")
            continue


loginSystem()
