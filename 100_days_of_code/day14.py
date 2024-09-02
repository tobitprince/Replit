"""
    Simple game of rock,paper and scissors.
"""

from getpass import getpass

print("Rock, Paper and Scissors!!!")
print()
print()
player1 = input("Player 1 enter you name: ").title()
player2 = input("Player 2 enter your name: ").title()

print("Choose between (R,P,S)")
print()

player1Move = getpass(f"{player1},enter move: ")
print()
player2Move = getpass(f"{player2}, enter move: ")
print()

if player1Move == "R":
    if player2Move == "R":
        print("both rock")
    elif player2Move == "P":
        print("paper wins", player2, "wins!!")
    elif player2Move == "S":
        print("rock wins", player1, "wins")
    else:
        print("Invalid entry")
elif player1Move == "P":
    if player2Move == "P":
        print("both paper")
    elif player2Move == "R":
        print("paper wins", player1, "wins!!")
    elif player2Move == "S":
        print("scissors wins", player2, "wins")
    else:
        print("Invalid entry")
elif player1Move == "S":
    if player2Move == "S":
        print("both scissors")
    elif player2Move == "R":
        print("rock wins", player2, "wins!!")
    elif player2Move == "P":
        print("scissors wins", player1, "wins")
    else:
        print("Invalid move", player2)
else:
    print("Invalid Move Player 1!")
