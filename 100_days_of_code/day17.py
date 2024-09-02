"""
    Rock, paper and scissors.
"""

from getpass import getpass
import sys

print("Rock, Paper and Scissors!!!")
print()
print()
player1 = input("Player 1 enter you name: ").title()
player2 = input("Player 2 enter your name: ").title()

print("Choose between (R,P,S)")
print()
PLAYER1COUNT = 0
PLAYER2COUNT = 0
while True:

    if PLAYER1COUNT != 3 and PLAYER2COUNT != 3:
        player1Move = getpass(f"{player1},enter move: ").upper()
        print()
        player2Move = getpass(f"{player2}, enter move: ").upper()
        print()

        if player1Move == "R":
            if player2Move == "R":
                print("Both rock, it's a draw")
                print(f"The score is {PLAYER1COUNT}:{PLAYER2COUNT}")
                continue
            if player2Move == "P":
                print("Paper wins", player2, "wins!!")
                PLAYER2COUNT += 1
                print(f"The score is {PLAYER1COUNT}:{PLAYER2COUNT}")
                continue
            if player2Move == "S":
                print("Rock wins", player1, "wins")
                PLAYER1COUNT += 1
                print(f"The score is {PLAYER1COUNT}:{PLAYER2COUNT}")
                continue
            print("Invalid entry")
            continue
        if player1Move == "P":
            if player2Move == "P":
                print("Both paper, it's a draw.")
                print(f"The score is {PLAYER1COUNT}:{PLAYER2COUNT}")
            if player2Move == "R":
                print("Paper wins", player1, "wins!!")
                PLAYER1COUNT += 1
                print(f"The score is {PLAYER1COUNT}:{PLAYER2COUNT}")

                continue
            if player2Move == "S":
                print("Scissors wins", player2, "wins")
                PLAYER2COUNT += 1
                print(f"The score is {PLAYER1COUNT}:{PLAYER2COUNT}")

                continue
            print("Invalid entry")
            continue
        if player1Move == "S":
            if player2Move == "S":
                print("Both scissors, it's a draw")
                print(f"The score is {PLAYER1COUNT}:{PLAYER2COUNT}")
                continue
            if player2Move == "R":
                print("Rock wins", player2, "wins!!")
                PLAYER2COUNT += 1
                print(f"The score is {PLAYER1COUNT}:{PLAYER2COUNT}")

                continue
            if player2Move == "P":
                print("scissors wins", player1, "wins")
                PLAYER1COUNT += 1
                print(f"The score is {PLAYER1COUNT}:{PLAYER2COUNT}")

                continue
            print("Invalid move", player2)
            continue
        print("Invalid Move Player 1!")
        continue
    if PLAYER1COUNT > PLAYER2COUNT:
        print()
        print(f"{player1} wins. The Score is {PLAYER1COUNT} : {PLAYER2COUNT}")
        print()
        print("The game is over! :(")
        sys.exit()
    else:
        print()
        print(f"{player2} wins. The Score is {PLAYER1COUNT} : {PLAYER2COUNT}")
        print()
        print("The game is over! :(")
        sys.exit()
