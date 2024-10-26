import os
import csv

with open("Day54Totals.csv",encoding="utf8") as file:
    content =csv.DictReader(file)
    TOTAL = 0
    for row in content:
        TOTAL += float(row["Cost"]) * float(row["Quantity"])
os.system("cls")
print ("Shop $$ Tracker".center(35,"-"))
print(f"The shop took a total of ${round(TOTAL,2)}")
