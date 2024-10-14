"""
Day 49
"""

import os
import time

f = open("high.score", "r", encoding="utf-8")
scores = f.read().split("\n")
f.close()

HIGHSCORE = 0
NAME = None

for rows in scores:
    data = rows.split()
    if data != []:
        if int(data[1]) > HIGHSCORE:
            HIGHSCORE = int(data[1])
            NAME = data[0]
os.system("cls")
for i in range(1,5):
    print(f"Analyzing High Scores {'.'*(i+1)}")
    time.sleep(1)
    os.system("cls")
print(f"The Current Leader is {NAME} with {HIGHSCORE} ")
