from getpass import getpass as input

print("Rock, Paper and Scissors!!!")
print()
print()
player1 = input("Player 1 enter you name: ").title()
player2 = input("Player 2 enter your name: ").title()

print("Choose between (R,P,S)")
print()
player1Count = 0
player2Count = 0
while True:

    if player1Count != 3 and player2Count != 3:
        player1Move = input(f"{player1},enter move: ").upper()
        print()
        player2Move = input(f"{player2}, enter move: ").upper()
        print()

        if player1Move == "R":
            if player2Move == "R":
                print("Both rock, it's a draw")
                print(f"The score is {player1Count}:{player2Count}")
                continue
            elif player2Move == "P":
                print("Paper wins", player2, "wins!!")
                player2Count += 1
                print(f"The score is {player1Count}:{player2Count}")
                continue
            elif player2Move == "S":
                print("Rock wins", player1, "wins")
                player1Count += 1
                print(f"The score is {player1Count}:{player2Count}")
                continue
            else:
                print("Invalid entry")
        elif player1Move == "P":
            if player2Move == "P":
                print("Both paper, it's a draw.")
                print(f"The score is {player1Count}:{player2Count}")
            elif player2Move == "R":
                print("Paper wins", player1, "wins!!")
                player1Count += 1
                print(f"The score is {player1Count}:{player2Count}")

                continue
            elif player2Move == "S":
                print("Scissors wins", player2, "wins")
                player2Count += 1
                print(f"The score is {player1Count}:{player2Count}")

                continue
            else:
                print("Invalid entry")
                continue
        elif player1Move == "S":
            if player2Move == "S":
                print("Both scissors, it's a draw")
                print(f"The score is {player1Count}:{player2Count}")
            elif player2Move == "R":
                print("Rock wins", player2, "wins!!")
                player2Count += 1
                print(f"The score is {player1Count}:{player2Count}")

                continue
            elif player2Move == "P":
                print("scissors wins", player1, "wins")
                player1Count += 1
                print(f"The score is {player1Count}:{player2Count}")

                continue
            else:
                print("Invalid move", player2)
                continue
        else:
            print("Invalid Move Player 1!")
            continue
    else:
        if player1Count > player2Count:
            print()
            print(f"{player1} wins. The Score is {player1Count} : {player2Count}")
            print()
            print("The game is over! :(")
            exit()
        else:
            print()
            print(f"{player2} wins. The Score is {player1Count} : {player2Count}")
            print()
            print("The game is over! :(")
            exit()
