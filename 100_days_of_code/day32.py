"""
Generate random greetings.
"""
import random
import os
import time

greetings = [
    "Bonjour",
    "Hola",
    "Zdravstvuyte",
    "Nǐn hǎo",
    "Salve",
    "Konnichiwa",
    "Guten Tag",
    "Hi",
    "Olá",
    "Anyoung haseyo",
    "Asalaam alaikum",
    "Shikamoo",
]

while True:
    print()
    random_number = random.randint(0, 11)
    print(f"{greetings[random_number]}".center(35))
    time.sleep(2)
    os.system("cls")
