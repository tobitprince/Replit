"""
    Fill the lyrics.
"""

print("Fill in the blank lyrics")
print()
print("Type in the blank lyrics and see if you are as cool as me")
print()
print("Never going to ____ you up.")
print()

print("")
COUNT = 1
while True:

    lyric = input("What is the missing word?: ")
    if lyric == "give":

        break
    print("Nope, Try again")
    COUNT += 1
if COUNT == 1:
    print(f"Woww! It only took you {COUNT} attempt.")
else:
    print(f"Well done! It only took you {COUNT} attempts.")
