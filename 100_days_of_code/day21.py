"""
This is a Math game.
"""

print("Math Game!!!!!!!")
print()
print("We're going to test your multiplication knowledge")
print()
multiple = int(input("Name your multiples: "))
POINT = 0
for i in range(1, 11):
    answer = int(input(f"What is {i} *  {multiple} = ?: "))
    if answer == i * multiple:
        print("That's amazing")
        POINT += 1
    else:
        print(f"That is not correct , The answer was {i*multiple}")
if POINT == 10:
    print()
    print("Amazing you got everything :)))")
else:
    print()
    print(f"You scored {POINT} out of 10")
