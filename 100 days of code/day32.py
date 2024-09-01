import random
import os, time

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
    randomNumber = random.randint(0, 11)
    print(f"{greetings[randomNumber]}".center(35))
    time.sleep(2)
    os.system("cls")
