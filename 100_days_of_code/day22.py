"""
A simple guessing game
"""

import random

print("Guess the number")
print()
number = random.randint(1, 1000000)
print(number)
print("I want you to guess the number I am thinking, it's between 1 and 1000000")
print()
COUNT = 0

while True:
    numero = int(input("What is your guess?: "))
    if numero < number:
        print("Oops that's too low , that's not the number .Try something higher")
        print()
        COUNT += 1
        continue
    if numero > number:
        print("Oops that's too high , that's not the number .Try something lower")
        print()
        COUNT += 1
        continue
    print()
    print("Are you Charles Xavier? How did you know? :))")
    COUNT += 1
    break
if COUNT == 1:
    print("And it only took you 1 attempt")
    print()
else:
    print(f"It took you {COUNT} attempts")
