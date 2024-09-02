"""
This module asks the user to guess the number.
"""

print("Guess the number")
print()
NUMBER = 3
print("I want you to guess the number I am thinking, it's between 1 and 10")
print()
COUNT = 0

while True:
    numero = int(input("What is your guess?: "))
    if numero < NUMBER:
        print("Oops that's too low , that's not the number .Try something higher")
        print()
        COUNT += 1
        continue
    if numero > NUMBER:
        print("Oops that's too high , that's not the number .Try something lower")
        print()
        COUNT += 1
        continue
    print()
    print("Are you charles Xavier? How did you know? :))")
    COUNT += 1
    break
if COUNT == 1:
    print("And it only took you 1 attempt")
    print()
else:
    print("It took you {COUNT} attempts")
