"""
Hangman
"""
import random
import os
import time

listOfWords = ["British", "Suave", "Integrity", "Accent", "Evil", "Genius", "Downton"]

word_chosen = random.choice(listOfWords).lower()

os.system("cls")

for x in range(5):
    print("HangMan!".center(35, "-").upper())
    print(f"Starting Game{'.'*(x+1)}")
    print("Please wait")
    time.sleep(1)
    os.system("cls")
print(word_chosen)
CHANCES = 6
correct_guesses = ["_"] * len(word_chosen)
guessed_letters = set()
while True:
    time.sleep(1)
    os.system("cls")
    print()
    print()
    print()
    print(" ".join(correct_guesses).center(50))
    if CHANCES != 0:
        if "_" in correct_guesses:
            print()
            print()
            letter = input("Enter a letter: ").lower()
            if letter in guessed_letters:
                print("You already guessed that letter. Try again.")
                continue
            guessed_letters.add(letter)


            if letter in word_chosen:


                print("\033[32m That's correct \033[0m")
                for i,neno in enumerate(word_chosen):
                    if neno == letter:
                        correct_guesses[i] = letter
            else:
                print("No thats not it!")
                CHANCES -= 1
                print(f"You still have \033[31m{CHANCES}\033[0m CHANCE(S) left")
                print()
        else:
            print(f"\033[32mYOU WON!!!!\033[0m\n with {CHANCES} CHANCE(s) still left!!")
            break
    else:
        print("\033[31m Game over, your CHANCES are over \033[0m",)
        print(f"The word was \033[32m {word_chosen.upper()}\033[0m!!!!!")
        break
